class Producto():
    def __init__(self,nombre, precio_base,stock):
        self.nombre=nombre
        self.precio_base=precio_base
        self.stock=stock

    def descuento(self, porcentaje):
        self.precio_base*=(1-porcentaje)
        print(f"nuevo precio {self.nombre} es {self.precio_base}")
    
        

    def actualizar(self,cantidad):
        if(self.stock+cantidad)<0:
            print(f"no hya suficiente")
        else:
            self.stock += cantidad
            print(f"nuevo {self.nombre} es {self.stock}")

class Categoria():
    
    listac=[]
    def __init__(self, categoria):
        self.categoria=categoria
        

    def nuevop(self,producto):
        Categoria.listac.append(producto)
        print(f"producto agregado {producto.nombre}")

    def valor(self):
        suma=0
        for m in self.listac:
            suma+=m.precio_base*m.stock
        print(f"precio total de la categoria {self.categoria} es {suma}")

class Pedido():
    def __init__ (cliente,)



        