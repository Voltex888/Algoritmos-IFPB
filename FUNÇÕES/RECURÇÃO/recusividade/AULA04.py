def vogais(n):
    return sum(1 for letra in n if letra.lower() in "aeiou")
def numeros(n):
    return sum(1 for letra in n if letra.isdigit())
frase = str(input("Digite uma frase: "))
print(f"Sua frase tem {vogais(frase)} vogais e {numeros(frase)} números")