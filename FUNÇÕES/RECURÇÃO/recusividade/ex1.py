def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n-1)
x = int(input("Digite um valor e veja seu fatorial: "))
resultado = fatorial(x)
print(f"O resultado de {x}! = {resultado}")