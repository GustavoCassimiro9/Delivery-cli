class ItemPedido(object):

    @property
    def pedido_id(self):
        return self._pedido_id

    @pedido_id.setter
    def pedido_id(self, pedido_id):
        self._pedido_id = pedido_id

    @property
    def produto_id(self):
        return self._produto_id

    @produto_id.setter
    def produto_id(self, produto_id):
        self._produto_id = produto_id

    @property
    def nome_produto(self):
        return self._nome_produto

    @nome_produto.setter
    def nome_produto(self, nome):
        self._nome_produto = nome

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self._quantidade = quantidade

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, preco):
        self._preco = preco

    @property
    def subtotal(self):
        return self._subtotal

    @subtotal.setter
    def subtotal(self, subtotal):
        self._subtotal = subtotal
