par = []
impar = []
for i in range(15):
    x = int(input())
    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)
    if len(par) == 5:
        for k in range(5):
            print(f"par[{k}] = {par[k]}")
        par = []
    if len(impar) == 5:
        for k in range(5):
            print(f"impar[{k}] = {impar[k]}")
        impar = []
for k in range(len(impar)):
    print(f"impar[{k}] = {impar[k]}")
for k in range(len(par)):
    print(f"par[{k}] = {par[k]}")