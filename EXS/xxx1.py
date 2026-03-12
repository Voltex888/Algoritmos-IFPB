n = int(input())
dolar = n / 5
print(f"{dolar}$")
dolar200 = dolar//200
dolar = dolar%200
dolar100 = dolar//100
dolar = dolar%100
dolar50 = dolar//50
dolar = dolar%50
dolar20 = dolar//20
dolar = dolar%20
dolar10 = dolar//10
dolar = dolar%10
dolar5 = dolar//5
dolar = dolar%5
dolar2 = dolar//2
dolar = dolar%2
dolar1 = dolar//1
print(f"{dolar200:.0f} nota(s) de 200,00$")
print(f"{dolar100:.0f} nota(s) de 100,00$")
print(f"{dolar50:.0f} nota(s) de 50,00$")
print(f"{dolar20:.0f} nota(s) de 20,00$")
print(f"{dolar10:.0f} nota(s) de 10,00$")
print(f"{dolar5:.0f} nota(s) de 5,00$")
print(f"{dolar2:.0f} nota(s) de 2,00$")
print(f"{dolar1:.0f} nota(s) de 1,00$")