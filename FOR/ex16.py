n = int(input())
total_c = 0
total_r = 0
total_s = 0
for i in range(n):
    quantidade, tipo = input().split()
    quantidade = int(quantidade)
    if tipo == "C":
        total_c += quantidade
    elif tipo == "R":
        total_r += quantidade
    elif tipo == "S":
        total_s += quantidade
total = total_c + total_r + total_s
per_c = (total_c / total) * 100
per_r = (total_r / total) * 100
per_s = (total_s / total) * 100
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {total_c}")
print(f"Total de ratos: {total_r}")
print(f"Total de sapos: {total_s}")
print(f"Percentual de coelhos: {per_c:.2f} %")
print(f"Percentual de ratos: {per_r:.2f} %")
print(f"Percentual de sapos: {per_s:.2f} %")