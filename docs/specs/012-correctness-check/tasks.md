# Tarefas — 012

- [x] Definições `algorithms/<id>.json` com checksums e origem.
- [x] Verificador em `scripts/hello.py test` (stdout, SHA-256, CRLF).
- [x] Regras novas em `check` e README gerado.
- [x] CI seletivo por algoritmo.
- [x] Teste negativo: checksum adulterado e programa errado falham.
- [x] CI completo verde no PR (jobs `docker`, macOS e Windows verdes no commit 8ab303e; o PR é seletivo, veja a spec 008).
- [ ] Adoção do runner canônico quando tools-benchmark#29 estiver aprovado (spec 013).
