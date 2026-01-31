import os
from _pydatetime import datetime


def pedir_entero_rango(mensaje: str, valor_min: int, valor_max: int) -> int:
    """
    Solicita al usuario un numero entero por teclado y valida que se encuentre
    dentro del rango especificado.

    El proceso se repite hasta que el usuario introduce un valor valido.

    :param mensaje: Mensaje mostrado al usuario para solicitar la entrada
    :param valor_min: Valor minimo permitido (incluido)
    :param valor_max: Valor maximo permitido (incluido)
    :return: Numero entero valido dentro del rango indicado
    """
    while True:

        try:
            # Captura la entrada, remueve espacios en blanco al principio y final
            # y hace la conversion a integer
            valor = int(input(mensaje).strip())

            # Comprueba que el valor se encuentre dentro del rango y lo devuelve.
            if valor_min <= valor <= valor_max : return valor
            # Si no se encuentra dentro del rango lanza un ValueError
            raise ValueError()

        # Captura el ValueError e informa al usuario antes de pedir de nuevo la entrada
        except ValueError:
            print(f"El valor introducido no es valido, debes introducir un numero entre {valor_min} y {valor_max}")


def pedir_booleano(mensaje: str) -> int:
    """
    Solicita al usuario un valor booleano representado como entero.

    El valor devuelto sera:
    - 0 para False
    - 1 para True

    :param mensaje: Mensaje mostrado al usuario
    :return: Valor entero 0 o 1
    """
    return pedir_entero_rango(mensaje, 0, 1)


def pedir_float(mensaje: str, valor_min: float = 0) -> float:
    """
    Solicita al usuario un numero decimal y valida que sea mayor o igual
    al valor minimo indicado.

    El numero devuelto se redondea a dos decimales.

    :param mensaje: Mensaje mostrado al usuario
    :param valor_min: Valor minimo permitido (por defecto 0)
    :return: Numero decimal válido con dos decimales
    """
    while True :

        try :
            # Captura la entrada, remueve espacios en blanco al principio y final
            # y hace la conversion a float, finalmente redondea a 2 decimales
            valor = round(float(input(mensaje).strip()), 2)

            # Comprueba que es mayor o igual que 0, si es asi lo devuelve si no lanza un ValueError
            if valor >= valor_min : return valor
            raise ValueError()

        # Captura el ValueError e informa al usuario antes de pedir de nuevo la entrada
        except ValueError:
            print(f"El valor introducido no es valido, debe ser un numero mayor que 0\n")


def obtener_fecha_hora() -> str:
    """
    Obtiene la fecha y hora actual del sistema en formato legible.

    :return: Fecha y hora formateadas como string
    """
    return datetime.now().strftime("%d/%m/%Y \tHora: %H:%M:%S")


def limpiar_terminal():
    """
    Limpia la terminal según el sistema operativo o el entorno de ejecucion.

    - Windows: usa el comando 'cls'
    - Linux/macOS: usa 'clear' si la variable TERM esta definida
    - IDEs: simula el limpiado imprimiendo líneas en blanco
    """
    # Terminal en Windows
    if os.name == "nt": os.system("cls")
    else:
        # Terminal en Linux
        if "TERM" in os.environ: os.system("clear")
        # Terminal en IDE
        else: print("\n" * 50)