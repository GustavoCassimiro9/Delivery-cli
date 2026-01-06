from db import get_connection
from Entregadores import Entregadores
class EntregadoresDAO(object):
    def listarTodas(self):
        resultado = []
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, nome, descricao, preco FROM entregadores")
        registros = cur.fetchall()
        for linha in registros:
            c = Entregadores()
            c.codigo = linha[0]
            c.nome = linha[1]
            c.descricao = linha[2]
            c.preco = linha[3]
            resultado.append(c)
        cur.close()
        conn.close()
        return resultado
    # Retornar restaurante pelo codigo
    def listar(self, id):
        c = None
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, nome, descricao, preco FROM entregadores WHERE id = {}".format(id))
        linha = cur.fetchone()
        if linha is not None and len(linha)>0:
            c = Entregadores()
            c.codigo = linha[0]
            c.nome = linha[1]
            c.descricao = linha[2]
            c.preco = linha[3]
        cur.close()
        conn.close()
        return c
    def cadastrar_entregadores(self, nome, descricao, preco):
        sucesso = False
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO entregadores (nome, descricao, preco) VALUES (%s, %s, %s)",
            (nome, descricao, preco)
        )
        
        conn.commit()
        if cur.rowcount == 1:
                sucesso = True
        cur.close()
        conn.close()

        return sucesso
    #atualizar dados ciente
    def atualizar(self, nome, descricao, preco, id):
        sucesso = False
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("UPDATE entregadores SET nome =  '{}', descricao = '{}', preco = '{}' WHERE id = {}".format(nome, descricao, preco, id))
        conn.commit()
        if cur.rowcount == 1:
                sucesso = True
        cur.close()
        conn.close()
        return sucesso
    #remover pessoa
    def remover(self, id):
        sucesso = False
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM entregadores WHERE id = {}".format(id))
        conn.commit()
        if cur.rowcount == 1:
                sucesso = True
        cur.close()
        conn.close()
        return sucesso
    def listar_telefones(self, entregador_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT ddd, numero FROM entregador_telefone WHERE entregador_id = %s",
            (entregador_id,)
        )
        telefones = cur.fetchall()  # lista de tuplas (ddd, numero)
        cur.close()
        conn.close()
        return telefones
    def adicionar_telefone(self, entregador_id, ddd, numero):
        sucesso = False
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO entregador_telefone (entregador_id, ddd, numero) VALUES (%s, %s, %s)",
            (entregador_id, ddd, numero)
        )
        conn.commit()
        if cur.rowcount == 1:
                sucesso = True
        cur.close()
        conn.close()
        return sucesso

    def remover_telefone(self, entregador_id, ddd, numero):
        sucesso = False
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM entregador_telefone WHERE entregador_id = %s AND ddd = %s AND numero = %s",
            (entregador_id, ddd, numero)
        )
        conn.commit()
        if cur.rowcount == 1:
                sucesso = True
        cur.close()
        conn.close()
        return sucesso