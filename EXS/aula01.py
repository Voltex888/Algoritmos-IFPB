x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
distancia = ((x2-x1)**2+(y2-y1)**2)**0.5
cor = "\033[1;37;40m"
print(f"{cor}{distancia:.4f}\033[m")