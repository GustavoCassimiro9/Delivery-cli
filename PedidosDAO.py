from db import get_connection, existe_id
from Pedidos import Pedidos
from ItemPedido import ItemPedido

class PedidosDAO(object):

    def listar_pedidos_cliente(self, cliente_id):
        if not existe_id("clientes", int(cliente_id)):
            return []

        resultado = []
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT 
                p.id,
                p.cliente_id,
                c.nome AS nome_cliente,
                p.restaurante_id,
                r.nome AS nome_restaurante,
                p.entregador_id,
                e.nome AS nome_entregador,
                p.nome,
                p.status,
                p.endereco_entrega
            FROM pedidos p
            JOIN clientes c     ON c.id = p.cliente_id
            JOIN restaurantes r ON r.id = p.restaurante_id
            JOIN entregadores e ON e.id = p.entregador_id
            WHERE p.cliente_id = %s
            ORDER BY p.id
        """, (cliente_id,))

        for linha in cur.fetchall():
            p = Pedidos()
            p.codigo = linha[0]
            p.cliente_id = linha[1]
            p.nome_cliente = linha[2]
            p.restaurante_id = linha[3]
            p.nome_restaurante = linha[4]
            p.entregador_id = linha[5]
            p.nome_entregador = linha[6]
            p.nome = linha[7]
            p.status = linha[8]
            p.endereco_entrega = linha[9]
            resultado.append(p)

        cur.close()
        conn.close()
        return resultado

    def listar_pedidos_restaurante(self, restaurante_id):
        if not existe_id("restaurantes", int(restaurante_id)):
            return []

        resultado = []
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT 
                p.id,
                p.cliente_id,
                c.nome AS nome_cliente,
                p.restaurante_id,
                r.nome AS nome_restaurante,
                p.entregador_id,
                e.nome AS nome_entregador,
                p.nome,
                p.status,
                p.endereco_entrega
            FROM pedidos p
            JOIN clientes c     ON c.id = p.cliente_id
            JOIN restaurantes r ON r.id = p.restaurante_id
            JOIN entregadores e ON e.id = p.entregador_id
            WHERE p.restaurante_id = %s
            ORDER BY p.id
        """, (restaurante_id,))

        for linha in cur.fetchall():
            p = Pedidos()
            p.codigo = linha[0]
            p.cliente_id = linha[1]
            p.nome_cliente = linha[2]
            p.restaurante_id = linha[3]
            p.nome_restaurante = linha[4]
            p.entregador_id = linha[5]
            p.nome_entregador = linha[6]
            p.nome = linha[7]
            p.status = linha[8]
            p.endereco_entrega = linha[9]
            resultado.append(p)

        cur.close()
        conn.close()
        return resultado

    def listar_pedidos_entregador(self, entregador_id):
        if not existe_id("entregadores", int(entregador_id)):
            return []

        resultado = []
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT 
                p.id,
                p.cliente_id,
                c.nome AS nome_cliente,
                p.restaurante_id,
                r.nome AS nome_restaurante,
                p.entregador_id,
                e.nome AS nome_entregador,
                p.nome,
                p.status,
                p.endereco_entrega
            FROM pedidos p
            JOIN clientes c     ON c.id = p.cliente_id
            JOIN restaurantes r ON r.id = p.restaurante_id
            JOIN entregadores e ON e.id = p.entregador_id
            WHERE p.entregador_id = %s
            ORDER BY p.id
        """, (entregador_id,))

        for linha in cur.fetchall():
            p = Pedidos()
            p.codigo = linha[0]
            p.cliente_id = linha[1]
            p.nome_cliente = linha[2]
            p.restaurante_id = linha[3]
            p.nome_restaurante = linha[4]
            p.entregador_id = linha[5]
            p.nome_entregador = linha[6]
            p.nome = linha[7]
            p.status = linha[8]
            p.endereco_entrega = linha[9]
            resultado.append(p)

        cur.close()
        conn.close()
        return resultado

    def listar(self, pedido_id):
        if not existe_id("pedidos", int(pedido_id)):
            return None

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

        cliente_ok, restaurante_ok, entregador_ok = self._validar_fks_pedido(
            cliente_id, restaurante_id, entregador_id, cur
        )
        
        if not cliente_ok:
            print(" Cliente não encontrado ")
            return None

        if not restaurante_ok:
            print(" Restaurante não encontrado ")
            return None

        if not entregador_ok:
            print(" Entregador não encontrado ")
            return None

        cur.execute("""
            INSERT INTO pedidos
            (cliente_id, restaurante_id, entregador_id, nome, status, endereco_entrega)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id
        """, (cliente_id, restaurante_id, entregador_id, nome, status, endereco))

        pedido_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return pedido_id

    def _validar_fks_pedido(self, cliente_id, restaurante_id, entregador_id, cur):
        cur.execute("""
            SELECT
                EXISTS (SELECT 1 FROM clientes WHERE id = %s),
                EXISTS (SELECT 1 FROM restaurantes WHERE id = %s),
                EXISTS (SELECT 1 FROM entregadores WHERE id = %s)
        """, (cliente_id, restaurante_id, entregador_id))

        return cur.fetchone()

    def atualizar_status(self, pedido_id, status):
       
        if not existe_id("pedidos", int(pedido_id)):
            return False

        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "UPDATE pedidos SET status = %s WHERE id = %s",
            (status, pedido_id)
        )
        conn.commit()

        sucesso = (cur.rowcount == 1)
        cur.close()
        conn.close()
        return sucesso

    def adicionar_item(self, pedido_id, produto_id, quantidade):
        
        if not existe_id("pedidos", int(pedido_id)):
            return False
        if not existe_id("produtos", int(produto_id)):
            return False

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT restaurante_id FROM pedidos WHERE id = %s", (pedido_id,))
        row_pedido = cur.fetchone()
        if not row_pedido:
            cur.close(); conn.close()
            return False
        restaurante_pedido = row_pedido[0]

        cur.execute("SELECT preco, restaurante_id FROM produtos WHERE id = %s", (produto_id,))
        row_produto = cur.fetchone()
        if not row_produto:
            cur.close(); conn.close()
            return False
        preco, restaurante_produto = row_produto

        if restaurante_produto != restaurante_pedido:
            cur.close(); conn.close()
            return False

        cur.execute("""
            INSERT INTO item_pedidos (pedido_id, produto_id, quantidade, preco)
            VALUES (%s, %s, %s, %s)
        """, (pedido_id, produto_id, quantidade, preco))

        conn.commit()
        sucesso = (cur.rowcount == 1)

        cur.close()
        conn.close()
        return sucesso

    def listar_itens_pedido(self, pedido_id):
        if not existe_id("pedidos", int(pedido_id)):
            return []

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
            ORDER BY i.id
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
