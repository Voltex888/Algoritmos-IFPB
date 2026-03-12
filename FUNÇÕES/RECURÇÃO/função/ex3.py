def verificar_letra(letra):
    letra = letra.lower()
    if letra in "aeiou":
        return "vogal"
    else:
        return "consoante"
a = input("Digite uma letra: ")
resultado = verificar_letra(a)
print(f"Sua letra é {resultado}")