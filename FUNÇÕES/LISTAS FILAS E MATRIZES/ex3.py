N = []
t = int(input())
for i in range(5):
    N.append(i % t)
    print(f"N[{i}] = {N[i]}")