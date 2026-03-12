fila = ["Matheus", "caio", "Pedro", "Magnum", "Ruan", "Miguel", "Luiz" ]
for i  in range(len(fila)): #fila
    proximapessoa = fila[0]
    fila.pop(0)
print(proximapessoa)

for i  in range(len(fila)): #pilha
    proximapessoa = fila[-1]
    fila.pop(-1)
print(proximapessoa)