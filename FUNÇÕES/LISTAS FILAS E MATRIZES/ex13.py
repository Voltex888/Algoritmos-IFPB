qtd = int(input())
fib = [0, 1]
for i in range(2, 61):
    fib.append(fib[i-1] + fib[i-2])
    
for x in range(qtd):
    n = int(input())
    print(f"Fib ({n}) = {fib[n]}")