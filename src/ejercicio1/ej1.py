import random
from src.utilidades import pedir_entero_rango


"""
EJERCICIO 1: JUEGO PIEDRA, PAPEL O TIJERA

Este modulo implementa el juego de Piedra, Papel o Tijera contra la maquina. 
El jugador y la maquina realizan jugadas aleatorias y se evaluan las rondas 
hasta que uno de los dos alcanza 2 victorias.

"""


def pedir_jugada() -> int:
    """
    Solicita al jugador una jugada valida por teclado.

    Las opciones disponibles son:
    - 1: Piedra
    - 2: Papel
    - 3: Tijera

    :return: Entero representando la jugada del jugador
    """
    return pedir_entero_rango("Introduce tu jugada (1 - Piedra | 2 - Papel | 3 - Tijera): ", 1, 3)


def generar_jugada() -> int:
    """
    Genera una jugada aleatoria para la maquina.

    :return: Entero entre 1 y 3 representando la jugada de la maquina
    """
    return random.randint(1, 3)


def jugada_to_string(valor: int) -> str:
    """
       Convierte una jugada numerica en su representacion en texto.

       :param valor: Valor entero de la jugada (1, 2 o 3)
       :return: Nombre de la jugada como string
       """
    jugadas = {
        1: "Piedra",
        2: "Papel",
        3: "Tijera"
    }

    return jugadas[valor]


def mostrar_jugada(valor_jugada: int, es_jugador: bool = True,) -> None:
    """
        Muestra por pantalla la jugada realizada.

        :param valor_jugada: Valor entero de la jugada
        :param es_jugador: Indica si la jugada pertenece al jugador o a la máquina
        :return: None
        """
    if es_jugador: print(
        f"           Tu jugada: {jugada_to_string(valor_jugada)}")
    else: print(
        f"Jugada de la maquina: {jugada_to_string(valor_jugada)}\n")


def evaluar_ronda(eleccion_jugador: int, eleccion_maquina: int) -> str:
    """
        Evalua el resultado de una ronda comparando la jugada del jugador
        con la jugada de la maquina.

        Actualiza el marcador global correspondiente según el resultado.

        :param eleccion_jugador: Jugada del jugador
        :param eleccion_maquina: Jugada de la maquina
        :return: Mensaje indicando el resultado de la ronda
        """
    match (eleccion_jugador, eleccion_maquina):
        # Caso de empate
        case (1, 1) | (2, 2) | (3, 3):
            return "Resultado: Empate esta ronda!"

        # Caso de Victoria para el jugador
        case (1, 3) | (2, 1) | (3, 2):
            global marcador_jugador
            marcador_jugador += 1
            return "Resultado: Has ganado esta ronda!\n"

        # Caso de Derrota para el jugador
        case _:
            global marcador_maquina
            marcador_maquina += 1
            return "Resultado: Has perdido esta ronda!\n"


def comprobar_ganador(marcador_jugador: int, marcador_maquina: int) -> bool:
    """
    Comprueba si alguno de los jugadores ha ganado la partida.

    La partida finaliza cuando alguno alcanza 2 victorias.

    :param marcador_jugador: Puntuacion actual del jugador
    :param marcador_maquina: Puntuacion actual de la maquina
    :return: True si hay ganador, False en caso contrario
    """
    # Devuelve False si ningun jugador tiene 2 puntos en el marcador
    if marcador_jugador < 2 and marcador_maquina < 2: return False

    # Evalua si es el jugador el que ha ganado e informa al usuario de que ha ganado
    if marcador_jugador == 2:
        print(
        "=================================================\n"+
        f"\t\t\u001b[32mHas ganado la partida ({marcador_jugador} - {marcador_maquina})\u001b[0m\n"+
        "=================================================")

    # Evalua si es la maquina la que ha ganado e informa al usuario de que ha perdido
    if marcador_maquina == 2:
        print(
        "==============================================================\n" +
        f"\t\t\u001b[31mLa maquina ha ganado la partida ({marcador_maquina} - {marcador_jugador})\u001b[0m\n" +
        "==============================================================")

    # Devuelve True porque hay ganador
    return True



##############################################
#             VARIABLES GLOBALES             #
##############################################

# MARCADOR DEL JUGADOR (int)
marcador_jugador = 0
# MARCADOR DE LA MAQUINA (int)
marcador_maquina = 0
# VARIABLE QUE ALMACENA EL GANADOR (bool)
ganador = False



#####################################################################
#                     BLOQUE DE EJECUCION                           #
#####################################################################

# Bucle que ejecuta el bloque de codigo hasta que haya un ganador
while not ganador:

    # Pide la eleccion del jugador
    eleccion_jugador = pedir_jugada()
    # Genera la eleccion de la maquina
    eleccion_maquina = generar_jugada()

    print()
    # Muestra las jugadas realizadas
    mostrar_jugada(eleccion_jugador)
    mostrar_jugada(eleccion_maquina, False)

    # Evalua y muestra quien ha ganado la ronda
    print(evaluar_ronda(eleccion_jugador, eleccion_maquina))

    # Comprueba si hay ganador de la partida
    ganador = comprobar_ganador(marcador_jugador, marcador_maquina)

