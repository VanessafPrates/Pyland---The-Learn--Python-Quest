# Quest 3: Loops

## O cenário

Ao entrar na Floresta dos Ecos, você percebe uma verdade importante: muitas ações em uma aventura se repetem.

Contar moedas.
Passar por inimigos.
Dar vários passos.
Verificar tentativas.
Recolher itens espalhados pelo mapa.

Fazer tudo isso manualmente, linha por linha, seria cansativo até para um mago paciente. É por isso que existem os **loops**.

## O que você vai aprender

Nesta fase, sua missão é entender como:

- repetir ações com `for`;
- repetir ações com `while`;
- controlar quantas vezes algo acontece;
- percorrer sequências simples;
- combinar repetição com `input()` para criar interação.

## A ideia principal

Um loop diz ao Python:

"repita esta ação enquanto fizer sentido."

Exemplo com `for`:

```python
for passo in range(5):
    print("Voce andou um passo no mapa.")
```

Isso repete a mensagem 5 vezes.

Exemplo com `while`:

```python
energia = 3

while energia > 0:
    print("Voce ainda consegue correr.")
    energia = energia - 1
```

Aqui a repetição continua enquanto a condição for verdadeira.

## Tradução para o mundo RPG

Loops ajudam quando você precisa:

- contar baús encontrados;
- atacar várias vezes;
- percorrer uma lista de aliados;
- repetir turnos de batalha;
- testar tentativas até acertar uma senha ou comando.

Quando combinados com `input()`, eles deixam a aventura com cara de jogo, porque o jogador pode responder a cada turno.

## Exemplo de interação com `while`

```python
tentativa = ""

while tentativa != "abracadabra":
    tentativa = input("Digite a palavra magica para abrir o portal: ")
    print("O portal continua observando voce...")

print("O portal se abriu.")
```

## Sua missão

Crie exercícios com os dois tipos de loop.

Parte 1:

Use `for` para:

- contar de 1 até 10;
- exibir 5 passos de caminhada do herói;
- mostrar a coleta de 3 itens.

Se quiser, use `input()` antes do loop para pedir o nome do herói e mostrar mensagens personalizadas.

Parte 2:

Use `while` para:

- reduzir a energia do personagem até zero;
- simular uma contagem regressiva antes de abrir um portal;
- repetir uma ação enquanto o herói ainda tiver vida.

Em pelo menos um exercício, use `input()` para permitir uma interação, como:

- pedir um comando de fuga;
- pedir uma senha mágica;
- perguntar se o jogador quer continuar explorando.

## Aviso de aventureiro

Com `while`, é preciso ter cuidado.

Se a condição nunca deixar de ser verdadeira, o loop pode continuar para sempre. Isso é como ficar preso em uma dungeon sem saída.

## Desafio extra

Crie uma rotina de batalha em que o herói ataque 3 vezes usando `for` e, depois, fuja enquanto a vida estiver abaixo de um valor usando `while`.

Se quiser deixar mais interativo, pergunte ao jogador qual ação ele quer tomar em cada turno:

```python
for turno in range(3):
    acao = input("Turno de batalha: atacar ou defender? ")
    print("Voce escolheu:", acao)
```

## Vitória da fase

Se você entender quando usar repetição em vez de copiar a mesma linha várias vezes e conseguir usar loops para criar pequenas interações de aventura, então conquistou uma habilidade essencial para qualquer aventureiro de Python.
