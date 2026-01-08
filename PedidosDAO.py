from db import get_connection
from Pedidos import Pedidos
from ItemPedido import ItemPedido

class PedidosDAO(object):

    def listar_pedidos_cliente(self, cliente_id):
        resultado = []
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT id,
                   cliente_id,
                   restaurante_id,
                   entregador_id,
                   nome,
                   status,
                   endereco_entrega
            FROM pedidos
            WHERE cliente_id = %s
            ORDER BY id
        """, (cliente_id,))

        for linha in cur.fetchall():
            p = Pedidos()
            p.codigo = linha[0]
            p.cliente_id = linha[1]
            p.restaurante_id = linha[2]
            p.entregador_id = linha[3]
            p.nome = linha[4]
            p.status = linha[5]
            p.endereco_entrega = linha[6]
            resultado.append(p)

        cur.close()
        conn.close()
        return resultado


    def listar(self, pedido_id):
        p = None
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT id,
                   cliente_id,
                   restaurante_id,
                   entregador_id,
                   nome,
                   status,
                   endereco_entrega
            FROM pedidos
            WHERE id = %s
        """, (pedido_id,))

        linha = cur.fetchone()

        if linha:
            p = Pedidos()
            p.codigo = linha[0]
            p.cliente_id = linha[1]
            p.restaurante_id = linha[2]
            p.entregador_id = linha[3]
            p.nome = linha[4]
            p.status = linha[5]
            p.endereco_entrega = linha[6]

        cur.close()
        conn.close()
        return p


    def criar_pedido(self, cliente_id, restaurante_id, entregador_id, nome, status, endereco):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO pedidos
            (cliente_id, restaurante_id, entregador_id, nome, status, endereco_entrega)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id
        """, (
            cliente_id,
            restaurante_id,
            entregador_id,
            nome,
            status,
            endereco
        ))

        pedido_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return pedido_id


    def atualizar_status(self, pedido_id, status):
        sucesso = False
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "UPDATE pedidos SET status = %s WHERE id = %s",
            (status, pedido_id)
        )

        conn.commit()
        if cur.rowcount == 1:
            sucesso = True

        cur.close()
        conn.close()
        return sucesso


    def adicionar_item(self, pedido_id, produto_id, quantidade):
        sucesso = False
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "SELECT preco FROM produtos WHERE id = %s",
            (produto_id,)
        )
        resultado = cur.fetchone()

        if resultado:
            preco = resultado[0]

            cur.execute("""
                INSERT INTO item_pedidos
                (pedido_id, produto_id, quantidade, preco)
                VALUES (%s, %s, %s, %s)
            """, (pedido_id, produto_id, quantidade, preco))

            conn.commit()
            if cur.rowcount == 1:
                sucesso = True

        cur.close()
        conn.close()
        return sucesso


    def listar_itens_pedido(self, pedido_id):
        resultado = []
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT i.pedido_id,
                   i.produto_id,
                   pr.nome,
                   i.quantidade,
                   i.preco,
                   i.subtotal
            FROM item_pedidos i
            JOIN produtos pr ON pr.id = i.produto_id
            WHERE i.pedido_id = %s
        """, (pedido_id,))

        for linha in cur.fetchall():
            item = ItemPedido()
            item.pedido_id = linha[0]
            item.produto_id = linha[1]
            item.nome_produto = linha[2]
            item.quantidade = linha[3]
            item.preco = linha[4]
            item.subtotal = linha[5]
            resultado.append(item)

        cur.close()
        conn.close()
        return resultado
