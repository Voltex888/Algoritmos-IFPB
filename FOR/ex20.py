x = int(input())
y = int(input())
if x > y:
    x, y = y, x
for i in range(x +1, y):
    resto = 0
    if i %5 == 2 or i %5 == 3:
        resto += i
        print(resto)