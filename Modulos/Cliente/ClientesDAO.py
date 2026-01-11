from db import get_connection, existe_id
from Modulos.Cliente.models.Clientes import Clientes
class ClientesDAO(object):
    def listarTodas(self):
        resultado = []
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, nome, endereco FROM clientes")
        registros = cur.fetchall()
        for linha in registros:
            c = Clientes()
            c.codigo = linha[0]
            c.nome = linha[1]
            c.endereco = linha[2]
            resultado.append(c)
        cur.close()
        conn.close()
        return resultado
    # Retornar cliente pelo codigo
    def listar(self, id):
        if not existe_id("clientes", int(id)):
            return None
        c = None
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, nome, endereco FROM clientes WHERE id = {}".format(id))
        linha = cur.fetchone()
        if linha is not None and len(linha)>0:
            c = Clientes()
            c.codigo = linha[0]
            c.nome = linha[1]
            c.endereco = linha[2]
        cur.close()
        conn.close()
        return c
    def cadastrar_cliente(self, nome, endereco):
        sucesso = False
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO clientes (nome, endereco) VALUES (%s, %s)",
            (nome, endereco)
        )
        
        conn.commit()
        if cur.rowcount == 1:
                sucesso = True
        cur.close()
        conn.close()

        return sucesso
    #atualizar dados ciente
    def atualizar(self, nome, endereco, id):
        if not existe_id("clientes", int(id)):
            return False
        sucesso = False
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("UPDATE clientes SET nome =  '{}', endereco = '{}' WHERE id = {}".format(nome, endereco, id))
        conn.commit()
        if cur.rowcount == 1:
                sucesso = True
        cur.close()
        conn.close()
        return sucesso
    #remover pessoa
    def remover(self, id):
        if not existe_id("clientes", int(id)):
            return False
        sucesso = False
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM clientes WHERE id = {}".format(id))
        conn.commit()
        if cur.rowcount == 1:
                sucesso = True
        cur.close()
        conn.close()
        return sucesso
    def listar_telefones(self, cliente_id):
        if not existe_id("clientes", int(cliente_id)):
            return []
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT ddd, numero FROM cliente_telefone WHERE cliente_id = %s",
            (cliente_id,)
        )
        telefones = cur.fetchall()  # lista de tuplas (ddd, numero)
        cur.close()
        conn.close()
        return telefones
    def adicionar_telefone(self, cliente_id, ddd, numero):
        if not existe_id("clientes", int(cliente_id)):
            return []
        sucesso = False
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO cliente_telefone (cliente_id, ddd, numero) VALUES (%s, %s, %s)",
            (cliente_id, ddd, numero)
        )
        conn.commit()
        if cur.rowcount == 1:
                sucesso = True
        cur.close()
        conn.close()
        return sucesso

    def remover_telefone(self, cliente_id, ddd, numero):
        if not existe_id("clientes", int(cliente_id)):
            return []
        sucesso = False
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM cliente_telefone WHERE cliente_id = %s AND ddd = %s AND numero = %s",
            (cliente_id, ddd, numero)
        )
        conn.commit()
        if cur.rowcount == 1:
                sucesso = True
        cur.close()
        conn.close()
        return sucesso
    

    def listar_favoritos(self, cliente_id):
        if not existe_id("clientes", int(cliente_id)):
            return []
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            """
            SELECT r.id, r.nome, r.endereco, r.categoria
            FROM cliente_favoritos cf
            JOIN restaurantes r ON r.id = cf.restaurante_id
            WHERE cf.cliente_id = %s
            ORDER BY r.nome
            """,
            (cliente_id,)
        )
        favoritos = cur.fetchall()

        cur.close()
        conn.close()
        return favoritos  # lista de tuplas (id, nome, endereco, categoria)

    def adicionar_favorito(self, cliente_id, restaurante_id):
        if not existe_id("clientes", int(cliente_id)):
            return False
        if not existe_id("restaurantes", int(restaurante_id)):
            return False
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
        "SELECT 1 FROM restaurantes WHERE id = %s",
        (restaurante_id,)
    )
        existe = cur.fetchone()

        if not existe:
            cur.close()
            conn.close()
            return False  

        
        cur.execute(
            "INSERT INTO cliente_favoritos (cliente_id, restaurante_id) VALUES (%s, %s)",
            (cliente_id, restaurante_id)
        )
        conn.commit()

        sucesso = (cur.rowcount == 1)
        cur.close()
        conn.close()
        return sucesso

    def remover_favorito(self, cliente_id, restaurante_id):
        if not existe_id("clientes", int(cliente_id)):
            return False
        if not existe_id("restaurantes", int(restaurante_id)):
            return False
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "DELETE FROM cliente_favoritos WHERE cliente_id = %s AND restaurante_id = %s",
            (cliente_id, restaurante_id)
        )
        conn.commit()

        sucesso = (cur.rowcount == 1)
        cur.close()
        conn.close()
        return sucesso