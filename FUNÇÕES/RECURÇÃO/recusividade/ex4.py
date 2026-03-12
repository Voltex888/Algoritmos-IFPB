def soma(n):
    if n == 1:
        return 1
    return 1/n + soma(n-1)
x = int(input("Digite um valor: "))
resultado = soma(x)
print(f"O resultado é {resultado}")