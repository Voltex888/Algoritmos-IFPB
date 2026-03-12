def verificar_valor(valor):
    if valor > 50:
        imposto = valor * 0.20
    if valor > 25:
        imposto = valor * 0.50
    else:
        imposto = valor
    return imposto
valor = 100
print(verificar_valor(valor))