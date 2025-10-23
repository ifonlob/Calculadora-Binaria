# Calculadora binaria de 8 bits en Python por consola.

## Índice
- [Descripción del módulo](#descripción-del-módulo)
- [Requisitos del sistema](#requisitos-del-sistema)
- [Instalación de Python](#instalación-de-python-en-los-diferentes-sistemas-operativos)
- [Ejecución del módulo](#ejecución-del-módulo)
- [Uso del archivo dependencias.txt](#uso-del-archivo-dependenciastxt-opcional)
- [Validaciones y mensajes de error](#validaciones-y-mensajes-de-error)
- [Problemas frecuentes (FAQ)](#problemas-frecuentes-faq)

## Descripción del módulo

Este proyecto consiste en una **calculadora binaria de 8 bits** que opera con números **enteros positivos**.  
- Los **operandos** se introducen como **números binarios** de **1 a 8 dígitos** (`0` y `1`).  
- La **operación** se elige mediante un **signo**: `+` (suma) o `-` (resta).  
- Si no se proporciona signo, el programa ejecuta **ambas operaciones** y muestra los resultados en bloques separados.  

**Uso**:
    
    python nombre_del_archivo.py <primer_binario> [operador] <segundo_binario>

**Ejemplo**:

*Ambas operaciones*

    python calculadora_binaria.py 101011 11
*Suma*

    python calculadora_binaria.py 10100111 + 101101
*Resta*

    python calculadora_binaria.py 10100111 - 101111

## Requisitos del sistema

- **Python 3.10 o superior**.  
- **Se requiere la dependencia `pytest`.**  
- Si en el futuro se añaden más librerías, se incluirán en el archivo **`dependecias.txt`** [(veáse sección 5)](#uso-del-archivo-dependenciastxt-opcional)

---

## Instalación de Python en los diferentes sistemas operativos.

### Linux

#### Debian/Ubuntu
```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
python3 --version
python3 -m pip --version
```
#### Fedora

```bash
sudo dnf install -y python3 python3-pip python3-virtualenv
python3 --version
python3 -m pip --version
```
#### Arch/Manjaro

```bash
sudo pacman -S --needed python python-pip
python --version
python -m pip --version
```
***Recomendación:***
Usar un entorno virtual, a continuación se muestra como instalarlo en un entorno Linux:
```bash
pip install virtualenv
virtualenv env
source . ./env/bin/activate
```
En el caso de que se descargue el archivo `pytest.ini` en la raíz del proyecto no hace falta especificar `source`.

De la misma forma, cuando se desee desactivar el entorno virtual se indicará con el comando `. ./env/bin/deactivate`

### Windows

#### Opción A — Microsoft Store

1. Abre **Microsoft Store**, busca **Python 3.1x**. *Recuerda que se necesita Python 3.10 o superior*
2. Instala y comprueba la instalación:
```cmd
py --version
py -m pip --version
```

#### Opción B — Instalador oficial
1. Descarga el instalador desde [https://www.python.org/downloads/](https://www.python.org/downloads/).  
2. Marca la casilla “**Add Python to PATH**” durante la instalación. 
3. Verifica la instalación:
```cmd
py --version
py -m pip --version
```
***Recomendación:***
Usar un entorno virtual, a continuación se muestra como instalarlo en Windows:
```cmd
py -m venv .venv
..venv\Scripts\Activate.ps1
```
De la misma forma, cuando se desee desactivar el entorno virtual se indicará con el comando `..venv\Scripts\Deactivate.ps1`

---

## Ejecución del módulo

### Sintaxis general
```bash
python calculadora_binaria.py OPERANDO1 [OPERADOR] OPERANDO2
```
En donde:

- `OPERANDO1` y `OPERANDO2`: cadenas binarias válidas (solo `0` y `1`, máximo 8 bits).  
- `SIGNO` (opcional):  
  - `+` → realiza **suma**.  
  - `-` → realiza **resta**.  
- Si no se especifica el signo, se ejecutan **ambas operaciones** con los mismos operandos.

> En Windows puedes usar `py` en lugar de `python`.  
> En Linux o macOS, usa `python3` si hay varias versiones instaladas.

### Ejemplos

**Suma explícita**
```bash
python calculadora.py 10101010 + 11111111
```

**Salida esperada**
> El resultado de sumar *10101010* y *11111111* es *110101001*

**Resta explícita**
```bash
python calculadora.py 11111111 - 10101010
```
> El resultado de restar *11111111* y *10101010* es *01010101*

**Sin operador (ejecuta ambas)**
```bash
python calculadora.py 11111111 11111111
```
**Salida esperada**

> Suma:	
El resultado de sumar *11111111* y *11111111* es *111111110*

> Resta:	
El resultado de restar *11111111* y *11111111* es *00000000*

---

## Uso del archivo `dependencias.txt` (opcional).

Si el proyecto requiere librerías externas, deben especificarse en el archivo **`dependecias.txt`** (una por línea).  
Ejemplo de contenido:
```txt
rich>=13.0
pytest
colorama==0.4.6
```
### Instalación de dependencias

> Usa el intérprete para invocar `pip` y evitar confusiones con `pip`/`pip3`. 

#### Linux/MacOS

```bash
python3 -m pip install -r dependecias.txt
```

#### Windows

```cmd
py -m pip install -r dependecias.txt
```

Si el archivo **no existe** o está vacío, el proyecto **no necesita ninguna dependencia** adicional. Aunque en este caso es necesario la dependencia `pytest` para ejecutar los tests.

---

## Validaciones y mensajes de error


- **Faltan argumentos o hay demasiados**  
  Mensaje: `Uso: 'nombre_del_archivo.py' <primer_número> [operador] <segundo_número>`
- **Operando inválido** (número binario menor 1 bit o mayor 8 bits)  
  Mensaje: `Error. Los números binarios deben ser de 1 hasta 8 bits`  
- **Signo/operación inválida** (distinta de `+` o `-`)  
  Mensaje: `Error. Los únicos operadores válidos son '+' y '-'.".`  
 **Primer número contiene caracteres no binarios** (`0` y `1` son los únicos válidos)  
  Mensaje:`Error. Por favor, introduzca el primer número binario de 1 hasta 8 bits (sólo 0 y 1) e inténtelo de nuevo.`
- **Segundo número contiene caracteres no binarios** (`0` y `1` son los únicos válidos)  
  Mensaje: `Error. Por favor, introduzca el segundo número binario de 1 hasta 8 bits (sólo 0 y 1) e inténtelo de nuevo.`
- **Error en la resta** (el primer número es menor que el segundo)  
  Mensaje: `Error. Para restar, el primer número no puede ser más pequeño.`

---

## Problemas frecuentes (FAQ)

- **“python: command not found” / “py no se reconoce”**  
  Indica que Python no está instalado o no se ha añadido al **PATH** del sistema.  
  **Solución:**  
  - Verifica si Python está instalado ejecutando:  
    ```
    python3 --version
    ```  
  - Si funciona con `python3`, crea un alias para usar `python`:  
    ```
    sudo ln -s /usr/bin/python3 /usr/bin/python
    ```  
  - En **Windows**, asegúrate de marcar la opción **“Add Python to PATH”** durante la instalación.

---

- **“pip no se reconoce” / “pip: command not found”**  
  Aparece cuando `pip` no está correctamente disponible o no se instaló con Python.  
  **Solución:**  
  - Ejecuta la instalación manual de paquetes con el intérprete:  
    ```
    python -m pip install nombre_paquete
    ```  
  - En **Windows**, usa:  
    ```
    py -m pip install nombre_paquete
    ```  
  - Si falla, reinstala `pip`:  
    ```
    python -m ensurepip --upgrade
    ```

---

- **Formato de operando incorrecto**  
  Se debe a valores que no son **binarios** válidos o que exceden los **8 bits** permitidos.  
  **Solución:**  
  - Asegúrate de introducir solo **0** y **1**.  
  - Usa operandos de longitud entre **1** y **8 bits**.  
  - Ejemplo válido:
    ```
    python calculadora_binaria.py 1101 + 101
    ```

---

- **Signo en posición incorrecta o ausente**  
  El error ocurre cuando el operador (`+` o `-`) está mal colocado o no se introduce.  
  **Solución:**  
  - Usa la sintaxis correcta:
    ```
    python calculadora_binaria.py <operando1> [signo] <operando2>
    ```  
  - Ejemplo correcto:
    ```
    python calculadora_binaria.py 101010 + 111
    ```

---

- **“Error. Para restar, el primer número no puede ser más pequeño.”**  
  Se produce cuando el segundo número binario es mayor que el primero.  
  **Solución:**  
  - Asegúrate de que el primer número sea **igual o mayor** que el segundo.  
  - El programa no admite resultados negativos. Si necesitas eso, deberás implementar la resta en **complemento a dos**.

---

- **“Uso: 'nombre_del_archivo.py' <primer_número> [operador] <segundo_número>”**  
  Indica que los argumentos pasados son **insuficientes o excesivos**.  
  **Solución:**  
  - Ejecuta el programa con exactamente **dos operandos** (y un operador opcional).  
  - Ejemplo correcto:
    ```
    python calculadora_binaria.py 101 + 11
    ```
