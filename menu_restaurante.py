from RestaurantesDAO import RestaurantesDAO

def menu_restaurante():
    print("============================")
    print("Cadastro de Restaurantes")
    print("============================")
    print("1 - Listar Todos os Restaurantes")
    print("2 - Listar um Restaurante")
    print("3 - Inserir um Restaurante")
    print("4 - Atualizar um Restaurante")
    print("5 - Remover um Restaurante")
    print("6 - Listar Telefones do Restaurante")
    print("7 - Adicionar Telefone ao Restaurante")
    print("8 - Remover Telefone do Restaurante")
    print("0 - Voltar")
    print("============================")

    try:
        opcao = int(input("Digite uma opção [0-11]: "))
    except ValueError:
        print("Opção inválida.")
        return

    if opcao == 1:
        return menu_listar_todos()
    elif opcao == 2:
        return menu_listar_um()
    elif opcao == 3:
        return menu_inserir_um()
    elif opcao == 4:
        return menu_atualizar_um()
    elif opcao == 5:
        return menu_remover_um()
    elif opcao == 6:
        return menu_listar_telefones()
    elif opcao == 7:
        return menu_adicionar_telefone()
    elif opcao == 8:
        return menu_remover_telefone()
    elif opcao == 0:
        return
    else:
        print("Opção inválida.")
        return menu_restaurante()

def menu_listar_todos():
    dao = RestaurantesDAO()
    restaurantes = dao.listarTodas()

    if not restaurantes:
        print("Nenhum registro encontrado")
    else:
        for c in restaurantes:
            print(f"ID = {c.codigo} | Nome = {c.nome} | Endereço = {c.endereco}, | Categoria = {c.categoria}")

    return menu_restaurante()

def menu_listar_um():
    dao = RestaurantesDAO()
    try:
        id_restaurante = int(input("Digite o ID do cliente: "))
    except ValueError:
        print("ID inválido.")
        return menu_restaurante()

    c = dao.listar(id_restaurante)
    if c is None:
        print("Nenhum registro encontrado")
    else:
        print(f"ID = {c.codigo}")
        print(f"Nome = {c.nome}")
        print(f"Endereço = {c.endereco}")
        print(f"categoria = {c.categoria}")

        telefones = dao.listar_telefones(c.codigo)
        if telefones:
            print("Telefones:")
            for ddd, numero in telefones:
                print(f"({ddd}) {numero}")
        else:
            print("Nenhum telefone cadastrado.")

    return menu_restaurante()

def menu_inserir_um():
    dao = RestaurantesDAO()
    nome = input("Digite o nome do restaurante: ")
    endereco = input("Digite o endereço do restaurante: ")
    categoria = input("Digite a categoria do restaurante: ")

    sucesso = dao.cadastrar_restaurante(nome, endereco, categoria)
    print("Restaurante cadastrado com sucesso" if sucesso else "Falha ao cadastrar restaurante")

    return menu_restaurante()

def menu_atualizar_um():
    dao = RestaurantesDAO()
    try:
        id_restaurante = int(input("Digite o ID do cliente: "))
    except ValueError:
        print("ID inválido.")
        return menu_restaurante()

    nome = input("Digite o nome do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    categoria = input("Digite a categoria do restaurante: ")

    sucesso = dao.atualizar(nome, endereco,categoria, id_restaurante)
    print("Restaurante atualizado com sucesso" if sucesso else "Falha ao atualizar restaurante ")

    return menu_restaurante()

def menu_remover_um():
    dao = RestaurantesDAO()
    try:
        id_restaurante = int(input("Digite o ID do cliente: "))
    except ValueError:
        print("ID inválido.")
        return menu_restaurante()

    sucesso = dao.remover(id_restaurante)
    print("Restaurante removido com sucesso" if sucesso else "Falha ao remover restaurante")

    return menu_restaurante()

# --------- TELEFONES ---------

def menu_listar_telefones():
    dao = RestaurantesDAO()
    try:
        id_restaurante = int(input("Digite o ID do cliente: "))
    except ValueError:
        print("ID inválido.")
        return menu_restaurante()

    telefones = dao.listar_telefones(id_restaurante)
    if not telefones:
        print("Nenhum telefone encontrado.")
    else:
        print("Telefones do cliente:")
        for ddd, numero in telefones:
            print(f"({ddd}) {numero}")

    return menu_restaurante()

def menu_adicionar_telefone():
    dao = RestaurantesDAO()
    try:
        id_restaurante = int(input("Digite o ID do cliente: "))
    except ValueError:
        print("ID inválido.")
        return menu_restaurante()

    ddd = input("Digite o DDD: ").strip()
    numero = input("Digite o número: ").strip()

    sucesso = dao.adicionar_telefone(id_restaurante, ddd, numero)
    print("Telefone adicionado com sucesso" if sucesso else "Falha ao adicionar telefone")

    return menu_restaurante()

def menu_remover_telefone():
    dao = RestaurantesDAO()
    try:
        id_restaurante = int(input("Digite o ID do cliente: "))
    except ValueError:
        print("ID inválido.")
        return menu_restaurante()

    ddd = input("Digite o DDD: ").strip()
    numero = input("Digite o número: ").strip()

    sucesso = dao.remover_telefone(id_restaurante, ddd, numero)
    print("Telefone removido com sucesso" if sucesso else "Falha ao remover telefone")

    return menu_restaurante()
