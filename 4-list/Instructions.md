# Quest 4: List

## O cenário

Depois de atravessar a Floresta dos Ecos, você chega ao **Mercado das Mochilas Infinitas**. Ali, os aventureiros mais experientes não carregam cada item em uma variável separada. Eles usam bolsas encantadas capazes de guardar vários elementos no mesmo lugar.

Essas bolsas mágicas são as **listas**.

Até aqui, você já aprendeu a guardar um valor em uma variável, tomar decisões com condicionais e repetir ações com loops. Agora vai aprender a lidar com **coleções de dados**.

## O que você vai aprender

Nesta fase, sua missão é entender como:

- criar uma lista;
- guardar vários valores no mesmo lugar;
- acessar elementos por posição;
- adicionar e remover itens;
- percorrer listas com loops;
- usar listas para representar inventários e grupos do mundo de RPG.

## A ideia principal

Uma lista é uma sequência de elementos entre colchetes.

Exemplo:

```python
inventario = ["espada", "pocao", "mapa"]
```

Nesse caso, a variável `inventario` não guarda apenas um valor. Ela guarda vários itens.

## Tradução para o mundo RPG

Listas são perfeitas para representar:

- inventário do herói;
- nomes de inimigos;
- salas de uma dungeon;
- recompensas encontradas;
- membros de um grupo.

Em vez de criar uma variável para cada item, você organiza tudo em uma lista.

## Primeiro exemplo de inventário

```python
inventario = ["espada", "pocao", "escudo"]

print(inventario)
print(inventario[0])
print(inventario[1])
```

Aqui:

- `inventario[0]` mostra o primeiro item;
- `inventario[1]` mostra o segundo item.

## Adicionando e removendo itens

Você pode alterar a lista durante a aventura.

Exemplo:

```python
inventario = ["espada", "pocao"]

inventario.append("chave antiga")
print(inventario)

inventario.remove("pocao")
print(inventario)
```

Isso combina muito com um RPG, porque o inventário muda o tempo todo.

## Usando `input()` com listas

Você também pode deixar o jogador escolher itens para guardar.

```python
item1 = input("Escolha o primeiro item da mochila: ")
item2 = input("Escolha o segundo item da mochila: ")
item3 = input("Escolha o terceiro item da mochila: ")

inventario = [item1, item2, item3]

print(inventario)
```

## Percorrendo uma lista com `for`

Como você já aprendeu loops, agora pode usar `for` para visitar cada item da lista.

```python
inventario = ["espada", "pocao", "tocha"]

for item in inventario:
    print("Voce carrega:", item)
```

Esse é um passo importante, porque mostra como listas e loops trabalham muito bem juntas.

## Sua missão

Crie um inventário de aventureiro usando listas.

Seu programa deve:

- pedir ao jogador pelo menos 3 itens com `input()`;
- guardar esses itens em uma lista;
- mostrar o inventário completo;
- mostrar pelo menos um item usando posição;
- usar um loop para exibir todos os itens.

Depois, faça uma pequena mudança no inventário:

- adicionar um item encontrado em uma sala;
- ou remover um item usado durante a jornada.

## Exemplo de inspiração

```python
item1 = input("Digite um item da mochila: ")
item2 = input("Digite outro item da mochila: ")
item3 = input("Digite mais um item da mochila: ")

inventario = [item1, item2, item3]

print("Inventario inicial:", inventario)
print("Primeiro item:", inventario[0])

inventario.append("amuleto")

for item in inventario:
    print("Item guardado:", item)
```

## Desafio extra

Monte uma pequena lista de inimigos encontrados pelo herói, como:

- goblin;
- slime;
- lobo;
- arqueiro sombrio.

Depois, use um loop para mostrar uma mensagem para cada encontro.

## Vitória da fase

Se você conseguir usar listas para guardar vários elementos e percorrê-los com `for`, então sua mochila de programador ficou muito mais poderosa.
