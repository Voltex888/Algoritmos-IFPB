x = str(input()).strip().upper()
i = x.count("SILVA")
branco = "\033[1;37;40m"
limpar = "\033[m"
if i >=1:
    print(f"Você tem {branco}Silva{limpar} no nome")
else:
    print(f"Você não tem {branco}Silva{limpar} no nome")