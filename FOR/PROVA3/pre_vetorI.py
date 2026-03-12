x = int(input())
N = []
for i in range(1000):
    N.append(i%x)
    print(f"N[{i}] = {N[i]}")