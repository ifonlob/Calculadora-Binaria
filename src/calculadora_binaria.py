import sys
def comprobacion_binario():
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Uso: 'nombre_del_archivo.py' <primer_número> [operador] <segundo_número>")
        sys.exit()
    if len(sys.argv) == 3:
        if not (1 < len(sys.argv[1]) > 8 ) or not ( 1 < len(sys.argv[2]) > 8):
            print("Error. Los números binarios deben ser de 1 hasta a 8 bits.")
        if sys.argv[1].replace("0","").replace("1","") != "":
            print("Error. Por favor, introduzca el primer número binario de 1 hasta 8 bits (sólo 0 y 1) e inténtelo de nuevo")
            sys.exit()
        if sys.argv[2].replace("0","").replace("1","") != "":
            print("Error. Por favor, introduzca un el segundo número binario de 1 hasta 8 bits (sólo 0 y 1) e inténtelo de nuevo.")
            sys.exit()
        return sys.argv[1], sys.argv[2]
    else: # Entra cuando el usuario introduce un operando.
        if not (1 < len(sys.argv[1]) > 8 ) or not ( 1 < len(sys.argv[2]) > 8):
            print("Error. Los números binarios deben ser de 1 hasta 8 bits.")
            sys.exit()
        if sys.argv[1].replace("0","").replace("1","") != "":
            print("Error. Por favor, introduzca el primer número binario de 1 hasta 8 bits (sólo 0 y 1) e inténtelo de nuevo")
            sys.exit()
        if sys.argv[3].replace("0","").replace("1","") != "":
            print("Error. Por favor, introduzca un el segundo número binario de 1 hasta 8 bits (sólo 0 y 1) e inténtelo de nuevo.")
            sys.exit()    
        return sys.argv[1].zfill(8), sys.argv[3].zfill(8)

def suma_binaria(binario1,binario2):
    """
    Realiza la suma binaria de dos números binarios de 8 bits.
    Esta función simula el proceso de suma binaria bit a bit, 
    considerando los posibles acarreos que se generan en cada posición.
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
        print("Suma:\t")
        print("El resultado de sumar","".join(map(str,binario1)),"y","".join(map(str,binario2)),"es","".join(map(str,resultado_acarreo)))
    else: #La última suma sin arrastrar acarreo
        print("Suma:\t")
        print("El resultado de sumar","".join(map(str,binario1)),"y","".join(map(str,binario2)),"es","".join(map(str,resultado)))
        
def resta_binaria(binario1,binario2):
    """
    Realiza la resta binaria de dos números binarios de 8 bits.
    Esta función resta bit a bit el segundo número binario del primero,
    aplicando un sistema de “préstamos” cuando el bit superior es 0 
    y el inferior es 1. 
    """
    
    while int(binario1,2) < int(binario2,2):
        print("Error. Para restar, el primer número no puede ser más pequeño.")
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
    print("Resta:\t")    
    print("El resultado de restar","".join(map(str,binario1)),"y","".join(map(str,binario2)),"es","".join(map(str,resultado)))
    
def calcular_resultado(binario1,binario2):
    """
    Esta función calcula el resultado según la entrada que recibe por consola (Suma, resta o ambos)"
    """
    if len(sys.argv) == 3:
        suma_binaria(binario1,binario2)
        print()
        resta_binaria(binario1,binario2)
    else: # Entra cuando el usuario introduce un operando.
        eleccion = sys.argv[2]
        if eleccion == "+":
            suma_binaria(binario1,binario2)
        elif eleccion == "-":
            resta_binaria(binario1,binario2)
        else:
            print("Error. Los únicos operadores válidos son '+' y '-'.")
            sys.exit()
        
def main():
    binario1,binario2 = comprobacion_binario()
    calcular_resultado(binario1,binario2)  
             
if __name__ == "__main__":
    main()