# 004 — Testes com GitHub Actions

## O quê
Workflow que, a cada push e PR, valida a estrutura e executa os Hello Worlds que têm toolchain disponível no runner, conferindo que a saída contém "Hello World".

## Requisitos
1. Job `check`: `python3 scripts/hello.py check`.
2. Jobs de execução por grupo (`base`, `apt`, `extra`), cada um rodando `scripts/hello.py test --group <g> --strict`.
3. Comparação tolerante: minúsculas, só letras, deve conter `helloworld` (aceita "Hello, World!", "hello world"...).
4. Cada teste roda numa cópia temporária da pasta, com timeout.
5. Localmente, linguagens sem toolchain são puladas; com `--strict`, toolchain ausente é falha.

## Critérios de aceite
- Workflow verde no PR.
- `meta.json` sem `test` é aceito (linguagem não executável no CI) e aparece como "not tested" no resumo.

## Fora de escopo
- Executar linguagens sem pacote no Ubuntu (esotéricas, proprietárias, gráficas).
