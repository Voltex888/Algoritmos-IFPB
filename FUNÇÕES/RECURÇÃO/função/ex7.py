def fibonacci(n):
    lista = []
    a = 0
    b = 1
    for _ in range(n):
        lista.append(a)
        a, b = b, a + b
    return lista
x = int(input(f"Digite um valor e veja a sequência na lista de fibonacci: "))
resultado = fibonacci(x)
print(f"A sequência de fibonacci com {x} números é {resultado}")