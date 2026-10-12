# Plano — 010

Esta spec é só documentação: ela fixa as definições que as specs 011 a 014 vão usar.

## Definições dos algoritmos
- Os cinco numéricos seguem o texto de cada benchmark no Benchmarks Game (constantes, número de iterações, formato da saída). Onde houver ambiguidade, vale a implementação de referência em C do próprio Benchmarks Game.
- `merge-sort`: top-down, estável, comparando os nomes byte a byte em UTF-8; o resultado vai para o stdout, um nome por linha.
- `binary-search`: busca clássica em lista ordenada por bytes UTF-8; para cada consulta encontrada, soma o índice (base 0) módulo 1000000007; imprime a contagem e a soma.
- `sha-256`: FIPS 180-4 escrito à mão, aplicado aos bytes do arquivo de entrada como estão (incluindo os `\n`).

## Implementação de referência
- Uma implementação de referência por algoritmo calcula as saídas esperadas e os checksums de todos os tamanhos. Onde ela mora e como roda é decidido na spec 011 (layout) e na 012 (verificação).
- Os valores de `check` desta spec foram calculados assim (Python 3, mesmo algoritmo das implementações em C do Benchmarks Game).
- Os tamanhos grandes dos numéricos são conferidos com as saídas publicadas pelo Benchmarks Game, e não só com a implementação de referência.

## Entradas de nomes
- O catálogo não gera amostras: consome as do contrato de entradas (dataset-tool#1). As necessidades do R1.3 são comentadas em dataset-tool#1 e dataset-names#24.
- A lista ordenada de `binary-search` é uma entrada derivada: um passo determinístico, fora da medição, ordena a amostra por bytes e registra o SHA-256.
- Se a release do dataset-names tiver menos de 1 000 000 nomes distintos, o maior tamanho passa a ser o total da release, registrado com a versão.

## Contrato de catálogo
- O mapeamento do R6 vira um comentário em benchmark-tool#29: ids do tipo de teste `algorithm`, parâmetro `n`, tamanhos, referência da entrada e checksums esperados.
- Nada aqui depende de detalhes do contrato que ainda não existem; quando ele for definido, a spec 011 adapta o layout e os metadados.

## Decisões
- Saída comparada byte a byte (só CRLF normalizado) em vez de tolerância numérica: os formatos `%.9f` do Benchmarks Game já são estáveis entre linguagens que usam IEEE 754 de 64 bits.
- Ordem de bytes UTF-8 em vez de collation: resultado idêntico em qualquer linguagem e sistema.
- Funções prontas de ordenação, busca e hash proibidas: mede-se a linguagem, não a biblioteca em C do runtime.
