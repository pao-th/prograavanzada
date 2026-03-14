from enum import Enum

class Persona():
    def __init__(self,idpersona,nombre,email):
        self.idpersona=idpersona
        self.nombre=nombre
        self.email=email
    
    def login(self):
        return f"bienvenido {self.nombre}"

    def actualizardatos(self,nombre,email):
        self.nombre=nombre
        self.email=email

class Cliente(Persona):
    def __init__(self, idpersona, nombre, email,puntosfidelidad=0,historialpedido=None):
        super().__init__(idpersona, nombre, email)
        self.puntosfidelidad=puntosfidelidad
        if historialpedido is None:
            self.historialpedido=[]
        else:
            self.historialpedido=historialpedido

    def realizarpedido(self,pedido:'Pedido'):
        self.historialpedido.append(pedido)
        print(f"pedido de {self.nombre} con ID:{pedido.idpedido}")

    def consultahistorial(self):
        print(f"{self.historialpedido}")

    def canjearpuntos(self,puntos):
        if puntos <= self.puntosfidelidad:
            self.puntosfidelidad -= puntos
            print(f"puntos de fidelidad ahora:{self.puntosfidelidad}")
        else:
            print("Puntos insuficientes")

    def __str__(self):
            return (f"ID:{self.idpersona}, "f"nombre:{self.nombre}, "f"email:{self.email}, "f"puntos:{self.puntosfidelidad}, "f"historial:{self.historialpedido} ")


class Empleado(Persona):
    ROL=Enum("Rol",["Barista","Mesero","Gerente"])

    def __init__(self, idempleado, nombre, email,rol):
        super().__init__(idempleado, nombre, email)
        self.idempleado=idempleado
        self.rol=Empleado.ROL(rol)

    def actualizarinven(self,invent,ingrediente,cantidad):
        invent.ingredientes[ingrediente]=invent.ingredientes.get(ingrediente,0)+cantidad
        print(f"Inventario actualizado {ingrediente}= {invent.ingredientes[ingrediente]}")


    def cambiarestadopedido(self,pedido:'Pedido',estado:'Pedido.ESTADO'):
        pedido.estado=estado
        print(f"Pedido {pedido.idpedido} cambia a estado {pedido.estado}")

    def __str__(self):
            return (f"ID:{self.idempleado}, "f"nombre:{self.nombre}, "f"email:{self.email}")

class Productobase():
    def __init__(self,idproducto,nombre,preciobase):
        self.idproducto=idproducto
        self.nombre=nombre
        self.preciobase=preciobase

class Bebida(Productobase):
    TEMP=Enum("Temperatura",["Fria","Caliente"])

    def __init__(self, idproducto, nombre, preciobase,tamaño,temperatura,modificadores):
        super().__init__(idproducto, nombre, preciobase)
        self.tamaño=tamaño
        self.temperatura=Bebida.TEMP(temperatura)
        self.modificadores=modificadores
    
    def agregarextra(self,extra):
        self.modificadores.append(extra)
        print(f"{self.modificadores}")

    def calcularpreciofinal(self):
        return self.preciobase+(0.5*len(self.modificadores))
    
    def __str__(self):
            extras=" ".join(self.modificadores) if self.modificadores else "sin extras"
            return (f"ID:{self.idproducto}, "f"nombre:{self.nombre}, "f"precio base:{self.preciobase}, "f"tamaño:{self.tamaño}, "f"{self.temperatura}, "f"modificador:{extras}")

class Postre(Productobase):
    def __init__(self, idproducto, nombre, preciobase,esvegano=False,singluten=False):
        super().__init__(idproducto, nombre, preciobase)
        self.esvegano=esvegano
        self.singluten=singluten

    def __str__(self):
            return (f"ID:{self.idproducto}, "f"nombre:{self.nombre}, "f"precio base:{self.preciobase}, "f"vegano:{self.esvegano}, "f"gluten: {self.singluten}")


class Pedido():
    ESTADO=Enum("ESTADO",["Pendiente","Preparando","Entregado"])

    def __init__(self,idpedido,productos,estado,total):
        self.idpedido=idpedido
        self.productos=productos
        self.estado=estado
        self.total=total

    def calculartotal(self):
        total=0

        for producto in self.productos:
            if isinstance(producto,Bebida):
                total += producto.calcularpreciofinal()
            else:
                total+=producto.preciobase
        self.total=total
        return total
    
    def validarstock(self,inventario):
        for producto in self.productos:
            if isinstance(producto,Bebida):
                for extra in producto.modificadores:
                    if inventario.ingredientes.get(extra,0) <=0:
                        inventario.notificarfaltante(extra)
                        return False
        return True
    def __str__(self):
            nproductos=" ".join([p.nombre for p in self.productos])
            return (f"ID:{self.idpedido}, "f"producto:{nproductos}, "f"estado:{self.estado}, "f"total:{self.total} ")
    __repr__=__str__

class Inventario():
    def __init__(self,ingredientes=None):
        if ingredientes is None:
            ingredientes={}
        self.ingredientes=ingredientes

    def reducirstock(self,ingrediente,cantidad):
        if self.ingredientes.get(ingrediente,0)>=cantidad:
                self.ingredientes[ingrediente]-=cantidad
        else:
                self.notificarfaltante(ingrediente)


    def notificarfaltante(self,ingrediente):
        print(f"falta el ingrediente {ingrediente}")

    def __str__(self):
            return (f"ingredientes:{self.ingredientes}")

