# Quest 7: Class

## O cenário

Depois de aprender a criar funções para organizar ações do jogo, os sábios de Pyland revelam uma técnica ainda mais poderosa: em vez de guardar tudo em variáveis soltas, agora você pode criar **tipos de personagem**, como se estivesse montando fichas completas de heróis, monstros e criaturas mágicas.

É aqui que entram as **classes**.

Se antes você criava variáveis separadas para nome, vida, ouro e classe do herói, agora pode reunir tudo isso em uma única estrutura mais organizada.

## O que você vai aprender

Nesta fase, sua missão é entender como:

- criar uma classe com `class`;
- definir atributos para um personagem;
- usar `__init__()` para montar a ficha inicial;
- criar métodos que representam ações do personagem;
- instanciar objetos;
- usar `input()` para criar um herói com dados escolhidos pelo jogador;
- juntar atributos e métodos em uma mesma entidade do jogo.

## A ideia principal

Uma classe é como um molde.

Pense assim:

- a **classe** é o modelo de ficha;
- o **objeto** é o personagem criado a partir dessa ficha.

Exemplo:

```python
class Heroi:
    def __init__(self, nome, classe, vida):
        self.nome = nome
        self.classe = classe
        self.vida = vida
```

Nesse exemplo:

- `Heroi` é a classe;
- `__init__()` prepara os dados iniciais;
- `self.nome`, `self.classe` e `self.vida` são atributos do personagem.

## Tradução para o mundo RPG

Uma classe pode ser usada para representar:

- um herói;
- um inimigo;
- um NPC;
- um monstro;
- um item especial;
- um baú mágico.

Em vez de espalhar as informações pelo código, você reúne tudo dentro de uma entidade mais fácil de entender.

Agora isso fará ainda mais sentido, porque você já conhece:

- variáveis para guardar dados;
- condicionais para decidir ações;
- loops para repetir eventos;
- listas para inventários e grupos;
- funções para organizar comportamentos.

A classe junta tudo isso em uma estrutura mais completa.

## Primeiro exemplo de herói

```python
class Heroi:
    def __init__(self, nome, classe, vida, ouro):
        self.nome = nome
        self.classe = classe
        self.vida = vida
        self.ouro = ouro
```

Agora podemos criar um herói assim:

```python
jogador = Heroi("Luna", "Maga", 100, 50)

print(jogador.nome)
print(jogador.classe)
print(jogador.vida)
print(jogador.ouro)
```

## Usando `input()` para criar o personagem

Como este curso tem cara de RPG, faz sentido deixar o jogador montar seu próprio herói.

```python
nome = input("Digite o nome do heroi: ")
classe = input("Escolha a classe: guerreiro, mago ou arqueiro: ")
vida = int(input("Digite a vida inicial: "))
ouro = int(input("Digite o ouro inicial: "))

jogador = Heroi(nome, classe, vida, ouro)
```

Aqui o jogador preenche a ficha, e a classe organiza essas informações.

## Métodos: ações do personagem

Além de guardar dados, uma classe também pode ter ações.

Essas ações são chamadas de **métodos**.

Exemplo:

```python
class Heroi:
    def __init__(self, nome, classe, vida):
        self.nome = nome
        self.classe = classe
        self.vida = vida

    def mostrar_status(self):
        print(self.nome, "-", self.classe, "-", self.vida, "de vida")
```

Depois, usamos assim:

```python
jogador = Heroi("Arin", "Guerreiro", 120)
jogador.mostrar_status()
```

## Exemplo com ação de batalha

```python
class Heroi:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def receber_dano(self, dano):
        self.vida = self.vida - dano
        print(self.nome, "recebeu", dano, "de dano.")
        print("Vida restante:", self.vida)
```

Uso:

```python
jogador = Heroi("Kael", 100)
jogador.receber_dano(20)
```

## Sua missão

Crie uma classe para representar um herói de Pyland.

Sua classe deve ter pelo menos:

- nome;
- classe;
- vida;
- ouro.

E também pelo menos 2 métodos, como:

- `mostrar_status()`;
- `receber_dano()`;
- `ganhar_ouro()`;
- `usar_pocao()`.

Use `input()` para pedir ao jogador os dados iniciais do personagem.

Depois:

- crie o objeto do herói;
- mostre o status;
- faça o herói passar por um evento;
- atualize os atributos.

Se quiser, adicione também uma lista de inventário dentro do personagem.

## Exemplo de fluxo da quest

Você pode montar a prática assim:

1. o jogador digita nome e classe;
2. o programa cria o herói com a classe `Heroi`;
3. o herói entra em uma caverna;
4. ele sofre dano ou ganha ouro;
5. o método `mostrar_status()` exibe o resultado.

## Missão recomendada

Monte um mini sistema em que:

1. o jogador cria um herói pelo teclado;
2. o herói encontra um goblin;
3. perde vida ao ser atacado;
4. ganha ouro ao vencer;
5. mostra o status final usando um método da própria classe.

## Desafio extra

Se quiser deixar a aula mais poderosa, tente uma destas opções:

- criar também uma classe `Inimigo`;
- criar um método `atacar()`;
- fazer classes diferentes começarem com atributos diferentes;
- criar um método que diga se o herói ainda está vivo;
- adicionar uma lista de itens ao herói.

## Vitória da fase

Você concluiu esta etapa com sucesso se conseguir perceber que:

- uma classe organiza dados e comportamentos;
- um objeto representa uma entidade do jogo;
- métodos são ações daquela entidade;
- classes deixam o código mais próximo de um RPG de verdade.

## Mensagem da guilda

Até aqui, você aprendeu a escrever comandos.

Agora está começando a construir criaturas, fichas e sistemas.

Isso é um passo importante para sair de pequenos exercícios e entrar em mundos mais organizados.
