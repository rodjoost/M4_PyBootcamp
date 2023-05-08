
class True_kin:
    """Personaje utilizable por jugador en video juego"""
    def __init__(self, raza, arma, hp):
        self.raza = raza
        self.arma = arma
        self.hp = hp

    def avanzar(self, n):
        """Funcion para avanzar cantidad de celdas determinadas"""
        print(f"El personaje {self.raza} avanza {n} celdas")


class Mutante:
    """Personaje utilizable por jugador en video juego"""

    def __init__(self, raza, arma, hp):
        self.raza = raza
        self.arma = arma
        self.hp = hp

    def warcry(self, grito):
        """Funcion que produce efecto en objeto enemigo"""
        print(f"El personaje {self.raza} grita {grito} y amedrenta al enemigo")

class Enemigo:
    """Enemigo comun en video juego"""
    def __init__(self, raza, arma, hp):
        self.raza = raza
        self.arma = arma
        self.hp = hp

    def defiende(self, cantidad):
        """Funcion que resta valor al hp del enemigo cuando este es atacado"""
        self.hp = self.hp - cantidad
        print(f"El enemigo {self.raza} se defiende y queda con {self.hp} de vida")


Player_1 = True_kin("Praetorian", "Espada Larga", 120)
Player_2 = Mutante("Cyclops", "Pistola Laser", 150)
Enemigo_1 = Enemigo("Kobold", "Garrote", 90)

Player_1.avanzar(7)
Player_2.warcry("Blashyrk!")
Enemigo_1.defiende(34)
