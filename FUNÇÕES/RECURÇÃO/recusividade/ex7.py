def resto(a, b):
    if a < b:
        return a
    return resto(a - b, b)
x = int(input("Digite um valor:  "))
y = int(input("Digite um valor:  "))
resultado = resto(x, y)
print(f"O resultado é {resultado}")