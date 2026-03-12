n1, n2, n3, n4 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
p1 = 2
p2 = 3
p3 = 4
p4 = 1
media = ((n1*p1)+(n2*p2)+(n3*p3)+(n4*p4))/(p1+p2+p3+p4)
print(f"Media: {media:.1f} ")
if media >= 7:
    print("Aluno aprovado.")
elif media <5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exame = float(input())
    print(f"Nota de exame: {exame:.1f}")
    media_final = (media+exame) /2
    if media_final >= 5:
        print(f"Media final: {media_final:.1f}")
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")