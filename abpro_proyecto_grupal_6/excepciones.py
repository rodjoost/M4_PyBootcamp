class Errores(Exception):
    def __init__(self):
        print("No existe stock para el producto solicitado")

class Exceso(Exception):
    def __init__(self):
        print("no se venden más de 10 productos")




