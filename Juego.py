from abc import ABC, abstractmethod

class Juego(ABC):
    @abstractmethod
    def jugar_turno(self):
        pass

    @abstractmethod
    def clear_console(self):
        pass

    @abstractmethod
    def mostrar_personajes_disponibles(self, jugador):
        pass

    @abstractmethod
    def guardar_estado(self, filename):
        pass

    @abstractmethod
    def cargar_estado(self, filename):
        pass
