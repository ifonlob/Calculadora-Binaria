import pytest
import sys
from calculadora_binaria import comprobacion_binario, suma_binaria, resta_binaria, calcular_resultado


@pytest.mark.parametrize(
    "linea, esperado, resultado_binario",
    [
        # Tests 8 bits
        (["calculadora_binaria.py", "00000001", "+", "00000001"], "El resultado de sumar", "00000010"),
        (["calculadora_binaria.py", "00001111", "+", "00000001"], "El resultado de sumar", "00010000"),
        (["calculadora_binaria.py", "11111111", "+", "00000001"], "El resultado de sumar", "100000000"),
        (["calculadora_binaria.py", "00000010", "-", "00000001"], "El resultado de restar", "00000001"),
        (["calculadora_binaria.py", "11111111", "-", "00001111"], "El resultado de restar", "11110000"),
        (["calculadora_binaria.py", "00000001", "-", "00000001"], "El resultado de restar", "00000000"),
        (["calculadora_binaria.py", "10101010", "01010101"], "El resultado de sumar", "11111111"),
        (["calculadora_binaria.py", "10101010", "01010101"], "El resultado de restar", "01010101"),
        # Números de diferentes longitudes (1-7 bits)
        (["calculadora_binaria.py", "1", "+", "1"], "El resultado de sumar", "00000010"),
        (["calculadora_binaria.py", "1", "-", "1"], "El resultado de restar", "00000000"),
        (["calculadora_binaria.py", "11", "+", "01"], "El resultado de sumar", "00000100"),
        (["calculadora_binaria.py", "11", "-", "01"], "El resultado de restar", "00000010"),
        (["calculadora_binaria.py", "1111", "+", "1"], "El resultado de sumar", "00010000"),
        (["calculadora_binaria.py", "1000", "-", "1"], "El resultado de restar", "00000111"),
        (["calculadora_binaria.py", "1111111", "+", "1"], "El resultado de sumar", "10000000"),
        (["calculadora_binaria.py", "1111111", "-", "1"], "El resultado de restar", "01111110"),
        (["calculadora_binaria.py", "1010", "0101"], "El resultado de sumar", "00001111"),
        (["calculadora_binaria.py", "1010", "0101"], "El resultado de restar", "00000101"),
    ]
)
def test_calculadora_binaria(monkeypatch, capsys, linea, esperado, resultado_binario):
    """Valida tanto la operación correcta (suma/resta) como el resultado binario obtenido."""
    monkeypatch.setattr(sys, "argv", linea)

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

    salida = capsys.readouterr().out
    assert esperado in salida
    assert resultado_binario in salida


# TESTS PARA OPERANDOS INVÁLIDOS

@pytest.mark.parametrize(
    "linea, mensaje_error",
    [
        # Números con caracteres no binarios - CON OPERADOR
        (["calculadora_binaria.py", "1012", "+", "1010"], 
         "Error. Por favor, introduzca el primer número binario de 1 hasta 8 bits (sólo 0 y 1) e inténtelo de nuevo"),
        
        (["calculadora_binaria.py", "1010", "+", "102a"], 
         "Error. Por favor, introduzca el segundo número binario de 1 hasta 8 bits (sólo 0 y 1) e inténtelo de nuevo."),
        
        # Números con caracteres no binarios - SIN OPERADOR
        (["calculadora_binaria.py", "abcd", "1010"], 
         "Error. Por favor, introduzca el primer número binario de 1 hasta 8 bits (sólo 0 y 1) e inténtelo de nuevo"),
        
        (["calculadora_binaria.py", "1010", "xyz"], 
         "Error. Por favor, introduzca el segundo número binario de 1 hasta 8 bits (sólo 0 y 1) e inténtelo de nuevo."),
        
        # Números con más de 8 bits - CON OPERADOR
        (["calculadora_binaria.py", "111111111", "+", "1010"], 
         "Error. Los números binarios deben ser de 1 hasta 8 bits."),
        
        (["calculadora_binaria.py", "1010", "+", "100000000"], 
         "Error. Los números binarios deben ser de 1 hasta 8 bits."),
        
        # Números con más de 8 bits - SIN OPERADOR
        (["calculadora_binaria.py", "111111111", "10101010"], 
         "Error. Los números binarios deben ser de 1 hasta 8 bits."),
        
        # Números vacíos (0 bits)
        (["calculadora_binaria.py", "", "+", "1010"], 
         "Error. Los números binarios deben ser de 1 hasta 8 bits."),
        
        (["calculadora_binaria.py", "1010", "+", ""], 
         "Error. Los números binarios deben ser de 1 hasta 8 bits."),
    ]
)
def test_operandos_invalidos(monkeypatch, capsys, linea, mensaje_error):
    """Valida que los operandos inválidos generen los mensajes de error correctos."""
    monkeypatch.setattr(sys, "argv", linea)
    
    with pytest.raises(SystemExit):
        comprobacion_binario()
    
    salida = capsys.readouterr().out
    assert mensaje_error in salida


# TESTS PARA OPERADORES INVÁLIDOS

@pytest.mark.parametrize(
    "linea, mensaje_error",
    [
        # Operadores no válidos
        (["calculadora_binaria.py", "1010", "*", "0101"], 
         "Error. Los únicos operadores válidos son '+' y '-'."),
        
        (["calculadora_binaria.py", "1010", "/", "0101"], 
         "Error. Los únicos operadores válidos son '+' y '-'."),
        
        (["calculadora_binaria.py", "1010", "x", "0101"], 
         "Error. Los únicos operadores válidos son '+' y '-'."),
        
        (["calculadora_binaria.py", "1010", "&", "0101"], 
         "Error. Los únicos operadores válidos son '+' y '-'."),
        
        (["calculadora_binaria.py", "1010", "suma", "0101"], 
         "Error. Los únicos operadores válidos son '+' y '-'."),
    ]
)
def test_operadores_invalidos(monkeypatch, capsys, linea, mensaje_error):
    """Valida que los operadores inválidos generen el mensaje de error correcto."""
    monkeypatch.setattr(sys, "argv", linea)
    
    bin1, bin2 = comprobacion_binario()  # Esto pasa porque los números son válidos
    
    with pytest.raises(SystemExit):
        calcular_resultado(bin1, bin2)
    
    salida = capsys.readouterr().out
    assert mensaje_error in salida


# TEST PARA RESTA CON PRIMER NÚMERO MENOR

@pytest.mark.parametrize(
    "linea, mensaje_error",
    [
        (["calculadora_binaria.py", "0001", "-", "1010"], 
         "Error. Para restar, el primer número no puede ser más pequeño."),
        
        (["calculadora_binaria.py", "00000001", "-", "11111111"], 
         "Error. Para restar, el primer número no puede ser más pequeño."),
        
        (["calculadora_binaria.py", "100", "-", "1000"], 
         "Error. Para restar, el primer número no puede ser más pequeño."),
    ]
)
def test_resta_numero_menor(monkeypatch, capsys, linea, mensaje_error):
    """Valida que la resta con primer número menor genere el error correcto."""
    monkeypatch.setattr(sys, "argv", linea)
    
    bin1, bin2 = comprobacion_binario()
    
    with pytest.raises(SystemExit):
        resta_binaria(bin1, bin2)
    
    salida = capsys.readouterr().out
    assert mensaje_error in salida


# TEST PARA NÚMERO INCORRECTO DE ARGUMENTOS

@pytest.mark.parametrize(
    "linea, mensaje_error",
    [
        (["calculadora_binaria.py"], 
         "Uso: 'nombre_del_archivo.py' <primer_número> [operador] <segundo_número>"),
        
        (["calculadora_binaria.py", "1010"], 
         "Uso: 'nombre_del_archivo.py' <primer_número> [operador] <segundo_número>"),
        
        (["calculadora_binaria.py", "1010", "+", "0101", "extra"], 
         "Uso: 'nombre_del_archivo.py' <primer_número> [operador] <segundo_número>"),
    ]
)
def test_argumentos_incorrectos(monkeypatch, capsys, linea, mensaje_error):
    """Valida que un número incorrecto de argumentos genere el mensaje de uso."""
    monkeypatch.setattr(sys, "argv", linea)
    
    with pytest.raises(SystemExit):
        comprobacion_binario()
    
    salida = capsys.readouterr().out
    assert mensaje_error in salida
