# faça um progama que leia a velocidade em KM/h e a quantidade de horas na viagem, a cada 1 km o carro roda 20 litros,
# e no final der a quantidade de litros que foi ultizada a durante a viagem
# e no fim mostre "xx Litros"
kmh = int(input())
horas = int(input())
km = kmh * horas
kml = km / 20
print(f"{kml} km(l)")