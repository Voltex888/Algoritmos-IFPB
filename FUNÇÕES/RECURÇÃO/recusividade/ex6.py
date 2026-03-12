def dividir(a, b):
    if a < b:
        return 0
    return 1 + dividir(a - b, b)
x = int(input("Digite um valor:  "))
y = int(input("Digite um valor:  "))
resultado = dividir(x, y)
print(f"O resultado é {resultado}")