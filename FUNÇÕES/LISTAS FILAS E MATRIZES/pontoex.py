qtd = int(input("Quantas pessoas serão cadastradas? "))
nomes = []
idades = []
cpfs = []
for i in range(qtd):
    print(f"\nCadastro {i+1}:")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cpf = input("CPF: ")
    nomes.append(nome)
    idades.append(idade)
    cpfs.append(cpf)
busca = input("\nDigite o nome da pessoa que deseja consultar: ")
if busca in nomes:
    i = nomes.index(busca)
    print(f"Idade: {idades[i]}")
    print(f"CPF: {cpfs[i]}")
else:
    print("Pessoa não encontrada.")