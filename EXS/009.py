# mes vai ser 30 dias
# o ano vai ser 365 dias
dias = int(input())
anos = dias//365
dias = dias%365
mes = dias//30
dias = dias%30
print(f"{anos} ano(s)")
print(f"{mes} mes(es)")
print(f"{dias} dia(s)")