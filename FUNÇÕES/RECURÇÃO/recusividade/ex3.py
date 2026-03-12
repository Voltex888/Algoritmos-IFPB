def pontencia(n1, n2):
    if n2 == 0:
        return 1
    return n1 * pontencia(n1, n2-1)
a = int(input("Digite um valor: "))
b = int(input("Digite um valor: "))
resultado = pontencia(a, b)
print(f"{a} elevado a {b} = {resultado}")