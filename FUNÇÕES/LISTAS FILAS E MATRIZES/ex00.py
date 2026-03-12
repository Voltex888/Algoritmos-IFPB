qtd = int(input())
nomes = []
idades = []
cpfs = []
for i in range(qtd):
    nome = input(f"Digite o {i+1}º nome: ")
    idade = int(input(f"Digite a {i+1}º idade: "))
    cpf = input(f"Digite o {i+1}º CPF: ")
    nomes.append(nome)
    idades.append(idade)
    cpfs.append(cpf)
busca = input("Agora vamos verificar os dados de uma pessoa, então digite um nome: ")
if busca in nomes:
    i = nomes.index(busca)
    print(f"Idade: {idades[i]} anos")
    print(f"CPF: {cpfs[i]}")
else:
    print("Pessoa não encontrada")