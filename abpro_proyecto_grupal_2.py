class Proveedor:
    def __init__(self, RUT, nombre_legal, razon_social, pais, tipo_persona ) :
        self.RUT = RUT
        self.nombre_legal =nombre_legal
        self.razon_social = razon_social
        self.pais = pais
        self.tipo_persona = tipo_persona

class Producto:
    def __init__(self, SKU, nombre, categoria, proveedor, stock, valor_neto):
        self.SKU=SKU
        self.nombre=nombre
        self.categoria=categoria
        self.proveedor=proveedor
        self.stock=stock
        self.valor_neto=valor_neto
        self.__Impuesto = 1.19
        self.vendedor = []

class Cliente:
    def __init__(self, id_cliente,nombre,correo,apellido=None,fecha_registro=None):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.fecha_registro = fecha_registro
        self.saldo=0

    def agregar_saldo(self,cantidad):
        self.saldo+=cantidad
    
    def mostrar_saldo(self):
        return self.saldo

class Vendedor:
    def __init__(self, RUN, nombre, apellido, seccion):
        self.RUN =RUN
        self.nombre =nombre 
        self.apellido =apellido
        self.seccion =seccion
        self.__comision=0
        self.producto = []



    def vender(self, cantidad_vendida , producto = Producto, cliente = Cliente ):
        self.cantidad_vendida=cantidad_vendida
        if producto.stock>self.cantidad_vendida:

            self.costo_total = producto.valor_neto*self.cantidad_vendida
            self.suma = 0.5*producto.valor_neto
            

            if cliente.saldo >= self.costo_total:

                cliente.saldo = cliente.saldo-self.costo_total
                producto.stock = producto.stock-self.cantidad_vendida
                self.__comision=self.__comision + self.suma

                print(f"se vendio {self.cantidad_vendida} unidades, con un costo total de $ {self.costo_total}, tu saldo actual es ${cliente.saldo}")
            else:
                print("no es posible comprar el producto por falta de saldo")
        
        else:
            print("no existe stock de dicho producto")
    

    def __str__(self):
        return f" la comisión del vendedor fue de ${self.__comision}"
        
 

manzana = Producto(325, "manzana", "frutas", "proveedor x", 100, 100)
cliente1 = Cliente(5,"pedro","js@gfsd.com")
cliente1.agregar_saldo(100000)
vendedor_1 = Vendedor(555, "Waton", "Loyola", "5")
vendedor_1.vender(5,manzana,cliente1)
print(vendedor_1.__str__())