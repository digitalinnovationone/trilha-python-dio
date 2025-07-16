import pytest
import importlib.util
import sys
from pathlib import Path

# Caminho absoluto para o arquivo desafio.py
desafio_path = Path(__file__).parent.parent / "01 - Estrutura de dados" / "desafio.py"
spec = importlib.util.spec_from_file_location("desafio", desafio_path)
desafio = importlib.util.module_from_spec(spec)
sys.modules["desafio"] = desafio
spec.loader.exec_module(desafio)

def test_saque_valido():
    saldo, extrato, numero_saques = desafio.sacar(
        saldo=500, valor=200, extrato="", limite=500, numero_saques=0, limite_saques=3
    )
    assert saldo == 300
    assert "Saque:" in extrato
    assert numero_saques == 1

def test_saque_acima_limite():
    saldo, extrato, numero_saques = desafio.sacar(
        saldo=1000, valor=600, extrato="", limite=500, numero_saques=0, limite_saques=3
    )
    assert saldo == 1000
    assert extrato == ""
    assert numero_saques == 0

def test_saque_acima_numero_saques():
    saldo, extrato, numero_saques = desafio.sacar(
        saldo=1000, valor=100, extrato="", limite=500, numero_saques=3, limite_saques=3
    )
    assert saldo == 1000
    assert extrato == ""
    assert numero_saques == 3

def test_saque_saldo_insuficiente():
    saldo, extrato, numero_saques = desafio.sacar(
        saldo=100, valor=200, extrato="", limite=500, numero_saques=0, limite_saques=3
    )
    assert saldo == 100
    assert extrato == ""
    assert numero_saques == 0

def test_saque_valor_negativo():
    saldo, extrato, numero_saques = desafio.sacar(
        saldo=1000, valor=-50, extrato="", limite=500, numero_saques=0, limite_saques=3
    )
    assert saldo == 1000
    assert extrato == ""
    assert numero_saques == 0