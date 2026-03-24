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
mana = int(input("Quantidade de mana? "))
gold = float(input("Quantidade de ouro? "))
print("------------------------------------------------")
print("                 Cadastro completo!               ")
print("------------------------------------------------\n")
print("Olá,", name)
print("Sua classe é ", char_class)
print("Estou vendo sua ficha, você tem ", hp, " de vida e ", mana, " de mana")
print("Você também tem ", gold, " de ouro.")
print("Tudo certo! Agora você está habilitado a escolher Quests\n")