-- Tabela de Sexos
CREATE TABLE sexo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(10) NOT NULL
);

-- Inserindo Tipos de Sexo
INSERT INTO sexo (tipo) VALUES ('M');
INSERT INTO sexo (tipo) VALUES ('F');
