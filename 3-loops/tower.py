print("--------------------------------------")
print("      Localização: Torre do Mago      ")
print("--------------------------------------")
print("Um rumor se espalhou pela guilda, a entrada de uma torre foi desbloqueada por aventureiros")
print("Nos salões desta torre ha 10 baús, mas ninguém com a coragem suficiente para abri-los\n")
print("Você tem 5 chances de abrir o baú certo e descobrir um item misteriso")
print("Boa Sorte!\n")
stamina = 5
continue_game = True
resp = input("Você deseja mesmo entrar? ")
if resp == "sim":
    print("Você adentra a Torre: ")
else:  
    print("Você volta correndo para a Guilda")
    continue_game = False

while continue_game:

    choice = int(input("Qual báu vai querer abrir? (1-10) \n"))
    if choice >= 1 and choice <= 3:
        print("Nesse báu não tem nada")
        print("[====]\n" 
              "[▓▓▓▓]\n" 
              "[▣ ▣ ▣]")
        stamina -= 1
        print(f"Agora você tem {stamina} tentativas")
    elif choice >= 4 and choice <= 6:
        print("Você encontrou um baú mímico!")
        print("[====]\n"
              "[ಠ益ಠ]\n" 
              "[▣ ▣ ▣]")
        print("Ele te devora e você perde todas suas chances")
        continue_game = False
    elif choice == 7:
        print("Você encontrou a Cueca do Mago! Parabéns? ")
        print("[====]\n"
              "[????]\n"
              "[▣ ▣ ▣]")
        stamina -= 1
        print(f"Agora você tem {stamina} tentativas")
    elif choice == 10:
        print("Parabéns! Você encontrou o Lendario Amuleto do Mago!")
        print("[====]\n"
              "[****]\n"
              "[▣ ▣ ▣]")
        print("Agora você da mais dano em inimigos arcanos")
        print("Você sai da Torre e se exibe para os aventureiros")
        continue_game = False

    if  stamina == 0:
        print("Você ficou sem stamina")
        continue_game = False