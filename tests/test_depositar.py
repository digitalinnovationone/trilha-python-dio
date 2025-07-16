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

def test_depositar_valor_positivo():
    saldo, extrato = desafio.depositar(0, 100, "")
    assert saldo == 100
    assert "Depósito:" in extrato

def test_depositar_valor_zero():
    saldo, extrato = desafio.depositar(0, 0, "")
    assert saldo == 0
    assert extrato == ""

def test_depositar_valor_negativo():
    saldo, extrato = desafio.depositar(0, -50, "")
    assert saldo == 0
    assert extrato == ""