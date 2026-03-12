valor = float(input("Digite o valor da sua compra e veja se vc concorre a algum desconto: "))
if valor >= 500 and valor < 1000:
    print(f"Parabéns, vc ganhou 5% de desconto na sua compra, ficando R$ {valor-valor*0.05}")
elif valor >= 1000 and valor <2000:
    print(f"Parabéns, vc ganhou 10% de desconto na sua compra, ficando R$ {valor-valor*0.10}")
elif valor >= 2000:
    print(f"Parabéns, vc ganhou 15% de desconto na sua compra, ficando R$ {valor-valor*0.15}")
else:
    print(f"Infelizmente vc não pode ter direito ao desconto poís seu valor foi R$ {valor}")