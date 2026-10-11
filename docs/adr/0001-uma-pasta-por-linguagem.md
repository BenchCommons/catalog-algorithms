# 0001 — Uma pasta por linguagem com metadados em `meta.json`

## Status
Aceito (2026-10-11).

## Contexto
Com centenas de linguagens, a estrutura plana na raiz empurra o README para o fim da listagem do GitHub, gera colisões de extensão (`.m`, `.st`, `.pl`, `.alg`…) resolvidas com nomes como `HelloWorld(MATLAB).m`, e obriga cada contribuição a editar o README à mão, o que causa conflitos de merge entre PRs.

## Decisão
- Cada linguagem vive em `languages/<slug>/`, com o programa `HelloWorld.<ext>` (ou o nome que a linguagem exige, ex.: `Makefile`) e um `meta.json` com nome, seção, ano, notas, posição no TIOBE e o comando de teste.
- O README é gerado a partir dos `meta.json` por `scripts/hello.py readme`; o CI falha se o README estiver desatualizado.

## Consequências
- Colisões de extensão deixam de existir; os nomes com parênteses somem.
- Uma contribuição toca só a própria pasta (mais o README regenerado).
- Links antigos para arquivos na raiz quebram.
