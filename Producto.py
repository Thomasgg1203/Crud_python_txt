class Producto:
    def __init__(self, nom, pre, cant, ven):
        self.nombre = nom
        self.precio = pre
        self.cantidad = cant
        self.ventas = ven
    
    #gets y sets
    #nombre
    def set_nombre(self, nom) -> None:
        self.nombre = nom
    
    def get_nombre(self) -> str:
        return self.nombre
    
    #precio
    def get_precio(self) -> float:
        return self.precio
    
    def set_precio(self, pre) -> None:
        self.precio = pre

    #cantidad
    def set_cantidad(self, cant) -> None:
        self.cantidad = cant

    def get_cantidad(self) -> int:
        return self.cantidad
    
    #ventas
    def set_ventas(self, vent) -> None:
        self.ventas = vent

    def get_ventas(self) -> int:
        return self.ventas