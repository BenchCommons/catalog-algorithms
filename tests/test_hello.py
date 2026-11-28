"""Tests for scripts/hello.py (issue #17).

Stdlib only: python3 -m unittest discover -s tests -v

They exercise observable behaviour on temporary catalogs and run no language
toolchain: only sh, printf, sleep and git (temporary repositories). The one
exception is RepositoryState, which reads the real tree, read-only.
Variables that CI sets (HELLO_CHANGED_SINCE, GITHUB_STEP_SUMMARY, ...) are
removed from the environment so the tests behave the same locally and in CI.
Every behaviour required by issue #17 and spec 012 is asserted here; there are no expectedFailure markers.
"""
import argparse
import contextlib
import hashlib
import importlib.util
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(REPO, "scripts", "hello.py")

spec = importlib.util.spec_from_file_location("hello", SCRIPT)
hello = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hello)

OUT = b"1.5\n2.5\n"
SHA = hashlib.sha256(OUT).hexdigest()
RUN_OK = "printf '1.5\\n2.5\\n'"


CI_VARS = ("HELLO_CHANGED_SINCE", "HELLO_DOCKER_MIRROR", "GITHUB_STEP_SUMMARY", "HELLO_ROOT",
           "GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE")


def clean_env():
    return {k: v for k, v in os.environ.items() if k not in CI_VARS}


def write_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh)


def definition(aid="algo", check=5, sha=SHA, **extra):
    d = {"id": aid, "name": aid, "description": "d", "source": "s", "input": "n: size",
         "check": check, "expected": {str(check): {"sha256": sha, "bytes": len(OUT),
                                                   "source": "cross-language",
                                                   "agreeing": ["c", "d"]}}}
    d.update(extra)
    return d


def meta(run=RUN_OK, group="docker", **test):
    t = {"group": group, "image": "python:3.12.11-slim", "run": run}
    t.update(test)
    return {"files": ["prog.txt"], "test": t}


def make_tree(root, algos=None, impls=None):
    """algos: {id: definition}; impls: {'slug/algorithm': meta}. Also adds a language.json per slug."""
    os.makedirs(os.path.join(root, "languages"), exist_ok=True)
    for aid, d in (algos or {}).items():
        write_json(os.path.join(root, "algorithms", aid + ".json"), d)
    for iid, m in (impls or {}).items():
        slug, algo = iid.split("/")
        lang = os.path.join(root, "languages", slug)
        if not os.path.exists(os.path.join(lang, "language.json")):
            write_json(os.path.join(lang, "language.json"), {"name": slug.title(), "section": "general"})
        write_json(os.path.join(lang, algo, "meta.json"), m)
        with open(os.path.join(lang, algo, "prog.txt"), "w") as fh:
            fh.write("x")


class TreeCase(unittest.TestCase):
    """Points the module at a temporary root for the duration of a test."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="hello-tests-")
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        env = mock.patch.dict(os.environ, clean_env(), clear=True)
        env.start()
        self.addCleanup(env.stop)
        for name, value in (("ROOT", self.tmp),
                            ("LANG_DIR", os.path.join(self.tmp, "languages")),
                            ("ALGO_DIR", os.path.join(self.tmp, "algorithms")),
                            ("README", os.path.join(self.tmp, "README.md"))):
            p = mock.patch.object(hello, name, value)
            p.start()
            self.addCleanup(p.stop)

    def impls(self):
        return {i["id"]: i for i in hello.load_implementations()}


class VerifyAlgorithm(unittest.TestCase):
    algo = definition()

    def test_match(self):
        ok, msg = hello.verify_algorithm(self.algo, 0, OUT, b"")
        self.assertTrue(ok)
        self.assertIn(SHA, msg)

    def test_checksum_mismatch_reports_both_hashes_and_output(self):
        ok, msg = hello.verify_algorithm(self.algo, 0, b"9.9\n", b"warn")
        self.assertFalse(ok)
        self.assertIn(SHA, msg)
        self.assertIn(hashlib.sha256(b"9.9\n").hexdigest(), msg)
        self.assertIn("9.9", msg)
        self.assertIn("warn", msg)

    def test_nonzero_exit_fails_even_with_right_output(self):
        ok, msg = hello.verify_algorithm(self.algo, 1, OUT, b"boom")
        self.assertFalse(ok)
        self.assertIn("exit 1", msg)
        self.assertIn("boom", msg)

    def test_crlf_is_normalized_but_other_whitespace_is_not(self):
        self.assertTrue(hello.verify_algorithm(self.algo, 0, OUT.replace(b"\n", b"\r\n"), b"")[0])
        self.assertFalse(hello.verify_algorithm(self.algo, 0, OUT + b"\n", b"")[0])
        self.assertFalse(hello.verify_algorithm(self.algo, 0, OUT.rstrip(b"\n"), b"")[0])

    def test_empty_stdout_fails(self):
        self.assertFalse(hello.verify_algorithm(self.algo, 0, b"", b"")[0])


class RunOnce(TreeCase):
    """run_once with group 'base': the same code path as docker, minus the docker command."""

    def run_impl(self, run, default_timeout=10, **test):
        make_tree(self.tmp, {"algo": definition()},
                  {"c/algo": meta(run=run, group="base", **test)})
        impl = self.impls()["c/algo"]
        return hello.run_once(impl, impl["test"], argparse.Namespace(timeout=default_timeout))

    def test_correct_output_passes(self):
        ok, msg = self.run_impl(RUN_OK)
        self.assertTrue(ok, msg)

    def test_wrong_output_fails(self):
        ok, msg = self.run_impl("printf '1.5\\n2.6\\n'")
        self.assertFalse(ok)
        self.assertIn("sha256 expected", msg)

    def test_implementation_error_fails(self):
        ok, msg = self.run_impl(RUN_OK + "; exit 3")
        self.assertFalse(ok)
        self.assertIn("exit 3", msg)

    def test_crash_without_output_fails_and_keeps_stderr(self):
        ok, msg = self.run_impl("echo compile error >&2; exit 1")
        self.assertFalse(ok)
        self.assertIn("compile error", msg)

    def test_stderr_is_not_part_of_the_checked_output(self):
        ok, msg = self.run_impl(RUN_OK + "; echo noise >&2")
        self.assertTrue(ok, msg)

    def test_timeout_fails_without_a_pass(self):
        ok, msg = self.run_impl("exec sleep 5", default_timeout=1)
        self.assertFalse(ok)
        self.assertTrue(msg.startswith("timeout after"), msg)

    def test_per_test_timeout_overrides_the_default(self):
        ok, msg = self.run_impl("exec sleep 5", default_timeout=60, timeout=1)
        self.assertFalse(ok)
        self.assertEqual(msg, "timeout after 1s")

    def test_bench_variables_reach_the_program(self):
        ok, msg = self.run_impl('printf "%s %s\\n" "$BENCH_ALGORITHM" "$BENCH_N"')
        self.assertFalse(ok)  # output differs from the registered checksum ...
        self.assertIn("algo 5", msg)  # ... but shows the check size reached the program

    def test_missing_definition_does_not_fall_back_to_hello_world_rule(self):
        make_tree(self.tmp, None, {"c/ghost": meta(run="echo Hello World", group="base")})
        impl = self.impls()["c/ghost"]
        ok, msg = hello.run_once(impl, impl["test"], argparse.Namespace(timeout=10))
        self.assertFalse(ok)
        self.assertIn("no usable algorithms/ghost.json", msg)


    def test_hello_world_needs_exit_zero_unless_allowed(self):
        make_tree(self.tmp, None, {"c/hello-world": meta(run="echo Hello World; exit 2", group="base"),
                                   "d/hello-world": meta(run="echo Hello World; exit 2", group="base",
                                                         allow_nonzero=True)})
        impls = self.impls()
        a = argparse.Namespace(timeout=10)
        self.assertFalse(hello.run_once(impls["c/hello-world"], impls["c/hello-world"]["test"], a)[0])
        self.assertTrue(hello.run_once(impls["d/hello-world"], impls["d/hello-world"]["test"], a)[0])

    def test_compile_kind_only_needs_exit_zero(self):
        make_tree(self.tmp, None, {"c/hello-world": meta(run="true", group="base", kind="compile"),
                                   "d/hello-world": meta(run="false", group="base", kind="compile")})
        impls = self.impls()
        a = argparse.Namespace(timeout=10)
        self.assertTrue(hello.run_once(impls["c/hello-world"], impls["c/hello-world"]["test"], a)[0])
        self.assertFalse(hello.run_once(impls["d/hello-world"], impls["d/hello-world"]["test"], a)[0])

    def docker_run(self, replies, **test):
        make_tree(self.tmp, {"algo": definition()}, {"c/algo": meta(**test)})
        impl = self.impls()["c/algo"]
        calls = []

        def fake(cmd, **kw):
            calls.append(cmd)
            return replies[min(len(calls), len(replies)) - 1]

        with mock.patch.object(hello.subprocess, "run", fake), \
                mock.patch.object(hello.time, "sleep") as sleep:
            result = hello.run_once(impl, impl["test"], argparse.Namespace(timeout=10))
        return result, calls, sleep

    def test_docker_failures_are_marked_as_infrastructure(self):
        pull = subprocess.CompletedProcess([], 125, b"", b"docker: Error response from daemon: pull access denied")
        (ok, msg), _, _ = self.docker_run([pull])
        self.assertFalse(ok)
        self.assertTrue(msg.startswith(hello.INFRA), msg)
        daemon = subprocess.CompletedProcess([], 1, b"", b"Unable to find image 'x' locally")
        (ok, msg), _, _ = self.docker_run([daemon])
        self.assertTrue(msg.startswith(hello.INFRA), msg)

    def test_program_failures_in_docker_are_not_infrastructure(self):
        for proc in (subprocess.CompletedProcess([], 0, b"wrong\n", b""),
                     subprocess.CompletedProcess([], 2, b"", b"segfault"),
                     subprocess.CompletedProcess([], 1, b"1.5\n", b"i/o timeout")):  # has stdout: the program ran
            (ok, msg), _, _ = self.docker_run([proc])
            self.assertFalse(ok)
            self.assertFalse(msg.startswith(hello.INFRA), msg)

    def test_program_exiting_125_is_not_infrastructure(self):
        # `docker run` passes the container's exit code through, so 125 alone proves nothing.
        for proc in (subprocess.CompletedProcess([], 125, b"", b""),
                     subprocess.CompletedProcess([], 125, b"1.5\n", b"docker: not really"),
                     subprocess.CompletedProcess([], 125, b"", b"my own message")):
            (ok, msg), _, _ = self.docker_run([proc])
            self.assertFalse(ok)
            self.assertFalse(msg.startswith(hello.INFRA), msg)

    def test_docker_cli_error_is_infrastructure(self):
        err = subprocess.CompletedProcess([], 125, b"", b"docker: Error response from daemon: boom")
        (ok, msg), _, _ = self.docker_run([err])
        self.assertTrue(msg.startswith(hello.INFRA), msg)

    def test_registry_rate_limit_is_retried_then_verified(self):
        limited = subprocess.CompletedProcess([], 1, b"", b"toomanyrequests: slow down")
        good = subprocess.CompletedProcess([], 0, OUT, b"")
        (ok, msg), calls, sleep = self.docker_run([limited, limited, good])
        self.assertTrue(ok, msg)
        self.assertEqual((len(calls), sleep.call_count), (3, 2))

    def test_persistent_rate_limit_fails(self):
        limited = subprocess.CompletedProcess([], 1, b"", b"toomanyrequests")
        (ok, msg), calls, _ = self.docker_run([limited])
        self.assertFalse(ok)
        self.assertEqual(len(calls), 3)
        self.assertTrue(msg.startswith(hello.INFRA), msg)

    def test_docker_platform_shell_and_extra_args(self):
        good = subprocess.CompletedProcess([], 0, OUT, b"")
        (ok, _), [cmd], _ = self.docker_run([good], platform="linux/386", shell="bash",
                                            docker_args=["--security-opt", "x"])
        self.assertTrue(ok)
        self.assertEqual(cmd[cmd.index("--platform") + 1], "linux/386")
        self.assertEqual(cmd[cmd.index("--entrypoint") + 1], "bash")
        self.assertLess(cmd.index("--security-opt"), cmd.index("python:3.12.11-slim"))

    def test_docker_default_platform_and_mirror(self):
        good = subprocess.CompletedProcess([], 0, OUT, b"")
        with mock.patch.dict(os.environ, {"HELLO_DOCKER_MIRROR": "mirror.example"}):
            (ok, _), [cmd], _ = self.docker_run([good])
            self.assertTrue(ok)
            self.assertEqual(cmd[cmd.index("--platform") + 1], "linux/amd64")
            self.assertIn("mirror.example/library/python:3.12.11-slim", cmd)
            (ok, _), [cmd], _ = self.docker_run([good], image="ghcr.io/x/y:1")
            self.assertIn("ghcr.io/x/y:1", cmd)

    def test_hello_world_rule_is_unchanged(self):
        make_tree(self.tmp, None, {"c/hello-world": meta(run="echo 'Hello, World!'", group="base")})
        impl = self.impls()["c/hello-world"]
        ok, _ = hello.run_once(impl, impl["test"], argparse.Namespace(timeout=10))
        self.assertTrue(ok)

    def test_docker_command_forwards_only_bench_variables_by_name(self):
        make_tree(self.tmp, {"algo": definition()}, {"c/algo": meta()})
        impl = self.impls()["c/algo"]
        seen = {}

        def fake(cmd, **kw):
            seen["cmd"], seen["env"] = cmd, kw["env"]
            return subprocess.CompletedProcess(cmd, 0, OUT, b"")

        with mock.patch.object(hello.subprocess, "run", fake):
            ok, msg = hello.run_once(impl, impl["test"], argparse.Namespace(timeout=10))
        self.assertTrue(ok, msg)
        cmd = seen["cmd"]
        self.assertEqual(cmd[:2], ["docker", "run"])
        self.assertEqual(cmd[cmd.index("-e") + 1], "BENCH_ALGORITHM")
        self.assertEqual([cmd[i + 1] for i, c in enumerate(cmd) if c == "-e"], ["BENCH_ALGORITHM", "BENCH_N"])
        self.assertNotIn("BENCH_N=5", " ".join(cmd))  # values travel in the environment, not the command line
        self.assertEqual((seen["env"]["BENCH_ALGORITHM"], seen["env"]["BENCH_N"]), ("algo", "5"))
        self.assertIn("python:3.12.11-slim", cmd)  # no HELLO_DOCKER_MIRROR in the environment
        self.assertEqual(cmd[-2:], ["-c", RUN_OK])


class CmdTest(TreeCase):
    def args(self, **kw):
        base = dict(changed_since=None, group=None, lang=None, algorithm=None, shard=None,
                    strict=True, retries=0, timeout=10)
        base.update(kw)
        return argparse.Namespace(**base)

    def run_cmd(self, **kw):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf), mock.patch.object(hello.time, "sleep") as self.sleep:
            rc = hello.cmd_test(self.args(**kw))
        return rc, buf.getvalue()

    def test_failure_gives_nonzero_exit_and_no_pass_line(self):
        make_tree(self.tmp, {"algo": definition()},
                  {"c/algo": meta(run="printf wrong", group="base")})
        rc, out = self.run_cmd()
        self.assertEqual(rc, 1)
        self.assertIn("FAIL c/algo", out)
        self.assertNotIn("PASS", out)

    def test_pass_prints_the_verified_checksum(self):
        make_tree(self.tmp, {"algo": definition()}, {"c/algo": meta(group="base")})
        rc, out = self.run_cmd()
        self.assertEqual(rc, 0)
        self.assertIn("PASS c/algo", out)
        self.assertIn("[verified: algo n=5 sha256=%s]" % SHA, out)

    def test_hello_world_pass_line_has_no_verified_tag(self):
        make_tree(self.tmp, None, {"c/hello-world": meta(run="echo Hello World", group="base")})
        rc, out = self.run_cmd()
        self.assertEqual(rc, 0)
        self.assertNotIn("verified", out)

    def test_algorithm_filter(self):
        make_tree(self.tmp, {"algo": definition()},
                  {"c/algo": meta(group="base"),
                   "c/hello-world": meta(run="false", group="base")})
        rc, out = self.run_cmd(algorithm=["algo"])
        self.assertEqual(rc, 0)
        self.assertNotIn("hello-world", out)

    def test_lang_filter_accepts_slug_and_id(self):
        make_tree(self.tmp, {"algo": definition()},
                  {"c/algo": meta(group="base"), "py/algo": meta(run="false", group="base")})
        self.assertEqual(self.run_cmd(lang=["c"])[0], 0)
        self.assertEqual(self.run_cmd(lang=["c/algo"])[0], 0)
        self.assertEqual(self.run_cmd(lang=["py"])[0], 1)

    def test_missing_toolchain_is_skipped_unless_strict(self):
        make_tree(self.tmp, {"algo": definition()},
                  {"c/algo": meta(run="no-such-tool-xyz", group="base")})
        self.assertEqual(self.run_cmd(strict=False)[0], 0)
        rc, out = self.run_cmd(strict=True)
        self.assertEqual(rc, 1)
        self.assertIn("missing tool", out)

    INFRA_FAIL = (False, hello.INFRA + "docker pull failed")

    def test_infrastructure_failure_of_an_algorithm_is_retried(self):
        make_tree(self.tmp, {"algo": definition()}, {"c/algo": meta(group="base")})
        with mock.patch.object(hello, "run_once", side_effect=[self.INFRA_FAIL, (True, "ok")]) as m:
            rc, out = self.run_cmd(retries=2)
        self.assertEqual((rc, m.call_count), (0, 2))
        self.assertIn("RETRY c/algo", out)
        self.assertIn("PASS c/algo (after retry)", out)

    def test_hello_world_failure_is_retried(self):
        make_tree(self.tmp, None, {"c/hello-world": meta(group="base")})
        with mock.patch.object(hello, "run_once", side_effect=[(False, "download failed"), (True, "ok")]) as m:
            rc, _ = self.run_cmd(retries=2)
        self.assertEqual((rc, m.call_count), (0, 2))

    def test_algorithm_timeout_is_retried(self):
        make_tree(self.tmp, {"algo": definition()}, {"c/algo": meta(group="base")})
        with mock.patch.object(hello, "run_once", return_value=(False, "timeout after 10s")) as m:
            rc, _ = self.run_cmd(retries=2)
        self.assertEqual((rc, m.call_count), (1, 3))

    def test_hello_world_timeout_is_not_retried(self):
        make_tree(self.tmp, None, {"c/hello-world": meta(group="base")})
        with mock.patch.object(hello, "run_once", return_value=(False, "timeout after 10s")) as m:
            rc, _ = self.run_cmd(retries=2)
        self.assertEqual((rc, m.call_count), (1, 1))
        self.sleep.assert_not_called()

    def test_wrong_output_exit_error_and_missing_definition_are_never_retried(self):
        for kind, run in (("wrong output", "printf wrong"), ("program error", "printf x; exit 3"),
                          ("crash", "echo boom >&2; exit 1")):
            with self.subTest(kind):
                make_tree(self.tmp, {"algo": definition()}, {"c/algo": meta(run=run, group="base")})
                with mock.patch.object(hello, "run_once", wraps=hello.run_once) as m:
                    rc, out = self.run_cmd(retries=2)
                self.assertEqual((rc, m.call_count), (1, 1))
                self.assertNotIn("RETRY", out)
        make_tree(self.tmp, None, {"c/ghost": meta(group="base")})
        with mock.patch.object(hello, "run_once", wraps=hello.run_once) as m:
            rc, _ = self.run_cmd(retries=2, algorithm=["ghost"])
        self.assertEqual((rc, m.call_count), (1, 1))

    def test_nondeterministic_wrong_output_cannot_pass_after_a_retry(self):
        make_tree(self.tmp, {"algo": definition()},
                  {"c/algo": meta(run='f="%s/n"; if [ -e "$f" ]; then printf "1.5\\n2.5\\n"; '
                                      'else touch "$f"; printf wrong; fi' % self.tmp, group="base")})
        rc, out = self.run_cmd(retries=2)
        self.assertEqual(rc, 1)
        self.assertNotIn("PASS", out)

    def test_retry_sleeps_between_attempts(self):
        make_tree(self.tmp, {"algo": definition()}, {"c/algo": meta(group="base")})
        with mock.patch.object(hello, "run_once", side_effect=[self.INFRA_FAIL, (True, "ok")]):
            self.run_cmd(retries=2)
        self.sleep.assert_called_once_with(30)

    def test_step_summary_lists_retried_passes(self):
        make_tree(self.tmp, {"algo": definition()}, {"c/algo": meta(group="base")})
        path = os.path.join(self.tmp, "summary.md")
        with mock.patch.dict(os.environ, {"GITHUB_STEP_SUMMARY": path}), \
                mock.patch.object(hello, "run_once", side_effect=[self.INFRA_FAIL, (True, "ok")]):
            self.run_cmd(retries=2)
        with open(path, encoding="utf-8") as fh:
            self.assertIn("`c/algo` passed after a retry", fh.read())

    def test_shards_partition_the_tests(self):
        impls = {"c%d/algo" % i: meta(group="base") for i in range(5)}
        make_tree(self.tmp, {"algo": definition()}, impls)
        seen = []
        for shard in ("1/2", "2/2"):
            rc, out = self.run_cmd(shard=shard)
            self.assertEqual(rc, 0)
            seen.append({l.split()[1] for l in out.splitlines() if l.startswith("PASS")})
        self.assertFalse(seen[0] & seen[1])
        self.assertEqual(seen[0] | seen[1], {"c%d/algo" % i for i in range(5)})

    def test_group_filter(self):
        make_tree(self.tmp, {"algo": definition()},
                  {"c/algo": meta(group="base"), "d/algo": meta(run="false", group="apt", apt=["x"])})
        rc, out = self.run_cmd(group="base")
        self.assertEqual(rc, 0)
        self.assertNotIn("d/algo", out)

    def test_step_summary_lists_failures(self):
        make_tree(self.tmp, {"algo": definition()}, {"c/algo": meta(run="printf wrong", group="base")})
        path = os.path.join(self.tmp, "summary.md")
        with mock.patch.dict(os.environ, {"GITHUB_STEP_SUMMARY": path}):
            self.run_cmd()
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        self.assertIn("0 passed, 1 failed", text)
        self.assertIn("`c/algo`", text)

    def test_apt_packages_are_unioned_sorted_and_filtered(self):
        make_tree(self.tmp, None,
                  {"a/hello-world": meta(group="apt", apt=["zsh", "bc"]),
                   "b/hello-world": meta(group="apt", apt=["bc", "awk"]),
                   "c/hello-world": meta(group="base")})
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            hello.cmd_apt(argparse.Namespace(group="apt", changed_since=None))
        self.assertEqual(buf.getvalue().strip(), "awk bc zsh")


class CheckAlgorithms(TreeCase):
    def errors(self, algos, impls):
        make_tree(self.tmp, algos, impls)
        return hello.check_algorithms(hello.load_implementations())

    def good(self):
        return {"algo": definition()}, {"c/algo": meta(run='./prog "$BENCH_N"'),
                                        "d/algo": meta(run='./prog "$BENCH_N"'), "c/hello-world": meta()}

    def test_valid_catalog_has_no_errors(self):
        self.assertEqual(self.errors(*self.good()), [])

    def test_hello_world_needs_no_definition(self):
        self.assertEqual(self.errors({}, {"c/hello-world": {"files": ["prog.txt"]}}), [])

    def assertHas(self, errs, text):
        self.assertTrue(any(text in e for e in errs), errs)

    def test_definition_id_must_match_file_name(self):
        self.assertHas(self.errors({"algo": definition("other")}, {}), "id must be 'algo'")

    def test_check_size_must_be_a_positive_int(self):
        for bad in (0, -1, "7", None):
            d = definition()
            d["check"] = bad
            self.assertHas(self.errors({"algo": d}, {}), "'check' must be a positive integer")

    def test_true_as_check_size_is_reported_as_an_error(self):
        d = definition()
        d["check"] = True
        self.assertHas(self.errors({"algo": d}, {}), "'check' must be a positive integer")

    def test_expected_output_for_check_size_is_required(self):
        d = definition()
        d["check"] = 9
        self.assertHas(self.errors({"algo": d}, {}), "no expected output for the check size")

    def test_checksum_must_be_lowercase_hex_sha256(self):
        for bad in ("ABC", SHA.upper(), SHA[:-1], ""):
            d = definition(sha=bad)
            self.assertHas(self.errors({"algo": d}, {}), "needs a lowercase hex sha256")

    def test_unknown_source_and_lonely_cross_language(self):
        d = definition()
        d["expected"]["5"]["source"] = "memory"
        self.assertHas(self.errors({"algo": d}, {}), "unknown source")
        d["expected"]["5"].update(source="cross-language", agreeing=["only-one"])
        self.assertHas(self.errors({"algo": d}, {}), "fewer than 2 languages agree")

    def test_empty_output_checksum_is_rejected(self):
        self.assertHas(self.errors({"algo": definition(sha=hashlib.sha256(b"").hexdigest())}, {}),
                       "expects an empty output")

    def test_absurdly_nested_json_is_an_error_not_a_crash(self):
        os.makedirs(os.path.join(self.tmp, "algorithms"))
        with open(os.path.join(self.tmp, "algorithms", "deep.json"), "w") as fh:
            fh.write("[" * 200000 + "]" * 200000)
        errs = []
        self.assertEqual(hello.load_algorithms(errs), {})
        self.assertHas(errs, "algorithms/deep.json")

    def test_recursion_error_while_reading_is_caught(self):
        make_tree(self.tmp, {"algo": definition()}, {})
        errs = []
        with mock.patch.object(hello.json, "load", side_effect=RecursionError("deep")):
            self.assertEqual(hello.load_algorithms(errs), {})
        self.assertHas(errs, "cannot read definition")

    def test_unicode_digit_size_keys_are_errors_not_exceptions(self):
        # '²'.isdigit() is True but int('²') raises ValueError (issue #17 review).
        for key in ("²", "٣", "①", "05", "0", "-1", "1.5", " 5", "5\n"):
            with self.subTest(key=repr(key)):
                d = definition()
                d["expected"][key] = d["expected"]["5"]
                self.assertHas(self.errors({"algo": d}, {}), "is not a size")

    def test_sha256_with_trailing_newline_is_rejected(self):
        self.assertHas(self.errors({"algo": definition(sha=SHA + "\n")}, {}), "needs a lowercase hex sha256")

    def test_check_never_raises_on_hostile_definitions(self):
        weird = [None, True, False, 0, -1, 1.5, "", "x", "²", "5\n", [], [1], {}, {"a": 1}, 10 ** 30, ["a", ["b"]]]
        base = definition()
        paths = [("id",), ("name",), ("description",), ("source",), ("input",), ("check",), ("expected",),
                 ("expected", "5"), ("expected", "5", "sha256"), ("expected", "5", "bytes"),
                 ("expected", "5", "source"), ("expected", "5", "agreeing")]
        for path in paths:
            for value in weird:
                d = json.loads(json.dumps(base))
                node = d
                for key in path[:-1]:
                    node = node[key]
                node[path[-1]] = value
                with self.subTest(path=path, value=repr(value)):
                    make_tree(self.tmp, {"algo": d}, {"c/algo": meta(run='./p "$BENCH_N"'),
                                                       "c/hello-world": meta()})
                    impls = hello.load_implementations()
                    hello.check_algorithms(impls)
                    hello.render_readme(hello.load_languages(), impls, hello.load_algorithms())
                    impl = {i["id"]: i for i in impls}["c/algo"]
                    ok, msg = hello.run_once(impl, dict(impl["test"], group="base", run="true"),
                                             argparse.Namespace(timeout=5))
                    self.assertIsInstance(ok, bool)
                    self.assertIsInstance(msg, str)

    def test_definition_without_id_still_verifies_and_check_reports_it(self):
        d = definition()
        del d["id"]
        make_tree(self.tmp, {"algo": d}, {"c/algo": meta(run=RUN_OK, group="base")})
        impl = self.impls()["c/algo"]
        ok, msg = hello.run_once(impl, impl["test"], argparse.Namespace(timeout=5))
        self.assertTrue(ok, msg)
        self.assertHas(hello.check_algorithms(hello.load_implementations()), "id must be 'algo'")

    def test_size_keys_must_be_numeric(self):
        d = definition()
        d["expected"]["abc"] = d["expected"]["5"]
        self.assertHas(self.errors({"algo": d}, {}), "is not a size")

    def test_required_metadata_fields(self):
        for key in ("name", "description", "source", "input"):
            for bad in (None, "", "  ", 3):
                d = definition()
                if bad is None:
                    del d[key]
                else:
                    d[key] = bad
                self.assertHas(self.errors({"algo": d}, {}), "missing or empty '%s'" % key)

    def test_bytes_is_required_and_positive(self):
        for bad in (None, 0, -3, "26", True):
            d = definition()
            if bad is None:
                del d["expected"]["5"]["bytes"]
            else:
                d["expected"]["5"]["bytes"] = bad
            self.assertHas(self.errors({"algo": d}, {}), "needs 'bytes' as a positive integer")

    def test_agreeing_must_be_distinct_slugs_of_existing_implementations(self):
        impls = {"a/algo": meta(run='./p "$BENCH_N"'), "b/algo": meta(run='./p "$BENCH_N"')}
        for bad in ("a", [1, 2], ["a", "a"], None):
            d = definition()
            d["expected"]["5"]["agreeing"] = bad
            self.assertHas(self.errors({"algo": d}, impls), "'agreeing' must be a list of distinct language slugs")
        d = definition()
        d["expected"]["5"]["agreeing"] = ["a", "zzz"]
        self.assertHas(self.errors({"algo": d}, impls), "lists 'zzz' as agreeing but languages/zzz/algo does not exist")
        d["expected"]["5"]["agreeing"] = ["a", "b"]
        self.assertEqual(self.errors({"algo": d}, impls), [])

    def test_agreeing_is_validated_for_published_sources_too_when_present(self):
        d = definition()
        d["expected"]["5"].update(source="benchmarks-game-output", agreeing=["nope"])
        self.assertHas(self.errors({"algo": d}, {}), "lists 'nope'")
        del d["expected"]["5"]["agreeing"]
        self.assertEqual(self.errors({"algo": d}, {}), [])

    def test_expected_must_be_a_non_empty_object_of_objects(self):
        for bad in (None, [], {}, "x"):
            d = definition()
            d["expected"] = bad
            self.assertHas(self.errors({"algo": d}, {}), "'expected' must map each size")
        d = definition()
        d["expected"]["7"] = "oops"
        self.assertHas(self.errors({"algo": d}, {}), "size 7 must be an object")

    def test_malformed_definition_files_are_errors_not_exceptions(self):
        good = definition("good")
        good["expected"]["5"].update(source="reference")
        del good["expected"]["5"]["agreeing"]
        make_tree(self.tmp, {"good": good}, {})
        with open(os.path.join(self.tmp, "algorithms", "broken.json"), "w") as fh:
            fh.write("{not json")
        write_json(os.path.join(self.tmp, "algorithms", "list.json"), [1, 2])
        errs = hello.check_algorithms(hello.load_implementations())
        self.assertHas(errs, "algorithms/broken.json: cannot read definition")
        self.assertHas(errs, "algorithms/list.json: definition must be a JSON object")
        self.assertEqual(len(errs), 2)

    def test_bench_n_token_forms(self):
        for run in ('./prog "$BENCH_N"', "./prog ${BENCH_N}", "./prog $BENCH_N", "prog '1' \"$BENCH_N\" # why"):
            with self.subTest(run=run):
                algos, impls = self.good()
                impls["c/algo"] = meta(run=run)
                self.assertEqual(self.errors(algos, impls), [])

    def test_bench_n_must_be_a_whole_name_outside_comments(self):
        for run in ("./prog 1000", "./prog $BENCH_NN", "./prog $MY_BENCH_N", "./prog 1000 # $BENCH_N",
                    "# $BENCH_N\n./prog 1000", ""):
            with self.subTest(run=run):
                algos, impls = self.good()
                impls["c/algo"] = meta(run=run)
                self.assertHas(self.errors(algos, impls), "must pass $BENCH_N")

    def test_hash_inside_quotes_is_not_a_comment(self):
        algos, impls = self.good()
        impls["c/algo"] = meta(run="./prog '#' \"$BENCH_N\"")
        self.assertEqual(self.errors(algos, impls), [])

    def test_implementation_without_definition(self):
        self.assertHas(self.errors({}, {"c/ghost": meta()}), "no algorithms/ghost.json")

    def test_implementation_needs_a_test(self):
        algos, impls = self.good()
        impls["c/algo"] = {"files": ["prog.txt"]}
        self.assertHas(self.errors(algos, impls), "needs a test")

    def test_compile_kind_does_not_verify_output(self):
        algos, impls = self.good()
        impls["c/algo"] = meta(run='cc "$BENCH_N"', kind="compile")
        self.assertHas(self.errors(algos, impls), "kind 'compile' does not verify output")

    def test_algorithms_must_use_docker(self):
        algos, impls = self.good()
        impls["c/algo"] = meta(run='./prog "$BENCH_N"', group="base")
        self.assertHas(self.errors(algos, impls), "pinned docker image")


class LoadAndReadme(TreeCase):
    def test_load_implementations_merges_language_and_meta(self):
        make_tree(self.tmp, {"algo": definition()}, {"c/algo": meta(), "c/hello-world": meta()})
        impls = self.impls()
        self.assertEqual(sorted(impls), ["c/algo", "c/hello-world"])
        i = impls["c/algo"]
        self.assertEqual((i["slug"], i["algorithm"], i["name"]), ("c", "algo", "C"))
        self.assertEqual([l["id"] for l in hello.load_languages()], ["c/hello-world"])

    def test_load_algorithms_reads_only_json_files(self):
        make_tree(self.tmp, {"algo": definition()})
        with open(os.path.join(self.tmp, "algorithms", "notes.txt"), "w") as fh:
            fh.write("x")
        self.assertEqual(list(hello.load_algorithms()), ["algo"])

    def test_load_algorithms_without_directory(self):
        self.assertEqual(hello.load_algorithms(), {})

    def render(self):
        make_tree(self.tmp, {"algo": definition()},
                  {"c/algo": meta(), "c/hello-world": meta(), "py/algo": meta(), "py/hello-world": meta()})
        return hello.render_readme(hello.load_languages(), hello.load_implementations(),
                                   hello.load_algorithms())

    def test_readme_is_deterministic(self):
        self.assertEqual(self.render(), self.render())

    def test_readme_lists_only_existing_implementations_and_claims_no_measurement(self):
        text = self.render()
        self.assertIn("2 implementations of 1 algorithms in 2 languages", text)
        self.assertIn("Nothing is measured yet", text)
        self.assertIn("| Measurement of time, memory and energy | none |", text)
        self.assertIn("[✅](languages/c/algo/)", text)
        self.assertIn("[✅](languages/py/algo/)", text)

    def test_readme_section_does_not_list_hello_world_as_an_algorithm(self):
        self.assertNotIn("`hello-world`](algorithms/", self.render())

    def test_readme_with_an_undefined_algorithm_does_not_raise_and_omits_it(self):
        make_tree(self.tmp, None, {"c/ghost": meta(), "c/hello-world": meta()})
        text = hello.render_readme(hello.load_languages(), hello.load_implementations(), {})
        self.assertNotIn("ghost", text)

    def test_readme_with_an_incomplete_definition_does_not_raise(self):
        make_tree(self.tmp, {"algo": {"id": "algo"}}, {"c/algo": meta(), "c/hello-world": meta()})
        hello.render_readme(hello.load_languages(), hello.load_implementations(), hello.load_algorithms())

    def test_readme_does_not_depend_on_input_order(self):
        make_tree(self.tmp, {"algo": definition()},
                  {"c/algo": meta(), "c/hello-world": meta(), "py/algo": meta(), "py/hello-world": meta()})
        impls = hello.load_implementations()
        a = hello.render_readme(hello.load_languages(), impls, hello.load_algorithms())
        langs = [i for i in impls if i["algorithm"] == "hello-world"]
        b = hello.render_readme(list(reversed(langs)), list(reversed(impls)), hello.load_algorithms())
        self.assertEqual(a, b)

    def test_cmd_readme_writes_identical_bytes_twice(self):
        make_tree(self.tmp, {"algo": definition()}, {"c/algo": meta(), "c/hello-world": meta()})
        out = []
        for _ in range(2):
            with contextlib.redirect_stdout(io.StringIO()):
                hello.cmd_readme(argparse.Namespace())
            with open(hello.README, "rb") as fh:
                out.append(fh.read())
        self.assertEqual(out[0], out[1])



class CmdCheck(TreeCase):
    def test_undefined_algorithm_is_reported_without_a_traceback(self):
        make_tree(self.tmp, None, {"c/ghost": meta(), "c/hello-world": meta()})
        with open(hello.README, "w") as fh:
            fh.write("stale")
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = hello.cmd_check(argparse.Namespace())
        self.assertEqual(rc, 1)
        self.assertIn("no algorithms/ghost.json", buf.getvalue())


    def test_unpinned_docker_image_and_missing_baseline_are_errors(self):
        make_tree(self.tmp, {"algo": definition()},
                  {"c/hello-world": meta(image="python:latest"), "d/algo": meta(run='./p "$BENCH_N"')})
        with open(hello.README, "w") as fh:
            fh.write("stale")
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = hello.cmd_check(argparse.Namespace())
        out = buf.getvalue()
        self.assertEqual(rc, 1)
        self.assertIn("docker image must be pinned to a version tag", out)
        self.assertIn("languages/d: missing the hello-world baseline", out)
        self.assertIn("README.md is out of date", out)


class ChangedScope(unittest.TestCase):
    """changed_scope on a real throwaway git repository."""

    def git(self, *args):
        env = dict(os.environ, GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_SYSTEM=os.devnull)
        subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", "-c", "commit.gpgsign=false",
                        *args], cwd=self.tmp, env=env, check=True, stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="hello-git-")
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        p = mock.patch.object(hello, "ROOT", self.tmp)
        p.start()
        self.addCleanup(p.stop)
        self.git("init", "-q", "-b", "base")
        for f in ("languages/c/hello-world/meta.json", "languages/py/algo/meta.json",
                  "algorithms/algo.json", "algorithms/other.json", "README.md", "scripts/hello.py",
                  ".github/workflows/hello-world.yml", ".github/ISSUE_TEMPLATE/bug.md", "docs/a.md"):
            self.write(f)
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "base")
        self.git("checkout", "-q", "-b", "work")

    def write(self, rel, text="x"):
        p = os.path.join(self.tmp, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w") as fh:
            fh.write(text)

    def scope(self, *changes, delete=(), rename=()):
        for rel in changes:
            self.write(rel, "changed")
        for rel in delete:
            os.remove(os.path.join(self.tmp, rel))
        for old, new in rename:
            os.makedirs(os.path.dirname(os.path.join(self.tmp, new)), exist_ok=True)
            os.rename(os.path.join(self.tmp, old), os.path.join(self.tmp, new))
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "work", "--allow-empty")
        return hello.changed_scope("base")

    def test_language_change_selects_that_slug(self):
        self.assertEqual(self.scope("languages/c/hello-world/meta.json"), ({"c"}, set()))

    def test_algorithm_definition_change_selects_that_algorithm(self):
        self.assertEqual(self.scope("algorithms/algo.json"), (set(), {"algo"}))

    def test_both_kinds_combine(self):
        self.assertEqual(self.scope("languages/py/algo/meta.json", "algorithms/other.json"),
                         ({"py"}, {"other"}))

    def test_docs_and_readme_select_nothing(self):
        self.assertEqual(self.scope("docs/a.md", "README.md"), (set(), set()))

    def test_scripts_change_means_run_everything(self):
        self.assertIsNone(self.scope("scripts/hello.py"))

    def test_workflow_change_means_run_everything(self):
        self.assertIsNone(self.scope(".github/workflows/hello-world.yml"))

    def test_other_github_files_do_not_force_everything(self):
        self.assertEqual(self.scope(".github/ISSUE_TEMPLATE/bug.md"), (set(), set()))

    def test_deleted_language_still_selects_its_slug(self):
        self.assertEqual(self.scope(delete=["languages/c/hello-world/meta.json"]), ({"c"}, set()))

    def test_rename_across_slugs_selects_the_destination(self):
        got = self.scope(rename=[("languages/c/hello-world/meta.json", "languages/py/hello-world/meta.json")])
        self.assertIn("py", got[0])  # git reports only the new path; the old slug has nothing left to run

    def test_rename_inside_a_slug(self):
        got = self.scope(rename=[("languages/c/hello-world/meta.json", "languages/c/other/meta.json")])
        self.assertEqual(got, ({"c"}, set()))

    def test_algorithm_definition_rename_selects_the_new_name(self):
        got = self.scope(rename=[("algorithms/algo.json", "algorithms/renamed.json")])
        self.assertEqual(got, (set(), {"renamed"}))

    def test_changes_on_the_base_branch_after_branching_are_ignored(self):
        self.git("checkout", "-q", "base")
        self.write("languages/c/hello-world/meta.json", "newer")
        self.git("commit", "-q", "-am", "base moves")
        self.git("checkout", "-q", "work")
        self.assertEqual(self.scope("docs/a.md"), (set(), set()))  # three-dot diff: merge-base semantics

    def test_no_changes(self):
        self.assertEqual(self.scope(), (set(), set()))

    def test_selected(self):
        c = {"slug": "c", "algorithm": "algo"}
        self.assertTrue(hello.selected(c, None))
        self.assertTrue(hello.selected(c, ({"c"}, set())))
        self.assertTrue(hello.selected(c, (set(), {"algo"})))
        self.assertFalse(hello.selected(c, ({"py"}, {"other"})))
        self.assertFalse(hello.selected(c, (set(), set())))


class SelectiveRun(TreeCase):
    """cmd_test --changed-since on a valid catalog in a throwaway git repository."""

    def git(self, *args):
        env = dict(os.environ, GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_SYSTEM=os.devnull)
        subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", "-c", "commit.gpgsign=false",
                        *args], cwd=self.tmp, env=env, check=True, stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)

    def run_changed(self):
        args = argparse.Namespace(changed_since="base", group=None, lang=None, algorithm=None,
                                  shard=None, strict=True, retries=0, timeout=10)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = hello.cmd_test(args)
        return rc, buf.getvalue()

    def test_only_the_changed_algorithm_runs(self):
        make_tree(self.tmp, {"algo": definition(), "other": definition("other")},
                  {"c/algo": meta(group="base"), "py/other": meta(run="false", group="base")})
        self.git("init", "-q", "-b", "base")
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "base")
        self.git("checkout", "-q", "-b", "work")
        write_json(os.path.join(self.tmp, "algorithms", "algo.json"), definition(description="changed"))
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "work")
        rc, out = self.run_changed()
        self.assertEqual(rc, 0, out)  # py/other would fail, so it must not have run
        self.assertIn("PASS c/algo", out)
        self.assertNotIn("py/other", out)

    def test_docs_only_change_runs_nothing_and_passes(self):
        make_tree(self.tmp, {"algo": definition()}, {"c/algo": meta(run="false", group="base")})
        self.git("init", "-q", "-b", "base")
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "base")
        self.git("checkout", "-q", "-b", "work")
        with open(os.path.join(self.tmp, "NOTES.md"), "w") as fh:
            fh.write("x")
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "docs")
        rc, out = self.run_changed()
        self.assertEqual(rc, 0, out)
        self.assertIn("0 passed, 0 failed", out)


class EndToEnd(unittest.TestCase):
    """Run a copy of scripts/hello.py against a temporary catalog, as CI does."""

    def run_script(self, impls, algos, *args):
        tmp = tempfile.mkdtemp(prefix="hello-e2e-")
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        os.makedirs(os.path.join(tmp, "scripts"))
        shutil.copy(SCRIPT, os.path.join(tmp, "scripts", "hello.py"))
        make_tree(tmp, algos, impls)
        return subprocess.run([sys.executable, os.path.join(tmp, "scripts", "hello.py"), "test",
                               "--strict", "--retries", "0", *args],
                              capture_output=True, text=True, timeout=60, env=clean_env())

    def test_correct_program_exits_zero(self):
        r = self.run_script({"c/algo": meta(group="base")}, {"algo": definition()})
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("1 passed, 0 failed", r.stdout)

    def test_wrong_program_exits_nonzero_and_prints_no_pass(self):
        r = self.run_script({"c/algo": meta(run="printf '1.5\\n9\\n'", group="base")}, {"algo": definition()})
        self.assertEqual(r.returncode, 1)
        self.assertNotIn("PASS", r.stdout)
        self.assertIn("0 passed, 1 failed", r.stdout)

    def test_wrong_checksum_in_the_definition_exits_nonzero(self):
        r = self.run_script({"c/algo": meta(group="base")}, {"algo": definition(sha="0" * 64)})
        self.assertEqual(r.returncode, 1)
        self.assertNotIn("PASS", r.stdout)
        self.assertIn("FAIL c/algo", r.stdout)

    def test_good_and_bad_together_still_fail_the_run(self):
        r = self.run_script({"c/algo": meta(group="base"),
                             "py/algo": meta(run="printf nope", group="base")}, {"algo": definition()})
        self.assertEqual(r.returncode, 1)
        self.assertIn("PASS c/algo", r.stdout)
        self.assertIn("FAIL py/algo", r.stdout)


class RepositoryState(unittest.TestCase):
    """Cheap invariants of the real tree, read-only (the full `check` runs in CI)."""

    def test_every_real_algorithm_definition_is_consistent(self):
        algos = hello.load_algorithms()
        self.assertTrue(algos)
        for aid, a in algos.items():
            self.assertEqual(a["id"], aid)
            self.assertIn(str(a["check"]), a["expected"])

    def test_real_catalog_passes_algorithm_rules(self):
        self.assertEqual(hello.check_algorithms(hello.load_implementations()), [])


if __name__ == "__main__":
    unittest.main()
