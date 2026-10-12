# Plano — 008

- `git diff --name-only <ref>...HEAD` dentro do harness.
- `actions/checkout` com `fetch-depth: 0` nos jobs de teste para ter a base do PR.
- Variável `HELLO_CHANGED_SINCE` no workflow, vazia fora de PRs.
