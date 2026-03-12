n = int(input())
for m in range(n):
    nota1, nota2, nota3 = input().split()
    nota1 = float(nota1)
    nota2 = float(nota2)
    nota3 = float(nota3)
    p1 = 2
    p2 = 3
    p3 = 5
    m = ((nota1 * p1)+(nota2 * p2)+(nota3 * p3)) /(p1 + p2 + p3)
    print(f"{m:.1f}")