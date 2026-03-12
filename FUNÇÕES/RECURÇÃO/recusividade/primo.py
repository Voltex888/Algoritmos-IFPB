def primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
x = int(input("Digite quantos valores terá a lista: "))
lista = [int(input(f"Digite o valor {i+1}°: ")) for i in range(x)]
total = sum(1 for y in lista if primo(y))
print(f"Sua lista tem {total} números primos")