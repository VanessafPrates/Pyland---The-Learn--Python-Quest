# Quest 6: First Quest

## O cenário

Chegou a hora da sua **primeira grande missão em Pyland**.

Depois de aprender a guardar informações, tomar decisões, repetir ações, organizar itens em listas e montar fichas com dicionários, você foi convocado pela Guilda do Vale Central para enfrentar sua primeira quest completa.

Nas ruínas de um castelo antigo, um artefato chamado **Coração de Pythonita** foi escondido. Para recuperá-lo, seu herói precisará atravessar salas perigosas, enfrentar inimigos, administrar recursos e usar suas próprias habilidades com inteligência.

Esta fase é uma revisão geral de tudo o que você aprendeu até agora.

## O que esta missão revisa

Para concluir esta quest, você vai precisar usar:

- **variáveis** para guardar os dados do herói;
- **condicionais** para tomar decisões durante a aventura;
- **loops** para repetir ações, turnos ou eventos;
- **listas** para representar inventário, salas ou inimigos.
- **dicionários** para organizar informações importantes do herói ou dos desafios.

## Sua missão principal

Crie um pequeno programa em Python que simule uma aventura do herói em busca do **Coração de Pythonita**.

O programa deve usar todos os conhecimentos anteriores.

Além disso, tente fazer a aventura conversar com o jogador por meio de `input()`, como em um pequeno RPG de texto.

## Requisitos da quest

Seu jogo ou simulação precisa ter pelo menos:

1. **Variáveis**

Crie variáveis para guardar informações como:

- nome do herói;
- classe do herói;
- vida;
- energia ou mana;
- ouro;
- quantidade de poções;
- dano base de ataque.

Sempre que fizer sentido, peça esses dados com `input()`.

2. **Condicionais**

Use decisões para situações como:

- verificar se o herói ainda está vivo;
- decidir se pode abrir uma porta;
- usar uma poção quando a vida estiver baixa;
- verificar se o ouro é suficiente para comprar algo;
- decidir se o herói venceu ou perdeu a missão.

Você também pode usar condicionais para interpretar escolhas do jogador, como `atacar`, `defender`, `usar pocao` ou `abrir bau`.

3. **Loops**

Use repetição para simular partes da aventura, como:

- uma sequência de salas no castelo;
- vários turnos de batalha;
- coleta de recompensas;
- tentativas até concluir um objetivo.

Uma boa ideia é usar um loop para manter a aventura acontecendo enquanto o herói ainda tiver vida.

4. **Listas**

Use listas para representar elementos da aventura.

Sugestões:

- inventário do herói;
- recompensas encontradas;
- inimigos do castelo;
- nomes das salas exploradas.

Percorra pelo menos uma dessas listas com `for`.

5. **Dicionários**

Use pelo menos um dicionário para organizar dados da aventura.

Sugestões:

- ficha do herói;
- informações de um inimigo;
- recompensa de um baú;
- status de uma sala.

Exemplo de ideia:

```python
heroi = {
    "nome": nome,
    "classe": classe,
    "vida": vida,
    "ouro": ouro
}
```

## Estrutura sugerida da aventura

Você pode montar a quest assim:

1. O herói entra no castelo.
2. O jogador informa o nome e a classe do herói com `input()`.
3. Ele passa por 3 salas usando um loop.
4. Em cada sala, algo acontece: inimigo, tesouro, armadilha, poção ou porta trancada.
5. O jogador pode tomar decisões digitando ações.
6. O programa toma decisões com `if`, `elif` e `else`.
7. Uma lista guarda itens, salas ou inimigos encontrados.
8. Um dicionário guarda a ficha do herói ou os dados de um inimigo importante.
9. No final, o herói encontra o artefato ou falha na missão.

## Interações que combinam com a quest

Para dar cara de RPG, experimente perguntas como:

- `Qual sera o nome do heroi?`
- `Escolha sua classe: guerreiro, mago ou arqueiro`
- `Voce quer atacar, defender ou usar pocao?`
- `Deseja abrir o bau? sim ou nao`
- `Voce quer entrar na sala secreta?`

## Exemplo de ideia

Você não precisa copiar este roteiro, mas pode se inspirar nele:

- o jogador escolhe nome e classe pelo teclado;
- o herói começa com 100 de vida;
- a ficha do herói é guardada em um dicionário;
- percorre 3 salas;
- em cada sala perde ou ganha algo;
- guarda itens em um inventário com lista;
- se a vida ficar abaixo de 40, pode usar poção;
- se derrotar todos os desafios, encontra o artefato;
- se a vida chegar a 0, a missão termina.

## Objetivo pedagógico

Esta é a fase em que você deixa de fazer exercícios isolados e começa a juntar tudo em uma experiência completa.

Até aqui, você aprendeu peças separadas do mapa. Agora, sua missão é montar o caminho inteiro.

## Desafio extra

Se quiser deixar sua quest mais interessante, adicione uma ou mais destas ideias:

- escolha de classe com efeitos diferentes;
- inimigos com nomes diferentes;
- baús com recompensas aleatórias;
- um inventário que cresce durante a missão;
- uma lista de salas especiais;
- um dicionário para guardar status do boss final;
- mais de um final possível.

## Vitória da fase

Você concluiu esta etapa com sucesso se seu programa:

- usar variáveis com sentido;
- tomar decisões com condicionais;
- repetir ações com loops;
- usar ao menos uma lista com sentido;
- usar ao menos um dicionário com sentido;
- contar uma pequena história jogável ou simulada;
- permitir pelo menos algumas escolhas do jogador com `input()`.

## Mensagem da guilda

Se você conseguir terminar esta missão, então não está mais apenas praticando comandos.

Você já está começando a pensar como um verdadeiro aventureiro de Python.
