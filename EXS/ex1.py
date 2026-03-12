X = []
for i in range(10):
    y = int(input())
    if y <= 0:
        y = 1
    X.append(y)
for j in range(len(X)):
    print(f"X[{j}] = {X[j]}")