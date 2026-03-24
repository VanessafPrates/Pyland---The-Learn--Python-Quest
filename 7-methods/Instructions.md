# Quest 6: Methods

## O cenário

Depois da sua primeira grande missão, algo ficou claro: vários trechos do seu código repetem as mesmas ações. Mostrar status. Calcular dano. Usar poção. Abrir baú. Os mestres de Pyland então apresentam uma técnica nova para transformar ações repetidas em habilidades reutilizáveis.

Em Python, isso normalmente aparece na forma de **funções**. Como o nome desta fase é `methods`, vamos tratar essas habilidades como técnicas especiais do seu grimório.

## O que você vai aprender

Nesta fase, sua missão é entender como:

- criar uma função com `def`;
- dar um nome claro para uma ação;
- receber informações por parâmetros;
- retornar resultados quando necessário;
- combinar funções com `input()` para montar ações de jogo.

## A ideia principal

Uma função permite agrupar um comportamento para chamá-lo sempre que quiser.

Exemplo:

```python
def saudar_heroi():
    print("Bem-vindo a Pyland, aventureiro.")

saudar_heroi()
```

Também é possível passar informações para a função:

```python
def mostrar_status(nome, vida):
    print(nome, "tem", vida, "pontos de vida.")

mostrar_status("Luna", 100)
```

Você também pode usar `input()` para receber dados do jogador e depois enviar essas informações para a função.

```python
nome = input("Nome do heroi: ")
vida = int(input("Vida atual: "))

def mostrar_status(nome, vida):
    print(nome, "tem", vida, "pontos de vida.")

mostrar_status(nome, vida)
```

## Tradução para o mundo RPG

Funções são úteis para criar habilidades como:

- mostrar a ficha do herói;
- calcular dano;
- usar poção;
- abrir inventário;
- anunciar início de batalha.

Em vez de repetir o mesmo bloco várias vezes, você cria a técnica uma vez e a invoca quando precisar.

Isso combina muito bem com jogos de texto, porque o jogador pode informar uma ação, e a função executa o efeito daquela escolha.

Também combina com listas, porque uma função pode mostrar todos os itens do inventário ou calcular o resultado de vários turnos de batalha.

## Sua missão

Crie pelo menos 3 funções para o seu mundo de aventura.

Sugestões:

- uma função para saudar o jogador;
- uma função para mostrar o status do personagem;
- uma função para calcular o dano de um ataque;
- uma função para verificar se o herói subiu de nível.

Use `input()` em pelo menos uma parte do programa para:

- receber o nome do herói;
- escolher a classe;
- informar o valor de ataque;
- decidir qual ação usar.

## Exemplo de inspiração

```python
def calcular_dano(ataque, bonus):
    return ataque + bonus

ataque = int(input("Digite o ataque base: "))
bonus = int(input("Digite o bonus magico: "))

dano_total = calcular_dano(ataque, bonus)
print(dano_total)
```

## Missão recomendada

Monte um mini sistema com:

1. uma função que receba nome e classe do herói;
2. uma função que receba vida atual e diga se ele está em perigo;
3. uma função que calcule o dano final de uma espada mágica.

Se quiser, crie também uma função para mostrar os itens de uma lista de inventário.

Tente começar a aventura com algo assim:

```python
nome = input("Digite o nome do heroi: ")
classe = input("Escolha a classe: guerreiro, mago ou arqueiro: ")
```

## Desafio extra

Crie uma função chamada `abrir_bau()` que retorne uma recompensa aleatória ou uma recompensa fixa, dependendo do que você já souber fazer.

Se quiser, faça o jogador escolher se deseja abrir ou não o baú antes de chamar a função.

## Vitória da fase

Se você perceber que uma função é como transformar uma ação frequente em uma habilidade reutilizável e conseguir conectá-la às escolhas do jogador, então já está pensando como alguém que programa com mais organização e menos repetição.
