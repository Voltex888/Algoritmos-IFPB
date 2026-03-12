n = int(input())
for m in range(n):
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())
    media = (n1+ n2 +n3) / 3
    if n1 >= n2 and n1 >= n3:
        maior = n1
    elif n2 >= n1 and n2 >= n3:
        maior = n2
    else:
        maior = n3
    if n1 <= n2 and n1 <= n3:
        menor = n1
    elif n2 <= n1 and n2 <= n3:
        menor = n2
    else:
        menor = n3
    print(f"{media:.1f}")
    print(f"{maior}")
    print(f"{menor:.1f}")