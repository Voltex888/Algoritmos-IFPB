def somar(n):
    if n == 0:
        return 0
    else:
        return n + somar(n-1)
a = int(input("Digite um valor: "))
resultado = somar(a)
print(f"O resultado da soma de 0 até {a} = {resultado}")