CREATE TABLE clientes (
  id serial NOT NULL,
  nome character varying NOT NULL,
  endereco character varying NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE restaurantes (
  id serial NOT NULL,
  nome character varying NOT NULL,
  endereco character varying NOT NULL,
  categoria character varying NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE produtos (
  id serial NOT NULL,
  restaurante_id int NOT NULL,
  nome character varying NOT NULL,
  descricao character varying NOT NULL,
  preco float NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_produtos_restaurante
    FOREIGN KEY (restaurante_id)
    REFERENCES restaurantes (id)
    ON DELETE CASCADE
);

CREATE TABLE entregadores (
  id serial NOT NULL,
  nome character varying NOT NULL,
  descricao character varying NOT NULL,
  preco float NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE pedidos (
  id serial NOT NULL,
  cliente_id int NOT NULL,
  restaurante_id int NOT NULL,
  entregador_id int NOT NULL,
  nome character varying NOT NULL,
  status character varying NOT NULL,
  endereco_entrega character varying NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_pedidos_cliente
    FOREIGN KEY (cliente_id)
    REFERENCES clientes (id)
    ON DELETE CASCADE,
  CONSTRAINT fk_pedidos_restaurante
    FOREIGN KEY (restaurante_id)
    REFERENCES restaurantes (id)
    ON DELETE CASCADE,
  CONSTRAINT fk_pedidos_entregador
    FOREIGN KEY (entregador_id)
    REFERENCES entregadores (id)
    ON DELETE CASCADE
);

CREATE TABLE item_pedidos (
  id serial NOT NULL,
  pedido_id int NOT NULL,
  produto_id int NOT NULL,
  quantidade int NOT NULL,
  preco float NOT NULL,
  subtotal float GENERATED ALWAYS AS (preco * quantidade) STORED,
  PRIMARY KEY (id),
  CONSTRAINT fk_item_pedidos_pedido
    FOREIGN KEY (pedido_id)
    REFERENCES pedidos (id)
    ON DELETE CASCADE,
  CONSTRAINT fk_item_pedidos_produto
    FOREIGN KEY (produto_id)
    REFERENCES produtos (id)
    ON DELETE CASCADE
);

CREATE TABLE cliente_favoritos (
  cliente_id int NOT NULL,
  restaurante_id int NOT NULL,
  CONSTRAINT pk_cf PRIMARY KEY (cliente_id, restaurante_id),
  CONSTRAINT fk_cf_cliente
    FOREIGN KEY (cliente_id)
    REFERENCES clientes (id)
    ON DELETE CASCADE,
  CONSTRAINT fk_cf_restaurante
    FOREIGN KEY (restaurante_id)
    REFERENCES restaurantes (id)
    ON DELETE CASCADE
);

CREATE TABLE cliente_telefone (
  cliente_id int NOT NULL,
  numero int NOT NULL,
  ddd int NOT NULL,
  CONSTRAINT pk_ct PRIMARY KEY (cliente_id, numero, ddd),
  CONSTRAINT fk_ct_cliente
    FOREIGN KEY (cliente_id)
    REFERENCES clientes (id)
    ON DELETE CASCADE
);

CREATE TABLE restaurante_telefone (
  restaurante_id int NOT NULL,
  numero int NOT NULL,
  ddd int NOT NULL,
  CONSTRAINT pk_rt PRIMARY KEY (restaurante_id, numero, ddd),
  CONSTRAINT fk_rt_restaurante
    FOREIGN KEY (restaurante_id)
    REFERENCES restaurantes (id)
    ON DELETE CASCADE
);

CREATE TABLE entregador_telefone (
  entregador_id int NOT NULL,
  numero int NOT NULL,
  ddd int NOT NULL,
  CONSTRAINT pk_et PRIMARY KEY (entregador_id, numero, ddd),
  CONSTRAINT fk_et_entregador
    FOREIGN KEY (entregador_id)
    REFERENCES entregadores (id)
    ON DELETE CASCADE
);
