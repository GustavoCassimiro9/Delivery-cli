from menu import mostrar_menu
from cliente import cadastrar_cliente
from restaurante import (
    listar_restaurantes,
    cadastrar_restaurante,
    atualizar_restaurante,
    excluir_restaurante
)
from pedido import criar_pedido, listar_pedidos_cliente

def main():
    while True:
        opcao = mostrar_menu()

        if opcao == "1":
            cadastrar_cliente()

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

if __name__ == "__main__":
    main()
