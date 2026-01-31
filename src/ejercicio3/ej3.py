import random
from src.utilidades import pedir_entero_rango, limpiar_terminal

"""
EJERCICIO 3: CARRERA DE COCHES

Dos coches avanzan de forma aleatoria hacia una meta situada a una distancia
definida por el usuario. En cada turno, los coches pueden avanzar, retroceder
o no moverse en funcion de un valor aleatorio.

El programa muestra graficamente la carrera y finaliza
cuando uno de los coches alcanza la meta.
"""


def pedir_pos_meta() -> int:
    """
     Solicita al usuario la distancia a la que se colocara la meta.

     La distancia debe estar comprendida entre 30 y 60.

     :return: Distancia de la meta
     """
    # Pide al usuario un entero entre 30 y 60 ambos incluidos
    return pedir_entero_rango(
        "Introduce a que distancia quieres que este la meta (30 ~ 60): ",
        30, 60)


def dibujar_coche(pos: int, meta: int, coche: str) -> None:
    """
    Muestra la posicion actual del coche y la meta.

    Si la posicion del coche supera la meta, se ajusta para que
    se dibuje exactamente en la meta.

    :param pos: Posicion actual del coche
    :param meta: Posicion de la meta
    :param coche: Emoticono que representa el coche
    :return: None
    """

    # Ajusta la posicion del coche a la meta si la ha sobrepasado
    if pos >= meta: pos = meta

    # Establece los espacios en blanco a dibujar antes del coche
    espacios_antes_coche = pos
    # Establece los espacion en blanco a dibujar despues del coche
    espacios_despues_coche = meta - espacios_antes_coche

    # Muestra la posicion del coche y la meta
    print(f"{" " * espacios_antes_coche}{coche}{" " * espacios_despues_coche}{ICONO_META}")


def calc_pos_coche(pos_coche: int, coche: str) -> int:
    """
    Calcula la nueva posicion de un coche en funcion de un valor aleatorio.

    El coche puede:
    - Retroceder 5 posiciones (pinchazo)
    - Avanzar 5 posiciones (turbo)
    - No moverse

    La posición nunca puede ser inferior a 0.

    :param pos_coche: Posicion actual del coche
    :param coche: emoticono que representa al coche
    :return: Nueva posicion del coche
    """
    # EMPIEZA A MOSTRAR EL EVENTO OCURRIDO
    # Comprueba que coche es, e imprime Coche A: o Coche B:
    if coche == COCHE_A: print("\u001b[34mCoche A: \u001b[0m", end="")
    else: print("\u001b[31mCoche B: \u001b[0m", end="")

    # Genera un valor aleatorio entre 1 y 100 ambos incluidos
    valor_aleatorio = random.randint(1, 100)

    # 20% posibilidades de retroceder 5 casillas
    if valor_aleatorio <= 20:
        avance = -5
        print(f"Pinchazo!!! Retrocede {-avance} casillas")

    # 30% posibilidades de avanzar 5 casillas
    elif 20 < valor_aleatorio <= 50:
        avance = 5
        print(f"Turbo! Avanza {avance} casillas")

    # 50% posibilidades de no hacer nada
    else:
        avance = 0
        print("No avanza!!")

    # Actualiza la posicion del coche en funcion del evento ocurrido.
    # Comprueba antes de actualizar que la posicion mas el avance sea mayor o igual que 5
    # y dependiendo del resultado incrementa el avance o no hace nada para evitar valores negativos
    pos_coche += avance if (pos_coche + avance) >= 5 else 0

    # Devuelve la nueva posicion del coche
    return pos_coche


def comprobar_ganador() -> str | None:
    """
    Comprueba si alguno de los coches ha alcanzado la meta o si la han alcanzado ambos y es empate.

    :return: Emoticono del coche ganador, empate o None si aun no hay ganador
    """
    # Empate
    if pos_coche_a >= META and pos_coche_b >= META: return "empate"
    # Gana Coche A
    elif pos_coche_a >= META : return COCHE_A
    # Gana Coche B
    elif pos_coche_b >= META : return COCHE_B

    return None


def mostrar_ganador(coche_ganador: str) -> None:
    """
    Muestra por pantalla el coche ganador de la carrera o si ha habido un empate.

    :param coche_ganador: Identificador del coche ganador
    :return: None
    """
    # Si hay un empate
    if coche_ganador == "empate":
        print("\n\u001b[33mLa carrera ha terminado en empate\u001b[0m\n")
        return

    # Si hay un coche ganador
    if coche_ganador == COCHE_A: print("\nEl \u001b[34mCoche A \u001b[0m", end="")
    else: print("\nEl \u001b[31mCoche B \u001b[0m", end="")

    print("ha ganado la carrera!\n")



##############################################
#                  CONSTANTES                #
##############################################

# EMOTICONO COCHE A
COCHE_A = "🚗"
# EMOTICONO COCHE B
COCHE_B = "🚙"
# EMOTICONO DE META
ICONO_META = "🏁"


##############################################
#                  VARIABLES                 #
##############################################

# POSICION DEL COCHE A
pos_coche_a = 0
# POSICION DEL COCHE B
pos_coche_b = 0
# VARIABLE PARA ALMACENAR AL GANADOR
ganador = None
# CONTADOR DE TURNOS
turno = 0


#####################################################################
#                     BLOQUE DE EJECUCION                           #
#####################################################################

# Limpia la terminal al iniciar el programa
limpiar_terminal()
# Constante que se inicializa con la entrada del usuario para determinar la posicion de la meta
META = pedir_pos_meta()

# Imprime las posiciones iniciales de ambos coches
print("\n\nPosiciones:\n")
dibujar_coche(pos_coche_a, META, COCHE_A)
dibujar_coche(pos_coche_b, META, COCHE_B)

# Pide al usario que introduzca Enter para que empiece la carrera
while not input("\nPulsa Enter para que avance el turno...") == "": print(
    "\u001b[31mTienes que pulsar la tecla enter\u001b[0m")

# Mientras que no haya ganador ejecuta la logica del juego
while ganador is None:
    # Limpia la terminal
    limpiar_terminal()
    # Incrementa en 1 el contador de turnos
    turno += 1
    # Muestra el turno
    print(f"\n--- Turno {turno} ---\n\n")

    # Calcula las posiciones de ambos coches y muestra los eventos ocurridos
    pos_coche_a = calc_pos_coche(pos_coche_a, COCHE_A)
    pos_coche_b = calc_pos_coche(pos_coche_b, COCHE_B)

    print("\n\nPosiciones:\n")
    # Muestra las posiciones de los coches
    dibujar_coche(pos_coche_a, META, COCHE_A)
    dibujar_coche(pos_coche_b, META, COCHE_B)

    # Comprueba si hay ganador
    ganador = comprobar_ganador()
    if ganador is not None:
        # Si hay ganador o empate lo muestra y termina la carrera
        mostrar_ganador(ganador)
        break

    else:
        # Si no hay ganador sigue pidiendo al usuario que introduzca Enter para avanzar turno
        while not input("\nPulsa Enter para que avance el turno...") == "": print(
        "\u001b[31mTienes que pulsar la tecla enter\u001b[0m")
