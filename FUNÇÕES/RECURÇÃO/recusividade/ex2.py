def menor(n):
    m = lista[0]
    for n in lista:
        if n < m:
            m = n
    return m
num = int(input("Digite quantos número vc quer testar: "))
lista = []
for i in range(num):
    x = int(input("Digite um valor: "))
    lista.append(x)
resultado = menor(lista)
print(f"O menor número é {resultado}")