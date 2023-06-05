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

        if movimiento > 5:
            try:
                raise ValueError("No se puede ejecutar un movimiento mayor a 5")
            
            except:
                print("Se ha asignado 5 como el valor maximo")
                print(f"El personaje avanza {5 * velocidad} celdas")

            finally:
                print("5 es el valor maximo que se le peude asignar a un personaje")

        else:
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

alfa = "abcdefghijklmnñopqrstuvwxyz"
nombre = input("Ingrese su nombre para comenzar: ")

if any(char not in alfa for char in nombre):
    try:
        print("Solo se permiten nombres con caracteres")
        raise TypeError()
    
    except:
        while any(char not in alfa for char in nombre):
            nombre = input("Ingrese su nombre para comenzar: ")

    finally:
        print("Su nombre se ha ingresado correctamente")


print("Cuantos puntos de movimiento desea utilizar?:")
player_1.avanzar(int(input()), player_1.velocidad)
player_1.atacar(10, player_1.destreza)
