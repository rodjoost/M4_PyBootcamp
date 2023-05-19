class Personaje:
    """Clase parent"""
    vidas = 3
    hp = 100
    destreza = 10
    velocidad = 5


class True_kin(Personaje):
    """Clase child"""
    raza = "True Kin"
    defensa = 30

    def avanzar(self, movimiento, velocidad):
        print(f"El personaje avanza {movimiento * velocidad} celdas")


class Rango(Personaje):
    """Clase child"""
    arma = "Arco"
    dmg = 5

    def atacar(self, destreza):
        print(f"El Jugador ataca con {self.arma} y hace {self.dmg * destreza} puntos de daño")


class Jugador(True_kin, Rango):
    def atacar(self, dano, destreza):
        """Soreescritura de método"""
        print(f"El Jugador ataca con {self.arma} y hace {dano + self.dmg * destreza} puntos de daño")


player_1 = Jugador()
player_1.vidas

player_1.avanzar(7, player_1.velocidad)
player_1.atacar(10, player_1.destreza)

print(Jugador.__mro__)
