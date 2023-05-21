#Librerias
import json
from tabulate import tabulate
from Producto import Producto

#funcionamiento del sistema
class Inventario:
    #------------Constructor------------
    def __init__(self, url_db):
        self.url_db = url_db
        self.productos = self.cargar_productos()

    #Metodo para leer el documento txt de forma que contenga json
    def cargar_productos(self):
        try:
            with open(self.url_db, 'r') as archivo:
                d= json.load(archivo)
                productos_j = d["productos"]
                #forma rapida de llenar la lista
                productos = [Producto(p["nombre"], p["precio"], p["cantidad"], p["ventas"]) for p in productos_j]
                return productos
        except FileNotFoundError:
            return []

    #--------------guardar los cambios--------------
    def guardar_productos(self):
        try:
            d = {
            "productos": [{
                "nombre": p.nombre,
                "precio": p.precio,
                "cantidad": p.cantidad,
                "ventas": p.ventas
            } for p in self.productos]
            }
            #forma de escribir en el archivo
            with open(self.url_db, 'w') as archivo:
                #forma de identar el codigo en el txt para que sea mas legible osea el (ident=4)
                json.dump(d, archivo, indent=4)
        except TypeError as e:
            print("productos no guardados, error: ", e)

    #-------------Metodo Adquirir---------------
    def adquirir_producto(self):
        print("Ingrese los siguientes datos: ")
        nombre = input("Nombre: ")
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: : "))

        #valida si existe
        for producto in self.productos:
            if (producto.nombre == nombre):
                producto.cantidad += cantidad
                producto.precio = precio
                break
        else:
            producto = Producto(nombre, precio, cantidad, 0)
            self.productos.append(producto)
        #
        self.guardar_productos()
        print("\nProducto adquirido correctamente\n")

    #-----------Vender productos-------------------
    def vender_producto(self):
        #Validar que los productos tengan cantidad suficiente
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad a vender: "))

        for producto in self.productos:
            if (producto.nombre == nombre):
                if (producto.cantidad >= cantidad):
                    producto.cantidad -= cantidad
                    producto.ventas += cantidad
                    self.guardar_productos()
                    print("\nVenta realizada con exito\n")
                else:
                    print("\nNo se puede realizar la venta, hay cantidad insuficiente\n")
                break
        else:
            print("El producto no existe.")

    #-----------------Mostrar productos----------------
    def mostrar_productos(self):
        filas = [[p.nombre, p.cantidad, p.precio] for p in self.productos]
        titulo_pro = ["Nombre", "Cantidad", "Precio"]
        tabla_productos = tabulate(filas, headers=titulo_pro, tablefmt="fancy_grid")
        print(tabla_productos)

    #------------------Mostrar ventas---------------------------
    def mostrar_ventas(self):
        ventas = {}
        for producto in self.productos:
            if producto.ventas > 0:
                ventas[producto.nombre] = ventas.get(producto.nombre, 0) + producto.ventas

        filas = [[nombre, cantidad] for nombre, cantidad in ventas.items()]
        titulo_venta = ["Nombre", "Cantidad"]
        tabla_ventas = tabulate(filas, headers=titulo_venta, tablefmt="fancy_grid")
        print(tabla_ventas)