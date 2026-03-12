pessoas = input("Digite o número de vagas: ")
certos = list(map(int, input("Digite 1 para cada pessoa confirmada e 0 para cada desistente: ").split()))
print(f"De {pessoas} pessoas, só {certos.count(1)} confirmaram presença e {certos.count(0)} desistaram")