class Produto:
    def __init__(self, codigo, nome, preco, estoque):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def __str__(self):
        return f"Código: {self.codigo} - Produto: {self.nome} - R${self.preco:.2f} - Quantidade: {self.estoque} em estoque"

def order_preco(value):
    return value.preco

def order_nome(value):
    return value.nome

def order_estoque(value):
    return value.estoque

def buscar_produto(produtos, busca):
    resultados = []
    for produto in produtos:
        if busca.lower() in produto.nome.lower() or busca == str(produto.codigo):
            resultados.append(produto)
    return resultados



produtos = [Produto("1", "Whey Isolado DUX", 279.9, 15),
            Produto("2","Tasty ISO Adaptogen", 269.9, 10),
            Produto("3", "Gold Whey", 149.9, 40),
            Produto("4", "Ultra Mass Gainers",99.9,8),
            Produto("5", "Mega Mass Gainers", 99.9, 7),
            Produto("6", "Creatina Pura", 189.9, 75),
            Produto("7", "NO Control Pre Workout", 129.9, 30),
            Produto("8", "Arginina", 139.9, 6),
            Produto("9", "Beta Flexx", 199.90, 4),
            Produto("10", "Mass Beef", 269.9, 2),
            Produto("11", "Vegan Protein", 169.9, 4),
            Produto("12", "Isofort", 169.90, 2),
            Produto("13", "Omega 3 Ultra", 129.90, 16),
            Produto("14", "Polimais A-Z", 39.90, 43),
            Produto("15", "Candy Bar Protein", 9.90, 139),
            Produto("16", "Whey Grego Bar", 8.90, 56),
            Produto("17", "Carb Up Black", 4.90, 12),
            Produto("18", "Triptofano", 119.90, 2),
            Produto("19", "Melatonina", 139.90, 3),
            Produto("20", "Testo Geron", 69.90, 2)
            ]

while True:
    print("-"*30)
    print("1 - Inserir produto")
    print("2 - Exibir produtos por preço")
    print("3 - Exibir produtos por nome")
    print("4 - Exibir produtos por quantidade em estoque")
    print("5 - Buscar produto por código ou nome")
    print("6 - Sair")
    print("-"*30)

    menu = input("Escolha uma opção: ")

    if menu == "1":
        codigo = input("Codigo do produto: ")
        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto: "))
        estoque = int(input("Quantidade em estoque: "))
        produto = Produto(codigo, nome, preco, estoque)
        produtos.append(produto)
        print(f"{produto.nome} inserido com sucesso!")
    elif menu == "2":
        produtos_ordenados = sorted(produtos, key=order_preco)
        print("-"*30)
        print("Ordenado por preço:")
        for produto in produtos_ordenados:
            print(produto)
    elif menu == "3":
        produtos_ordenados = sorted(produtos, key=order_nome)
        print("-"*30)
        print("Ordenado por nome:")
        for produto in produtos_ordenados:
            print(produto)
    elif menu == "4":
        produtos_ordenados = sorted(produtos, key=order_estoque)
        print("-"*30)
        print("Ordenado por Quantidade em estoque:")
        for produto in produtos_ordenados:
            print(produto)

    elif menu == "5":
        busca = input("Digite o nome ou código do produto: ")
        resultados = buscar_produto(produtos, busca)
        if resultados:
            for produto in resultados:
                print(produto)
        else:
            print("Produto não encontrado!")

    elif menu == "6":
        print("Obrigado! Volte sempre!")
        break
    else:
        print("Opção inválida!")
