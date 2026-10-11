# 001 — Expandir linguagens e reorganizar o README

## O quê
Cobrir com um programa "Hello World" todas as linguagens do TIOBE Index (top 100, snapshot de setembro de 2026), as linguagens historicamente marcantes e as linguagens modernas em evidência, e reorganizar o README como um catálogo navegável.

## Por quê
O README listava ~60 linguagens em texto corrido, com descrições duplicadas e sem critério de organização. Vários arquivos tinham extensão ou sintaxe incorreta (Prolog em sintaxe qmake, Fortran fixed-form inválido, Delphi sem programa executável, Solidity incompatível com compiladores atuais).

## Requisitos
1. Toda linguagem do TIOBE 1–100 tem um arquivo correspondente (ou mapeamento explícito para um arquivo existente, ex.: ML → Standard ML).
2. Linguagens puramente gráficas (Scratch, LabVIEW, Ladder Logic) têm uma representação textual declarada como tal.
3. Arquivos seguem `HelloWorld.<ext>`; em colisão de extensão, `HelloWorld(<Linguagem>).<ext>`.
4. README agrupa linguagens em: TIOBE Top 50, TIOBE 51–100, Históricas, Modernas/Hype, Esotéricas & Outras, com link para cada arquivo.

## Critérios de aceite
- Todo link do README aponta para um arquivo existente (verificável por script).
- Arquivos executáveis com toolchain disponível localmente imprimem "Hello World".

## Fora de escopo
- CI que compila todas as linguagens.
- Reorganizar arquivos em diretórios.
