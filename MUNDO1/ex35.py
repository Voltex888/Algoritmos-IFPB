print("-=-"*20)
print("Analisador de triângulo")
print("-=-"*20)
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terçeiro segmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Podem formar um triângulo")
else:
    print("Não podem formar um triângulo")