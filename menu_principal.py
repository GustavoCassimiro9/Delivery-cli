from Modulos.Pedido.menu_pedido import menu_pedidos
from Modulos.Cliente.menu_cliente import menu_cliente
from Modulos.Restaurante.menu_restaurante import menu_restaurante
from Modulos.Entregador.menu_entregador import menu_entregador
from Modulos.Produtos.menu_produto import menu_produtos

def mostrar_menu():
    while True:
        print("\n=== DELIVERY CLI ===")
        print("\n=== O QUE VOCÊ QUER MODIFICAR? ===")
        print("1  - Clientes")
        print("2  - Restaurantes")
        print("3  - Entregadores")
        print("4  - Produtos")
        print("6  - Pedido")
        print("0  - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            menu_cliente()

        elif opcao == "2":
            menu_restaurante()

        elif opcao == "3":
            menu_entregador()

        elif opcao == "4":
            menu_produtos()

        elif opcao == "6":
            menu_pedidos()

        elif opcao == "0":
            print("👋 Encerrando aplicação...")
            break

        else:
            print("❌ Opção inválida")
