# Programa simples de supermercado

# Variáveis para guardar os produtos e seus preços
produtos = {
    "Arroz": 5.50,
    "Feijão": 7.20,
    "Macarrão": 3.80,
    "Leite": 4.50
}

# Variáveis para guardar o carrinho do cliente
carrinho = {}

# Função para mostrar os produtos disponíveis
def mostrar_produtos():
    print("\nProdutos disponíveis:")
    for nome, preco in produtos.items():
        print(f"{nome} - R$ {preco:.2f}")

# Função para adicionar itens ao carrinho
def adicionar_carrinho():
    produto = input("\nDigite o nome do produto que deseja comprar: ")
    if produto in produtos:
        qtd = int(input("Digite a quantidade: "))
        carrinho[produto] = carrinho.get(produto, 0) + qtd
        print(f"{qtd}x {produto} adicionado(s) ao carrinho!")
    else:
        print("Produto não encontrado.")

# Função para calcular o total da compra
def calcular_total():
    total = 0
    print("\nCarrinho de compras:")
    for produto, qtd in carrinho.items():
        preco = produtos[produto]
        subtotal = preco * qtd
        print(f"{produto} - {qtd}x R$ {preco:.2f} = R$ {subtotal:.2f}")
        total += subtotal
    print(f"\nTotal da compra: R$ {total:.2f}")

# Programa principal
while True:
    print("\n--- Supermercado ---")
    print("1. Mostrar produtos")
    print("2. Adicionar ao carrinho")
    print("3. Finalizar compra")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        mostrar_produtos()
    elif opcao == "2":
        adicionar_carrinho()
    elif opcao == "3":
        calcular_total()
    elif opcao == "4":
        print("Obrigado por comprar no nosso supermercado!")
        break
    else:
        print("Opção inválida, tente novamente.")
