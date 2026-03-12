qtd = int(input())
Fib = [0, 1]
for x in range(2, 61):
    Fib.append(Fib[x-1]+Fib[x-2])
for i in range(qtd):
    x = int(input())
    print(f"Fib({x}) = {Fib[x]}")