from ClientesDAO import ClientesDAO

def menu_cliente():
    print("============================")
    print("Cadastro de Clientes")
    print("============================")
    print("1 - Listar Todos os Clientes")
    print("2 - Listar um Cliente")
    print("3 - Inserir um Cliente")
    print("4 - Atualizar um Cliente")
    print("5 - Remover um Cliente")
    print("6 - Listar Telefones do Cliente")
    print("7 - Adicionar Telefone ao Cliente")
    print("8 - Remover Telefone do Cliente")
    print("9 - Listar Restaurantes Favoritos do Cliente")
    print("10 - Adicionar Restaurante Favorito")
    print("11 - Remover Restaurante Favorito")
    print("0 - Voltar")
    print("============================")

    try:
        opcao = int(input("Digite uma opção [0-11]: "))
    except ValueError:
        print("Opção inválida.")
        return

    if opcao == 1:
        return menu_listar_todos_clientes()
    elif opcao == 2:
        return menu_listar_um_cliente()
    elif opcao == 3:
        return menu_inserir_um_cliente()
    elif opcao == 4:
        return menu_atualizar_um_cliente()
    elif opcao == 5:
        return menu_remover_um_cliente()
    elif opcao == 6:
        return menu_listar_telefones_cliente()
    elif opcao == 7:
        return menu_adicionar_telefone_cliente()
    elif opcao == 8:
        return menu_remover_telefone_cliente()
    elif opcao == 9:
        return menu_listar_favoritos_cliente()
    elif opcao == 10:
        return menu_adicionar_favorito_cliente()
    elif opcao == 11:
        return menu_remover_favorito_cliente()
    elif opcao == 0:
        return
    else:
        print("Opção inválida.")
        return menu_cliente()

def menu_listar_todos_clientes():
    dao = ClientesDAO()
    clientes = dao.listarTodas()

    if not clientes:
        print("Nenhum registro encontrado")
    else:
        for c in clientes:
            print(f"ID = {c.codigo} | Nome = {c.nome} | Endereço = {c.endereco}")

    return menu_cliente()

def menu_listar_um_cliente():
    dao = ClientesDAO()
    try:
        id_cliente = int(input("Digite o ID do cliente: "))
    except ValueError:
        print("ID inválido.")
        return menu_cliente()

    c = dao.listar(id_cliente)
    if c is None:
        print("Nenhum registro encontrado")
    else:
        print(f"ID = {c.codigo}")
        print(f"Nome = {c.nome}")
        print(f"Endereço = {c.endereco}")

        telefones = dao.listar_telefones(c.codigo)
        if telefones:
            print("Telefones:")
            for ddd, numero in telefones:
                print(f"({ddd}) {numero}")
        else:
            print("Nenhum telefone cadastrado.")

        favoritos = dao.listar_favoritos(c.codigo)
        if favoritos:
            print("Restaurantes favoritos:")
            for (rid, rnome, rend, rcat) in favoritos:
                print(f"- ID {rid} | {rnome} | {rend} | {rcat}")
        else:
            print("Nenhum restaurante favorito cadastrado.")

    return menu_cliente()

def menu_inserir_um_cliente():
    dao = ClientesDAO()
    nome = input("Digite o nome do cliente: ")
    endereco = input("Digite o endereço do cliente: ")

    sucesso = dao.cadastrar_cliente(nome, endereco)
    print("Cliente cadastrado com sucesso" if sucesso else "Falha ao cadastrar cliente")

    return menu_cliente()

def menu_atualizar_um_cliente():
    dao = ClientesDAO()
    try:
        id_cliente = int(input("Digite o ID do cliente: "))
    except ValueError:
        print("ID inválido.")
        return menu_cliente()

    nome = input("Digite o nome do cliente: ")
    endereco = input("Digite o endereço do cliente: ")

    sucesso = dao.atualizar(nome, endereco, id_cliente)
    print("Cliente atualizado com sucesso" if sucesso else "Falha ao atualizar cliente")

    return menu_cliente()

def menu_remover_um_cliente():
    dao = ClientesDAO()
    try:
        id_cliente = int(input("Digite o ID do cliente: "))
    except ValueError:
        print("ID inválido.")
        return menu_cliente()

    sucesso = dao.remover(id_cliente)
    print("Cliente removido com sucesso" if sucesso else "Falha ao remover cliente")

    return menu_cliente()

# --------- TELEFONES ---------

def menu_listar_telefones_cliente():
    dao = ClientesDAO()
    try:
        id_cliente = int(input("Digite o ID do cliente: "))
    except ValueError:
        print("ID inválido.")
        return menu_cliente()

    telefones = dao.listar_telefones(id_cliente)
    if not telefones:
        print("Nenhum telefone encontrado.")
    else:
        print("Telefones do cliente:")
        for ddd, numero in telefones:
            print(f"({ddd}) {numero}")

    return menu_cliente()

def menu_adicionar_telefone_cliente():
    dao = ClientesDAO()
    try:
        id_cliente = int(input("Digite o ID do cliente: "))
    except ValueError:
        print("ID inválido.")
        return menu_cliente()

    ddd = input("Digite o DDD: ").strip()
    numero = input("Digite o número: ").strip()

    sucesso = dao.adicionar_telefone(id_cliente, ddd, numero)
    print("Telefone adicionado com sucesso" if sucesso else "Falha ao adicionar telefone")

    return menu_cliente()

def menu_remover_telefone_cliente():
    dao = ClientesDAO()
    try:
        id_cliente = int(input("Digite o ID do cliente: "))
    except ValueError:
        print("ID inválido.")
        return menu_cliente()

    ddd = input("Digite o DDD: ").strip()
    numero = input("Digite o número: ").strip()

    sucesso = dao.remover_telefone(id_cliente, ddd, numero)
    print("Telefone removido com sucesso" if sucesso else "Falha ao remover telefone")

    return menu_cliente()

# --------- FAVORITOS ---------

def menu_listar_favoritos_cliente():
    dao = ClientesDAO()
    try:
        id_cliente = int(input("Digite o ID do cliente: "))
    except ValueError:
        print("ID inválido.")
        return menu_cliente()

    favoritos = dao.listar_favoritos(id_cliente)
    if not favoritos:
        print("Nenhum restaurante favorito encontrado.")
    else:
        print("Restaurantes favoritos do cliente:")
        for (rid, rnome, rend, rcat) in favoritos:
            print(f"- ID {rid} | {rnome} | {rend} | {rcat}")

    return menu_cliente()

def menu_adicionar_favorito_cliente():
    dao = ClientesDAO()
    try:
        id_cliente = int(input("Digite o ID do cliente: "))
        restaurante_id = int(input("Digite o ID do restaurante: "))
    except ValueError:
        print("ID inválido.")
        return menu_cliente()

    sucesso = dao.adicionar_favorito(id_cliente, restaurante_id)
    print("Favorito adicionado com sucesso" if sucesso else "Falha ao adicionar favorito ou restaurante nao existe")

    return menu_cliente()

def menu_remover_favorito_cliente():
    dao = ClientesDAO()
    try:
        id_cliente = int(input("Digite o ID do cliente: "))
        restaurante_id = int(input("Digite o ID do restaurante: "))
    except ValueError:
        print("ID inválido.")
        return menu_cliente()

    sucesso = dao.remover_favorito(id_cliente, restaurante_id)
    print("Favorito removido com sucesso" if sucesso else "Falha ao remover favorito")

    return menu_cliente()