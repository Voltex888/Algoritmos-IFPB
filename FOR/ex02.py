positivo = 0
for num in range(6):
    num = float(input(""))
    if num >= 0:
        positivo = positivo + 1
print(f"{positivo} valores positivos")