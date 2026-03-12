a = []
for i in range(100):
    x = float(input())
    a.append(x) 
    if x <= 10:
        print(f"A[{i}] = {a[i]}")