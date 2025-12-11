CREATE TABLE usuarios (
    id_usuarios INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    telefone VARCHAR(20)
);

INSERT INTO usuarios (nome, email, senha, telefone) VALUES ('pedro', 'pedro@gmail', 'senhasecreta','2295944694');

CREATE TABLE endereco (
    id_endereco INT AUTO_INCREMENT PRIMARY KEY ON DELETE CASCADE ON UPDATE CASCADE,
    id_usuarios INT NOT NULL ON DELETE CASCADE ON UPDATE CASCADE,
    bairro VARCHAR(255) NOT NULL ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_usuarios) REFERENCES usuarios(id_usuarios) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO endereco (id_usuarios, bairro) VALUES (1,'nova suiça');

CREATE TABLE pagamentos (
    id_pagamento INT AUTO_INCREMENT PRIMARY KEY,
    tipo_pagamento VARCHAR(100) NOT NULL,
    status_pagamento VARCHAR(100) NOT NULL,
    valor_total DECIMAL(10,2)
);

INSERT INTO pagamentos (tipo_pagamento, status_pagamento, valor_total) VALUES ('dinheiro','pago', 8);

CREATE TABLE restaurantes (
    id_restaurantes INT AUTO_INCREMENT PRIMARY KEY ON DELETE CASCADE ON UPDATE CASCADE,
    id_produto INT,
    id_usuarios INT,
    id_endereco INT,
    nome_restaurante VARCHAR(150) NOT NULL,
    categoria VARCHAR(100),
    FOREIGN KEY (id_usuarios) REFERENCES usuarios(id_usuarios) ON DELETE SET NULL,
    FOREIGN KEY (id_endereco) REFERENCES endereco(id_endereco) ON DELETE SET NULL,
    FOREIGN KEY (id_produto) REFERENCES produtos(id_produto) ON DELETE SET NULL
);

INSERT INTO restaurantes (id_usuarios, id_endereco, nome_restaurante, categoria) VALUES (1, 1,'quinta rica', 'almoços');

CREATE TABLE produtos (
    id_produto INT AUTO_INCREMENT PRIMARY KEY,
    id_restaurantes INT,
    descricao TEXT NOT NULL,
    FOREIGN KEY (id_restaurantes) REFERENCES restaurantes(id_restaurantes) ON DELETE CASCADE ON UPDATE CASCADE
);



CREATE TABLE entregas (
    id_entrega INT AUTO_INCREMENT PRIMARY KEY,
    id_endereco INT NOT NULL,
    data_entrega DATE,
    FOREIGN KEY (id_endereco) REFERENCES endereco(id_endereco) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO entregas (id_entrega, data_entrega) VALUES (1, '2025-04-11');

CREATE TABLE pedidos (
    id_pedidos INT AUTO_INCREMENT PRIMARY KEY ON DELETE CASCADE ON UPDATE CASCADE,
    id_restaurantes INT,
    id_usuarios INT NOT NULL,
    id_endereco INT NOT NULL,
    id_pagamento INT NOT NULL,
    id_entrega INT NOT NULL,
    FOREIGN KEY (id_restaurantes) REFERENCES restaurantes(id_restaurantes) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_usuarios) REFERENCES usuarios(id_usuarios) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_endereco) REFERENCES endereco(id_endereco) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_pagamento) REFERENCES pagamentos(id_pagamento) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_entrega) REFERENCES entregas(id_entrega) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO pedidos (id_restaurantes, id_usuarios, id_endereco, id_pagamento, id_entrega) VALUES (1, 1, 1, 1, 1);

CREATE TABLE itens_pedido (
    id_item_pedido INT AUTO_INCREMENT PRIMARY KEY,
    id_pedidos INT NOT NULL,
    nome_item VARCHAR(100) NOT NULL,
    quantidade INT NOT NULL,
    preco_unitario DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_pedidos) REFERENCES pedidos(id_pedidos) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO itens_pedido (id_pedidos, nome_item, quantidade, preco_unitario) VALUES (1, 'file mignon', 8, 300);

CREATE TABLE avaliacoes (
    id_avaliacao INT AUTO_INCREMENT PRIMARY KEY,
    id_pedidos INT NOT NULL,
    nota INT,
    comentario TEXT,
    FOREIGN KEY (id_pedidos) REFERENCES pedidos(id_pedidos) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO avaliacoes (id_pedidos, nota, comentario) VALUES (1, 10, 'bom');