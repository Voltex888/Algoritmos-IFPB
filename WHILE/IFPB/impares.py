n = int(input())
for _ in range(n):
    x, y = input().split()
    x = int(x)
    y = int(y)
    soma = 0
    if x > y:
        x, y = y, x
    for i in range(x + 1, y):
        if i %2 !=0:
            soma += i
    print(soma)