def maior(n1, n2):
    if n1 > n2:
        maior = n1
    else:
        maior = n2
    return maior
a = int(input("Digite um valor: "))
b = int(input("Digite outro valor: "))
resultado = maior(a, b)
print(f"O maior é {resultado}")