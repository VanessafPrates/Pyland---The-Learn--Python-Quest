name = "Gliminessa"
char_class = "Warrior"
bag = ["Capa fedida", "Espada sem fio"]
hp = 100
gold = 1000
print("------------------------------------------")
print("Bem-vinda ", name, " à cidade de Pyland")
print("------------------------------------------\n")
print("Guilda - pegue quests, acesse seus itens e consulte seu level")
print("Vendedores - compre equipamentos se tiver o ouro necessario")
print("Masmorra - Enfrente inimigos, ganhe exp e ouro!\n")
ação = input("Onde deseja ir primeiro? ")

if ação == "guilda":
    decision = input("Olá Aventureira(o), deseja consultar sua ficha? ")
    if decision =="sim":
        level = int(input("Digite o nivel do heroi: "))

        if level < 5:
            print("Aprendiz")
        elif level < 10:
            print("Aventureiro")
        else:
            print("Veterano")
    
        print(f"Nome: {name}, classe {char_class}, level {level}")
        print(f"Na sua mochila você tem os seguintes itens: {bag}")
    else: 
        print("Boa Sorte nas proximas aventuras!")
        exit(0)
elif ação == "vendedores":
    print("Bem-vinda a loja Seu Gold é Meu")
    print(f"Você tem {gold}g")
    decision = input("Deseja comprar ou só olhar os itens? ")
    if decision == "comprar":
        print("Itens à venda:" \
        "[1] Capa Reluzente 100g" \
        "[2] Espada de Mithril 1.000g")
        buy = input("Qual item deseja comprar? ")
        if buy == "1":
            if gold < 100: 
                sold = gold - 100
                print("DING")
                print("Parabéns agora você tem uma        -Capa Reluzente-        ")
                print(f"Agora você tem {sold}g")
                print("Volte Sempre! ")
                print("Você sai da loja")
                exit(0)
            else:
                print("Não vendemos fiado! ")
                print("Você é expulso da loja")
                exit(0)
        if buy == "2":
            if gold < 1000:
                sold = gold - 1000
                print("DING")
                print("Parabéns agora você tem uma        -Espada de Mithril-        ")
                print(f"Agora você tem {sold}g")
                print("Volte Sempre! ")
                print("Você sai da loja")
                exit(0)
            else:
                print("Volte quando tiver o dinheiro")
                exit(0)
    elif decision == "olhar":
        print("Você baba na vitrine vendo os seguintes itens:" \
        "Capa Reluzente" \
        "Espada de Mithril")
        print("Você volta para a cidade")
        exit(0)

else:
    decision = input("Deseja entrar na caverna escura ou voltar para a cidade? ")
    if decision == "entrar":
        print("Você entrou na caverna escura")
        print(f"Seus status {hp} de vida e itens {bag}")
        print("----------------------------------------")
        print("             Slime aparece              ")
        print("             (づ｡◕‿‿◕｡)づ             ")
        print("----------------------------------------")
        atack = input("Enfrentar o slime ?")
        if atack == "sim":
            print("Você mata o slime com sua espada!")
            print("Recompensa: +10g e 20 exp")
        else:
            print("Você sai correndo da masmorra")


