
from Guerrero import Guerrero
from Hechicero import Hechicero

class GuerreroHechicero(Guerrero, Hechicero):
    def __init__(self, nombre, nivel, fuerza, arma, poder_magico, conjuro, tipo_dualidad):
        Guerrero.__init__(self, nombre, nivel, fuerza, arma)
        Hechicero.__init__(self, nombre, nivel, poder_magico, conjuro)
        self.tipo_dualidad = tipo_dualidad
    
    def mostrar_info(self):
        super(Guerrero, self).mostrar_info()
        super(Hechicero, self).mostrar_info()
        print(f"Tipo de Dualidad: {self.tipo_dualidad}")
