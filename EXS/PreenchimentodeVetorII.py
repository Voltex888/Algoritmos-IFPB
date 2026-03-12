n = []
t = int(input())
for i in range(1000):
    n.append(i%t)
    print(f"N[{i}] = {n[i]}")