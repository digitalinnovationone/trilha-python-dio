-- Tabela de Níveis de Cargo
CREATE TABLE cargonivel (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(100) NOT NULL
);

-- Inserindo Níveis de Cargo
INSERT INTO cargonivel (descricao) VALUES ('Interno');
INSERT INTO cargonivel (descricao) VALUES ('Externo');