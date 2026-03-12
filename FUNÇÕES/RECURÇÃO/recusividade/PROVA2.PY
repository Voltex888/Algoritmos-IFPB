def primo(n):
    total = 0
    for i in range(len(n)):
        cont = 0
        for j in range(1, n[i]+1):
            if n[i] % j == 0:
                cont += 1
        if cont == 2:
            total += 1
    return total    
lista = []
x = int(input("Digite quantos valores vc quer na lista: "))
for i in range(x):
    y = int(input(f"Digite o valor {i+1}°: "))
    lista.append(y)
resultado = primo(lista)
print(f"Sua lista tem {resultado} números primos!! ")