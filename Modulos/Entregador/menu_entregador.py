from Modulos.Entregador.EntregadoresDAO import EntregadoresDAO

def menu_entregador():
    print("============================")
    print("Cadastro de Entregadores")
    print("============================")
    print("1 - Listar Todos os Entregadores")
    print("2 - Listar um Entregadores")
    print("3 - Inserir um Entregador")
    print("4 - Atualizar um Entregador")
    print("5 - Remover um Entregador")
    print("6 - Listar Telefones do Entregador")
    print("7 - Adicionar Telefone ao Entregador")
    print("8 - Remover Telefone do Entregador")
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
        return menu_entregador()

def menu_listar_todos():
    dao = EntregadoresDAO()
    restaurantes = dao.listarTodas()

    if not restaurantes:
        print("Nenhum registro encontrado")
    else:
        for c in restaurantes:
            print(f"ID = {c.codigo} | Nome = {c.nome} | Descrição = {c.descricao}, | Preco = {c.preco}")

    return menu_entregador()

def menu_listar_um():
    dao = EntregadoresDAO()
    try:
        id_entregador = int(input("Digite o ID: "))
    except ValueError:
        print("ID inválido.")
        return menu_entregador()

    c = dao.listar(id_entregador)
    if c is None:
        print("Nenhum registro encontrado")
    else:
        print(f"ID = {c.codigo}")
        print(f"Nome = {c.nome}")
        print(f"Discricao = {c.descricao}")
        print(f"Preco = {c.preco}")

        telefones = dao.listar_telefones(c.codigo)
        if telefones:
            print("Telefones:")
            for ddd, numero in telefones:
                print(f"({ddd}) {numero}")
        else:
            print("Nenhum telefone cadastrado.")

    return menu_entregador()

def menu_inserir_um():
    dao = EntregadoresDAO()
    nome = input("Digite o nome do entregador: ")
    descricao = input("Digite a descricao do entregador: ")
    preco = input("Digite o preco do entregador: ")

    sucesso = dao.cadastrar_entregadores(nome, descricao, preco)
    print("Entregador cadastrado com sucesso" if sucesso else "Falha ao cadastrar")

    return menu_entregador()

def menu_atualizar_um():
    dao = EntregadoresDAO()
    try:
        id_restaurante = int(input("Digite o ID: "))
    except ValueError:
        print("ID inválido.")
        return menu_entregador()

    nome = input("Digite o nome do entregador: ")
    descricao = input("Digite a descricao do entregador: ")
    preco = input("Digite o preco do entregador: ")

    sucesso = dao.atualizar(nome, descricao,preco , id_restaurante)
    print("Restaurante atualizado com sucesso" if sucesso else "Falha ao atualizar restaurante ")

    return menu_entregador()

def menu_remover_um():
    dao = EntregadoresDAO()
    try:
        id_entregador = int(input("Digite o ID: "))
    except ValueError:
        print("ID inválido.")
        return menu_entregador()

    sucesso = dao.remover(id_entregador)
    print("Entregador removido com sucesso" if sucesso else "Falha ao remover")

    return menu_entregador()

# --------- TELEFONES ---------

def menu_listar_telefones():
    dao = EntregadoresDAO()
    try:
        id_entregador = int(input("Digite o ID: "))
    except ValueError:
        print("ID inválido.")
        return menu_entregador()

    telefones = dao.listar_telefones(id_entregador)
    if not telefones:
        print("Nenhum telefone encontrado.")
    else:
        print("Telefones:")
        for ddd, numero in telefones:
            print(f"({ddd}) {numero}")

    return menu_entregador()

def menu_adicionar_telefone():
    dao = EntregadoresDAO()
    try:
        id_entregador= int(input("Digite o ID: "))
    except ValueError:
        print("ID inválido.")
        return menu_entregador()

    ddd = input("Digite o DDD: ").strip()
    numero = input("Digite o número: ").strip()

    sucesso = dao.adicionar_telefone(id_entregador, ddd, numero)
    print("Telefone adicionado com sucesso" if sucesso else "Falha ao adicionar telefone")

    return menu_entregador()

def menu_remover_telefone():
    dao = EntregadoresDAO()
    try:
        id_entregador = int(input("Digite o ID: "))
    except ValueError:
        print("ID inválido.")
        return menu_entregador()

    ddd = input("Digite o DDD: ").strip()
    numero = input("Digite o número: ").strip()

    sucesso = dao.remover_telefone(id_entregador, ddd, numero)
    print("Telefone removido com sucesso" if sucesso else "Falha ao remover telefone")

    return menu_entregador()
