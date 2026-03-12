testes = int(input())
fib = [0, 1]
for i in range(2, 61):
    fib.append(fib[i-1]+fib[i-2])
for j in range(testes):
    x = int(input())
    print(f"Fib({x}) = {fib[x]}")