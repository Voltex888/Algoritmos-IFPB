alunos = []
for i in range(2):
    print(f"\nAluno {i+1}")
    nome = input("Nome: ")
    matricula = input("Matrícula: ")
    cpf = input("CPF: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    nota4 = float(input("Nota 4: "))
    aluno = {
        "nome": nome,
        "matricula": matricula,
        "cpf": cpf,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "nota4": nota4}
    alunos.append(aluno)
for a in alunos:
    if a["nota2"] > 70:
        print(a["nome"], "-", a["nota2"])
for a in alunos:
    media = (a["nota1"] + a["nota2"] + a["nota3"] + a["nota4"]) / 4
    print(f"\nNome: {a['nome']}")
    print(f"Matrícula: {a['matricula']}")
    print(f"CPF: {a['cpf']}")
    print(f"Notas: {a['nota1']}, {a['nota2']}, {a['nota3']}, {a['nota4']}")
    print(f"Média final: {media:.2f}")