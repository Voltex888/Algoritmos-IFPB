#cre um progama para um supermercado que guarde variaveis
from random import choice
chocolate = 15
refri = 6
sal = 1
cafe = 5
feijao = 9
pipoca = 10
listadeprecos = chocolate, sal, cafe, feijao, pipoca
pedidos = str(input(f"Oque vc gostaria de comprar, temos\n pipoca 10 R$\n sal 1 R$\n feijão 9 R$\n café 5 Reais\n refri 6 R$\n chocolate 15 R$\n " ))
pedidos = (listadeprecos)
print(f"Deu {pedidos} R$")
