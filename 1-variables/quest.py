#Seu programa deve guardar:

# nome do personagem;
# classe do personagem;
#  quantidade de vida;
# quantidade de mana ou energia;
# quantidade de ouro.


print("------------Bem-vindo a Guilda de Pyland------------")
print("Faça seu cadastro para receber Quests")
print("------------------------------------------------\n")
name = input("Qual o seu nome? ")
char_class = input("Qual sua classe? ")
hp = int(input("Quantidade de HP? "))
mana = int(input("Quantidade de mana ou energia? "))
gold = float(input("Quantidade de ouro? "))
print("------------------------------------------------")
print("                 Cadastro completo!               ")
print("------------------------------------------------\n")
print("Olá,", name)
print("Sua classe é ", char_class)
print("Estou vendo sua ficha, você tem ", hp, " de vida e ", mana, " de mana ou energia")
print("Você também tem ", gold, " de ouro.")
print("Tudo certo! Agora você está habilitado a escolher Quests\n")

print("Sua primeira Quest é derrotar 5 slimes")
print("Para derrotar você perderá 20 de HP")
print("Sua recompensa será 50 ouros, 100 de EXP e uma capa fedida\n")
resp = input("Deseja seguir para essa quest ? ")

if resp =="sim":
    print("          Quest Concluida!         ")
    hp_loss = hp - 20
    reward = gold + 50
    exp = 100
    print("Agora seu HP é ", hp_loss)
    print("Você tem ", reward, "de ouro e ", exp, "de EXP")
    print("E podera equipar a Capa fedida na sua proxima quest!")
else:
    print("Não temos mais quests disponiveis, volte outra hora")