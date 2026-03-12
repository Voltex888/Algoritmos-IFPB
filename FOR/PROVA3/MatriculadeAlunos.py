# faca uma lista que leia 5 nome de alunos e peça a eles a sua matricula, o nome da sua mãe, o seu cpf, 
# as suas 4 notas, diga sua média, e retorne sua maior nota e menor nota, e se for acima 7 apareça aprovado.
qtd = int(input("Quantos alunos deseja cadastrar? "))
alunos = []
for i in range(qtd):
    print(f"\nAluno {i+1}")
    nome = input("Nome: ")
    matricula = input("Matrícula: ")
    mae = input("Nome da mãe: ")
    cpf = input("CPF: ")
    notas4 = list(map(float, input("Digite as 4 notas separadas por espaço: ").split()))
    media = sum(notas4) / len(notas4)
    maiornota = max(notas4)
    menornota = min(notas4)
    aluno = {
        "nome": nome,
        "matricula": matricula,
        "mae": mae,
        "cpf": cpf,
        "notas": notas4,
        "maior": maiornota,
        "menor": menornota,
        "media": media
    }
    alunos.append(aluno)
print("-=-" * 20)
for i, aluno in enumerate(alunos, start=1):
    print(f"\nAluno {i}: {aluno['nome']}")
    print(f"Matrícula: {aluno['matricula']}")
    print(f"Mãe: {aluno['mae']}")
    print(f"CPF: {aluno['cpf']}")
    print(f"Notas: {aluno['notas']}")
    print(f"Maior nota: {aluno['maior']}")
    print(f"Menor nota: {aluno['menor']}")
    print(f"Média: {aluno['media']:.2f}")
    if aluno["media"] >= 7:
        print(f"{aluno['nome']} foi aprovado.")
    else:
        print(f"{aluno['nome']} foi reprovado.")