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
    print("0 - Voltar")
    print("============================")

    try:
        opcao = int(input("Digite uma opção [0-8]: "))
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
            print(f"Código = {c.codigo} | Nome = {c.nome} | Endereço = {c.endereco}")

    return menu_cliente()

def menu_listar_um_cliente():
    dao = ClientesDAO()
    try:
        codigo = int(input("Digite o código do cliente: "))
    except ValueError:
        print("Código inválido.")
        return menu_cliente()

    c = dao.listar(codigo)
    if c is None:
        print("Nenhum registro encontrado")
    else:
        print(f"Código = {c.codigo}")
        print(f"Nome = {c.nome}")
        print(f"Endereço = {c.endereco}")

        telefones = dao.listar_telefones(c.codigo)
        if telefones:
            print("Telefones:")
            for ddd, numero in telefones:
                print(f"({ddd}) {numero}")
        else:
            print("Nenhum telefone cadastrado.")

    return menu_cliente()

def menu_inserir_um_cliente():
    dao = ClientesDAO()
    nome = input("Digite o nome do cliente: ")
    endereco = input("Digite o endereço do cliente: ")

    sucesso = dao.cadastrar_cliente(nome, endereco)
    if sucesso:
        print("Cliente cadastrado com sucesso")
    else:
        print("Falha ao cadastrar cliente")

    return menu_cliente()

def menu_atualizar_um_cliente():
    dao = ClientesDAO()
    nome = input("Digite o nome do cliente: ")
    endereco = input("Digite o endereço do cliente: ")

    try:
        codigo = int(input("Digite o código do cliente: "))
    except ValueError:
        print("Código inválido.")
        return menu_cliente()

    sucesso = dao.atualizar(nome, endereco, codigo)
    if sucesso:
        print("Cliente atualizado com sucesso")
    else:
        print("Falha ao atualizar cliente")

    return menu_cliente()

def menu_remover_um_cliente():
    dao = ClientesDAO()
    try:
        codigo = int(input("Digite o código do cliente: "))
    except ValueError:
        print("Código inválido.")
        return menu_cliente()

    sucesso = dao.remover(codigo)
    if sucesso:
        print("Cliente removido com sucesso")
    else:
        print("Falha ao remover cliente")

    return menu_cliente()

# --------- TELEFONES ---------

def menu_listar_telefones_cliente():
    dao = ClientesDAO()
    try:
        codigo = int(input("Digite o código do cliente: "))
    except ValueError:
        print("Código inválido.")
        return menu_cliente()

    telefones = dao.listar_telefones(codigo)
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
        codigo = int(input("Digite o código do cliente: "))
    except ValueError:
        print("Código inválido.")
        return menu_cliente()

    ddd = input("Digite o DDD: ")
    numero = input("Digite o número: ")

    sucesso = dao.adicionar_telefone(codigo, ddd, numero)
    if sucesso:
        print("Telefone adicionado com sucesso")
    else:
        print("Falha ao adicionar telefone")

    return menu_cliente()

def menu_remover_telefone_cliente():
    dao = ClientesDAO()
    try:
        codigo = int(input("Digite o código do cliente: "))
    except ValueError:
        print("Código inválido.")
        return menu_cliente()

    ddd = input("Digite o DDD: ")
    numero = input("Digite o número: ")

    sucesso = dao.remover_telefone(codigo, ddd, numero)
    if sucesso:
        print("Telefone removido com sucesso")
    else:
        print("Falha ao remover telefone")

    return menu_cliente()
