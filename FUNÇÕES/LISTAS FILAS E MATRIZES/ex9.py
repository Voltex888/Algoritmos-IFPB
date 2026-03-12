alunos = []
a, b = map(int,input().split())
for i in range(a):
    aluno = input()
    alunos.append(aluno)
    alunos.sort()
print(alunos[b-1])