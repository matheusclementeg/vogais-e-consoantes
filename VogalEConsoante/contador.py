def cont():
    texto = input("Digite um texto:\n")
    vogais = 0
    consoantes = 0

    for caracter in texto:
        if caracter in 'aáàâãeéêèiíìîoóòôõuúùû':
            vogais = vogais + 1
        else:
            consoantes = consoantes + 1

    print("Vogais: %s " %vogais)
    print("Consoantes: %i " %consoantes)