n = int(input())
for i in range(n):
    x , y = map(float,input().split())
    if y == 0:
        print("divisao impossivel")
    else:
        divisao = x / y
        print(f"{divisao:.1f}")