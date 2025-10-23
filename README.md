# Calculadora binaria de 8 bits en Python por consola.

Aplicación de línea de comandos que permite **sumar** y **restar** números binarios de **1 a 8 bits**, en donde todas las salidas se muestran en **formato binario de 8 bits**, rellenando con ceros a la izquierda cuando sea necesario. Si no se especifica un operador, el programa ejecuta **ambas operaciones** (suma y resta).

**Uso**:
    
    python nombre_del_archivo.py <primer_binario> [operador] <segundo_binario>

**Ejemplo**:

*Ambas operaciones*

    python calculadora_binaria.py 10100111 00001011
*Suma*

    python calculadora_binaria.py 10100111 + 00001011
*Resta*

    python calculadora_binaria.py 10100111 - 00001011

## Descripción del módulo

Este proyecto consiste en una **calculadora binaria de 8 bits** que opera con números **enteros sin signo**.  
- Los **operandos** se introducen como **números binarios** de **1 a 8 dígitos** (`0` y `1`).  
- La **operación** se elige mediante un **signo**: `+` (suma) o `-` (resta).  
- Si no se proporciona signo, el programa ejecuta **ambas operaciones** y muestra los resultados en bloques separados.  
- Antes de realizar los cálculos, los operandos se **ajustan a 8 bits**, completándolos con ceros a la izquierda.

## Requisitos del sistema

- **Python 3.10 o superior**.  
- **Se requiere la dependencia `pytest`.**  
- Si en el futuro se añaden más librerías, se incluirán en el archivo **`dependecias.txt`** (véase sección 5).

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
Usar un entorno virtual, a continuación se muestra como instalarlo:
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
Usar un entorno virtual, a continuación se muestra como instalarlo:
```cmd
py -m venv .venv
..venv\Scripts\Activate.ps1
```
De la misma forma, cuando se desee desactivar el entorno virtual se indicará con el comando `..venv\Scripts\Deactivate.ps1`

---

## Ejecución del módulo

### Sintaxis general
```bash
python calculadora_binaria.py OPERANDO1 [SIGNO] OPERANDO2
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