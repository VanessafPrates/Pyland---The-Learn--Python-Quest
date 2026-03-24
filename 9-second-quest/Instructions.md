# Quest 9: Second Quest

## O cenário

Depois de aprender a criar classes em Python, a Guilda de Pyland confia a você uma nova responsabilidade: montar um grupo completo de aventureiros para enfrentar a próxima expedição ao **Templo das Três Coroas**.

Desta vez, não basta controlar apenas um herói. Será preciso montar uma pequena equipe com funções diferentes em batalha.

Os sábios da guilda pediram que você crie três tipos de herói:

- `Wizard`
- `Warrior`
- `Rouge`

Cada um deles deve ter sua própria identidade, seus próprios atributos e seu lugar no grupo.

## O que esta missão revisa

Para concluir esta quest, você vai usar conhecimentos de:

- variáveis;
- `input()`;
- condicionais;
- loops;
- listas;
- dicionários, se quiser organizar dados extras;
- funções, se quiser separar partes do código;
- classes e objetos.

## Sua missão principal

Crie um programa em Python em que o jogador monte um grupo com **3 heróis**.

Para isso, seu programa deve:

1. criar as classes `Wizard`, `Warrior` e `Rouge`;
2. permitir escolher a classe de cada herói;
3. pedir os atributos de cada personagem;
4. criar os 3 objetos;
5. guardar esse grupo em uma lista;
6. mostrar a ficha final do time.

## Objetivo da guilda

A ideia desta fase é fazer você sair de um único personagem e começar a pensar em **grupos de objetos**.

Você vai criar vários heróis diferentes a partir de classes e depois reunir todos em uma party, como em um RPG clássico.

## Estrutura sugerida

Você pode montar o sistema assim:

1. criar a classe `Wizard`;
2. criar a classe `Warrior`;
3. criar a classe `Rouge`;
4. pedir ao jogador os dados de 3 heróis;
5. a cada criação, perguntar qual classe ele quer;
6. criar o objeto correspondente;
7. adicionar o herói a uma lista chamada `grupo`;
8. no final, mostrar todos os membros do grupo.

## Atributos sugeridos

Cada personagem pode ter atributos como:

- nome;
- vida;
- ataque;
- defesa;
- mana;
- agilidade.

Você não precisa usar exatamente os mesmos atributos para todas as classes.

Por exemplo:

- `Wizard` pode ter mais mana;
- `Warrior` pode ter mais vida e defesa;
- `Rouge` pode ter mais agilidade.

## Exemplo de ideia para as classes

Você pode pensar assim:

```python
class Wizard:
    def __init__(self, nome, vida, mana, ataque):
        self.nome = nome
        self.vida = vida
        self.mana = mana
        self.ataque = ataque
```

E fazer algo parecido para `Warrior` e `Rouge`.

## Exibindo a ficha do herói

Se quiser, cada classe pode ter um método como `mostrar_status()` para exibir os dados do personagem.

Exemplo:

```python
def mostrar_status(self):
    print("Nome:", self.nome)
```

Depois, no final da criação do grupo, você pode usar um loop para mostrar todos os heróis.

## Interação com o jogador

Como esta é uma quest de RPG, o programa deve conversar com o jogador.

Perguntas que combinam com a missão:

- `Qual sera o nome do heroi?`
- `Escolha a classe: Wizard, Warrior ou Rouge`
- `Digite a vida do personagem:`
- `Digite o ataque do personagem:`
- `Digite a defesa do personagem:`

## Exemplo de fluxo da aventura

Você pode seguir este roteiro:

1. o jogador cria o primeiro herói;
2. escolhe entre `Wizard`, `Warrior` e `Rouge`;
3. define os atributos;
4. o programa cria o objeto;
5. o herói entra para a lista `grupo`;
6. isso se repete até o grupo ter 3 membros;
7. no final, a guilda apresenta a equipe completa.

## Exemplo de organização do grupo

Depois de criar os objetos, guarde todos em uma lista:

```python
grupo = []
```

E então adicione cada novo herói:

```python
grupo.append(heroi)
```

Depois, percorra essa lista com `for` para mostrar a equipe montada.

## Sua missão

Seu programa deve obrigatoriamente:

- criar as classes `Wizard`, `Warrior` e `Rouge`;
- pedir ao jogador o nome e atributos dos personagens;
- permitir escolher qual classe cada herói terá;
- criar 3 heróis;
- guardar os 3 heróis em uma lista;
- exibir os dados finais do grupo.

## Desafio extra

Se quiser tornar a quest mais interessante, adicione uma ou mais destas ideias:

- impedir classes repetidas no grupo;
- dar atributos iniciais diferentes para cada classe;
- criar um método de ataque para cada classe;
- mostrar qual grupo ficou mais equilibrado;
- pedir um nome para o grupo, como "Companhia da Pythonita".

## Vitória da fase

Você concluiu a missão com sucesso se conseguir:

- criar várias classes em Python;
- instanciar objetos diferentes;
- usar `input()` para montar personagens;
- guardar objetos em uma lista;
- formar um grupo completo de 3 heróis.

## Mensagem da guilda

Na primeira grande missão, você provou que sabia controlar um herói.

Agora, em Pyland, você começa a pensar como líder de equipe.

E todo grande líder sabe que uma boa party pode mudar o destino de uma aventura inteira.
