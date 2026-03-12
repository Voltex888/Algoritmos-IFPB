# Cédulas
nota = int(input())
print(nota)
nota100 = nota //100
nota = nota%100
nota50 = nota //50
nota = nota%50
nota20 = nota //20
nota = nota%20
nota10 = nota//10
nota = nota%10
nota5 = nota //5
nota = nota%5
nota2 = nota//2
nota = nota %2
nota1 = nota//1
print(f"{nota100} R$ 100,00")
print(f"{nota50} R$ 50,00")
print(f"{nota20} R$ 20,00")
print(f"{nota10} R$ 10,00")
print(f"{nota5} R$ 5,00")
print(f"{nota2} R$ 2,00")
print(f"{nota1} R$ 1,00")