""" Este programa es un juego de batalla por turnos en el que dos jugadores compiten entre sí utilizando equipos de personajes. Cada jugador puede elegir entre diferentes tipos de personajes, como guerreros, hechiceros o guerreros hechiceros, cada uno con habilidades únicas.

El juego comienza con la opción de cargar una partida existente o comenzar una nueva. Si se elige cargar una partida existente, el juego recuperará el estado guardado previamente. De lo contrario, los jugadores pueden ingresar sus nombres y crear sus equipos de personajes eligiendo el tipo de personaje y sus atributos.

Una vez que se crean los equipos, los jugadores se turnan para atacar al otro equipo con sus personajes. El juego continúa hasta que uno de los equipos queda derrotado.

Para ejecutar el programa, simplemente ejecute el archivo principal app.py con el comando python app.py. Se le pedirá que decida si desea cargar una partida existente o comenzar una nueva. Siga las instrucciones en pantalla para ingresar la información requerida, como nombres de jugadores y tipos de personajes, y luego disfrute de la batalla."""


from JuegoBatalla import JuegoBatalla
from Jugador import Jugador
from Equipo import Equipo
from Guerrero import Guerrero
from Hechicero import Hechicero
from GuerreroHechicero import GuerreroHechicero
def crear_personaje():
    while True:
        while True:
            tipo_personaje = input("Ingrese el tipo de personaje (Guerrero/Hechicero/GuerreroHechicero): ").lower()
            if tipo_personaje in ['guerrero', 'hechicero', 'guerrerohechicero']:
                break
            else:
                print("Por favor, ingrese uno de los siguientes valores: Guerrero, Hechicero o GuerreroHechicero.")
        
        nombre_personaje = ""
        while not nombre_personaje.strip() or nombre_personaje.isdigit():
            nombre_personaje = input("Ingrese el nombre del personaje: ").strip()
            if not nombre_personaje:
                print("Por favor, ingrese un nombre no vacío para el personaje.")
            elif nombre_personaje.isdigit():
                print("El nombre del personaje no puede ser un número.")
        
        while True:
            try:
                nivel_personaje = int(input("Ingrese el nivel del personaje: "))
                break
            except ValueError:
                print("El nivel debe ser un número entero.")
        
        if tipo_personaje == "guerrero":
            while True:
                try:
                    fuerza = int(input("Ingrese la fuerza del guerrero: "))
                    break
                except ValueError:
                    print("La fuerza debe ser un número entero.")
            arma = ""
            while not arma.strip() or arma.isdigit():
                arma = input("Ingrese el arma del guerrero: ").strip()
                if not arma:
                    print("Por favor, ingrese un nombre no vacío para el arma.")
                elif arma.isdigit():
                    print("El arma no puede ser un número.")
            return Guerrero(nombre_personaje, nivel_personaje, fuerza, arma)
        elif tipo_personaje == "hechicero":
            while True:
                try:
                    poder_magico = int(input("Ingrese el poder mágico del hechicero: "))
                    break
                except ValueError:
                    print("El poder mágico debe ser un número entero.")
            conjuro = ""
            while not conjuro.strip():
                conjuro = input("Ingrese el conjuro del hechicero: ").strip()
                if not conjuro:
                    print("Por favor, ingrese un conjuro no vacío.")
            return Hechicero(nombre_personaje, nivel_personaje, poder_magico, conjuro)
        elif tipo_personaje == "guerrerohechicero":
            while True:
                try:
                    fuerza = int(input("Ingrese la fuerza del guerrero hechicero: "))
                    poder_magico = int(input("Ingrese el poder mágico del guerrero hechicero: "))
                    break
                except ValueError:
                    print("La fuerza y el poder mágico deben ser números enteros.")
            arma = ""
            while not arma.strip() or arma.isdigit():
                arma = input("Ingrese el arma del guerrero hechicero: ").strip()
                if not arma:
                    print("Por favor, ingrese un nombre no vacío para el arma.")
                elif arma.isdigit():
                    print("El arma no puede ser un número.")
            conjuro = ""
            while not conjuro.strip() or conjuro.isdigit():
                conjuro = input("Ingrese el conjuro del guerrero hechicero: ").strip()
                if not conjuro:
                    print("Por favor, ingrese un conjuro no vacío .")
                elif conjuro.isdigit():
                    print("El conjuro no puede ser un número.")
            tipo_dualidad = ""
            while not tipo_dualidad.strip() or tipo_dualidad.isdigit():
                tipo_dualidad = input("Ingrese el tipo de dualidad del guerrero hechicero: ").strip()
                if not tipo_dualidad:
                    print("Por favor, ingrese un tipo de dualidad no vacío .")
                elif tipo_dualidad.isdigit():
                    print("El tipo de dualidad no puede ser un número.")
            
            return GuerreroHechicero(nombre_personaje, nivel_personaje, fuerza, arma, poder_magico, conjuro, tipo_dualidad)
        else:
            print("Tipo de personaje no válido.")

def main():
    print("Bienvenido al juego de batalla!")
    while True:
        opcion = input("¿Desea cargar la partida existente? (s/n): ").lower()
        if opcion in ['s', 'n']:
            break
        else:
            print("Por favor, ingrese 's' para cargar la partida existente o 'n' para iniciar una partida nueva.")
    if opcion == 's':
        juego = JuegoBatalla(None, None)
        juego.cargar_estado("partida_guardada.pickle")
    else:
        jugador1_nombre = ""
        while not jugador1_nombre.strip() or jugador1_nombre.isdigit():  # Mientras el nombre del jugador 1 esté vacío, solo contenga espacios o sea un número
            jugador1_nombre = input("Nombre del jugador 1: ").strip()
            if not jugador1_nombre:
                print("Por favor, ingrese un nombre no vacío para el jugador 1.")
            elif jugador1_nombre.isdigit():
                print("El nombre del jugador 1 no puede ser un número.")

        jugador2_nombre = ""
        while not jugador2_nombre.strip() or jugador2_nombre.isdigit():  # Mientras el nombre del jugador 2 esté vacío, solo contenga espacios o sea un número
            jugador2_nombre = input("Nombre del jugador 2: ").strip()
            if not jugador2_nombre:
                print("Por favor, ingrese un nombre no vacío para el jugador 2.")
            elif jugador2_nombre.isdigit():
                print("El nombre del jugador 2 no puede ser un número.")

        equipo_jugador1 = Equipo(jugador1_nombre)
        equipo_jugador2 = Equipo(jugador2_nombre)

        while True:
            try:
                cantidad_personajes_jugador1 = int(input(f"Ingrese la cantidad de personajes para {jugador1_nombre}: "))
                break
            except ValueError:
                print("Por favor, ingrese un valor numérico.")

        while True:
            try:
                cantidad_personajes_jugador2 = int(input(f"Ingrese la cantidad de personajes para {jugador2_nombre}: "))
                break
            except ValueError:
                print("Por favor, ingrese un valor numérico.")

        for i in range(cantidad_personajes_jugador1):
            print(f"Creando personaje {i+1} para {jugador1_nombre}:")
            personaje = crear_personaje()
            if personaje:
                equipo_jugador1.agregar_personaje(personaje)

        for i in range(cantidad_personajes_jugador2):
            print(f"Creando personaje {i+1} para {jugador2_nombre}:")
            personaje = crear_personaje()
            if personaje:
                equipo_jugador2.agregar_personaje(personaje)

        jugador1 = Jugador(jugador1_nombre, equipo_jugador1)
        jugador2 = Jugador(jugador2_nombre, equipo_jugador2)

        juego = JuegoBatalla(jugador1, jugador2)

    juego.jugar_turno()

if __name__ == "__main__":
    main()
