class Entregadores(object):
    @property
    def codigo(self):
        return self._codigo
    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    @property
    def descricao(self):
        return self._descricao
    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao
    @property
    def preco(self):
        return self._preco
    @preco.setter
    def preco(self, preco):
        self._preco = preco