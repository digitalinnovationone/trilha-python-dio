from dataclasses import dataclass


@dataclass
class Cliente:
    email: str
    telefone: str
    status: str


@dataclass
class PessoaFisica(Cliente):
    nome: str
    cpf: str
    renda_mensal: float


@dataclass
class PessoaJuridica(Cliente):
    nome_fantasia: str
    cnpj: str
    faturamento_anual: float
