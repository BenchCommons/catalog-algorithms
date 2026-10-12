# AGENTS.md — catalog-algorithms

Follow the org-wide rules in [BenchCommons/.github AGENTS.md](https://github.com/BenchCommons/.github/blob/main/AGENTS.md) and the decisions in [.product](https://github.com/BenchCommons/.product). This file only adds what is specific to this repo.

## Role
Catalog (`catalog-*`): classic algorithm implementations across languages. It currently holds Hello World in 452 languages. Roadmap: issue #11.

## Layout and commands
- `languages/<slug>/`: the program plus `meta.json` (name, files, section, tiobe, test).
- `python3 scripts/hello.py check`: metadata, files and README consistency. CI requires it.
- `python3 scripts/hello.py readme`: regenerates `README.md`. Never edit the README by hand.
- `python3 scripts/hello.py test [--lang X] [--changed-since origin/master]`: runs programs and checks that the output contains "Hello World".
- Test groups: `base`, `apt`, `extra`, `docker` (pinned image; one platform per image), `macos`, `windows`. `kind: compile` is only for languages that cannot print.

## Rules
- Use the real implementation of the language. Never fake a test.
- Pin images, packages and release URLs. Use `curl -f --retry` for downloads.
