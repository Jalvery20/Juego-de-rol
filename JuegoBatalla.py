from Juego import Juego
import pickle
import os
class JuegoBatalla(Juego):
    def __init__(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_personajes_disponibles(self, jugador):
        for idx, personaje in enumerate(jugador.equipo.personajes):
            if personaje.salud > 0:
                print(f"{idx + 1}. {personaje.nombre} - Salud: {personaje.salud} - Ataque: {personaje.ataque}")

    def guardar_estado(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump((self.jugador1, self.jugador2), f)
        print("Estado del juego guardado con éxito.")
        exit()  # Termina el juego después de guardar

    def cargar_estado(self, filename):
        try:
            with open(filename, 'rb') as f:
                self.jugador1, self.jugador2 = pickle.load(f)
                print("Estado del juego cargado con éxito.")
        except FileNotFoundError:
            print("El archivo especificado no existe.")
        except Exception as e:
            print("Error al cargar el estado del juego:", e)

    def jugar_turno(self):
        while True:
            jugadores = [self.jugador1, self.jugador2]
            for idx, jugador in enumerate(jugadores):
                atacante = jugador
                defensor = jugadores[(idx + 1) % 2]  # El otro jugador es el defensor

                print(f"Turno de {atacante.nombre}:")
                if defensor.esta_derrotado():
                    print(f"¡{atacante.nombre} gana la batalla!")
                    return
                
                while True:
                    print("Personajes disponibles para atacar:")
                    self.mostrar_personajes_disponibles(atacante)
                    print("0. Guardar partida")
                    opcion_ataque = int(input("Elige el número del personaje para atacar: ")) - 1
                    if opcion_ataque == -1:
                        self.guardar_estado("partida_guardada.pickle")
                        return
                    if opcion_ataque < 0 or opcion_ataque >= len(atacante.equipo.personajes):
                        print("La opción seleccionada no es válida.")
                        continue
                    
                    print("Personajes disponibles para ser atacados:")
                    self.mostrar_personajes_disponibles(defensor)
                    opcion_defensa = int(input("Elige el número del personaje a ser atacado: ")) - 1
                    
                    if opcion_defensa < 0 or opcion_defensa >= len(defensor.equipo.personajes):
                        print("La opción seleccionada no es válida.")
                        continue
                    
                    self.clear_console()
                    atacante_actual = atacante.equipo.personajes[opcion_ataque]
                    defensor_actual = defensor.equipo.personajes[opcion_defensa]

                    atacante_actual.atacar(defensor_actual)
                    if defensor.esta_derrotado():
                        print(f"¡{atacante.nombre} gana la batalla!")
                        return
                    break  # Salimos del bucle si no hay errores
