# 010 — Conjunto de algoritmos e E/S canônica

Issue: #11.

## O quê
Escolher o primeiro conjunto de algoritmos clássicos do catálogo e definir, para cada um, a entrada canônica (parametrizada por um tamanho `n` e determinística), a saída esperada com checksum e a regra que confirma a correção numa execução sem medição antes de qualquer medida. Esta spec define **o que** cada implementação calcula e imprime. O formato das pastas, o runner e os marcadores de resultado pertencem ao contrato de catálogo ([benchmark-tool#29](https://github.com/BenchCommons/benchmark-tool/issues/29)), e o formato das entradas pertence ao contrato de entradas ([dataset-tool#1](https://github.com/BenchCommons/dataset-tool/issues/1)). Esta spec referencia os dois e não os redefine.

## Por quê
- Comparar linguagens exige que todas façam exatamente o mesmo trabalho sobre exatamente a mesma entrada, e que a saída prove isso.
- O Hello World mede só o custo de inicialização. Os algoritmos medem computação numérica, alocação de memória, recursão, inteiros, strings e bytes.
- Partir de benchmarks conhecidos permite comparar com resultados publicados e reaproveitar saídas de referência já conferidas por muitas implementações.

## Conjunto inicial

| Id | Algoritmo | O que exercita | Origem | Entrada |
|---|---|---|---|---|
| `hello-world` | Hello World | inicialização do runtime | este repositório | nenhuma |
| `n-body` | simulação de 5 corpos (planetas jovianos) | ponto flutuante, laços apertados | Benchmarks Game | `n` (passos) |
| `fannkuch-redux` | inversões de prefixo em permutações | inteiros, arrays pequenos | Benchmarks Game | `n` (tamanho da permutação) |
| `spectral-norm` | norma espectral de uma matriz infinita truncada | ponto flutuante, produto matriz-vetor | Benchmarks Game | `n` (ordem da matriz) |
| `binary-trees` | criação e percurso de árvores binárias | alocação e coleta de memória, recursão | Benchmarks Game | `n` (profundidade máxima) |
| `mandelbrot` | conjunto de Mandelbrot em bitmap PBM | ponto flutuante, bits, saída binária | Benchmarks Game | `n` (largura e altura) |
| `merge-sort` | ordenação estável por intercalação de nomes | comparação de strings, cópia de memória | clássico | `n` nomes do dataset-names |
| `binary-search` | busca binária de nomes numa lista ordenada | acesso aleatório, comparação de strings | clássico | `n` nomes ordenados e `n` consultas |
| `sha-256` | resumo SHA-256 (FIPS 180-4) dos bytes da entrada | inteiros de 32 bits, rotações, bytes | clássico | `n` nomes do dataset-names |

### Critérios da escolha
1. **Linhagem do Benchmarks Game** para os cinco numéricos: definições estáveis desde os anos 2000, saídas de referência públicas e milhares de implementações já conferidas. Ficaram de fora `fasta`, `k-nucleotide`, `reverse-complement`, `regex-redux` e `pidigits`, porque dependem de E/S de gigabytes, de expressões regulares ou de bignum, que muitas linguagens do catálogo não têm. Podem entrar numa spec futura.
2. **Algoritmos sobre o dataset-names** para texto real: nomes em UTF-8 de várias escritas, com tamanhos variados, que exercitam strings de um jeito que os benchmarks numéricos não fazem.
3. **Implementação escrita à mão** em `merge-sort`, `binary-search` e `sha-256`. As funções prontas da biblioteca padrão (`sort`, `bsearch`, `hashlib`) são proibidas, para que se meça a linguagem e não uma rotina em C embutida no runtime. Os cinco numéricos seguem as regras de cada benchmark no Benchmarks Game.
4. **Viável para a maioria das linguagens**: nenhum algoritmo exige bignum, threads, regex ou bibliotecas externas. Paralelismo é opcional e não faz parte da definição.

## Requisitos

### R1. Entrada canônica
1. Todo algoritmo recebe um único parâmetro de tamanho `n`, inteiro positivo.
2. Os cinco numéricos não leem arquivo: a entrada é só `n`, e as constantes (por exemplo, as condições iniciais do `n-body`) fazem parte da definição do algoritmo.
3. `merge-sort`, `binary-search` e `sha-256` leem amostras de nomes entregues pelo **contrato de entradas** de [dataset-tool#1](https://github.com/BenchCommons/dataset-tool/issues/1), a partir de uma release do [dataset-names](https://github.com/BenchCommons/dataset-names) fixada por versão e checksum ([dataset-names#24](https://github.com/BenchCommons/dataset-names/issues/24)). Formato, codificação, semente e checksum da amostra são os do contrato. Do lado do catálogo valem estas necessidades, que serão levadas à issue dona:
   - amostra de `n` nomes distintos de `given_names`, sem reposição, com semente fixa;
   - UTF-8 sem BOM, um nome por linha, cada linha terminada por `\n` (LF);
   - para `binary-search`, uma segunda amostra de `n` consultas com outra semente, tirada do conjunto completo, de modo que parte das consultas não esteja na lista.
4. Entradas derivadas (a lista ordenada de `binary-search`) são produzidas por um passo determinístico, fora da medição, e têm o próprio SHA-256 registrado.
5. A forma de invocar o programa (argumentos, stdin, variáveis de ambiente) é a do runner canônico do contrato de catálogo. Enquanto ele não existe, a convenção proposta é `<programa> <n>` para os numéricos e `<programa> <arquivo>` (ou `<arquivo-lista> <arquivo-consultas>`) para os de nomes.

### R2. Saída esperada por algoritmo
A saída canônica é o stdout completo, em bytes. A comparação normaliza só fim de linha (CRLF para LF).

| Id | Saída canônica |
|---|---|
| `hello-world` | contém `Hello World` (regra atual de `scripts/hello.py test`) |
| `n-body` | energia antes e depois da simulação, cada uma com 9 casas decimais (`%.9f`), uma por linha |
| `fannkuch-redux` | linha 1: checksum (soma alternada dos flips por permutação); linha 2: `Pfannkuchen(<n>) = <máximo de flips>` |
| `spectral-norm` | a norma com 9 casas decimais (`%.9f`) |
| `binary-trees` | as linhas `stretch tree`, `<iterações>\t trees of depth <d>\t check: <c>` e `long lived tree`, no formato do Benchmarks Game |
| `mandelbrot` | arquivo PBM binário (`P4\n<n> <n>\n` seguido dos bits), 50 iterações, limite 4.0 |
| `merge-sort` | os `n` nomes ordenados por ordem de bytes UTF-8 (equivale à ordem de code points), um por linha, terminados por `\n` |
| `binary-search` | linha 1: quantas consultas foram encontradas; linha 2: soma dos índices (base 0) encontrados, módulo 1000000007 |
| `sha-256` | o resumo SHA-256 do arquivo de entrada inteiro, em hexadecimal minúsculo, seguido de `\n` |

- Ordem de bytes evita collation dependente de locale, que muda entre linguagens e sistemas.
- O módulo 1000000007 cabe em inteiro de 32 bits com sinal após cada soma, para linguagens sem inteiros de 64 bits.

### R3. Tamanhos
Cada algoritmo tem um tamanho `check` (rápido, para a verificação de correção e para o CI) e tamanhos de medição.

| Id | `check` | medição |
|---|---|---|
| `n-body` | 1000 | 50 000; 5 000 000; 50 000 000 |
| `fannkuch-redux` | 7 | 9; 10; 12 |
| `spectral-norm` | 100 | 500; 2000; 5500 |
| `binary-trees` | 10 | 14; 18; 21 |
| `mandelbrot` | 200 | 1000; 4000; 16 000 |
| `merge-sort`, `binary-search`, `sha-256` | 1000 | 100 000; 1 000 000 (ou o maior tamanho que a release do dataset-names oferecer) |

Os maiores tamanhos numéricos são os do Benchmarks Game, o que permite comparar com resultados publicados. Os menores existem para que linguagens lentas (interpretadores esotéricos, shells) consigam terminar.

### R4. Saídas de referência e checksums
1. Toda combinação (algoritmo, tamanho) tem uma saída esperada e o SHA-256 dela, registrados junto da definição do algoritmo.
2. Para os numéricos, a saída esperada vem de uma implementação de referência e é conferida contra a saída publicada pelo Benchmarks Game quando ela existe. Valores no tamanho `check`, obtidos com a implementação de referência:

| Id | `n` | Saída | SHA-256 da saída |
|---|---|---|---|
| `n-body` | 1000 | `-0.169075164` / `-0.169087605` | `76de83d6d51a74f82828547423f516e7815cfe8cfea6290a2831aa173f806de7` |
| `fannkuch-redux` | 7 | `228` / `Pfannkuchen(7) = 16` | `2dc0a3cd4a547ba69389f97f3b447bd4d487fe6216c3cacd2f9bf8c908dc127f` |
| `spectral-norm` | 100 | `1.274219991` | `a95e11fa07f7b196ef488e73f67afbbbc16cf6a2c6de5f8d54ea49821fe604e6` |
| `binary-trees` | 10 | 6 linhas, de `stretch tree of depth 11\t check: 4095` a `long lived tree of depth 10\t check: 2047` | `b7f92c56b5d8aeb0a4d698842d1d87a57b4909865c3c84e5e10313e16663c3cb` |
| `mandelbrot` | 200 | PBM de 5011 bytes | `97610473750700638fc63d13cfa49d339b67c18e7f26b3f9c9acb61e746472d5` |

3. Para os algoritmos de nomes, a saída esperada é calculada a partir da amostra fixada (ordenação por bytes, busca, `sha256sum`) e muda só quando a versão da release do dataset-names muda.
4. `sha-256` também tem de reproduzir os vetores de teste do FIPS 180-4 (`abc`, a mensagem vazia e a de 448 bits).

### R5. Correção antes da medição
1. Antes de qualquer medida, a implementação roda **sem medição** no tamanho `check`, e a saída tem de ser idêntica à esperada (R2 e R4). Se falhar, a implementação não é medida.
2. Antes de medir num tamanho `n`, há uma execução sem medição nesse `n` cujo SHA-256 do stdout tem de bater com o checksum esperado. As execuções medidas não são usadas para conferir a correção.
3. Uma falha de correção é registrada como resultado da implementação naquele tamanho (falhou, com o motivo) e nunca vira um número de desempenho.
4. O mecanismo (comandos, harness, marcadores) é o da spec 012 e do contrato de catálogo. Esta spec fixa só a regra e os dados esperados.

### R6. Relação com o contrato de catálogo
O contrato de catálogo é de [benchmark-tool#29](https://github.com/BenchCommons/benchmark-tool/issues/29) e não é redefinido aqui. Esta spec entrega ao contrato:
- os ids dos algoritmos, que são os valores do tipo de teste `algorithm` proposto lá, com o parâmetro de tamanho `n`;
- para cada algoritmo, os tamanhos `check` e de medição, a referência da entrada (versão e checksum da release, via dataset-tool) e os checksums das saídas esperadas;
- a regra de correção do R5, que alimenta a verificação sem medição do contrato.

Ficam com o contrato: o layout de cada implementação, o esquema de metadados, o Dockerfile fixado, o runner canônico, os marcadores de resultado e o esquema dos resultados. A saída de medição é a do perfratio ([perfratio#240](https://github.com/BenchCommons/perfratio/issues/240)). O `hello-world` entra no contrato como linha de base: seu tempo e sua memória são o custo de inicialização da linguagem, a ser separado do tempo do algoritmo.

## Critérios de aceite
- Cada algoritmo do conjunto tem id, definição, entrada canônica, tamanhos, formato de saída e regra de correção.
- Os valores de referência no tamanho `check` dos numéricos foram conferidos contra o Benchmarks Game.
- As necessidades de entrada do R1.3 estão registradas em dataset-tool#1, e a lista do R6 em benchmark-tool#29.
- A spec não define layout de pastas, runner, marcadores nem formato de arquivo de entrada.

## Fora de escopo
- O layout `languages/<lang>/<algoritmo>/` e os metadados por implementação (spec 011).
- O harness da verificação de correção (spec 012).
- Medição, publicação de resultados e o uso do perfratio (spec 013).
- As implementações em si (spec 014).
- Variantes paralelas ou com várias threads.
