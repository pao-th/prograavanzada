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
    def __init__(self, cliente,productosc):
        self.cliente=cliente
        self.productosc=productosc
        self.estado="pendiente"


    def calcular_total(self):
        sumap=sum( p.precio_base for p in self.productosc)
        iva=sumap*1.16
        return iva
    
    def finalizar_p(self):
        if self.estado== "completado":
            print("pedido completo")
            
        self.estado= "completado"
        for p in self.productosc:
            p.actualizar_stock(-1)
        print("hecho")
        
class Tienda:
    def __init__(self,nombret):
        self.nombret=nombret
        self.categorias=[]
        self.pedidosr=[]

    def rcategoria(self,categoria):
        self.categorias.append(categoria)
        print(f"categoria agregada: {categoria.nombre_categoria}")

    def greporte(self):
        total=0
        for pedido in self.pedidosr:
            if pedido.estado =="completado":
                total += pedido.calcular_total()
        print(f"ingrsos: {total.ingresos}")
        return total
    
    def productocaro(self):
        mayor= None
        for cat in self.categorias:
            for productos in cat.listap:
                if mayor is None or prod.precio_base > mayor.precio_base:
                    mayor=prod 
        
        if mayor:
            print(f"producto mas caro: {mayor.nombre} (${mayor.precio_base})")
        return mayor




        