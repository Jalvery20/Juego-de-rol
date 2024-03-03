class Jugador:
    def __init__(self, nombre, equipo):
        self.nombre = nombre
        self.equipo = equipo

    def esta_derrotado(self):
        for personaje in self.equipo.personajes:
            if personaje.salud > 0:
                return False
        return True
