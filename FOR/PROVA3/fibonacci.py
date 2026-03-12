testes = int(input())
Fib = [0, 1]
for j in range(2, 61):
    Fib.append(Fib[j-1]+Fib[j-2])
for i in range(testes):
    x = int(input())
    print(f"Fib({x}) = {Fib[x]}")
    