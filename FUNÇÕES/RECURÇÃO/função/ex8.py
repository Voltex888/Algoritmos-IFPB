def primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
x = int(input("Digite um número e veja se ele é primo: "))
resultado = primo(x)
if resultado == True:
    print("É primo")
else:
    print("Não é primo")