nota = int(input())
print(nota)
notas100 = nota//100
nota = nota%100
notas50 = nota//50
nota = nota%50
notas20 = nota//20
nota = nota%20
notas10 = nota//10
nota = nota%10
notas5 = nota//5
nota = nota%5
notas2 = nota//2
nota = nota%2
notas1 = nota//1
print(f"{notas100} nota(s) de R$100,00")
print(f"{notas50} nota(s) de R$50,00")
print(f"{notas20} nota(s) de R$20,00")
print(f"{notas10} nota(s) de R$10,00")
print(f"{notas5} nota(s) de R$5,00")
print(f"{notas2} nota(s) de R$2,00")
print(f"{notas1} nota(s) de R$1,00")