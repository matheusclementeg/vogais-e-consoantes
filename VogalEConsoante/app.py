import contador
def menu():
    print("========================")
    print("     Verifica Vogal e Consoante    ")
    print("========================")
    print("[1] - Imprime Vogal")
    print("[2] - Imprime Consoante")
    print("[3] - Contador de Vogais e Consoantes")
    print("[0] - Sair")
    print(" ")


loop = True
texto = ""
while loop:
    menu()
    res = int(input("Opcao: "))

    if res == 1:
        texto = input("Digite uma palavra\n")
        for vogal in texto:
            if vogal in 'aeiou':
                print(vogal)
    elif res == 2:
        texto2 = input("Digite uma palavra\n")
        for cons in texto2:
            if cons not in 'aeiou':
                print(cons)

    if res == 3:
        contador.cont()
    if res == 0:
        loop = False
