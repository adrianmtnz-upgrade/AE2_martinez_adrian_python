import time
from src.utilidades import pedir_float, pedir_booleano, obtener_fecha_hora, pedir_entero_rango, limpiar_terminal


"""
EJERCICIO 2: GESTION DE CUENTA BANCARIA

Modulo de gestion de una cuenta bancaria.

Permite crear una cuenta, realizar depositos y retiros, consultar el saldo
y mostrar estadisticas completas de movimientos, ingresos y retiros.

"""


def crear_cuenta() -> None:
    """
        Crea una nueva cuenta bancaria solicitando un saldo inicial al usuario.

        Inicializa el saldo actual, registra el deposito inicial en el historial
        y actualiza el contador de movimientos.
        """

    global saldo_actual
    global cant_total_depositos
    global historial_depositos
    global historial_movimientos

    # Variable que almacena el saldo actual de la cuenta,
    # se inicializa pidiendole una cantidad inicial al usuario
    saldo_actual = pedir_float("Por favor, introduce el saldo inicial: ")
    # Variable que contiene la fecha y hora actual en el momento de la operacion
    fecha_hora = obtener_fecha_hora()

    # Agrega el saldo de la transaccion inicial a la cantidad de dinero depositado del historial
    cant_total_depositos += saldo_actual
    # Registra en el historial de depositos la transaccion inicial
    historial_depositos[fecha_hora] = saldo_actual
    # Incrementa el contador de movimientos bancarios
    historial_movimientos += 1

    # Muestra al usuario que la cuenta se ha creado correctamente y el saldo actual
    print(f"Cuenta creada correctamente saldo inicial: {saldo_actual:.2f}$")

    # Espera 2 segundos y limpia la terminal
    time.sleep(2)
    limpiar_terminal()


def depositar_dinero() -> None :
    """
        Solicita una cantidad al usuario y la deposita en la cuenta.

        Actualiza el saldo actual, el total de depositos, el historial
        de ingresos y el contador de movimientos.
        """
    global saldo_actual
    global cant_total_depositos
    global historial_depositos
    global historial_movimientos

    # Variable que almacena la cantidad de dinero que va a depositar el usuario
    cant_deposito = pedir_float("Introduce la cantidad que quieres depositar en tu cuenta: ", 1)
    # Variable que contiene la fecha y hora actual en el momento de la operacion
    fecha_hora = obtener_fecha_hora()

    # Agrega el deposito realizado a la cantidad de saldo actual de la cuenta
    saldo_actual += cant_deposito
    # Agrega el saldo del deposito realizado a la cantidad del historial de depositos
    cant_total_depositos += cant_deposito
    # Registra en el historial de depositos la transaccion del deposito actual
    historial_depositos[fecha_hora] = cant_deposito
    # Incrementa el contador de movimientos bancarios
    historial_movimientos += 1

    # Muestra al usuario que el deposito se ha realizado correctamente
    print("\u001b[32mDeposito realizado correctamente\u001b[0m\n")

    # Espera 2 segundos y limpia la terminal
    time.sleep(2)
    limpiar_terminal()


def retirar_dinero() -> None:
    """
        Permite retirar dinero de la cuenta si el saldo es suficiente.

        Si el saldo no es suficiente, ofrece al usuario la opcion de corregir
        el importe o volver al menu principal.
        """
    global saldo_actual
    global cant_total_retiros
    global historial_retiros
    global historial_movimientos

    # Variable que almacena la cantidad de dinero que va a retirar el usuario
    cant_retiro = pedir_float("Introduce la cantidad que quieres retirar: ", 1)

    # Comprueba que la cantidad que se va a retirar sea inferior o igual al saldo disponible
    if cant_retiro <= saldo_actual:
        # Resta al saldo actual la cantidad del retiro
        saldo_actual -= cant_retiro
        # Obtiene fecha y hora del movimiento
        fecha_hora = obtener_fecha_hora()

        # Agrega el saldo del retiro realizado a la cantidad del historial de retiros
        cant_total_retiros += cant_retiro
        # Registra en el historial de retiros la transaccion del retiro actual
        historial_retiros[fecha_hora] = cant_retiro
        # Incrementa el contador de movimientos bancarios
        historial_movimientos += 1

        # Muestra al usuario que el deposito se ha realizado correctamente
        print("\u001b[32mRetiro realizado correctamente\u001b[0m\n")

        # Espera 2 segundos y limpia la terminal
        time.sleep(2)
        limpiar_terminal()

        # Sale de la funcion, innecesario pero mejora legibilidad
        return

    # Si la cantidad del retiro es superior al saldo disponible:
    else:
        # Informa al usuario
        print("Lo siento, la operacion no se puede realizar. El saldo actual de la cuenta es insuficiente.")

        # Da a elegir al usuario entre corregir el importe del retiro o volver al menu
        match pedir_booleano("Para corregir el importe a retirar introduce: 1\n"
                             "Para volver al menu introduce: 0\n"):
            # Corregir importe
            case 1:
                retirar_dinero()
                print("\n")

            # Volver al menu
            case 0:
                limpiar_terminal()
                return


def mostrar_saldo() -> None:
    """
     Muestra el saldo actual de la cuenta por pantalla.
     """

    print(f"\u001b[36mSaldo actual: {saldo_actual:.2f}$\n\u001b[0m")

    # Espera 2 segundos y limpia la terminal
    time.sleep(2)
    limpiar_terminal()


def mostrar_estadisticas() -> None:
    """
    Muestra estadisticas de la cuenta bancaria.

    Incluye numero total de movimientos, dinero ingresado,
    dinero retirado y el historial detallado de cada operación.
    """

    print(f"\n\n                            MOSTRANDO ESTADISTICAS DE TU CUENTA\n"
          f"_______________________________________________________________________________________________\n\n")

    # Muestra la cantidad total de movimientos y especifica cuantos son depositos y cuantos son retiros
    print(f"\t\tCANTIDAD DE MOVIMIENTOS: {historial_movimientos}\t\t\t"
          f"\u001b[32mDEPOSITOS: {len(historial_depositos)}\u001b[0m\t  "
          f"\u001b[31mRETIROS: {len(historial_retiros)}\u001b[0m")

    # Muestra la cantidad total que se ha ingresado y retirado desde la creacion de la cuenta
    print(f"\t\t\u001b[32mDINERO TOTAL INGRESADO: {cant_total_depositos:.2f}$\u001b[0m\t\t\t"
          f"\u001b[31mDINERO TOTAL RETIRADO: {cant_total_retiros:.2f}$\u001b[0m\n")

    # Muestra el historial de depositos realizados
    print("\nHistorial de Depositos:\n")

    # Utiliza un bucle for para recorrer el mapa de depositos y mostrar
    # en formato legible fecha, hora y cantidad del deposito
    for fecha_hora, ingreso in historial_depositos.items():
        print(f"FECHA: {fecha_hora}\t\t\t\t\u001b[32m INGRESO: {ingreso:.2f}$\u001b[0m")

    # Muestra el historial de depositos realizados
    print("\nHistorial de Retiros:\n")

    # Utiliza un bucle for para recorrer el mapa de retiros y mostrar
    # en formato legible fecha, hora y cantidad del retiro
    for fecha_hora, retiro in historial_retiros.items():
        print(f"FECHA: {fecha_hora}\t\t\t\t\u001b[31m RETIRO: {retiro:.2f}$\u001b[0m")

    print("\n\n\n")

    # Pide al usuario que introduzca cualquier entrada para volver al menu
    input("Introduce cualquier tecla para volver al menu")
    # Limpia la terminal
    limpiar_terminal()



##############################################
#             VARIABLES GLOBALES             #
##############################################

# CANTIDAD DE SALDO ACTUAL EN LA CUENTA (float)
saldo_actual = 0
# CANTIDAD TOTAL DE DINERO DEPOSITADO (float)
cant_total_depositos = 0
# CANTIDAD TOTAL DE DINERO RETIRADO (float)
cant_total_retiros = 0
# HISTORIAL DE DEPOSITOS (map {str, float})
historial_depositos = {}
# HISTORIAL DE RETIROS (map {str, float})
historial_retiros = {}
# CONTADOR DE MOVIMIENTOS BANCARIOS REALIZADOS (int)
historial_movimientos = 0



#####################################################################
#                     BLOQUE DE EJECUCION                           #
#####################################################################

# Limpiar la terminal al iniciar el programa
limpiar_terminal()

print("\n\n\u001b[36mBIENVENIDO AL BANCO SABATER\u001b[0m\n")
print("\nVamos a crear tu nueva cuenta\n")

# Llama a la funcion para asignar el saldo inicial de la cuenta
crear_cuenta()

# Bucle infinito hasta que el usuario introduzca la opcion de salir
while True:

    # Muestra el menu de opciones y le pide al usuario
    # que introduzca un entero correspondiente a la opcion a realizar
    opcion = pedir_entero_rango("\n\n\t\tMENU DE OPCIONES DE TU CUENTA\n"
                                "\t____________________________________\n\n"
                                "Introduce el numero correspondiente a la opcion que deseas realizar\n\n"
                                "\t1 - Ingresar dinero\n"
                                "\t2 - Retirar dinero\n"
                                "\t3 - Mostrar saldo\n"
                                "\t4 - Estadisticas\n"
                                "\t5 - Salir\n"
                                "\nOpcion elegida: ",
                                1, 5)
    print("\n")

    # Realiza la operacion correspondiente a la eleccion del usuario
    match opcion:
        # Depositar dinero
        case 1: depositar_dinero()
        # Retirar dinero
        case 2: retirar_dinero()
        # Mostrar saldo actual
        case 3: mostrar_saldo()
        # Mostrar estadisticas de la cuenta
        case 4: mostrar_estadisticas()
        # Salir
        case 5:
                print("Gracias por utilizar nuestro banco")
                print("Fin de la operacion")
                break
        # No hay caso por defecto ya que en la entrada se valida que solo sea un entero del 1 al 5