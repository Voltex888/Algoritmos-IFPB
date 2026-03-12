lista = []
prioridade = []
for i in range(5):
    pessoa = input(f"{i}° pessoa: ")
    c = input("s para prioridade ou n para normal: ").upper()
    if c == "S":
        prioridade.append(pessoa)
    else:
        lista.append(pessoa)
fila_final = []
for i in range(5):
    if len(prioridade) >=1:
        fila_final.append(prioridade[0])
        prioridade.pop(0)
    if len(lista) >=1:
        for i in range(1):
            fila_final.append(lista[0])
            lista.pop(0)
    if len(lista) >=1:
        for i in range(1):
            fila_final.append(lista[0])
            lista.pop(0)
print("Fila final organizada:")
for i in range(5):
    print(f"{i+1}°: {fila_final[i]}")