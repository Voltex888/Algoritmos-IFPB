from random import randint
computador = randint(0, 5)
print("-=-"*20)
print("Eu vou pensar em número entre 0 a 5. Tente adivinhar...")
print("-=-"*20)
jogador = int(input("Em que número eu pensei: "))
if jogador == computador:
    print(f"Você me venceu dessa vez, meu número era {computador}")
else:
    print(f"Você perdeu kkkkkkk, meu número é {computador}")