from db import get_connection

def criar_pedido():
    cliente_id = input("ID do cliente: ")
    restaurante_id = input("ID do restaurante: ")
    endereco = input("Endereço de entrega: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO pedidos (cliente_id, restaurante_id, status, endereco_entrega)
        VALUES (%s, %s, %s, %s)
        RETURNING id
    """, (cliente_id, restaurante_id, "ABERTO", endereco))

    pedido_id = cur.fetchone()[0]
    conn.commit()

    print(f"\n🧾 Pedido criado! ID: {pedido_id}")

    adicionar_itens(cur, pedido_id)
    conn.commit()

    cur.close()
    conn.close()

def adicionar_itens(cur, pedido_id):
    while True:
        produto_id = input("\nID do produto (0 para finalizar): ")
        if produto_id == "0":
            print("✔️ Pedido finalizado!")
            break

        quantidade = int(input("Quantidade: "))

        cur.execute(
            "SELECT preco FROM produtos WHERE id = %s",
            (produto_id,)
        )
        resultado = cur.fetchone()

        if not resultado:
            print("❌ Produto não encontrado")
            continue

        preco = resultado[0]
        subtotal = preco * quantidade

        cur.execute("""
            INSERT INTO item_pedidos
            (pedido_id, produto_id, quantidade, preco_unitario, subtotal)
            VALUES (%s, %s, %s, %s, %s)
        """, (pedido_id, produto_id, quantidade, preco, subtotal))

        print("➕ Item adicionado com sucesso!")

def listar_pedidos_cliente():
    cliente_id = input("ID do cliente: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT p.id, p.status, r.nome
        FROM pedidos p
        JOIN restaurantes r ON r.id = p.restaurante_id
        WHERE p.cliente_id = %s
        ORDER BY p.id
    """, (cliente_id,))

    pedidos = cur.fetchall()

    print("\n=== PEDIDOS DO CLIENTE ===")
    if not pedidos:
        print("Nenhum pedido encontrado.")
    else:
        for p in pedidos:
            print(f"Pedido {p[0]} | Status: {p[1]} | Restaurante: {p[2]}")

    cur.close()
    conn.close()
