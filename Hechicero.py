from Personaje import Personaje

class Hechicero(Personaje):
    def __init__(self, nombre, nivel, poder_magico, conjuro):
        Personaje.__init__(self, nombre,nivel,50, poder_magico)
        self.poder_magico = poder_magico
        self.conjuro = conjuro
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Poder Mágico: {self.poder_magico}, Conjuro: {self.conjuro}")
