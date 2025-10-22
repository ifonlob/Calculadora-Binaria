import pytest
import sys
from calculadora_binaria import comprobacion_binario, suma_binaria, resta_binaria

@pytest.mark.parametrize(
    "linea, esperado, resultado_binario",
    [
        (["calculadora_binaria.py", "00000001", "+", "00000001"], "El resultado de sumar", "00000010"),
        (["calculadora_binaria.py", "00001111", "+", "00000001"], "El resultado de sumar", "00010000"),
        (["calculadora_binaria.py", "11111111", "+", "00000001"], "El resultado de sumar", "100000000"),
        (["calculadora_binaria.py", "00000010", "-", "00000001"], "El resultado de restar", "00000001"),
        (["calculadora_binaria.py", "11111111", "-", "00001111"], "El resultado de restar", "11110000"),
        (["calculadora_binaria.py", "00000001", "-", "00000001"], "El resultado de restar", "00000000"),
        (["calculadora_binaria.py", "10101010", "01010101"], "El resultado de sumar", "11111111"),
        (["calculadora_binaria.py", "10101010", "01010101"], "El resultado de restar", "01010101"),
    ]
)
def test_calculadora_binaria(monkeypatch, capsys, linea, esperado, resultado_binario):
    """Valida tanto la operación correcta (suma/resta) como el resultado binario obtenido."""
    # Simula los argumentos como si se ejecutara desde terminal
    monkeypatch.setattr(sys, "argv", linea)

    # Llamada a las funciones según si hay o no operador
    if len(linea) == 3:
        bin1, bin2 = comprobacion_binario()
        suma_binaria(bin1, bin2)
        resta_binaria(bin1, bin2)
    elif linea[2] == "+":
        bin1, bin2 = comprobacion_binario()
        suma_binaria(bin1, bin2)
    elif linea[2] == "-":
        bin1, bin2 = comprobacion_binario()
        resta_binaria(bin1, bin2)

    # Captura la salida del programa
    salida = capsys.readouterr().out

    # Verifica que la operación fue correctamente reconocida
    assert esperado in salida
    # Verifica que el resultado binario es el correcto
    assert resultado_binario in salida
