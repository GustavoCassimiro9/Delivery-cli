from Modulos.Produtos.ProdutosDAO import ProdutosDAO

def menu_produtos():
    print("============================")
    print("         PRODUTOS")
    print("============================")
    print("1 - Listar Todos os Produtos")
    print("2 - Listar Produtos por Restaurante")
    print("3 - Cadastrar Produto")
    print("4 - Atualizar Produto")
    print("5 - Remover Produto")
    print("0 - Voltar")
    print("============================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        menu_listar_todos()
    elif opcao == "2":
        menu_listar_por_restaurante()
    elif opcao == "3":
        menu_cadastrar()
    elif opcao == "4":
        menu_atualizar()
    elif opcao == "5":
        menu_remover()


def menu_listar_todos():
    dao = ProdutosDAO()
    produtos = dao.listar_todos()

    for p in produtos:
        print(f"{p.codigo} | {p.nome} | {p.preco}")

    menu_produtos()


def menu_listar_por_restaurante():
    dao = ProdutosDAO()
    restaurante_id = input("ID do restaurante: ")

    produtos = dao.listar_por_restaurante(restaurante_id)
    for p in produtos:
        print(f"{p.codigo} | {p.nome} | {p.preco}")

    menu_produtos()


def menu_cadastrar():
    dao = ProdutosDAO()

    restaurante_id = input("ID do restaurante: ")
    nome = input("Nome do produto: ")
    descricao = input("Descrição: ")
    preco = input("Preço: ")

    sucesso = dao.cadastrar(restaurante_id, nome, descricao, preco)
    print("Produto cadastrado." if sucesso else "Erro ao cadastrar produto.")

    menu_produtos()


def menu_atualizar():
    dao = ProdutosDAO()

    produto_id = input("ID do produto: ")
    nome = input("Novo nome: ")
    descricao = input("Nova descrição: ")
    preco = input("Novo preço: ")

    sucesso = dao.atualizar(produto_id, nome, descricao, preco)
    print("Produto atualizado." if sucesso else "Erro ao atualizar produto.")

    menu_produtos()


def menu_remover():
    dao = ProdutosDAO()
    produto_id = input("ID do produto: ")

    sucesso = dao.remover(produto_id)
    print("Produto removido." if sucesso else "Erro ao remover produto.")

    menu_produtos()
