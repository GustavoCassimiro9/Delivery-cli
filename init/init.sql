CREATE TABLE clientes (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  endereco VARCHAR(255) NOT NULL
);

CREATE TABLE restaurantes (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  endereco VARCHAR(255) NOT NULL,
  categoria VARCHAR(50) NOT NULL
);

CREATE TABLE entregadores (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(100) NOT NULL
);

CREATE TABLE produtos (
  id SERIAL PRIMARY KEY,
  restaurante_id INT NOT NULL,
  nome VARCHAR(100) NOT NULL,
  descricao TEXT,
  preco NUMERIC(10,2) NOT NULL,

  CONSTRAINT fk_produto_restaurante
    FOREIGN KEY (restaurante_id)
    REFERENCES restaurantes(id)
);

CREATE TABLE pedidos (
  id SERIAL PRIMARY KEY,
  cliente_id INT NOT NULL,
  restaurante_id INT NOT NULL,
  entregador_id INT,
  status VARCHAR(30) NOT NULL,
  endereco_entrega VARCHAR(255) NOT NULL,

  CONSTRAINT fk_pedido_cliente
    FOREIGN KEY (cliente_id)
    REFERENCES clientes(id),

  CONSTRAINT fk_pedido_restaurante
    FOREIGN KEY (restaurante_id)
    REFERENCES restaurantes(id),

  CONSTRAINT fk_pedido_entregador
    FOREIGN KEY (entregador_id)
    REFERENCES entregadores(id)
);

CREATE TABLE item_pedidos (
  id SERIAL PRIMARY KEY,
  pedido_id INT NOT NULL,
  produto_id INT NOT NULL,
  quantidade INT NOT NULL,
  preco_unitario NUMERIC(10,2) NOT NULL,
  subtotal NUMERIC(10,2) NOT NULL,

  CONSTRAINT fk_item_pedido
    FOREIGN KEY (pedido_id)
    REFERENCES pedidos(id),

  CONSTRAINT fk_item_produto
    FOREIGN KEY (produto_id)
    REFERENCES produtos(id)
);

CREATE TABLE cliente_favoritos (
  cliente_id INT NOT NULL,
  restaurante_id INT NOT NULL,

  PRIMARY KEY (cliente_id, restaurante_id),

  CONSTRAINT fk_favorito_cliente
    FOREIGN KEY (cliente_id)
    REFERENCES clientes(id),

  CONSTRAINT fk_favorito_restaurante
    FOREIGN KEY (restaurante_id)
    REFERENCES restaurantes(id)
);

CREATE TABLE cliente_telefone (
  cliente_id INT NOT NULL,
  ddd VARCHAR(3) NOT NULL,
  numero VARCHAR(15) NOT NULL,

  PRIMARY KEY (cliente_id, ddd, numero),

  CONSTRAINT fk_telefone_cliente
    FOREIGN KEY (cliente_id)
    REFERENCES clientes(id)
);

CREATE TABLE restaurante_telefone (
  restaurante_id INT NOT NULL,
  ddd VARCHAR(3) NOT NULL,
  numero VARCHAR(15) NOT NULL,

  PRIMARY KEY (restaurante_id, ddd, numero),

  CONSTRAINT fk_telefone_restaurante
    FOREIGN KEY (restaurante_id)
    REFERENCES restaurantes(id)
);

CREATE TABLE entregador_telefone (
  entregador_id INT NOT NULL,
  ddd VARCHAR(3) NOT NULL,
  numero VARCHAR(15) NOT NULL,

  PRIMARY KEY (entregador_id, ddd, numero),

  CONSTRAINT fk_telefone_entregador
    FOREIGN KEY (entregador_id)
    REFERENCES entregadores(id)
);
