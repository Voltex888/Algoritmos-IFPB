N = []
x = int(input())
for i in range(10):
    N.append(i%x)
    print(f"N[{i}] = {N[i]}")