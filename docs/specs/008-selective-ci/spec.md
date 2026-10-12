# 008 — CI seletivo nos PRs

Issue: #5.

## O quê
Nos pull requests, executar só os testes das linguagens alteradas; a suíte completa roda nos pushes para `master`, num agendamento diário e sob demanda.

## Requisitos
1. `scripts/hello.py test --changed-since <ref>`: seleciona as linguagens com arquivos alterados em `languages/<slug>/` desde `<ref>`.
2. Se `scripts/` ou `.github/workflows/` mudarem, todas as linguagens são testadas.
3. Um grupo sem linguagens selecionadas passa sem executar nada.
4. Workflow: `pull_request` usa `--changed-since` contra a base do PR; `push` em `master`, `schedule` (diário) e `workflow_dispatch` rodam tudo.

## Critérios de aceite
- Um PR que altera uma única linguagem executa só o teste dela.
- O job `check` continua validando todos os metadados e o README.

## Fora de escopo
- Um job por linguagem (avaliado na issue #5; a seleção resolve o custo principal sem multiplicar jobs).
