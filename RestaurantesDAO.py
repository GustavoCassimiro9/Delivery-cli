from db import get_connection
from Restaurantes import Restaurantes
class RestaurantesDAO(object):
    def listarTodas(self):
        resultado = []
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, nome, endereco, categoria FROM restaurantes")
        registros = cur.fetchall()
        for linha in registros:
            c = Restaurantes()
            c.codigo = linha[0]
            c.nome = linha[1]
            c.endereco = linha[2]
            c.categoria = linha[3]
            resultado.append(c)
        cur.close()
        conn.close()
        return resultado
    # Retornar restaurante pelo codigo
    def listar(self, id):
        c = None
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, nome, endereco, categoria FROM restaurantes WHERE id = {}".format(id))
        linha = cur.fetchone()
        if linha is not None and len(linha)>0:
            c = Restaurantes()
            c.codigo = linha[0]
            c.nome = linha[1]
            c.endereco = linha[2]
            c.categoria = linha[3]
        cur.close()
        conn.close()
        return c
    def cadastrar_restaurante(self, nome, endereco, categoria):
        sucesso = False
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO restaurantes (nome, endereco, categoria) VALUES (%s, %s, %s)",
            (nome, endereco, categoria)
        )
        
        conn.commit()
        if cur.rowcount == 1:
                sucesso = True
        cur.close()
        conn.close()

        return sucesso
    #atualizar dados ciente
    def atualizar(self, nome, endereco, categoria, id):
        sucesso = False
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("UPDATE restaurantes SET nome =  '{}', endereco = '{}', categoria = '{}' WHERE id = {}".format(nome, endereco, categoria, id))
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
        cur.execute("DELETE FROM restaurantes WHERE id = {}".format(id))
        conn.commit()
        if cur.rowcount == 1:
                sucesso = True
        cur.close()
        conn.close()
        return sucesso
    def listar_telefones(self, restaurante_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT ddd, numero FROM restaurante_telefone WHERE restaurante_id = %s",
            (restaurante_id,)
        )
        telefones = cur.fetchall()  # lista de tuplas (ddd, numero)
        cur.close()
        conn.close()
        return telefones
    def adicionar_telefone(self, restaurante_id, ddd, numero):
        sucesso = False
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO restaurante_telefone (restaurante_id, ddd, numero) VALUES (%s, %s, %s)",
            (restaurante_id, ddd, numero)
        )
        conn.commit()
        if cur.rowcount == 1:
                sucesso = True
        cur.close()
        conn.close()
        return sucesso

    def remover_telefone(self, restaurante_id, ddd, numero):
        sucesso = False
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM restaurante_telefone WHERE restaurante_id = %s AND ddd = %s AND numero = %s",
            (restaurante_id, ddd, numero)
        )
        conn.commit()
        if cur.rowcount == 1:
                sucesso = True
        cur.close()
        conn.close()
        return sucesso