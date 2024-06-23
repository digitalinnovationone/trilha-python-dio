# Database_Drims

## Descrição do Projeto

Database_Drims é um projeto de banco de dados relacional desenvolvido para gerenciar informações de funcionários internos e externos (jogadores) em uma organização. O sistema diferencia entre esses dois tipos de funcionários com base no nível do cargo.

## Estrutura do Banco de Dados

### Tabela de Cargos

A tabela `cargos` armazena os diferentes cargos disponíveis na organização.

```sql
CREATE TABLE cargos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

-- Inserindo Cargos
INSERT INTO cargos (nome) VALUES ('Cargo Nivel 1 Interno');
INSERT INTO cargos (nome) VALUES ('Cargo Nivel 2 Externo');
```

### Tabela de Níveis de Cargo

A tabela `cargonivel` define os níveis de cargo disponíveis para os funcionários.

```sql
CREATE TABLE cargonivel (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

-- Inserindo Níveis de Cargo
INSERT INTO cargonivel (nome) VALUES ('Nivel 1');
INSERT INTO cargonivel (nome) VALUES ('Nivel 2');
```

### Tabela de Salários para Funcionários

A tabela `salario_funcionarios` armazena informações sobre os salários dos funcionários internos.

```sql
CREATE TABLE salario_funcionarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    valor DECIMAL(15, 2) NOT NULL
);
```

### Tabela de Sexos

A tabela `sexo` armazena as opções de sexo dos funcionários.

```sql
CREATE TABLE sexo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(10) NOT NULL
);

-- Inserindo Tipos de Sexo
INSERT INTO sexo (tipo) VALUES ('M');
INSERT INTO sexo (tipo) VALUES ('F');
```

### Tabela de Funcionários Internos

A tabela `funcionarios_internos` armazena informações detalhadas sobre os funcionários internos, incluindo jogadores.

```sql
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

-- Adição de Índices
CREATE INDEX idx_cargo_id ON funcionarios_internos (cargo_id);
CREATE INDEX idx_cargonivel_id ON funcionarios_internos (cargonivel_id);
CREATE INDEX idx_salario_funcionario_id ON funcionarios_internos (salario_funcionario_id);
```

## Melhorias Potenciais

Para uma maior robustez e flexibilidade do sistema, considere as seguintes melhorias potenciais:

- **Adição de Índices:** Índices foram adicionados para melhorar a performance das consultas no banco de dados.
- **Campos Opcionais:** Implementar campos opcionais para informações adicionais que podem não ser obrigatórias para todos os funcionários internos.
- **Proteção de Dados:** Implementar medidas de segurança adequadas para proteger informações sensíveis, como CPF e dados pessoais.