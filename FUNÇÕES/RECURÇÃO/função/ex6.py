def fatorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado
x = int(input(f"Digite um valor e veja seu fatorial: "))
r = fatorial(x)
print(f"O resultado é {r}")