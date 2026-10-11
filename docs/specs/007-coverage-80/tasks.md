# Tarefas — 007

- [x] Harness (`kind`, `docker`, `--shard`).
- [x] Testes por lote.
- [x] Job `docker` no workflow.
- [x] CI verde.
- [ ] Reativar testes que passam localmente mas falham no runner (removidos do `meta.json` no commit seguinte a cd50685; definições anteriores no histórico do git):
  - `dbase` (Harbour: `hbrun: not found`), `emojicode` (`emojicodec: not found`), `newtonscript` (tarball não extraído),
    `v` (`/tmp/v/v: not found`), `x10` (`X10Launcher: required file not found`), `pl-i` (toolchain 32-bit: `ld: cannot find hello.o`),
    `agda` (apt, sem saída; provável timeout), `vale` (imagem sem `libz.so.1`).
  - Pista: 5 das 6 falhas Docker usam a tag móvel `buildpack-deps:bookworm`; "not found" em arquivo existente costuma indicar interpretador ELF ausente.
