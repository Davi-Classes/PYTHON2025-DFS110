-- "dump.sql" é um arquivo utilizado como script inicial do banco de dados.
CREATE TABLE produtos (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(255) NOT NULL,
    preco DECIMAL(6, 2) NOT NULL,
    descricao VARCHAR(500),
    quantidade INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE clientes (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    data_nascimento DATE NOT NULL,
    fl_ativo BOOL NOT NULL DEFAULT true
);
