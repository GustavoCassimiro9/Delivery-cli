from restaurante import (
    listar_restaurantes,
    cadastrar_restaurante,
    atualizar_restaurante,
    excluir_restaurante
)
from pedido import criar_pedido, listar_pedidos_cliente
from menu_cliente import menu_cliente
def mostrar_menu():
    while True:
        print("\n=== DELIVERY CLI ===")
        print("\n=== O QUE VOCÊ QUER MODIFICAR? ===")
        print("1  - Clientes")
        print("2  - Listar Restaurantes")
        print("3  - Cadastrar Restaurante")
        print("4  - Atualizar Restaurante")
        print("5  - Excluir Restaurante")
        print("6  - Criar Pedido")
        print("7  - Listar Pedidos de um Cliente")
        print("0  - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            menu_cliente()

        elif opcao == "2":
            listar_restaurantes()

        elif opcao == "3":
            cadastrar_restaurante()

        elif opcao == "4":
            atualizar_restaurante()

        elif opcao == "5":
            excluir_restaurante()

        elif opcao == "6":
            listar_restaurantes()
            criar_pedido()

        elif opcao == "7":
            listar_pedidos_cliente()

        elif opcao == "0":
            print("👋 Encerrando aplicação...")
            break

        else:
            print("❌ Opção inválida")
