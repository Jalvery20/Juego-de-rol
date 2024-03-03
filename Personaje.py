

class Personaje:
    def __init__(self, nombre,nivel, salud, ataque):
        self.nombre = nombre
        self.nivel = nivel
        self.salud = salud
        self.ataque = ataque

    def recibir_ataque(self, ataque):
        self.salud -= ataque
        if self.salud <= 0:
            print(f"{self.nombre} ha sido derrotado!")

    def atacar(self, otro_personaje):
        print(f"{self.nombre} ataca a {otro_personaje.nombre} con {self.ataque} de daño")
        otro_personaje.recibir_ataque(self.ataque)
