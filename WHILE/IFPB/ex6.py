s = 0
n = 0
x = int(input())
y = int(input())
while (x-s) > 0:
    s += y
    print(f"{x-y*n} - {y} = {x-s}")
    n += 1
print(n)
print(x%y)