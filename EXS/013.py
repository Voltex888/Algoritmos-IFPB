# Você vai criar um sistema de cadastro rápido.
# Peça ao usuário que digite nome, idade e altura na mesma linha, separados por espaço, por exemplo:
nome, idade, altura = input("Digite seu nome, ao lado com um espaço a sua idade e da mesma forma sua altura: ").split()
nome = str(nome)
idade = int(idade)
altura =int(altura)
print(f"Nome: {nome}, Idade: {idade} ano(s), Altura: {altura} CM ")