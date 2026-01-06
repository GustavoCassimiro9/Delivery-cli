from pedido import criar_pedido, listar_pedidos_cliente
from menu_cliente import menu_cliente
from menu_restaurante import menu_restaurante
from menu_entregador import menu_entregador
def mostrar_menu():
    while True:
        print("\n=== DELIVERY CLI ===")
        print("\n=== O QUE VOCÊ QUER MODIFICAR? ===")
        print("1  - Clientes")
        print("2  - Restaurantes")
        print("3  - Entregadores")
        print("6  - Criar Pedido")
        print("7  - Listar Pedidos de um Cliente")
        print("0  - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            menu_cliente()

        elif opcao == "2":
            menu_restaurante()
        elif opcao == "3":
            menu_entregador()

        

        elif opcao == "7":
            listar_pedidos_cliente()

        elif opcao == "0":
            print("👋 Encerrando aplicação...")
            break

        else:
            print("❌ Opção inválida")
