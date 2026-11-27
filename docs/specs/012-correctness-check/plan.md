# Plano — 012

- `scripts/hello.py`: `load_algorithms()`, `verify_algorithm()`, `check_algorithms()`, `changed_scope()`, filtro `--algorithm`. `run_once` exporta `BENCH_ALGORITHM` e `BENCH_N`, repassa as duas ao `docker run` e separa stdout de stderr para algoritmos.
- `algorithms/<id>.json` fica na raiz, fora de `languages/`, porque o algoritmo é compartilhado por todas as linguagens.
- O runner canônico (`run.sh` byte a byte igual em cada implementação, `BENCH_VERIFY_*`, `BENCH_RESULT_*`) está especificado em tools-benchmark/docs/specs/010-catalog-contract (rascunho em PR aberto no momento). Este repositório **não** o copia: quando o contrato estiver aprovado, uma spec de adoção (013) adapta `meta.json` e adiciona o runner.

## Decisões
- Verificar por SHA-256 de stdout em vez de diff de texto: é a regra da spec 010 e funciona igual para saída binária futura.
- `BENCH_N` no `test.run` em vez de um número fixo em cada `meta.json`: o tamanho `check` fica num lugar só (a definição).
- Docker obrigatório para algoritmos: os `base` usam as ferramentas do runner do GitHub, sem versão fixada, o que quebra a reprodutibilidade que a verificação precisa.
