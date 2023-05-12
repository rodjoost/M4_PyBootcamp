from excepciones import Errores
from excepciones import Exceso


class Proveedor:
    def __init__(self, RUT, nombre_legal, razon_social, pais, tipo_persona ) :
        self.RUT = RUT
        self.nombre_legal =nombre_legal
        self.razon_social = razon_social
        self.pais = pais
        self.tipo_persona = tipo_persona


class Bodega:
    def __init__(self, stock):
        self.stock = stock
        
        
class Producto:
    def __init__(self, SKU, nombre, categoria, proveedor, stock, valor_neto):
        self.SKU=SKU
        self.nombre=nombre
        self.categoria=categoria
        self.proveedor=proveedor
        self.stock=stock
        self.valor_neto=valor_neto
        self.vendedor = []


class Sucursal(Bodega):
    def __init__(self, stock_sucursal,bodega):
        super().__init__(bodega.stock)
        self.stock_sucursal = stock_sucursal

    def reponer_stock(self):
        if self.stock_sucursal < 50:
            print("Se esta solicitando y reponiendo productos")
            if self.stock >= 300:
                self.stock -= 300
                self.stock_sucursal += 300
                bodega.stock = self.stock
            else:
              #  open("excepciones.py") 

                print("No hay suficiente stock para reponer")


class Orden_de_compra:
    def __init__(self, id_ordencompra, despacho, producto):
        self.ID_ordencompra = id_ordencompra
        self.producto = producto
        self.despacho = despacho

        if self.despacho:
            self.cargo_despacho = 5000
        else:
            self.cargo_despacho = 0
        
    def detalle(self):
        valor_neto=self.producto.valor_neto
        impuesto=self.producto.valor_neto*0.19
        total=valor_neto+impuesto+self.cargo_despacho
        return total


        

class Cliente:
    def __init__(self, id_cliente,nombre,correo,apellido=None,fecha_registro=None):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.fecha_registro = fecha_registro
        self.saldo=0

    def agregar_saldo(self,cantidad):
        try:
            if cantidad < 0:
                raise ValueError("La cantidad debe ser un número positivo")
            self.saldo+=cantidad

        except ValueError as e:
            print(e)
    
    
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
        try:
            if cantidad_vendida>10:
                raise Exceso
        except Exceso as e:
            e

    
        try:
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
                raise Errores
        except Errores as e:
            e


    

    def __str__(self):
        return f" la comisión del vendedor fue de ${self.__comision}"
        
 
bodega = Bodega(350)
sucursal1 = Sucursal(49, bodega)
manzana = Producto(325, "manzana", "frutas", "proveedor x", 100, 100)
cliente1 = Cliente(5,"pedro","js@gfsd.com")
cliente1.agregar_saldo(100000)
vendedor_1 = Vendedor(555, "Waton", "Loyola", "5")
vendedor_1.vender(350, manzana, cliente1)
print(vendedor_1.__str__())
sucursal1.reponer_stock()
print(sucursal1.stock)  # Imprime el stock restante en la bodega
print(sucursal1.stock_sucursal)  #Imprime el stock actualizado de sucursal
orden = Orden_de_compra(1, True, manzana)
print(orden.detalle())
