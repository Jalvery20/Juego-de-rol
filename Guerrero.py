from Personaje import Personaje


class Guerrero(Personaje):
    def __init__(self, nombre, nivel, fuerza, arma):
        Personaje.__init__(self,nombre,nivel, 100, fuerza)
        self.fuerza = fuerza
        self.arma = arma
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Fuerza: {self.fuerza}, Arma: {self.arma}")
