-- cria Banco de dados
-- query tool 
-- cola isso

SET search_path = public;

-- Tabelas
CREATE TABLE funcionario (
    cpf NUMERIC PRIMARY KEY,
    nome VARCHAR(100),
    datanasc DATE,
    tipo INTEGER
);

CREATE TABLE livro (
    codigo INT PRIMARY KEY,
    titulo VARCHAR(255),
    autor VARCHAR(255),
    editora VARCHAR(255),
    genero VARCHAR(255),
    altura DECIMAL,
    largura DECIMAL,
    profundidade DECIMAL,
    preco_compra DECIMAL,
    preco_venda DECIMAL,
    num_prateleira INT,
    num_andar INT,
    quantidade_disponivel INT
);

CREATE TABLE autor (
    codigo SERIAL PRIMARY KEY,
    autor VARCHAR(255)
);

CREATE TABLE fornecedor (
    cnpj NUMERIC PRIMARY KEY,
    razao_social VARCHAR(255),
    endereco VARCHAR(255)
);

CREATE TABLE cliente (
    cpf NUMERIC PRIMARY KEY,
    nome VARCHAR(100),
    endereco VARCHAR(255),
    datanasc DATE,
    tipo INTEGER
);

CREATE TABLE transportadora (
    cnpj NUMERIC PRIMARY KEY,
    razao_social VARCHAR(255),
    endereco VARCHAR(255)
);

CREATE TABLE venda_presencial (
    cpf_cliente NUMERIC REFERENCES cliente(cpf),
    codigo_livro INT REFERENCES livro(codigo),
    cpf_funcionario NUMERIC REFERENCES funcionario(cpf),
    quantidade INT,
    met_pag_presencial VARCHAR(255),
    data_hora TIMESTAMP,
    PRIMARY KEY (cpf_cliente, codigo_livro, cpf_funcionario)
);

CREATE TABLE venda_online (
    cpf_cliente NUMERIC REFERENCES cliente(cpf),
    codigo_livro INT REFERENCES livro(codigo),
    data_entrega_transporte DATE,
    met_pag_online VARCHAR(255),
    data_hora TIMESTAMP,
    quantidade INT,
    cnpj_transportadora NUMERIC REFERENCES transportadora(cnpj),
    PRIMARY KEY (cpf_cliente, codigo_livro)
);

CREATE TABLE prepara (
    cpf_cliente NUMERIC REFERENCES cliente(cpf),
    codigo_livro INT REFERENCES livro(codigo),
    cpf_funcionario NUMERIC REFERENCES funcionario(cpf),
    PRIMARY KEY (cpf_cliente, codigo_livro, cpf_funcionario)
);

CREATE TABLE distribuidora (
    cnpj NUMERIC PRIMARY KEY,
    razao_social VARCHAR(255),
    endereco VARCHAR(255)
);

CREATE TABLE compra (
    cnpj_fornecedor NUMERIC REFERENCES fornecedor(cnpj),
    codigo_livro INT REFERENCES livro(codigo),
    quantidade INT,
    data_hora TIMESTAMP,
    data_entrega_distribuicao DATE,
    cnpj_distribuidora NUMERIC REFERENCES distribuidora(cnpj),
    PRIMARY KEY (cnpj_fornecedor, codigo_livro)
);

-- Índices
CREATE UNIQUE INDEX indice_autor ON autor(autor);
CREATE UNIQUE INDEX indice_cpf_funcionario ON funcionario(cpf);
CREATE UNIQUE INDEX indice_cpf_cliente ON cliente(cpf);
CREATE UNIQUE INDEX indice_cnpj_fornecedor ON fornecedor(cnpj);
CREATE UNIQUE INDEX indice_cnpj_distribuidora ON distribuidora(cnpj);
CREATE UNIQUE INDEX indice_cnpj_transportadora ON transportadora(cnpj);

-- Inserir dados de exemplo
INSERT INTO funcionario (cpf, nome, datanasc, tipo) VALUES
    (12345678901, 'João Silva', '1990-01-01', 1),
    (23456789012, 'Maria Oliveira', '1985-05-10', 2);

INSERT INTO livro (codigo, titulo, autor, editora, genero, altura, largura, profundidade, preco_compra, preco_venda, num_prateleira, num_andar, quantidade_disponivel) VALUES
    (1, 'Livro 1', 'Autor 1', 'Editora A', 'Ficção', 20, 15, 5, 30.0, 50.0, 1, 1, 100),
    (2, 'Livro 2', 'Autor 2', 'Editora B', 'Romance', 18, 12, 4, 25.0, 40.0, 2, 1, 80);

INSERT INTO autor (autor) VALUES
    ('Autor 1'),
    ('Autor 2');

INSERT INTO fornecedor (cnpj, razao_social, endereco) VALUES
    (12345678901234, 'Fornecedor A', 'Rua A, 123'),
    (23456789012345, 'Fornecedor B', 'Rua B, 456');

INSERT INTO cliente (cpf, nome, endereco, datanasc, tipo) VALUES
    (34567890123, 'Ana Souza', 'Av. Principal, 789', '1988-03-15', 1),
    (45678901234, 'Carlos Lima', 'Rua C, 567', '1995-07-20', 2);

INSERT INTO transportadora (cnpj, razao_social, endereco) VALUES
    (12345678901234, 'Transportadora X', 'Rua X, 789'),
    (23456789012345, 'Transportadora Y', 'Rua Y, 456');

INSERT INTO venda_presencial (cpf_cliente, codigo_livro, cpf_funcionario, quantidade, met_pag_presencial, data_hora) VALUES
    (34567890123, 1, 12345678901, 2, 'Dinheiro', '2023-10-28 15:30:00'),
    (45678901234, 2, 23456789012, 1, 'Cartão', '2023-10-28 16:45:00');

INSERT INTO venda_online (cpf_cliente, codigo_livro, data_entrega_transporte, met_pag_online, data_hora, quantidade, cnpj_transportadora) VALUES
    (34567890123, 1, '2023-10-30', 'Boleto', '2023-10-28 17:30:00', 1, 12345678901234),
    (45678901234, 2, '2023-10-31', 'Cartão', '2023-10-28 18:15:00', 2, 23456789012345);

INSERT INTO prepara (cpf_cliente, codigo_livro, cpf_funcionario) VALUES
    (34567890123, 1, 12345678901),
    (45678901234, 2, 23456789012);

INSERT INTO distribuidora (cnpj, razao_social, endereco) VALUES
    (34567890123456, 'Distribuidora A', 'Rua D, 789');
