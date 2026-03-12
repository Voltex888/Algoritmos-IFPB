painel = ["F", "A", "C", "E"]
qtd = int(input())
brindes = 0
for i in range(qtd):
    entrada = input().split()
    for letra in entrada:
        painel.append(letra)
    if len(painel) >= 8:
        ultimas = painel[-4:]
        anteriores = painel [-8: -4]
        if ultimas == anteriores[::-1]:
            brindes += 1
            for i in range(8):
                painel.pop()
            if len(painel) == 0:
                painel = ["F", "A", "C", "E"]
print(brindes)