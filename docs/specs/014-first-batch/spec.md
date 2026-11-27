# 014 — Primeiro lote de implementações

Issue: #11. Depende da 010, 011 e 012.

## O quê
Implementar três algoritmos numéricos da spec 010 em três linguagens, com saída verificada no CI. É um corte vertical: pouco, completo e reproduzível.

## Escolha do recorte
Cobertura real verificada em `languages/` (452 linguagens, 377 com teste) e custo de CI:

| Critério | Resultado |
|---|---|
| Algoritmos sem dependência externa | os cinco numéricos. `merge-sort`, `binary-search` e `sha-256` dependem de [tools-dataset#1](https://github.com/BenchCommons/tools-dataset/issues/1), aberta, e ficam fora |
| Checksums independentes | `n-body`, `fannkuch-redux` e `spectral-norm` têm saída publicada no Benchmarks Game, e o SHA-256 dela é o da spec 010. `binary-trees` e `mandelbrot` ficam para outro lote (a conferência de `mandelbrot` está em aberto na spec 010) |
| Linguagens | `c`, `javascript` e `python`: toolchains já usados no catálogo em imagens fixadas (`gcc:14.3.0`, `node:22.20.0-slim`, `python:3.12.11-slim`), reaproveitadas do cache dos testes de Hello World |
| Custo de CI | 9 execuções no tamanho `check`, cada uma em menos de 1 s além do pull e da compilação; entram nos 4 shards do job `docker` |

## Requisitos
1. Implementações escritas à mão, seguindo a definição do Benchmarks Game, em `languages/{c,javascript,python}/{n-body,fannkuch-redux,spectral-norm}/`. Sem bibliotecas além da padrão (`math`, `stdio`).
2. C compilado com `gcc -O2 -ffp-contract=off`, para que contração de multiplicação e soma (FMA) não mude os bits do resultado em outras arquiteturas.
3. Cada `meta.json` usa `group: docker`, imagem fixada e `$BENCH_N`.
4. Definições em `algorithms/` com checksums de todos os tamanhos da spec 010 (R3). Saídas do tamanho `check` coincidem com os arquivos publicados; as dos demais tamanhos foram produzidas por C e JavaScript (e Python nos pequenos) com SHA-256 idêntico.

## Resultado
| Algoritmo | `check` | SHA-256 do `check` |
|---|---|---|
| `n-body` | 1000 | `76de83d6d51a74f82828547423f516e7815cfe8cfea6290a2831aa173f806de7` |
| `fannkuch-redux` | 7 | `2dc0a3cd4a547ba69389f97f3b447bd4d487fe6216c3cacd2f9bf8c908dc127f` |
| `spectral-norm` | 100 | `a95e11fa07f7b196ef488e73f67afbbbc16cf6a2c6de5f8d54ea49821fe604e6` |

Os outros tamanhos estão em `algorithms/<id>.json`.

## Fora de escopo
- Medição de qualquer tipo (depende de tools-benchmark#29 e #30).
- `binary-trees`, `mandelbrot` e os algoritmos de nomes.
- Mais linguagens.
