import sys
"""
Calculadora binaria por consola.

Permite sumar o restar dos números binarios de 8 bits, recibidos como argumentos al ejecutar el programa.
Controla errores en la entrada y muestra resultados en binario.

Uso:
    python nombre_del_archivo.py <primer_binario> <segundo_binario>

Ejemplo:
    python calculadora_binaria.py 10100111 00001011
"""
def pedir_binario():
    if len(sys.argv) != 3:
        print("Uso: 'nombre_del_archivo.py' <primer_número> <segundo_número>")
        sys.exit()
    if len(sys.argv[1]) != 8 or len(sys.argv[2]) != 8:
        print("Error. Los números binarios deben ser de 8 bits.")
        sys.exit()
    if sys.argv[1].replace("0","").replace("1","") != "":
        print("Error. Por favor, introduzca el primer número binario de 8 bits (sólo 0 y 1) e inténtelo de nuevo")
        sys.exit()
    if sys.argv[2].replace("0","").replace("1","") != "":
        print("Error. Por favor, introduzca un el segundo número binario de 8 bits (sólo 0 y 1) e inténtelo de nuevo.")
        sys.exit()
    return sys.argv[1], sys.argv[2]

def suma_binaria(binario1,binario2):
    """
    Realiza la suma binaria de dos números binarios de 8 bits.

    Esta función simula el proceso de suma binaria bit a bit, 
    considerando los posibles acarreos que se generan en cada posición.
    Si la suma produce un acarreo adicional al bit más significativo, 
    el resultado contendrá 9 bits.

    Parámetros: (Lo que recibe)
        binario1 (str): Primer número binario de 8 bits (por ejemplo, '10101010').
        binario2 (str): Segundo número binario de 8 bits (por ejemplo, '11110000').

    Salida:
        Muestra en pantalla el resultado de la suma binaria en formato de cadena, 
        con o sin bit de acarreo adicional. 
        Ejemplo: "El número binario es: 110011010".

    Ejemplo:
        >>> suma_binaria("10101010", "01010101")
        El número binario es: 11111111
    """
    
    resultado = [0] * 8
    binario1 = list(map(int,binario1))
    binario2 = list(map(int,binario2))
    acarreo = [0] * 9
    for i in range(7,-1,-1):
        if (binario1[i] == 0 and binario2[i] == 1) or (binario1[i] == 1 and binario2[i] == 0):
            if acarreo[i] == 1:
                resultado[i] = 0
                acarreo[i-1] = 1
            else:
                resultado[i] = 1
        elif binario1[i] == 0 and binario2[i] == 0:
            if acarreo[i] == 1:
                resultado[i] = 1
            else:
                resultado[i] = 0
        else: #Ambos 1
            if acarreo[i] == 1:
                resultado[i] = 1
                acarreo[i-1] = 1
            else:
                resultado[i] = 0
                acarreo[i - 1] = 1
    if acarreo[0] == 1:
        resultado_acarreo = [1] + resultado
        print("El número binario es:","".join(map(str,resultado_acarreo)))
    else: #La última suma sin arrastrar acarreo
        print("El número binario es:","".join(map(str,resultado)))
        
def resta_binaria(binario1,binario2):
    """
    Realiza la resta binaria de dos números binarios de 8 bits.

    Esta función resta bit a bit el segundo número binario del primero,
    aplicando un sistema de “préstamos” (borrow) cuando el bit superior es 0 
    y el inferior es 1. El proceso imita la resta binaria tradicional. 
    Si el segundo número es mayor que el primero, el programa se detiene 
    mostrando un mensaje de error.

    Parámetros:
        binario1 (str): Primer número binario minuendo (debe ser igual o mayor).
        binario2 (str): Segundo número binario sustraendo.

    Salida:
        Imprime en pantalla el resultado de la resta en formato binario de 8 bits.
        Ejemplo: "El número binario es: 00101010".

    Ejemplo:
        >>> resta_binaria("10101010", "00001111")
        El número binario es: 10011011
    """
    
    while int(binario1,2) < int(binario2,2):
        print("El primer número no puede ser más pequeño, vuelva a introducir el primer número correctamente.")
        sys.exit()
    binario1 = list(map(int, binario1))
    binario2 = list(map(int, binario2))
    resultado = [0] * 8
    acarreo = 0
    for i in range(7,-1,-1):
        resta = binario1[i] - binario2[i] - acarreo
        if resta >= 0:
            resultado[i] = resta
            acarreo = 0
        else:
            resultado[i] = 1
            acarreo = 1    
    print("El número binario es:","".join(map(str,resultado)))
        
def main():
    binario1,binario2 = pedir_binario()
    print("Bienvenido a la calculadora binaria, introduzca '1' a continuación si deseas sumar o '2' si deseas restar.\n")
    try:
        eleccion = int(input())
        if eleccion != 1 and eleccion != 2:
            print("Error. Los únicos valores válidos son 1 o 2.")
            sys.exit()
        if eleccion == 1:
            suma_binaria(binario1,binario2)
        else: # Elección 2 (resta)
            resta_binaria(binario1,binario2)
    except ValueError:
        print("Error. Los únicos valores válidos son 1 o 2.")
        sys.exit()  
             
if __name__ == "__main__":
    main()