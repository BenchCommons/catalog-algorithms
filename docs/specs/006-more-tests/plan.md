# Plano — 006

- `scripts/hello.py`: grupos `macos` e `windows`; o workflow roda `python` no Windows.
- PostgreSQL já vem no runner Ubuntu: o grupo `extra` inicia o serviço para testar PL/pgSQL.
- Validação local: `docker run ubuntu:24.04` com os pacotes do grupo `apt` e `scripts/hello.py test --lang ...`.
