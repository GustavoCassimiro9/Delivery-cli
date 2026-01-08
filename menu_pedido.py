from enum import Enum
from PedidosDAO import PedidosDAO
from ProdutosDAO import ProdutosDAO


class StatusPedido(Enum):
    PENDENTE = "PENDENTE"
    FINALIZADO = "FINALIZADO"
    CANCELADO = "CANCELADO"


def menu_pedidos():
    print("============================")
    print("         PEDIDOS")
    print("============================")
    print("1 - Criar Pedido")
    print("2 - Listar Pedidos do Cliente")
    print("3 - Listar Pedidos do Restaurante")
    print("4 - Listar Pedidos do Entregador")
    print("5 - Listar Itens do Pedido")
    print("6 - Cancelar Pedido")
    print("7 - Finalizar Pedido")
    print("0 - Voltar")
    print("============================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        menu_criar_pedido()
    elif opcao == "2":
        menu_listar_pedidos_cliente()
    elif opcao == "3":
        menu_listar_pedidos_restaurante()
    elif opcao == "4":
        menu_listar_pedidos_entregadores()
    elif opcao == "5":
        menu_listar_itens_pedido()
    elif opcao == "6":
        menu_cancelar_pedido()
    elif opcao == "7":
        menu_finalizar_pedido()


def menu_criar_pedido():
    pedidos_dao = PedidosDAO()
    produtos_dao = ProdutosDAO()

    cliente_id = input("ID do cliente: ")
    restaurante_id = input("ID do restaurante: ")
    entregador_id = input("ID do entregador: ")
    nome = input("Nome do pedido: ")
    endereco = input("Endereço de entrega: ")

    pedido_id = pedidos_dao.criar_pedido(
        cliente_id,
        restaurante_id,
        entregador_id,
        nome,
        StatusPedido.PENDENTE.value,
        endereco
    )

    produtos = produtos_dao.listar_por_restaurante(restaurante_id)

    if not produtos:
        print("Este restaurante não possui produtos cadastrados.")
        menu_pedidos()
        return

    print("\nPRODUTOS DISPONÍVEIS:")
    for p in produtos:
        print(f"{p.codigo} | {p.nome} | {p.preco}")

    produtos_validos = [str(p.codigo) for p in produtos]

    while True:
        produto_id = input("\nID do produto (0 para finalizar): ")

        if produto_id == "0":
            break

        if produto_id not in produtos_validos:
            print("Produto inválido para este restaurante.")
            continue

        try:
            quantidade = int(input("Quantidade: "))
        except ValueError:
            print("Quantidade inválida.")
            continue

        pedidos_dao.adicionar_item(pedido_id, produto_id, quantidade)

    menu_pedidos()


def menu_listar_pedidos_cliente():
    dao = PedidosDAO()
    cliente_id = input("ID do cliente: ").strip()

    pedidos = dao.listar_pedidos_cliente(cliente_id)
    if not pedidos:
        print("Nenhum pedido encontrado.")
        return menu_pedidos()
    cliente_nome = pedidos[0].nome_cliente
    print("\n==============================")
    print(f"Cliente {cliente_id} - {cliente_nome}")
    print("==============================")

    for p in pedidos:
        print(
            f"Pedido {p.codigo} | "
            f"Restaurante {p.restaurante_id} - {p.nome_restaurante} | "
            f"Entregador {p.entregador_id} - {p.nome_entregador} | "
            f"{p.nome} | "
            f"{p.status} | "
            f"{p.endereco_entrega}"
        )

    menu_pedidos()



def menu_listar_pedidos_restaurante():
    dao = PedidosDAO()
    restaurante_id = input("ID do restaurante: ").strip()

    pedidos = dao.listar_pedidos_restaurante(restaurante_id)
    if not pedidos:
        print("Nenhum pedido encontrado.")
        return menu_pedidos()

    restaurante_nome = pedidos[0].nome_restaurante
    print("\n==============================")
    print(f"Restaurante {restaurante_id} - {restaurante_nome}")
    print("==============================")

    for p in pedidos:
        print(
            f"Pedido {p.codigo} | "
            f"Cliente {p.cliente_id} - {p.nome_cliente} | "
            f"Entregador {p.entregador_id} - {p.nome_entregador} | "
            f"{p.nome} | "
            f"{p.status} | "
            f"{p.endereco_entrega}"
        )

    menu_pedidos()

def menu_listar_pedidos_entregadores():
    dao = PedidosDAO()
    entregador_id = input("ID do entregador: ").strip()

    pedidos = dao.listar_pedidos_entregador(entregador_id)
    if not pedidos:
        print("Nenhum pedido encontrado.")
        return menu_pedidos()

    # imprime o entregador UMA VEZ
    entregador_nome = pedidos[0].nome_entregador
    print("\n==============================")
    print(f"Entregador {entregador_id} - {entregador_nome}")
    print("==============================")

    for p in pedidos:
        print(
            f"Pedido {p.codigo} | "
            f"Cliente {p.cliente_id} - {p.nome_cliente} | "
            f"Restaurante {p.restaurante_id} - {p.nome_restaurante} | "
            f"{p.nome} | "
            f"{p.status} | "
            f"{p.endereco_entrega}"
        )

    menu_pedidos()


def menu_listar_itens_pedido():
    dao = PedidosDAO()
    pedido_id = input("ID do pedido: ")

    itens = dao.listar_itens_pedido(pedido_id)
    for item in itens:
        print(
            f"{item.nome_produto} | "
            f"{item.quantidade} | "
            f"{item.preco} | "
            f"{item.subtotal}"
        )

    menu_pedidos()


def menu_cancelar_pedido():
    dao = PedidosDAO()
    pedido_id = input("ID do pedido: ")

    p = dao.listar(pedido_id)
    if p and p.status == StatusPedido.PENDENTE.value:
        dao.atualizar_status(pedido_id, StatusPedido.CANCELADO.value)

    menu_pedidos()


def menu_finalizar_pedido():
    dao = PedidosDAO()
    pedido_id = input("ID do pedido: ")

    p = dao.listar(pedido_id)
    if p and p.status == StatusPedido.PENDENTE.value:
        dao.atualizar_status(pedido_id, StatusPedido.FINALIZADO.value)

    menu_pedidos()
