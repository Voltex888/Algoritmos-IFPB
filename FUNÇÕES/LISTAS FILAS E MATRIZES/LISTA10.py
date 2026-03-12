frutas = ["Goiaba", "Banana", "Laranja", "Manga"]
posicao = frutas.index("Goiaba")
frutas.insert(posicao, "Uva")
print(frutas.count("Goiaba"))
print(frutas.index("Goiaba"))
print(frutas)