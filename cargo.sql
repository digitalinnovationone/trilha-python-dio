-- Tabela de Cargos
CREATE TABLE cargos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    nivel INT NOT NULL CHECK (nivel IN (1, 2)) -- Nivel 1: Interno, Nivel 2: Externo
);

-- Inserindo Cargos
INSERT INTO cargos (nome, nivel) VALUES ('Cargo Nivel 1 Interno', 1);
INSERT INTO cargos (nome, nivel) VALUES ('Cargo Nivel 2 Externo', 2);