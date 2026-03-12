def soma (x, y):
    r = x + y
    return r
def multiplica (a,b,c,d):
    x = soma(a,b)
    y = soma(c,d)
    res = x*y
    return res
valor1 = int(input("Digite valor 1: "))
valor2 = int(input("Digite valor 2: "))
valor3 = int(input("Digite valor 3: "))
valor4 = int(input("Digite valor 4: "))
resposta = multiplica(valor1,valor2,valor3,valor4)
print(resposta)