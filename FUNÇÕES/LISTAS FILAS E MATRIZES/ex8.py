n = int(input())
painel = ['F', 'A', 'C', 'E']
brindes = 0
for _ in range(n):
    entrada = input().split()
    for letra in entrada:
        painel.append(letra)
    if len(painel) >= 8:
        ultimas = painel[-4:]
        anteriores = painel[-8:-4]
        if ultimas == anteriores[::-1]:
            brindes += 1
            for _ in range(8):
                painel.pop()
            if len(painel) == 0:
                painel.extend(['F', 'A', 'C', 'E'])
print(brindes)
