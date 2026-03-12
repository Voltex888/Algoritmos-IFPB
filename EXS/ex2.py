x = int(input())
N = [x]
for i in range(10):
    print(f"N[{i}] = {N[i]}")
    x *= 2
    N.append(x)