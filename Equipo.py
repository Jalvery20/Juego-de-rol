
class Equipo:
    def __init__(self, nombre_equipo):
        self.nombre_equipo = nombre_equipo
        self.personajes = []
    
    def agregar_personaje(self, personaje):
        self.personajes.append(personaje)
    
    def eliminar_personaje(self, nombre_personaje):
        for personaje in self.personajes:
            if personaje.nombre == nombre_personaje:
                self.personajes.remove(personaje)
                print(f"{nombre_personaje} ha sido eliminado del equipo.")
                return
        print(f"No se encontró un personaje llamado {nombre_personaje} en el equipo.")
    
    def mostrar_equipo(self):
        print(f"Nombre de Equipo: {self.nombre_equipo}")
        for personaje in self.personajes:
            personaje.mostrar_info()
    
    def mejorar_equipo(self, aumento_nivel):
        for personaje in self.personajes:
            personaje.nivel += aumento_nivel
    
    def curar_equipo(self):
        for personaje in self.personajes:
            personaje.salud = 100
    
    def __add__(self, otro_equipo):
        nuevo_equipo = Equipo(f"{self.nombre_equipo} + {otro_equipo.nombre_equipo}")
        nuevo_equipo.personajes.extend(self.personajes + otro_equipo.personajes)
        return nuevo_equipo
