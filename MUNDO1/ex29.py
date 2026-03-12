kmh = int(input("Digite a velocidade em que você passou no ultimo radar: "))
if kmh > 80:
    multa = (kmh - 80) * 7
    print(f"Vc foi multado em R$ {multa:.2f}")
elif kmh == 80:
    print("Vc passou raspando")
else:
    print("Vc não recebeu multa")