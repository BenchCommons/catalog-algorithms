# 011 — Layout por linguagem: `languages/<lang>/<algoritmo>/`

Issue: #11.

## O quê
Organizar o catálogo com a **linguagem primeiro** e os algoritmos dentro dela. Cada linguagem tem um `language.json` com seus metadados e um diretório por algoritmo implementado. O Hello World passa a ser o primeiro algoritmo (`hello-world`), a linha de base de custo de inicialização.

## Por quê
- Linguagem é a unidade de toolchain: imagem, pacotes e versão fixada são compartilhados por todos os algoritmos dela.
- Quem contribui adiciona um algoritmo numa linguagem que já conhece, sem espalhar arquivos pelo repositório.
- Substitui o layout `algorithms/<algo>/<lang>/`, citado por engano na issue #11 e na spec 010.

## Requisitos
1. `languages/<lang>/language.json` com `name`, e `section` ou `tiobe`. Opcionais: `year`, `tags`, `notes`, `brazilian_notes`.
2. `languages/<lang>/<algoritmo>/meta.json` com `files` e, opcionalmente, `test`. O formato de `test` não muda (specs 004, 006 e 007).
3. `<algoritmo>` é um id em kebab-case da lista da spec 010 ou `hello-world`. O id da implementação no catálogo é `<lang>/<algoritmo>`.
4. A migração usa `git mv`, preservando o histórico de cada arquivo.
5. `scripts/hello.py` (`check`, `readme`, `test`, `apt-packages`, `--changed-since`) passa a funcionar sobre implementações `<lang>/<algoritmo>`. `--lang` continua aceitando o slug da linguagem e roda todos os algoritmos dela.
6. O README continua sendo a tabela de linguagens do Hello World, agora com links para `languages/<lang>/hello-world/`.

## Critérios de aceite
- `python3 scripts/hello.py check` passa: 452 linguagens, mesma contagem de testes.
- Nenhum `meta.json` no nível da linguagem; nenhum arquivo de programa fora de um diretório de algoritmo.
- `git log --follow` num arquivo migrado mostra o histórico anterior.
- O CI verde executa a suíte completa, porque `scripts/` muda.

## Fora de escopo
- Implementar os algoritmos da spec 010 (spec 014).
- O formato de metadados exigido pelo contrato de catálogo (benchmark-tool spec 010). Um adaptador gera esse formato depois, a partir destes arquivos.
