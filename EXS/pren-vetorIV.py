impar = []
par = []
for i in range(15):
    x = int(input())
    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)
    if len(par) == 5:
        for i in range(len(par)):
            print(f"par[{i}] = {par[i]}")
        par = []
    if len(impar) == 5:
        for j in range(len(impar)):
            print(f"impar[{j}] = {impar[j]}")
        impar = []
for j in range(len(impar)):
    print(f"impar[{j}] = {impar[j]}")    
for i in range(len(par)):
    print(f"par[{i}] = {par[i]}")
