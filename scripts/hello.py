#!/usr/bin/env python3
"""catalog-algorithms tooling (Hello World library).

Usage:
  python3 scripts/hello.py readme                 # regenerate README.md
  python3 scripts/hello.py check                  # validate metadata, files and README
  python3 scripts/hello.py test [--group G] [--lang SLUG ...] [--algorithm ID ...] [--strict]
  python3 scripts/hello.py apt-packages [--group G]
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANG_DIR = os.path.join(ROOT, "languages")
ALGO_DIR = os.path.join(ROOT, "algorithms")
README = os.path.join(ROOT, "README.md")
REPO = "BenchCommons/catalog-algorithms"
TIOBE_MONTH = "September 2026"
TEST_GROUPS = ("base", "apt", "extra", "docker", "macos", "windows")

# Section id -> (title, intro). Order defines README order.
SECTIONS = [
    ("historical", "Historical languages",
     "Languages that shaped programming, ordered by the year they first appeared."),
    ("modern", "Modern & trending languages",
     "New or fast-growing languages that are not (yet) in the TIOBE top 100."),
    ("general", "More general-purpose languages",
     "Functional, logic, object-oriented and scripting languages outside the TIOBE top 100."),
    ("assembly", "Assembly, IR & bytecode",
     "Machine-level languages for specific architectures and virtual machines."),
    ("shells", "Shells & automation", "Command shells, OS scripting and desktop automation."),
    ("scientific", "Scientific, math & statistics", "Numerical computing, computer algebra and statistics."),
    ("query", "Query languages", "Databases, graphs and data querying."),
    ("hardware", "Hardware, GPU & quantum", "Hardware description, GPU kernels and quantum programs."),
    ("blockchain", "Smart contracts", "Blockchain and smart-contract languages."),
    ("game", "Game & embedded scripting", "Languages embedded in game engines and applications."),
    ("markup", "Markup, templates & web",
     "Documents, stylesheets and templates. They render or produce \"Hello World\" instead of printing it."),
    ("config", "Configuration, build & infrastructure",
     "Build systems, configuration languages and infrastructure as code."),
    ("esoteric", "Esoteric languages", "Languages designed as jokes, puzzles or experiments."),
]
SECTION_IDS = {s[0] for s in SECTIONS}
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")


BASELINE = "hello-world"
LANGUAGE_FILE = "language.json"


def load_algorithms():
    """algorithms/<id>.json: definition of each algorithm and the expected output checksums (spec 010, 012)."""
    algos = {}
    if os.path.isdir(ALGO_DIR):
        for name in sorted(os.listdir(ALGO_DIR)):
            if name.endswith(".json"):
                with open(os.path.join(ALGO_DIR, name), encoding="utf-8") as fh:
                    algos[name[:-5]] = json.load(fh)
    return algos


def load_implementations():
    """One entry per languages/<lang>/<algorithm>/, merging language.json with the algorithm's meta.json."""
    impls = []
    for slug in sorted(os.listdir(LANG_DIR)):
        path = os.path.join(LANG_DIR, slug)
        if not os.path.isdir(path):
            continue
        with open(os.path.join(path, LANGUAGE_FILE), encoding="utf-8") as fh:
            language = json.load(fh)
        for algorithm in sorted(os.listdir(path)):
            adir = os.path.join(path, algorithm)
            if not os.path.isdir(adir):
                continue
            with open(os.path.join(adir, "meta.json"), encoding="utf-8") as fh:
                meta = json.load(fh)
            impl = dict(language)
            impl.update(meta)
            impl.update(slug=slug, algorithm=algorithm, id="%s/%s" % (slug, algorithm), dir=adir)
            impls.append(impl)
    return impls


def load_languages():
    """The Hello World baseline of every language: one entry per language, used by the README."""
    return [i for i in load_implementations() if i["algorithm"] == BASELINE]


def link(lang, label=None):
    f = lang["files"][0]
    url = "languages/%s/%s/%s" % (lang["slug"], lang["algorithm"], quote(f))
    return "[`%s`](%s)" % (label or f, url)


def row(cells):
    return "| " + " | ".join(cells) + " |"


def table(header, rows):
    out = [row(header), "|" + "|".join(["---"] * len(header)) + "|"]
    out += [row(r) for r in rows]
    return "\n".join(out)


def tested(lang):
    test = lang.get("test")
    if not test:
        return ""
    return "🔧" if test.get("kind") == "compile" else "✅"


def name_key(lang):
    return lang["name"].lower().lstrip("(")


def algorithm_section(impls, algos):
    """README table of the algorithms whose output is verified, per language (only what exists in the repo)."""
    by = {}
    for i in impls:
        if i["algorithm"] != BASELINE:
            by.setdefault(i["algorithm"], {})[i["slug"]] = i
    slugs = sorted({s for v in by.values() for s in v})
    names = {i["slug"]: i["name"] for i in impls if i["slug"] in slugs}
    n_impl = sum(len(v) for v in by.values())
    header = ["Algorithm", "Input", "Check size"] + [names[s] for s in slugs]
    rows = []
    for aid in sorted(by):
        a = algos[aid]
        cells = []
        for s in slugs:
            i = by[aid].get(s)
            cells.append("[✅](languages/%s/%s/)" % (s, aid) if i else "")
        rows.append(["[`%s`](algorithms/%s.json)" % (aid, aid), a["input"], "`%s`" % a["check"]] + cells)
    return ("## Algorithms\n\n"
            "**%d implementations of %d algorithms in %d languages.** Each one is run in CI in a pinned Docker image at the "
            "*check* size, and the SHA-256 of its stdout must equal the expected one in `algorithms/<id>.json` "
            "(see [spec 012](docs/specs/012-correctness-check/spec.md)). ✅ means that check passes in CI.\n\n"
            "**Nothing is measured yet.** There are no timings, memory or energy numbers in this repository. Measuring needs "
            "the catalog contract in [tools-benchmark#29](https://github.com/BenchCommons/tools-benchmark/issues/29) "
            "and the perfratio engine in [tools-benchmark#30](https://github.com/BenchCommons/tools-benchmark/issues/30), "
            "both still open. The other algorithms planned in [spec 010](docs/specs/010-algorithm-set/spec.md) "
            "(`binary-trees`, `mandelbrot`, and the name-based `merge-sort`, `binary-search`, `sha-256`) are not implemented; "
            "the name-based ones also wait on [tools-dataset#1](https://github.com/BenchCommons/tools-dataset/issues/1).\n\n"
            % (n_impl, len(by), len(slugs)) + table(header, rows) + "\n")


def render_readme(langs, impls=None, algos=None):
    impls = load_implementations() if impls is None else impls
    algos = load_algorithms() if algos is None else algos
    count = len(langs)
    n_tested = sum(1 for l in langs if l.get("test"))
    n_run = sum(1 for l in langs if l.get("test") and l["test"].get("kind") != "compile")
    pct = round(100.0 * n_tested / count)
    top50 = sorted((l for l in langs if l.get("tiobe", {}).get("rank")), key=lambda l: l["tiobe"]["rank"])
    next50 = sorted((l for l in langs if l.get("tiobe", {}).get("group") == "51-100"),
                    key=lambda l: l["tiobe"].get("as", l["name"]).lower())
    brazilian = sorted((l for l in langs if "brazilian" in l.get("tags", [])), key=name_key)

    parts = []
    parts.append("""# catalog-algorithms

> Classic algorithm implementations across programming languages, for the
> [BenchCommons](https://github.com/BenchCommons) toolset. Today: Hello World in {count} languages and
> {n_algo_impl} implementations of {n_algo} classic algorithms, with output checked in CI. Nothing is measured yet.

[![CI](https://github.com/{repo}/actions/workflows/hello-world.yml/badge.svg)](https://github.com/{repo}/actions/workflows/hello-world.yml)
![Languages](https://img.shields.io/badge/languages-{count}-blue)
![Tested in CI](https://img.shields.io/badge/tested%20in%20CI-{tested}%20({pct}%25)-brightgreen)
![TIOBE coverage](https://img.shields.io/badge/TIOBE%20top%20100-100%25-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

This repository is the BenchCommons catalog of **classic algorithm implementations across languages**.
The goal is to compare languages by running the same algorithm on the same input, with a pinned toolchain and
output checked against a canonical expected output before anything is measured.

| | Implemented today | Planned (not here yet) |
|---|---|---|
| Hello World (startup baseline) | {count} languages, {tested} with a CI test | |
| Algorithms, output checked in CI | {algo_list}, in {algo_langs} | `binary-trees`, `mandelbrot`, `merge-sort`, `binary-search`, `sha-256` |
| Measurement of time, memory and energy | none | [perfratio](https://github.com/BenchCommons/perfratio) through [tools-benchmark](https://github.com/BenchCommons/tools-benchmark), after [#29](https://github.com/BenchCommons/tools-benchmark/issues/29) and [#30](https://github.com/BenchCommons/tools-benchmark/issues/30) |

The roadmap is tracked in [issue #11](https://github.com/{repo}/issues/11) and in [`docs/specs/`](docs/specs/ROADMAP.md).

It starts from **Hello World**, the first program almost everyone writes in a new language since Brian Kernighan
used it in 1974. Hello World does almost no work, so it is the **startup-cost baseline** for each language:
the time and memory a toolchain needs before any algorithm runs. The catalog has it in **{count} languages**:
every language in the [TIOBE Index](https://www.tiobe.com/tiobe-index/) top 100, the languages that shaped
computing history, the new languages people are talking about, Brazilian languages, and a long tail of assembly,
shell, scientific, hardware, markup and esoteric languages.

**{tested} of {count} programs ({pct}%) are checked** by GitHub Actions on Linux, macOS and Windows. Every push to the main branch, the daily schedule and manual runs test all of them; a pull request tests only the languages and algorithms it changes (everything, if `scripts/` or the workflows change):

- ✅ **{run} run** and their output is checked to contain "Hello World";
- 🔧 **{compiled} are compiled or validated** with the language's official tool, for languages that cannot print text
  (shaders, smart contracts, hardware, configuration) or have no free runtime.
""".format(repo=REPO, count=count, tested=n_tested, pct=pct, run=n_run, compiled=n_tested - n_run,
           n_algo_impl=sum(1 for i in impls if i["algorithm"] != BASELINE),
           n_algo=len({i["algorithm"] for i in impls if i["algorithm"] != BASELINE}),
           algo_list=", ".join("`%s`" % a for a in sorted({i["algorithm"] for i in impls if i["algorithm"] != BASELINE})),
           algo_langs=", ".join(sorted({i["name"] for i in impls if i["algorithm"] != BASELINE}))))

    toc = ["- [Algorithms](#algorithms)", "- [TIOBE Index — Top 50](#tiobe-index--top-50)", "- [TIOBE Index — 51 to 100](#tiobe-index--51-to-100)"]
    sec_with_rows = [s for s in SECTIONS if any(l.get("section") == s[0] for l in langs)]
    for sid, title, _ in sec_with_rows:
        if sid == "esoteric":
            toc.append("- [Brazilian languages 🇧🇷](#brazilian-languages-)")
        toc.append("- [%s](#%s)" % (title, anchor(title)))
    toc += ["- [Running the tests](#running-the-tests)", "- [Contributing](#contributing)"]
    parts.append("## Contents\n\n" + "\n".join(toc) + "\n")

    parts.append(algorithm_section(impls, algos))
    parts.append("## TIOBE Index — Top 50\n\nRanking from the TIOBE Index of **%s**. Rankings change every month; "
                 "the list is a snapshot. Purely graphical languages (Scratch, LabVIEW, Ladder Logic) have no text "
                 "syntax, so their files contain a textual representation.\n\n" % TIOBE_MONTH
                 + table(["#", "Language", "File", "CI", "Notes"],
                         [[str(l["tiobe"]["rank"]), "**%s**" % l["tiobe"].get("as", l["name"]), link(l), tested(l),
                           l.get("notes", "")] for l in top50]) + "\n")
    parts.append("## TIOBE Index — 51 to 100\n\nTIOBE publishes positions 51–100 unranked, in alphabetical order.\n\n"
                 + table(["Language", "File", "CI", "Notes"],
                         [["**%s**" % l["tiobe"].get("as", l["name"]), link(l), tested(l), l.get("notes", "")]
                          for l in next50]) + "\n")

    for sid, title, intro in sec_with_rows:
        if sid == "esoteric":
            parts.append("## Brazilian languages 🇧🇷\n\nLanguages created in Brazil or designed for programming in "
                         "Portuguese. Some of them also appear in other tables.\n\n"
                         + table(["Language", "File", "CI", "Notes"],
                                 [["**%s**" % l["name"], link(l), tested(l), l.get("brazilian_notes", l.get("notes", ""))]
                                  for l in brazilian]) + "\n")
        rows = [l for l in langs if l.get("section") == sid]
        if sid == "historical":
            rows.sort(key=lambda l: (l.get("year", 9999), name_key(l)))
            body = table(["Language", "Year", "File", "CI", "Notes"],
                         [["**%s**" % l["name"], str(l.get("year", "")), link(l), tested(l), l.get("notes", "")]
                          for l in rows])
        else:
            rows.sort(key=name_key)
            body = table(["Language", "File", "CI", "Notes"],
                         [["**%s**" % l["name"], link(l), tested(l), l.get("notes", "")] for l in rows])
        parts.append("## %s\n\n%s\n\n%s\n" % (title, intro, body))

    parts.append("""## Running the tests

```sh
python3 scripts/hello.py check              # metadata, files and README are consistent
python3 scripts/hello.py test               # run every language whose toolchain is installed locally
python3 scripts/hello.py test --lang python --lang rust
python3 scripts/hello.py test --algorithm n-body              # only one algorithm: checks stdout against algorithms/n-body.json
python3 scripts/hello.py test --changed-since origin/master   # only languages and algorithms changed on this branch
python3 scripts/hello.py readme             # regenerate this README from languages/*/language.json and */meta.json
```

## Contributing

The catalog is organized **by language, with one folder per algorithm inside it**:

```
languages/<lang>/
├── language.json          # the language: name, section or TIOBE position, year, notes
├── hello-world/           # the startup-cost baseline every language has
│   ├── meta.json          # files and test of this implementation
│   └── HelloWorld.<ext>
└── <algorithm>/           # n-body, fannkuch-redux, spectral-norm (more in docs/specs/010-algorithm-set)
    ├── meta.json          # files and a docker test; the run command reads $BENCH_N
    └── <program>.<ext>

algorithms/<algorithm>.json  # definition: check size and the expected SHA-256 of stdout per size
```

1. Check the tables above: is the language already covered?
2. For a new language, create `languages/<lang>/` (lowercase, hyphens) with a `language.json`:
   ```json
   {"name": "Python", "section": "general", "notes": ""}
   ```
   `section` is one of: %s.
3. Add the implementation in `languages/<lang>/<algorithm>/` (`hello-world` first) with the program and a `meta.json`:
   ```json
   {"files": ["HelloWorld.py"], "test": {"group": "base", "run": "python3 HelloWorld.py"}}
   ```
   `test` is optional: add it when the language can run on a GitHub runner. `group` is `base` (tools preinstalled
   on Ubuntu), `apt` (with an `"apt": ["package"]` list), `extra` (tools set up in the workflow), `macos` or
   `windows`, or `docker` (with a pinned `"image"`; `run` executes inside it). `needs` lists the commands that must
   exist (defaults to the first word of `run`). Set `"kind": "compile"` when the program cannot print and the test
   only checks that the official tool accepts it.
4. The program should be the idiomatic, minimal version for that language; Hello World prints (or displays) `Hello World`.
5. An algorithm other than `hello-world` needs a definition in `algorithms/<id>.json` (spec 010 and 012). Its `test` must use
   `group: docker` with a pinned image and pass `"$BENCH_N"` to the program; the test passes only if the SHA-256 of
   stdout equals the expected one for the check size. Do not use the language's built-in sort, search or hash for
   `merge-sort`, `binary-search` and `sha-256`.
6. Run `python3 scripts/hello.py readme` and `python3 scripts/hello.py check`, then open a pull request.

## Contributors

Maintained by [@matbrgz](https://github.com/matbrgz).

[![matbrgz](https://github.com/matbrgz.png?size=64)](https://github.com/matbrgz)

[![Contributors](https://contrib.rocks/image?repo=%s)](https://github.com/%s/graphs/contributors)

## License

[MIT](LICENSE)
""" % (", ".join("`%s`" % s[0] for s in SECTIONS), REPO, REPO))
    return "\n".join(parts)


def anchor(title):
    a = title.lower()
    a = re.sub(r"[^\w\- ]", "", a, flags=re.UNICODE)
    return a.replace(" ", "-")


def cmd_readme(_args):
    with open(README, "w", encoding="utf-8") as fh:
        fh.write(render_readme(load_languages(), load_implementations(), load_algorithms()))
    print("README.md regenerated")


def cmd_check(_args):
    errors = []
    langs = load_languages()
    impls = load_implementations()
    ALGO_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
    for slug in sorted(os.listdir(LANG_DIR)):
        path = os.path.join(LANG_DIR, slug)
        if not os.path.isdir(path):
            continue
        entries = set(os.listdir(path))
        if LANGUAGE_FILE not in entries:
            errors.append("languages/%s: missing %s" % (slug, LANGUAGE_FILE))
        if BASELINE not in entries:
            errors.append("languages/%s: missing the %s baseline" % (slug, BASELINE))
        stray = sorted(e for e in entries - {LANGUAGE_FILE} if not os.path.isdir(os.path.join(path, e)))
        if stray:
            errors.append("languages/%s: files outside an algorithm folder: %s" % (slug, stray))
        for e in entries:
            if os.path.isdir(os.path.join(path, e)) and not ALGO_RE.match(e):
                errors.append("languages/%s/%s: algorithm ids must be kebab-case" % (slug, e))
    names = {}
    ranks = {}
    for l in langs:
        where = "languages/%s" % l["slug"]
        if not SLUG_RE.match(l["slug"]):
            errors.append("%s: invalid slug" % where)
        for key in ("name",):
            if key not in l:
                errors.append("%s: missing '%s'" % (where, key))
        if l.get("name", "").lower() in names:
            errors.append("%s: duplicate name '%s' (also in %s)" % (where, l["name"], names[l["name"].lower()]))
        names[l.get("name", "").lower()] = where
        if "section" not in l and "tiobe" not in l:
            errors.append("%s: needs 'section' or 'tiobe'" % where)
        if "section" in l and l["section"] not in SECTION_IDS:
            errors.append("%s: unknown section '%s'" % (where, l["section"]))
        rank = l.get("tiobe", {}).get("rank")
        if rank:
            if rank in ranks:
                errors.append("%s: TIOBE rank %d also used by %s" % (where, rank, ranks[rank]))
            ranks[rank] = where
    for l in impls:
        where = "languages/%s" % l["id"]
        if "files" not in l:
            errors.append("%s: missing 'files'" % where)
        for f in l.get("files", []):
            if not os.path.isfile(os.path.join(l["dir"], f)):
                errors.append("%s: file '%s' not found" % (where, f))
        present = set(os.listdir(l["dir"])) - {"meta.json"}
        extra = present - set(l.get("files", []))
        if extra:
            errors.append("%s: files not listed in meta.json: %s" % (where, sorted(extra)))
        test = l.get("test")
        if test:
            if test.get("group") not in TEST_GROUPS:
                errors.append("%s: test.group must be one of %s" % (where, TEST_GROUPS))
            if not test.get("run"):
                errors.append("%s: test.run is empty" % where)
            if test.get("group") == "apt" and not test.get("apt"):
                errors.append("%s: apt group needs an 'apt' package list" % where)
            if test.get("group") == "docker":
                image = test.get("image", "")
                if ":" not in image or image.endswith(":latest"):
                    errors.append("%s: docker image must be pinned to a version tag" % where)
            if test.get("kind", "run") not in ("run", "compile"):
                errors.append("%s: test.kind must be 'run' or 'compile'" % where)
    errors += check_algorithms(impls)
    platforms = {}
    for l in impls:
        t = l.get("test") or {}
        if t.get("group") == "docker":
            platforms.setdefault(t["image"], set()).add(t.get("platform", "linux/amd64"))
    for image, plats in sorted(platforms.items()):
        if len(plats) > 1:
            errors.append("docker image %s is used with several platforms %s; the local tag cache would mix them "
                          "(use a platform-specific image such as i386/...)" % (image, sorted(plats)))
    if len(ranks) != 50:
        errors.append("TIOBE top 50 has %d ranked languages, expected 50" % len(ranks))
    next50 = [l for l in langs if l.get("tiobe", {}).get("group") == "51-100"]
    if len(next50) != 50:
        errors.append("TIOBE 51-100 has %d languages, expected 50" % len(next50))
    stray = [f for f in os.listdir(ROOT) if f.lower().startswith("helloworld")]
    if stray:
        errors.append("Hello World files outside languages/: %s" % stray)
    with open(README, encoding="utf-8") as fh:
        if fh.read() != render_readme(langs, impls, load_algorithms()):
            errors.append("README.md is out of date: run `python3 scripts/hello.py readme`")
    for e in errors:
        print("ERROR", e)
    print("%d languages, %d with tests, %d errors" % (len(langs), sum(1 for l in langs if l.get("test")), len(errors)))
    return 1 if errors else 0


SHA_RE = re.compile(r"^[0-9a-f]{64}$")


def check_algorithms(impls):
    """algorithms/<id>.json is consistent, and every algorithm implementation is tested against it (spec 012)."""
    errors = []
    algos = load_algorithms()
    for aid, a in sorted(algos.items()):
        where = "algorithms/%s.json" % aid
        if a.get("id") != aid:
            errors.append("%s: id must be '%s'" % (where, aid))
        if not isinstance(a.get("check"), int) or a["check"] < 1:
            errors.append("%s: 'check' must be a positive integer" % where)
        expected = a.get("expected", {})
        if str(a.get("check")) not in expected:
            errors.append("%s: no expected output for the check size" % where)
        for n, e in expected.items():
            if not n.isdigit():
                errors.append("%s: expected key '%s' is not a size" % (where, n))
            if not SHA_RE.match(e.get("sha256", "")):
                errors.append("%s: size %s needs a lowercase hex sha256" % (where, n))
            if e.get("source") not in ("benchmarks-game-output", "cross-language", "reference"):
                errors.append("%s: size %s has an unknown source" % (where, n))
            if e.get("source") == "cross-language" and len(e.get("agreeing", [])) < 2:
                errors.append("%s: size %s is cross-language but fewer than 2 languages agree" % (where, n))
    for l in impls:
        if l["algorithm"] == BASELINE:
            continue
        where = "languages/%s" % l["id"]
        if l["algorithm"] not in algos:
            errors.append("%s: no algorithms/%s.json" % (where, l["algorithm"]))
        elif not l.get("test"):
            errors.append("%s: an algorithm needs a test (its output is checked before anything is measured)" % where)
        elif l["test"].get("kind") == "compile":
            errors.append("%s: kind 'compile' does not verify output" % where)
        elif l["test"].get("group") != "docker":
            errors.append("%s: algorithms are tested in a pinned docker image" % where)
        elif "BENCH_N" not in l["test"].get("run", ""):
            errors.append("%s: test.run must pass $BENCH_N to the program" % where)
    return errors


def normalize(text):
    return re.sub(r"[^a-z]", "", text.lower())


def changed_scope(ref):
    """(slugs, algorithms) changed since ref, or None when tooling changed and everything must run.

    A change in algorithms/<id>.json selects every implementation of that algorithm.
    """
    out = subprocess.run(["git", "diff", "--name-only", "%s...HEAD" % ref], cwd=ROOT, check=True,
                         stdout=subprocess.PIPE).stdout.decode()
    slugs, algos = set(), set()
    for path in out.split():
        if path.startswith(("scripts/", ".github/workflows/")):
            return None
        if path.startswith("languages/"):
            slugs.add(path.split("/")[1])
        elif path.startswith("algorithms/") and path.endswith(".json"):
            algos.add(os.path.basename(path)[:-5])
    return slugs, algos


def selected(l, scope):
    return scope is None or l["slug"] in scope[0] or l["algorithm"] in scope[1]


def verify_algorithm(algo, returncode, stdout, stderr):
    """Untimed correctness check (spec 012): the SHA-256 of stdout must equal the expected one for the check size.

    Only line endings are normalized (CRLF to LF), as in spec 010 R2. Returns (ok, message).
    """
    got = hashlib.sha256(stdout.replace(b"\r\n", b"\n")).hexdigest()
    want = algo["expected"][str(algo["check"])]["sha256"]
    if returncode == 0 and got == want:
        return True, "%s n=%s sha256=%s" % (algo["id"], algo["check"], got)
    return False, "%s n=%s: exit %s, sha256 expected %s got %s\nstdout: %s\nstderr: %s" % (
        algo["id"], algo["check"], returncode, want, got,
        stdout[:500].decode("utf-8", "replace"), (stderr or b"")[-1000:].decode("utf-8", "replace"))


def run_once(l, test, args):
    """Run one language test in a fresh temp dir; return (ok, output)."""
    tmp = tempfile.mkdtemp(prefix="hello-%s-%s-" % (l["slug"], l["algorithm"]))
    algo = load_algorithms().get(l["algorithm"])
    env = dict(os.environ, HELLO_ROOT=ROOT)
    if algo:
        # Same variable names as the catalog contract (tools-benchmark spec 010, runner environment).
        env.update(BENCH_ALGORITHM=algo["id"], BENCH_N=str(algo["check"]))
    try:
        for f in l["files"]:
            shutil.copy(os.path.join(l["dir"], f), tmp)
        if test["group"] == "docker":
            # Containers may run as a non-root user: make the work dir readable and writable.
            os.chmod(tmp, 0o777)
            for f in os.listdir(tmp):
                os.chmod(os.path.join(tmp, f), 0o666)
            image = test["image"]
            mirror = os.environ.get("HELLO_DOCKER_MIRROR")
            if mirror and "/" not in image.split(":")[0]:
                image = "%s/library/%s" % (mirror, image)  # official images, avoids Docker Hub rate limits
            cmd = ["docker", "run", "--rm", "--platform", test.get("platform", "linux/amd64"),
                   "-v", "%s:/src" % tmp, "-w", "/src", "--entrypoint", test.get("shell", "sh")]
            if algo:
                cmd += ["-e", "BENCH_ALGORITHM", "-e", "BENCH_N"]
            cmd += test.get("docker_args", []) + [image, "-c", test["run"]]
        else:
            cmd = ["sh", "-c", test["run"]]
        for _ in range(3):
            # An algorithm's stdout is the output under test, so stderr must not be mixed into it.
            proc = subprocess.run(cmd, cwd=tmp, env=env, stdin=subprocess.DEVNULL,
                                  stdout=subprocess.PIPE, timeout=test.get("timeout", args.timeout),
                                  stderr=subprocess.PIPE if algo else subprocess.STDOUT)
            out = proc.stdout.decode("utf-8", "replace")
            if "toomanyrequests" not in out + (proc.stderr or b"").decode("utf-8", "replace"):
                break
            time.sleep(60)  # registry rate limit: wait and retry
        if algo:
            ok, out = verify_algorithm(algo, proc.returncode, proc.stdout, proc.stderr)
        elif test.get("kind") == "compile":
            ok = proc.returncode == 0
        else:
            ok = "helloworld" in normalize(out) and (proc.returncode == 0 or test.get("allow_nonzero"))
    except subprocess.TimeoutExpired:
        out, ok = "timeout after %ds" % test.get("timeout", args.timeout), False
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return ok, out


def cmd_test(args):
    langs = [l for l in load_implementations() if l.get("test")]
    if args.changed_since:
        scope = changed_scope(args.changed_since)
        if scope is not None:
            langs = [l for l in langs if selected(l, scope)]
            print("Testing changed since %s: languages %s, algorithms %s" % (
                args.changed_since, ", ".join(sorted(scope[0])) or "none", ", ".join(sorted(scope[1])) or "none"))
    if args.group:
        langs = [l for l in langs if l["test"]["group"] == args.group]
    if args.lang:
        langs = [l for l in langs if l["slug"] in args.lang or l["id"] in args.lang]
    if args.algorithm:
        langs = [l for l in langs if l["algorithm"] in args.algorithm]
    if args.shard:
        index, total = (int(n) for n in args.shard.split("/"))
        langs = [l for i, l in enumerate(langs) if i % total == index - 1]
    passed, failed, skipped, retried = [], [], [], []
    for l in langs:
        test = l["test"]
        if test["group"] == "docker":
            needs = ["docker"]
        else:
            needs = test.get("needs") or [test["run"].split()[0]]
        missing = [n for n in needs if shutil.which(n) is None]
        if missing:
            if args.strict:
                failed.append((l, "missing tool: %s" % ", ".join(missing)))
                print("FAIL %-24s missing tool: %s" % (l["id"], ", ".join(missing)), flush=True)
            else:
                skipped.append(l)
            continue
        flaky = False
        for attempt in range(args.retries + 1):
            ok, out = run_once(l, test, args)
            if ok:
                break
            if attempt < args.retries and not out.startswith("timeout after"):
                flaky = True
                print("RETRY %s (attempt %d failed)" % (l["id"], attempt + 1), flush=True)
                time.sleep(30)  # most failures here are transient downloads
        if ok:
            passed.append(l)
            if flaky:
                retried.append(l)
            print("PASS %s%s%s" % (l["id"], " (after retry)" if flaky else "",
                                   "  [verified: %s]" % out if l["algorithm"] != BASELINE else ""), flush=True)
        else:
            failed.append((l, out))
            print("FAIL %-24s exit/output:\n%s" % (l["id"], out[-2000:]), flush=True)
    print("\n%d passed, %d failed, %d skipped (toolchain not installed)" % (len(passed), len(failed), len(skipped)))
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as fh:
            fh.write("### Hello World tests%s\n\n" % (" — group `%s`" % args.group if args.group else ""))
            fh.write("%d passed, %d failed, %d skipped\n\n" % (len(passed), len(failed), len(skipped)))
            for l in retried:
                fh.write("- 🔁 `%s` passed after a retry\n" % l["id"])
            for l, _ in failed:
                fh.write("- ❌ `%s`\n" % l["id"])
    return 1 if failed else 0


def cmd_apt(args):
    pkgs = set()
    scope = changed_scope(args.changed_since) if args.changed_since else None
    for l in load_implementations():
        if not selected(l, scope):
            continue
        t = l.get("test")
        if t and (not args.group or t["group"] == args.group):
            pkgs.update(t.get("apt", []))
    print(" ".join(sorted(pkgs)))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("readme")
    sub.add_parser("check")
    t = sub.add_parser("test")
    t.add_argument("--group", choices=TEST_GROUPS)
    t.add_argument("--lang", action="append")
    t.add_argument("--algorithm", action="append", help="only this algorithm id (e.g. hello-world, n-body)")
    t.add_argument("--strict", action="store_true", help="fail when a toolchain is missing")
    t.add_argument("--timeout", type=int, default=180)
    t.add_argument("--shard", help="run only shard I of N, as I/N")
    t.add_argument("--retries", type=int, default=2, help="re-run a failing test this many times (network flakes)")
    t.add_argument("--changed-since", default=os.environ.get("HELLO_CHANGED_SINCE") or None,
                   help="only languages changed since this git ref (all when scripts/ or workflows change)")
    a = sub.add_parser("apt-packages")
    a.add_argument("--group", choices=TEST_GROUPS)
    a.add_argument("--changed-since", default=os.environ.get("HELLO_CHANGED_SINCE") or None)
    args = p.parse_args()
    return {"readme": cmd_readme, "check": cmd_check, "test": cmd_test, "apt-packages": cmd_apt}[args.cmd](args) or 0


if __name__ == "__main__":
    sys.exit(main())
