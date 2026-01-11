from db import get_connection
from Modulos.Produtos.models.Produtos import Produtos

class ProdutosDAO(object):

    def listar_todos(self):
        resultado = []
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT id, restaurante_id, nome, descricao, preco
            FROM produtos
            ORDER BY id
        """)

        for linha in cur.fetchall():
            p = Produtos()
            p.codigo = linha[0]
            p.restaurante_id = linha[1]
            p.nome = linha[2]
            p.descricao = linha[3]
            p.preco = linha[4]
            resultado.append(p)

        cur.close()
        conn.close()
        return resultado


    def listar_por_restaurante(self, restaurante_id):
        resultado = []
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT id, restaurante_id, nome, descricao, preco
            FROM produtos
            WHERE restaurante_id = %s
        """, (restaurante_id,))

        for linha in cur.fetchall():
            p = Produtos()
            p.codigo = linha[0]
            p.restaurante_id = linha[1]
            p.nome = linha[2]
            p.descricao = linha[3]
            p.preco = linha[4]
            resultado.append(p)

        cur.close()
        conn.close()
        return resultado


    def listar(self, produto_id):
        p = None
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT id, restaurante_id, nome, descricao, preco
            FROM produtos
            WHERE id = %s
        """, (produto_id,))

        linha = cur.fetchone()

        if linha:
            p = Produtos()
            p.codigo = linha[0]
            p.restaurante_id = linha[1]
            p.nome = linha[2]
            p.descricao = linha[3]
            p.preco = linha[4]

        cur.close()
        conn.close()
        return p


    def cadastrar(self, restaurante_id, nome, descricao, preco):
        sucesso = False
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO produtos (restaurante_id, nome, descricao, preco)
            VALUES (%s, %s, %s, %s)
        """, (restaurante_id, nome, descricao, preco))

        conn.commit()
        if cur.rowcount == 1:
            sucesso = True

        cur.close()
        conn.close()
        return sucesso


    def atualizar(self, produto_id, nome, descricao, preco):
        sucesso = False
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            UPDATE produtos
            SET nome = %s, descricao = %s, preco = %s
            WHERE id = %s
        """, (nome, descricao, preco, produto_id))

        conn.commit()
        if cur.rowcount == 1:
            sucesso = True

        cur.close()
        conn.close()
        return sucesso


    def remover(self, produto_id):
        sucesso = False
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "DELETE FROM produtos WHERE id = %s",
            (produto_id,)
        )

        conn.commit()
        if cur.rowcount == 1:
            sucesso = True

        cur.close()
        conn.close()
        return sucesso
