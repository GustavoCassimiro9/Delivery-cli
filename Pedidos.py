class Pedidos(object):

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo

    @property
    def cliente_id(self):
        return self._cliente_id

    @cliente_id.setter
    def cliente_id(self, cliente_id):
        self._cliente_id = cliente_id

    @property
    def restaurante_id(self):
        return self._restaurante_id

    @restaurante_id.setter
    def restaurante_id(self, restaurante_id):
        self._restaurante_id = restaurante_id

    @property
    def entregador_id(self):
        return self._entregador_id

    @entregador_id.setter
    def entregador_id(self, entregador_id):
        self._entregador_id = entregador_id

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def endereco_entrega(self):
        return self._endereco_entrega

    @endereco_entrega.setter
    def endereco_entrega(self, endereco):
        self._endereco_entrega = endereco
