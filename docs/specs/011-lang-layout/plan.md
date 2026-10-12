# Plano — 011

- Script de migração único (fora do repo): para cada `languages/<lang>/`, `git mv` dos programas para `hello-world/`, gera `language.json` com os campos de linguagem do `meta.json` atual e `hello-world/meta.json` com `files` e `test`.
- `scripts/hello.py`:
  - `load_implementations()` lê `language.json` e cada `*/meta.json`, e devolve entradas com `slug` (linguagem), `algorithm`, `id = <lang>/<algoritmo>` e `dir`. As funções de README usam as entradas `hello-world`.
  - `check` valida `language.json`, cada `meta.json` de algoritmo, arquivos listados, arquivos não listados e ids de algoritmo em kebab-case.
  - `test` e `apt-packages` iteram sobre implementações. `--lang` filtra por linguagem e `--changed-since` seleciona pela linguagem do caminho alterado.
- Contrato de catálogo (benchmark-tool spec 010): glob `languages/*/*`, linguagem = diretório pai, algoritmo = diretório folha. A correção do exemplo é feita lá.
