par = 0
for i in range(5):
    pares = int(input())
    if pares %2 == 0:
        par += 1
print(f"{par} valores pares")