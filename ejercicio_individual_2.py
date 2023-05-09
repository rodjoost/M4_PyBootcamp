
class True_kin:
    """Personaje utilizable por jugador en video juego"""
    def __init__(self, raza, arma, hp):
        self.raza = raza
        self.arma = arma
        self.hp = hp

    def avanzar(self, n):
        """Método para avanzar cantidad de celdas determinadas"""
        print(f"El personaje {self.raza} avanza {n} celdas")


class Mutante:
    """Personaje utilizable por jugador en video juego"""
    def __init__(self, raza, arma, hp):
        self.raza = raza
        self.arma = arma
        self.hp = hp

    def warcry(self, grito):
        """Método que produce efecto en objeto enemigo"""
        print(f"El personaje {self.raza} grita {grito} y amedrenta al enemigo")


class Enemigo:
    """Enemigo comun en video juego"""
    def __init__(self, raza, arma, hp):
        self.raza = raza
        self.arma = arma
        self.hp = hp

    def defiende(self, cantidad):
        """Método que resta valor al hp del enemigo cuando este es atacado"""
        print(f"El enemigo {self.raza} tiene {self.hp} de vida al comienzo del combate")
        self.hp -= cantidad
        print(f"El enemigo {self.raza} se defiende y queda con {self.hp} de vida")


class NPC:
    """Clase de personaje no jugable, quien puede entregar efectos temporales, y tener distintos nivels de afinidad con el jugador"""
    def __init__(self, clase, faccion, hp, reputacion=None):
        self.clase = clase
        self.faccion = faccion
        self.hp = hp
        self.reputacion = reputacion

    def bendicion(self, jugador, *efecto):
        """Método que da efectos temporales al jugador"""
        print(f"El {self.clase} bendice a {jugador} quien recibe {efecto}")

    def cambia_rep(self, jugador):
        """Método que cambia la afindad del NPC hacia el jugador, representado por reputación, según la clase de este"""
        print(f"Reputacion inicial de {self.clase} es {self.reputacion}")
        if type(jugador) == Mutante:
            self.reputacion -= 50
        else:
            self.reputacion += 20
        print(f"{self.clase} se encuentra con {jugador.raza}")
        print(f"La reputacion de {self.clase} cambia a {self.reputacion}")


player_1 = True_kin("Praetorian", "Espada Larga", 120)
player_2 = Mutante("Cyclops", "Pistola Laser", 150)
enemigo_1 = Enemigo("Kobold", "Garrote", 90)
npc_1 = NPC("Hermitaño", "Esper", 70, 100)

player_1.avanzar(7)
player_2.warcry("Blashyrk!")
enemigo_1.defiende(34)
npc_1.bendicion(player_1.raza, "Vigor +1", "Espíritu +1")
npc_1.cambia_rep(player_2)