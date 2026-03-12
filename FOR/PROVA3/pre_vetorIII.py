x = float(input())
N =[x]
for i in range(100):
    print(f"N[{i}] = {N[i]:.4f}")
    x /= 2
    N.append(x)