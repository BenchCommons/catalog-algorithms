# Plano — 014

- Os checksums dos tamanhos grandes foram calculados uma vez com as próprias implementações (C e JavaScript em todos os tamanhos, mais Python até `n-body 50000`, `fannkuch-redux 9` e `spectral-norm 500`) e gravados nas definições. Só o `check` roda no CI. `fannkuch-redux 12` leva cerca de 40 s em C, por isso não entra no CI.
- Referência extra, de memória e não registrada como fonte: os valores de `n-body 50000000` (`-0.169059907`), `fannkuch-redux 12` (`3968050`, `Pfannkuchen(12) = 65`) e `spectral-norm 5500` (`1.274224153`) coincidem com os publicados pelo Benchmarks Game.
- Em Python, `fannkuch-redux` e `spectral-norm` usam laços simples (sem NumPy); ficam lentos nos tamanhos grandes, o que é parte do que se quer medir.
- JavaScript formata com `toFixed(9)`, que arredonda o valor decimal exato; difere de `printf` só em empates exatos, que não ocorrem nestes dados (os três checksums coincidem em todos os tamanhos).
