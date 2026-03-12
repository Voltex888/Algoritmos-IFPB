N = []
for i in range(20):
    x = int(input())
    N.append(x)
N.reverse()
for i in range(20):
    print(f"N[{i}] = {N[i]}")