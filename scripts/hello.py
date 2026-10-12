#!/usr/bin/env python3
"""Hello World library tooling.

Usage:
  python3 scripts/hello.py readme                 # regenerate README.md
  python3 scripts/hello.py check                  # validate metadata, files and README
  python3 scripts/hello.py test [--group G] [--lang SLUG ...] [--strict]
  python3 scripts/hello.py apt-packages [--group G]
"""
import argparse
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
README = os.path.join(ROOT, "README.md")
REPO = "matbrgz/Hello-World"
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


def load_languages():
    langs = []
    for slug in sorted(os.listdir(LANG_DIR)):
        path = os.path.join(LANG_DIR, slug)
        if not os.path.isdir(path):
            continue
        meta_path = os.path.join(path, "meta.json")
        with open(meta_path, encoding="utf-8") as fh:
            meta = json.load(fh)
        meta["slug"] = slug
        langs.append(meta)
    return langs


def link(lang, label=None):
    f = lang["files"][0]
    url = "languages/%s/%s" % (lang["slug"], quote(f))
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


def render_readme(langs):
    count = len(langs)
    n_tested = sum(1 for l in langs if l.get("test"))
    n_run = sum(1 for l in langs if l.get("test") and l["test"].get("kind") != "compile")
    pct = round(100.0 * n_tested / count)
    top50 = sorted((l for l in langs if l.get("tiobe", {}).get("rank")), key=lambda l: l["tiobe"]["rank"])
    next50 = sorted((l for l in langs if l.get("tiobe", {}).get("group") == "51-100"),
                    key=lambda l: l["tiobe"].get("as", l["name"]).lower())
    brazilian = sorted((l for l in langs if "brazilian" in l.get("tags", [])), key=name_key)

    parts = []
    parts.append("""# Hello World 🌍

> "Hello World" in every programming language we can get our hands on.

[![CI](https://github.com/{repo}/actions/workflows/hello-world.yml/badge.svg)](https://github.com/{repo}/actions/workflows/hello-world.yml)
![Languages](https://img.shields.io/badge/languages-{count}-blue)
![Tested in CI](https://img.shields.io/badge/tested%20in%20CI-{tested}%20({pct}%25)-brightgreen)
![TIOBE coverage](https://img.shields.io/badge/TIOBE%20top%20100-100%25-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

Since 1974, when Brian Kernighan used it in *Programming in C: A Tutorial*, printing **Hello World** has been
the first program almost everyone writes in a new language. This repository collects that program in
**{count} languages**: every language in the [TIOBE Index](https://www.tiobe.com/tiobe-index/) top 100,
the languages that shaped computing history, the new languages people are talking about, Brazilian languages,
and a long tail of assembly, shell, scientific, hardware, markup and esoteric languages.

**{tested} of {count} programs ({pct}%) are checked on every push** by GitHub Actions on Linux, macOS and Windows:

- ✅ **{run} run** and their output is checked to contain "Hello World";
- 🔧 **{compiled} are compiled or validated** with the language's official tool, for languages that cannot print text
  (shaders, smart contracts, hardware, configuration) or have no free runtime.
""".format(repo=REPO, count=count, tested=n_tested, pct=pct, run=n_run, compiled=n_tested - n_run))

    toc = ["- [TIOBE Index — Top 50](#tiobe-index--top-50)", "- [TIOBE Index — 51 to 100](#tiobe-index--51-to-100)"]
    sec_with_rows = [s for s in SECTIONS if any(l.get("section") == s[0] for l in langs)]
    for sid, title, _ in sec_with_rows:
        if sid == "esoteric":
            toc.append("- [Brazilian languages 🇧🇷](#brazilian-languages-)")
        toc.append("- [%s](#%s)" % (title, anchor(title)))
    toc += ["- [Running the tests](#running-the-tests)", "- [Contributing](#contributing)"]
    parts.append("## Contents\n\n" + "\n".join(toc) + "\n")

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
python3 scripts/hello.py test --changed-since origin/master   # only languages changed on this branch
python3 scripts/hello.py readme             # regenerate this README from languages/*/meta.json
```

## Contributing

1. Check the tables above: is the language already covered?
2. Create a folder `languages/<slug>/` (lowercase, hyphens) with:
   - the program, usually named `HelloWorld.<extension>`;
   - a `meta.json`, for example:
     ```json
     {
       "name": "Python",
       "files": ["HelloWorld.py"],
       "section": "general",
       "notes": "",
       "test": {"group": "base", "run": "python3 HelloWorld.py"}
     }
     ```
     `section` is one of: %s.
     `test` is optional: add it when the language can run on a GitHub runner. `group` is `base` (tools preinstalled
     on Ubuntu), `apt` (with an `"apt": ["package"]` list), `extra` (tools set up in the workflow), `macos` or
     `windows`, or `docker` (with a pinned `"image"`; `run` executes inside it). `needs` lists the commands that must
     exist (defaults to the first word of `run`). Set `"kind": "compile"` when the program cannot print and the test
     only checks that the official tool accepts it.
3. The program should print (or display) `Hello World` and be the idiomatic, minimal version for that language.
4. Run `python3 scripts/hello.py readme` and `python3 scripts/hello.py check`, then open a pull request.

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
        fh.write(render_readme(load_languages()))
    print("README.md regenerated")


def cmd_check(_args):
    errors = []
    langs = load_languages()
    names = {}
    ranks = {}
    for l in langs:
        where = "languages/%s" % l["slug"]
        if not SLUG_RE.match(l["slug"]):
            errors.append("%s: invalid slug" % where)
        for key in ("name", "files"):
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
        for f in l.get("files", []):
            if not os.path.isfile(os.path.join(LANG_DIR, l["slug"], f)):
                errors.append("%s: file '%s' not found" % (where, f))
        present = set(os.listdir(os.path.join(LANG_DIR, l["slug"]))) - {"meta.json"}
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
    if len(ranks) != 50:
        errors.append("TIOBE top 50 has %d ranked languages, expected 50" % len(ranks))
    next50 = [l for l in langs if l.get("tiobe", {}).get("group") == "51-100"]
    if len(next50) != 50:
        errors.append("TIOBE 51-100 has %d languages, expected 50" % len(next50))
    stray = [f for f in os.listdir(ROOT) if f.lower().startswith("helloworld")]
    if stray:
        errors.append("Hello World files outside languages/: %s" % stray)
    with open(README, encoding="utf-8") as fh:
        if fh.read() != render_readme(langs):
            errors.append("README.md is out of date: run `python3 scripts/hello.py readme`")
    for e in errors:
        print("ERROR", e)
    print("%d languages, %d with tests, %d errors" % (len(langs), sum(1 for l in langs if l.get("test")), len(errors)))
    return 1 if errors else 0


def normalize(text):
    return re.sub(r"[^a-z]", "", text.lower())


def changed_slugs(ref):
    """Slugs changed since ref, or None when tooling changed and everything must run."""
    out = subprocess.run(["git", "diff", "--name-only", "%s...HEAD" % ref], cwd=ROOT, check=True,
                         stdout=subprocess.PIPE).stdout.decode()
    slugs = set()
    for path in out.split():
        if path.startswith(("scripts/", ".github/workflows/")):
            return None
        if path.startswith("languages/"):
            slugs.add(path.split("/")[1])
    return slugs


def cmd_test(args):
    langs = [l for l in load_languages() if l.get("test")]
    if args.changed_since:
        slugs = changed_slugs(args.changed_since)
        if slugs is not None:
            langs = [l for l in langs if l["slug"] in slugs]
            print("Testing languages changed since %s: %s" % (args.changed_since, ", ".join(sorted(slugs)) or "none"))
    if args.group:
        langs = [l for l in langs if l["test"]["group"] == args.group]
    if args.lang:
        langs = [l for l in langs if l["slug"] in args.lang]
    if args.shard:
        index, total = (int(n) for n in args.shard.split("/"))
        langs = [l for i, l in enumerate(langs) if i % total == index - 1]
    passed, failed, skipped = [], [], []
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
                print("FAIL %-24s missing tool: %s" % (l["slug"], ", ".join(missing)), flush=True)
            else:
                skipped.append(l)
            continue
        tmp = tempfile.mkdtemp(prefix="hello-%s-" % l["slug"])
        try:
            for f in l["files"]:
                shutil.copy(os.path.join(LANG_DIR, l["slug"], f), tmp)
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
                       "-v", "%s:/src" % tmp, "-w", "/src", "--entrypoint", test.get("shell", "sh"),
                       image, "-c", test["run"]]
            else:
                cmd = ["sh", "-c", test["run"]]
            for _ in range(3):
                proc = subprocess.run(cmd, cwd=tmp, env=dict(os.environ, HELLO_ROOT=ROOT), stdin=subprocess.DEVNULL,
                                      stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=test.get("timeout", args.timeout))
                out = proc.stdout.decode("utf-8", "replace")
                if "toomanyrequests" not in out:
                    break
                time.sleep(60)  # registry rate limit: wait and retry
            if test.get("kind") == "compile":
                ok = proc.returncode == 0
            else:
                ok = "helloworld" in normalize(out) and (proc.returncode == 0 or test.get("allow_nonzero"))
        except subprocess.TimeoutExpired:
            out, ok = "timeout after %ds" % test.get("timeout", args.timeout), False
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
        if ok:
            passed.append(l)
            print("PASS %s" % l["slug"], flush=True)
        else:
            failed.append((l, out))
            print("FAIL %-24s exit/output:\n%s" % (l["slug"], out[-2000:]), flush=True)
    print("\n%d passed, %d failed, %d skipped (toolchain not installed)" % (len(passed), len(failed), len(skipped)))
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as fh:
            fh.write("### Hello World tests%s\n\n" % (" — group `%s`" % args.group if args.group else ""))
            fh.write("%d passed, %d failed, %d skipped\n\n" % (len(passed), len(failed), len(skipped)))
            for l, _ in failed:
                fh.write("- ❌ `%s`\n" % l["slug"])
    return 1 if failed else 0


def cmd_apt(args):
    pkgs = set()
    slugs = changed_slugs(args.changed_since) if args.changed_since else None
    for l in load_languages():
        if slugs is not None and l["slug"] not in slugs:
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
    t.add_argument("--strict", action="store_true", help="fail when a toolchain is missing")
    t.add_argument("--timeout", type=int, default=180)
    t.add_argument("--shard", help="run only shard I of N, as I/N")
    t.add_argument("--changed-since", default=os.environ.get("HELLO_CHANGED_SINCE") or None,
                   help="only languages changed since this git ref (all when scripts/ or workflows change)")
    a = sub.add_parser("apt-packages")
    a.add_argument("--group", choices=TEST_GROUPS)
    a.add_argument("--changed-since", default=os.environ.get("HELLO_CHANGED_SINCE") or None)
    args = p.parse_args()
    return {"readme": cmd_readme, "check": cmd_check, "test": cmd_test, "apt-packages": cmd_apt}[args.cmd](args) or 0


if __name__ == "__main__":
    sys.exit(main())
