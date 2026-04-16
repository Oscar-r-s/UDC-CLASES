
def menu_y_opcion(opciones_posibles, equipo):
    print(
    '''  
    ---------------------------------------------------------------------

        Menú de opciones: 
        (1) Añadir jugador 
        (2) Eliminar jugador 
        (3) Mostrar jugador 
        (4) Listar jugadores 
        (5) Crear convocatoria 
        (6) Terminar '''
    )
    opcion_escogida = int(input("   Elige una opción : "))

    if opcion_escogida == 6 :
        print("---     PROGRAMA TERMINADO       ---")
        return

    else :
        opciones_posibles[opcion_escogida](equipo)
        menu_y_opcion(opciones_posibles, equipo)

def add_jugador(equipo):
    dorsal = int(input("Introduce el dorsal del jugador : "))

    while dorsal in equipo:
        dorsal = input("Ese dorsal ya existe, introduce otro : ")

    nombre = input("Introduce el nombre del jugador : ")

    equipo[dorsal] = nombre

def eliminar_jugador(equipo):
    dorsal = int(input("Introduce el dorsal del jugador a eliminar: "))

    while dorsal not in equipo :
        dorsal = int(input("Dorsal inexistente. Introduce un dorsal que SÍ esté en el equipo : "))
    equipo.pop(dorsal)

def mostrar_jugador(equipo):
    dorsal = int(input("Introduce el dorsal : "))

    print(f"El jugador de dorsal {dorsal} es {equipo[dorsal]}")

def listar_plantilla(equipo):
    print("Plantilla Actual : ")

    for clave, valor in equipo.items() :
        print(f"{clave}     {valor}")

def crear_convocatoria(equipo):
    convocatoria = {}
    numero_jugadores = 12
    print(f"Introduzca el dorsal de los {numero_jugadores} jugadores convocados :")

    for i in range(numero_jugadores + 1 ):
        dorsal = int(input("Introduce el dorsal : "))

        while dorsal not in equipo :
            dorsal = int(input("El dorsal no existe, inténtalo de nuevo : "))

        convocatoria[dorsal] = equipo[dorsal]
    
    print('\nJugadores convocados : ')

    for clave, valor  in convocatoria.items() :
        print(f"{valor}")

#---------------------------------------------------------------------------------------
def main():
    opciones = {
        1 : add_jugador,
        2 : eliminar_jugador,
        3 : mostrar_jugador,
        4 : listar_plantilla,
        5 : crear_convocatoria,
        # 6 : terminar
    } 
    plantilla = {
        0 : "Williams-Goss", 1 : "Causeur", 3 : "Randolph", 5 : "Rudy",
        6 : "Abalde", 8 : "Hanga", 11 : "Hezonja", 12 : "Alocén",
        13 : "Rodríguez", 14 : "Deck", 17 : "Poirier", 21 : "Cornelie",
        22 : "Tavares", 23 : "Llull", 28 : "Yabusele", 30 : "Ndiaye"
    }
    opcion_escogida = menu_y_opcion(opciones, plantilla)


if __name__ == "__main__":
    main()