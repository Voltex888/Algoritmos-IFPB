lista =[]
n = -1
while n != 0:
    n = int(input())
    if n != 0:
        lista.append(n)
print(f"O maior é = {max(lista)}")
print(f"O menor é = {min(lista)}")
print(f"A soma é = {sum(lista)}")
print(f"quantidade = {len(lista)}")