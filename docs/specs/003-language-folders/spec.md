# 003 — Uma pasta por linguagem e README gerado

## O quê
Mover cada Hello World para `languages/<slug>/` com um `meta.json`, e gerar o README a partir desses metadados (ver [ADR 0001](../../adr/0001-uma-pasta-por-linguagem.md)).

## Requisitos
1. Todo arquivo `HelloWorld*` da raiz migra para a pasta da sua linguagem, preservando o histórico (`git mv`).
2. `meta.json`: `name`, `files`, e pelo menos um de `section` ou `tiobe`; opcionais `year`, `notes`, `tags`, `test`.
3. `scripts/hello.py readme` gera o README; `scripts/hello.py check` valida metadados, arquivos e se o README está atualizado.
4. Sem dependências além da biblioteca padrão do Python 3.9+.

## Critérios de aceite
- `python3 scripts/hello.py check` passa.
- Nenhum `HelloWorld*` sobra na raiz.

## Fora de escopo
- Executar os programas (spec 004).
