# Plano — 007

- Harness: `kind`, grupo `docker`, `--shard`; README com selos e percentual.
- Linguagens divididas em 6 lotes, cada lote validado localmente (Docker com emulação amd64; apt via container `ubuntu:24.04`).
- Workflow: job `docker` em matriz de 4 shards.
