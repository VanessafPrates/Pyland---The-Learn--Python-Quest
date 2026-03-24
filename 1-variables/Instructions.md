# Quest 1: Variables

## O cenário

Você acaba de chegar à vila inicial de Pyland. Antes de partir para as masmorras, precisa organizar sua mochila, registrar seu nome de aventureiro e anotar os recursos básicos da jornada.

É aqui que entram as **variáveis**.

Em Python, variáveis servem para **guardar informações**. Pense nelas como etiquetas mágicas presas em caixas, bolsas ou frascos. Cada etiqueta aponta para um valor que você pode consultar depois.

## O que você vai aprender

Nesta fase, sua missão é entender como:

- criar variáveis;
- guardar textos, números e valores simples;
- usar `input()` para receber dados do jogador;
- converter tipos com `int()`;
- trocar o valor de uma variável;
- exibir informações com `print()`.

## A ideia principal

Uma variável é como escrever algo assim:

```python
nome_heroi = "Luna"
ouro = 25
vida = 100
```

Nesse exemplo:

- `nome_heroi` guarda um texto;
- `ouro` guarda um número inteiro;
- `vida` guarda outro número.

Depois disso, você pode usar esses nomes para mostrar ou reaproveitar os valores:

```python
print(nome_heroi)
print(ouro)
print(vida)
```

## Recebendo dados do jogador

Até aqui, os valores foram escritos direto no código. Mas em uma aventura de verdade, faz mais sentido deixar o próprio jogador preencher a ficha do herói.

Para isso, usamos `input()`.

Exemplo:

```python
nome_heroi = input("Digite o nome do seu heroi: ")
classe = input("Digite a classe do seu heroi: ")
```

Nesse caso, o programa faz uma pergunta e guarda a resposta em uma variável.

## Um detalhe importante sobre `input()`

Tudo o que entra com `input()` chega como **texto**.

Isso significa que, se o jogador digitar um número, o Python ainda vai entender aquilo como texto até que você converta.

Exemplo:

```python
vida = input("Digite a vida do heroi: ")
print(vida)
```

Aqui `vida` ainda será um texto, mesmo que o jogador digite `100`.

## Conversão de tipos com cast

Quando você quiser transformar esse texto em número, pode usar um cast, como `int()`.

Exemplo:

```python
vida = int(input("Digite a vida do heroi: "))
ouro = int(input("Digite a quantidade de ouro: "))
```

Agora `vida` e `ouro` passam a ser números inteiros, e você poderá fazer contas com eles.

Exemplo:

```python
ouro = int(input("Quantas moedas voce encontrou? "))
ouro = ouro + 10
print(ouro)
```

Sem conversão, o Python não entenderia corretamente essa conta do jeito que você espera.

## Tradução para o mundo RPG

Imagine o seguinte:

- o nome do herói precisa ser registrado;
- a quantidade de ouro precisa ser contada;
- a vida do personagem precisa ser acompanhada;
- o nome da arma precisa ser salvo;
- o nível do aventureiro precisa ser atualizado.

Tudo isso pode ser feito com variáveis.

## Regras importantes da guilda

1. O nome da variável deve fazer sentido.
2. Evite espaços. Use `_` para separar palavras.
3. O valor pode mudar durante a aventura.

Exemplo:

```python
ouro = 10
ouro = 15
print(ouro)
```

Aqui o herói começou com `10` moedas e depois passou a ter `15`.

## Sua missão

Crie um pequeno cadastro de personagem usando variáveis.

Seu programa deve guardar:

- nome do personagem;
- classe do personagem;
- quantidade de vida;
- quantidade de mana ou energia;
- quantidade de ouro.

Use `input()` para pedir esses dados ao jogador.

Use cast com `int()` nos valores numéricos.

Depois, exiba tudo com `print()`.

## Desafio extra

Depois do cadastro inicial:

- aumente o ouro encontrado em uma missão;
- reduza a vida após uma batalha;
- troque o nome da arma equipada.

## Exemplo de inspiração

```python
nome = input("Nome do heroi: ")
classe = input("Classe do heroi: ")
vida = int(input("Vida inicial: "))
mana = int(input("Mana inicial: "))
ouro = int(input("Ouro inicial: "))

print(nome)
print(classe)
print(vida)
print(mana)
print(ouro)
```

## Missão bônus da taverna

Depois de cadastrar o herói, faça pequenas alterações nos números:

- some ouro após encontrar um tesouro;
- diminua a vida após uma batalha;
- aumente a mana após beber uma poção mágica.

Isso ajuda a perceber a diferença entre **guardar**, **ler** e **atualizar** valores.

## Vitória da fase

Se ao final você conseguir olhar para um valor e pensar:

"isso pode ser guardado em uma variável",

então sua primeira habilidade foi desbloqueada.
