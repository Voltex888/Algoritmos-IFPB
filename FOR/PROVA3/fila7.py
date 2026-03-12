N = []
for i in range(5):
    x = int(input())
    N.append(x)
    N.sort(reverse=True)
for j in range(5):
    print(f"N[{j}] = {N[j]}")