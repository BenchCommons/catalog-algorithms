# 009 — Arrumação pós-mudança

Issue: #11.

## O quê
O repositório saiu de `matbrgz/Hello-World` para `BenchCommons/catalog-algorithms` e passa a ser o catálogo de implementações de algoritmos clássicos em várias linguagens. Atualizar as referências ao endereço antigo e a apresentação do README para o novo propósito, mantendo o README gerado.

## Requisitos
1. `REPO` em `scripts/hello.py` passa a ser `BenchCommons/catalog-algorithms`; selo de CI, contribuidores e links do README derivam dele.
2. Nenhuma referência a `matbrgz/Hello-World` fora de `languages/` e do histórico de specs concluídas.
3. A introdução do README, gerada por `scripts/hello.py readme`, descreve o catálogo de algoritmos clássicos (medidos com perfratio via benchmark-tool) e apresenta o Hello World como a linha de base de custo de inicialização de cada linguagem.
4. A introdução aponta para a issue #11 e para `docs/specs/ROADMAP.md`.
5. O README continua sem edição manual: toda mudança passa pelo gerador.

## Critérios de aceite
- `python3 scripts/hello.py check` passa com 0 erros.
- `grep -rn "matbrgz/Hello-World" --exclude-dir=languages --exclude-dir=docs .` não encontra nada.
- O selo de CI do README aponta para `BenchCommons/catalog-algorithms`.

## Fora de escopo
- Renomear o workflow `hello-world.yml` ou o script `scripts/hello.py` (a nova estrutura vem na spec 011).
- Conjunto de algoritmos e E/S canônica (spec 010).
- O PR #10 (retentativas no CI), já integrado a `master` antes desta spec.
