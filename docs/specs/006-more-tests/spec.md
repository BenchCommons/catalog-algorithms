# 006 — Ampliar a cobertura de testes

## O quê
Aumentar o número de linguagens executadas no CI (spec 004), usando todos os caminhos viáveis num runner do GitHub.

## Requisitos
1. Novos grupos de teste `macos` (runner `macos-latest`) e `windows` (runner `windows-latest`), para linguagens que só existem nessas plataformas.
2. Pacotes apt do Ubuntu 24.04, `pipx` e `npx` para linguagens com implementação empacotada.
3. Linguagens de markup e configuração são testadas pela renderização ou leitura natural (pandoc, xmllint, asciidoctor, jq, yq, tomllib), conferindo que o resultado contém "Hello World".
4. Interpretadores próprios em `scripts/esolang.py` para esotéricas pequenas (Befunge-93, HQ9+, Unlambda, Whitespace), além de Brainfuck, Ook! e COW.
5. Cada linguagem é testada com a implementação dela ou uma implementação compatível da mesma linguagem, nunca de outra.

## Critérios de aceite
- Workflow verde com os novos grupos.
- Comandos novos do grupo `apt` validados num container `ubuntu:24.04` antes do push.

## Fora de escopo
- Linguagens proprietárias (SAS, MATLAB, LabVIEW…) e as que exigem hardware ou serviços externos.
