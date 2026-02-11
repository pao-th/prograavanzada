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
    def __init__(self, categoria):
        self.categoria=categoria
        self.lista= []
        

    def nuevop(self,producto):
        self.lista.append(producto)
        print(f"producto agregado {producto.nombre}")

    def valor(self):
        suma=0
        for m in self.lista:
            suma+=m.precio_base*m.stock
        print(f"precio total de la categoria {self.categoria} es {suma}")


class Pedido():
    def __init__(self,cliente):
        self.cliente=cliente
        self.lista_comprados=[]
        self.estado="Pendiente"
    
    def agregar_producto(self,product):
        self.lista_comprados.append(product)
        print(f"Agregaste el producto {product.nombre} al carrito")
    
    def calcula_total(self):
        total=0
        for x in self.lista_comprados:
            total+=x.precio_base 
        print(f"El total de productos comprados es ${total}, el iva es ${0.16*total} y dando sumado ${1.16*total:0.2f}")
    
    def finalizar_pedido(self,listab):
        self.estado="Completado"
        for x in self.lista_comprados:
            for y in listab:
                if x.nombre==y.nombre:
                    y.stock-=1
                    print(f"El producto {y.nombre} se le quito un elemento")
