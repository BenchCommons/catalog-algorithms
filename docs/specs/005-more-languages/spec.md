# 005 — Ampliar a biblioteca de linguagens

## O quê
Adicionar algumas centenas de linguagens para tornar o repositório uma das coleções mais completas de Hello World: assembly e bytecode, shells, científicas, consultas, hardware/GPU, smart contracts, scripting de jogos, markup/templates, configuração/infra, mais linguagens de propósito geral, históricas e esotéricas.

## Requisitos
1. Cada linguagem segue o formato da spec 003.
2. Programa idiomático e mínimo; linguagens sem saída de texto (markup, config) mostram/geram "Hello World" da forma natural da linguagem.
3. Sempre que houver pacote no Ubuntu, a linguagem ganha `test` (spec 004).

## Critérios de aceite
- `scripts/hello.py check` passa e o workflow fica verde.

## Fora de escopo
- Linguagens cujo Hello World não pode ser escrito com confiança (ex.: Malbolge, Piet).
