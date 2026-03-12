for i in range(2):
    nome = input().capitalize()
    matricula = int(input())
    cpf = input().strip()
    n1, n2, n3, n4 = map(float,input().split())
    pessoa = {"nome =": nome, "matricula =": matricula, "CPF =": cpf, "n1 =": n1, "n2 =": n2, "n3 =": n3, "n4 =": n4,}
    for i in range(2):
        print(pessoa)      