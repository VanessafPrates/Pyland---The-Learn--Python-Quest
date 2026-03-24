# Quest 2: Conditionals

## O cenário

Você deixou a vila e agora está diante da **Encruzilhada das Decisões**. Em Pyland, nem toda porta se abre, nem todo item pode ser usado a qualquer momento, e nem todo inimigo deve ser enfrentado.

Para seguir vivo, seu personagem precisa tomar decisões.

É aqui que entram as **condicionais**.

## O que você vai aprender

Nesta fase, sua missão é entender como:

- verificar se uma condição é verdadeira ou falsa;
- usar `if`;
- usar `else`;
- usar `elif` para múltiplos caminhos;
- usar `input()` para deixar o jogador escolher o que fazer.

## A ideia principal

Condicionais são o jeito que o programa tem de pensar:

"se isso acontecer, faça uma coisa; senão, faça outra."

Exemplo:

```python
ouro = int(input("Quantas moedas voce tem? "))

if ouro >= 30:
    print("Voce pode comprar a espada.")
else:
    print("Voce ainda nao tem ouro suficiente.")
```

Agora o jogo escuta o jogador antes de tomar uma decisão.

## Tradução para o mundo RPG

Você pode usar condicionais para decidir:

- se o herói pode entrar em uma caverna;
- se há vida suficiente para enfrentar um dragão;
- se o jogador ganhou experiência bastante para subir de nível;
- se um item raro pode ser comprado;
- se uma poção deve ser usada agora ou guardada.

Também pode perguntar diretamente ao jogador qual ação ele quer tomar.

## Estrutura básica

```python
if condicao:
    print("Algo acontece")
else:
    print("Outra coisa acontece")
```

Quando existem mais possibilidades:

```python
nivel = int(input("Digite o nivel do heroi: "))

if nivel < 5:
    print("Aprendiz")
elif nivel < 10:
    print("Aventureiro")
else:
    print("Veterano")
```

## Exemplo com escolha do jogador

```python
acao = input("Voce quer entrar na caverna ou voltar para a vila? ")

if acao == "entrar":
    print("Voce atravessa a entrada escura.")
else:
    print("Voce recua para um lugar seguro.")
```

Esse tipo de interação já começa a dar ao programa um ar de RPG de texto.

## Sua missão

Crie um programa que analise o estado de um personagem e tome decisões.

Use variáveis para representar pelo menos:

- vida;
- ouro;
- nível;
- chave mágica ou item especial.

Use `input()` para receber pelo menos parte dessas informações do jogador.

Depois, crie condições como estas:

- se a vida estiver baixa, mostrar que o herói deve recuar;
- se houver ouro suficiente, permitir comprar um item;
- se tiver a chave mágica, abrir a porta do castelo;
- caso contrário, bloquear a passagem.

Inclua também ao menos uma decisão direta do jogador, como:

- comprar ou não um item;
- entrar ou não em uma sala;
- usar ou não uma poção.

## Exemplo de interação

```python
vida = int(input("Digite a vida do heroi: "))
tem_chave = input("Voce possui a chave magica? ")

if vida < 30:
    print("O heroi precisa descansar antes de seguir.")
elif tem_chave == "sim":
    print("A porta do castelo se abre.")
else:
    print("A passagem continua trancada.")
```

## Desafio extra

Monte um sistema simples de rank:

- nível baixo: "Novato";
- nível médio: "Explorador";
- nível alto: "Lenda de Pyland".

Se quiser ir além, pergunte ao jogador se ele aceita ou não uma missão da guilda e responda de acordo com a escolha.

## Vitória da fase

Se você conseguir fazer o programa responder com caminhos diferentes dependendo dos valores guardados e das escolhas digitadas pelo jogador, então aprendeu a arte das decisões.
