# 012 — Verificação de correção sem medição

Issue: #11. Depende da 010 (saídas e checksums) e da 011 (layout).

## O quê
Fixar **como este repositório** confere a saída de cada implementação de algoritmo contra a saída canônica, sem medir nada, e onde ficam os checksums esperados. A regra de correção é a do R5 da spec 010; esta spec entrega a parte que mora no catálogo.

## O que não é
- Não é o runner canônico nem os marcadores de resultado. Eles pertencem ao contrato de catálogo ([tools-benchmark#29](https://github.com/BenchCommons/tools-benchmark/issues/29), spec 010 de lá, `BENCH_VERIFY_OK`/`BENCH_VERIFY_FAIL`). Esta spec não os redefine nem os implementa.
- Não mede tempo, memória nem energia. Medir depende do contrato (#29) e do perfratio (#30), ainda abertos.

## Requisitos
1. **Definição por algoritmo** em `algorithms/<id>.json`: `id`, `name`, `description`, `source`, `input`, `check` (tamanho `n` da verificação rápida) e `expected`, um mapa `"<n>"` para `{sha256, bytes, source, agreeing}`.
2. `expected[<n>].source` é uma de:
   - `benchmarks-game-output`: o SHA-256 é o do arquivo de saída publicado pelo Benchmarks Game, byte a byte;
   - `cross-language`: duas ou mais implementações independentes deste catálogo (`agreeing`) produziram o mesmo SHA-256; o valor não é cópia de arquivo publicado;
   - `reference`: saída de uma implementação de referência única (reservado; nenhum valor usa hoje).
3. **Entrada.** O tamanho chega à implementação pela variável de ambiente `BENCH_N`, e o id do algoritmo por `BENCH_ALGORITHM`. São os nomes que o contrato de catálogo usa na tabela de ambiente do runner; aqui só o verificador local as define.
4. **Verificação.** `python3 scripts/hello.py test` executa o `test.run` de cada implementação de algoritmo com `BENCH_N = check`, captura **só o stdout**, troca CRLF por LF e compara o SHA-256 com `expected[check].sha256`. Passa se o código de saída é 0 e os checksums são iguais. Qualquer outra coisa falha, com os dois checksums, o início do stdout e o fim do stderr na mensagem.
5. **Isolamento.** Implementações de algoritmo rodam em imagem Docker com tag fixada (`test.group = docker`), uma plataforma por imagem (regra existente do `check`).
6. **`check` (estático).** Falha, com uma mensagem por problema e sem traceback, se: `algorithms/<id>.json` não é JSON válido ou não é um objeto; `id` difere do nome do arquivo; falta `name`, `description`, `source` ou `input` (texto não vazio); `check` não é um inteiro positivo (`true` não vale); falta `expected[check]`; um tamanho não tem `sha256` hexadecimal minúsculo de 64 caracteres, `bytes` inteiro positivo ou `source` conhecida; `agreeing`, quando existe (obrigatório em `cross-language`, com 2 ou mais), não é uma lista de slugs distintos de linguagens que têm esse algoritmo; um diretório de algoritmo não tem definição; uma implementação de algoritmo não tem `test`, usa `kind: compile`, não usa `docker` ou não menciona a variável `BENCH_N` como nome inteiro fora de comentários de shell. O `check` não consegue provar que o programa de fato recebe `$BENCH_N` (por exemplo `echo $BENCH_N; ./prog 1000` passa); isso é coberto pelo teste de verificação.
7. **CI seletivo.** `--changed-since` seleciona também as implementações de um algoritmo cuja definição mudou. Mudanças em `scripts/` ou nos workflows continuam rodando tudo.
8. **README.** A tabela de algoritmos do README é gerada por `scripts/hello.py readme` a partir das definições e dos `meta.json`. Só aparece ✅ para o que existe e é testado. O README não afirma medição.
9. **Novas tentativas.** `hello.py test --retries N` (padrão 2) repete só falhas que não dizem nada sobre a correção do programa. Para algoritmos: falha de infraestrutura do Docker ou do registro (`docker run` com código 125, pull, `toomanyrequests`, daemon indisponível) e timeout. Uma saída errada, um código de saída diferente de zero do programa, um erro de compilação ou a falta de definição utilizável nunca são repetidos e falham de imediato. Um algoritmo sem `algorithms/<id>.json` utilizável (com `check` e `expected[check].sha256`) falha no `test`; ele não cai na regra do Hello World. Fora dos algoritmos nada muda, exceto que um timeout deixa de ser repetido (o código já tinha essa intenção).

## Critérios de aceite
- `python3 scripts/hello.py check` passa e o README gerado está em dia.
- Trocar um checksum esperado ou o programa por uma versão errada faz o teste daquela implementação falhar sem produzir nenhum número de desempenho (o verificador nem mede).
- Todas as implementações da spec 014 passam no tamanho `check`.

## Limites conhecidos
- Só o tamanho `check` roda no CI (custo). Os checksums dos tamanhos de medição estão registrados, mas a conferência neles antes de cada medição (R5.2 da spec 010) é do harness de medição, que ainda não existe.
- `mandelbrot` (saída binária) não passa pela normalização de CRLF sem risco; fica para quando for implementado.
- Os tamanhos maiores têm origem `cross-language`, não arquivo publicado.
