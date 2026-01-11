class Restaurantes(object):
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
    def endereco(self):
        return self._endereco
    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco
    @property
    def categoria(self):
        return self._categoria
    @categoria.setter
    def categoria(self, categoria):
        self._categoria = categoria
