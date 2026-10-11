# 007 — Cobertura de 80%

## O quê
Levar a cobertura de testes no CI para perto de 80% das linguagens.

## Decisões do mantenedor (2026-10-11)
- Validação sem execução conta como teste, com selo próprio no README: ✅ executado e saída conferida; 🔧 compilado/validado pela ferramenta oficial.
- Programas que abrem diálogos gráficos (MsgBox, display dialog) podem passar a usar a saída de console idiomática da linguagem.

## Requisitos
1. `test.kind`: `run` (padrão) ou `compile`; `compile` só quando a linguagem não imprime texto ou só existe compilador/validador livre.
2. Grupo `docker`: imagem fixada em versão exata (`latest` é rejeitado pelo `check`), executada com `--platform linux/amd64`.
3. `--shard I/N` no `test` para dividir o grupo `docker` em jobs paralelos.
4. Mesmas regras da spec 006: implementação real da linguagem, nunca simular a saída.

## Critérios de aceite
- Workflow verde; README mostra a contagem de ✅ e 🔧 e o percentual.

## Fora de escopo
- Linguagens proprietárias sem runtime livre, gráficas ou extintas sem implementação.
