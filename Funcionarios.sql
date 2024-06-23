-- Tabela de Funcionários Internos
CREATE TABLE funcionarios_internos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARBINARY(100) NOT NULL,
    cargo_id INT,
    cargonivel_id INT,
    salario_funcionario_id INT,
    sexo_id INT,
    endereco_id INT,
    estado_id INT,
    cep_id INT,
    telefone VARCHAR(20),
    FOREIGN KEY (cargo_id) REFERENCES cargos(id),
    FOREIGN KEY (cargonivel_id) REFERENCES cargonivel(id),
    FOREIGN KEY (salario_funcionario_id) REFERENCES salario_funcionarios(id),
    FOREIGN KEY (sexo_id) REFERENCES sexo(id),
    FOREIGN KEY (endereco_id) REFERENCES endereco(id),
    FOREIGN KEY (estado_id) REFERENCES estado(id),
    FOREIGN KEY (cep_id) REFERENCES cep(id)
);

-- Tabela de Jogadores
CREATE TABLE jogadores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARBINARY(100) NOT NULL,
    cargo_id INT,
    cargonivel_id INT,
    salario_jogador_id INT,
    sexo_id INT,
    endereco_id INT,
    estado_id INT,
    cep_id INT,
    telefone VARCHAR(20),
    FOREIGN KEY (cargo_id) REFERENCES cargos(id),
    FOREIGN KEY (cargonivel_id) REFERENCES cargonivel(id),
    FOREIGN KEY (salario_jogador_id) REFERENCES salario_jogadores(id),
    FOREIGN KEY (sexo_id) REFERENCES sexo(id),
    FOREIGN KEY (endereco_id) REFERENCES endereco(id),
    FOREIGN KEY (estado_id) REFERENCES estado(id),
    FOREIGN KEY (cep_id) REFERENCES cep(id)
);

-- Adição de Índices
CREATE INDEX idx_cargo_id ON funcionarios_internos (cargo_id);
CREATE INDEX idx_cargonivel_id ON funcionarios_internos (cargonivel_id);
CREATE INDEX idx_salario_funcionario_id ON funcionarios_internos (salario_funcionario_id);
