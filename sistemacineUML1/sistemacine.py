from enum import Enum


class Persona():
    def __init__(self,idpersona,nombre,email,telefono):
        self.idpersona=idpersona
        self.nombre=nombre
        self.email=email
        self.telefono=telefono
        
    def login(self):
        print("bienvenido")


    def logout(self):
        print("Adios")

    def actualizardatos(self,idpersona,nombre,email,telefono):
        self.idpersona=idpersona
        self.nombre=nombre
        self.email=email
        self.telefono=telefono
        print("datos actualizados")

class Usuario(Persona):
    def __init__(self,idpersona,nombre,email,telefono,puntosfidelidad=0):
        super().__init__(idpersona,nombre,email,telefono)
        self.puntosfidelidad=puntosfidelidad
        self.historialreservas=[]
    
    def creserva(self,funcion,asientos:list):
        dispo=all(a in funcion.asientoslib for a in asientos)
        if dispo:
            for a in asientos:
             funcion.asientoslib.remove(a)
            self.historialreservas.append({"funcion":funcion,"asientos":asientos})
            print(f"reserva para {funcion.pelicula.titulo} sala{funcion.sala.idespacio}, asientos{asientos}")
            return True
        else:
            print("Los asientos seleccionados estan ocupados")
            return False
    
    def consultapromo(self):
        print("Promoción de estudiante, código:10")
        print("Promoción de 3ra edad, código:20")
        print("Promoción de primavera,código=30")

    def cancelareserva(self,funcion):
        reserva=next((r for r in self.historialreservas if r["funcion"]==funcion),None)
        if reserva:
            asientosliberados = reserva["asientos"]
            for a in asientosliberados:
                funcion.asientoslib.append(a)
            self.historialreservas.remove(reserva)
            print(f"Reserva cancelada de {funcion.pelicula.titulo}")
            
        else:
            print("no tienes una todavia ninguna reserva")

    def __str__(self):
            return (f"ID:{self.idpersona}, "f"Nombre:{self.nombre}, "f"Email:{self.email}, "f"Puntos de fidelidad:{self.puntosfidelidad}")
      
class Empleado(Persona):
        ROL=Enum("Rol",["Taquillero","Limpieza","Admin"])

        def __init__(self,nombre,email,telefono,rol,idempleado,horario):
            super().__init__(idempleado,nombre,email,telefono)
            self.idempleado=idempleado
            self.rol=rol
            self.horario=horario

        def marcarentrada(self):
            print(f"{self.nombre} entrada marcada")

        def gestionarfunciones(self,funcion):
            if self.rol==Empleado.ROL.Admin:
                 print(f"funcion agregada: {funcion.pelicula.titulo} en la hora {funcion.horarioinicio} sala {funcion.sala}")
            else:
                print("no gestionas funciones")

        def __str__(self):
                return (f"Nombre:{self.nombre}, "f"email:{self.email}, "f"telefono:{self.telefono}, "f"{self.rol} "f"idempleado:{self.idempleado}, "f"horario:{self.horario}")

#infraestuctura
class Espacio():
    def __init__(self,idespacio,nombre,ubicacion):
        self.idespacio=idespacio
        self.nombre=nombre
        self.ubicacion=ubicacion

    def verificardispo(self,disponibilidad=True):
        self.disponibilidad=disponibilidad

        if self.disponibilidad:
            print("disponible")
        else:
            print("no disponible")

    def limpiarespacio(self):
        print(f"Limpiado {self.nombre}")

    def __str__(self):
            return (f"ID:{self.idespacio}, "f"nombre:{self.nombre}, "f"ubicacion:{self.ubicacion}")

class Sala(Espacio):
    TIPO=Enum("Tipo",["DosD","TresD","IMAX"])

    def __init__(self, idespacio, nombre, ubicacion,capacidadtotal,tipo,esvip=False):
        super().__init__(idespacio, nombre, ubicacion)
        self.capacidadtotal=capacidadtotal
        self.esvip=esvip
        self.tipo=tipo
        
        self.listasientos=[f"A{i}"for i in range(1,capacidadtotal +1)]

  
    def ajustaraforo(self,aforo):
        self.capacidadtotal=aforo
        
    def obtenertipoS(self):
        return self.tipo
       

class Comida(Espacio):
    def __init__(self, idespacio, nombre, ubicacion, listap:list,stockac:dict):
        super().__init__(idespacio, nombre, ubicacion)
        self.listap=listap
        self.stockac=stockac

    def venderproducto(self,producto:str):
        if producto in self.stockac and self.stockac[producto]>0:
            self.stockac[producto] -=1
            print("vendido")
        else:
            print("producto agotado")

    def actualizarinventario(self,producto:str,cantidad:int):
        self.stockac[producto]=cantidad

#3.funciones y peliculas
class Pelicula():
    def __init__(self,titulo,duracion,clasificacion,genero):
        self.titulo=titulo
        self.duracion=duracion
        self.clasificacion=clasificacion
        self.genero=genero

    def obsinopsis(self,sinopsis):
        self.sinopsis=sinopsis
        print(f"{self.titulo} Sinopsis:{self.sinopsis}")
    
    def esapta(self):#modific
        return self.clasificacion.lower() in ("todo público")
    
    def __str__(self):
        return (f"Título:{self.titulo}, "f"duración:{self.duracion}, "f"clasificación:{self.clasificacion}, "f"genero:{self.genero}")


class Funcion():
    def __init__(self,idfuncion,pelicula:Pelicula,sala:Sala,horarioinicio,preciobase):
        self.idfuncion=idfuncion
        self.pelicula=pelicula
        self.sala=sala
        self.horarioinicio=horarioinicio
        self.preciobase=preciobase

        self.asientoslib=list(sala.listasientos)

    def calcasientoslib(self,sala,asientoslib=None):
        self.asientoslib=sala.capacidadtotal if asientoslib is None else asientoslib

    def obtdetallduncion(self):
        print(f"{self.pelicula.titulo} en {self.sala.nombre} a las {self.horarioinicio}")

    def __str__(self):
            return (f"ID:{self.idfuncion}, "f"Película:{self.pelicula}, "f"sala:{self.sala}, "f"hora:{self.horarioinicio}, "f"precio:{self.preciobase}")
  
#gestion comercial

class Promocion():
    def __init__(self, codigo,descripcion,porcentaje,fexpiracion):
        self.codigo=codigo
        self.descripcion=descripcion
        self.porcentaje=porcentaje
        self.fexpiracion=fexpiracion

    def esvalida(self,usuario:Usuario)->bool:
        self.usuario=usuario
        return self.fexpiracion>0

    def aplicdescuento(self,monto):
        self.monto=monto
        return monto *(1-self.porcentaje/100)
    
    def __str__(self):
        return (f"descuento:{self.codigo}, "f"descripcion:{self.descripcion}, "f"porcentaje:{self.porcentaje}, "f"fexpiracion:{self.fexpiracion}")
  

class Reserva():
    ESTADO=Enum("Estado",["Pendiente","Pagada","Promocion"])
    def __init__(self,idreserva,usuario:Usuario,funcion:Funcion,asientos,estado, montot):
        self.idreserva=idreserva
        self.usuario=usuario
        self.funcion=funcion
        self.asientos=asientos
        self.montot=montot
        self.estado=estado

    def confpago(self):
        print(f"confirmo de pago {self.estado}")

    def genticket(self):
        print(f"tickect {self.idreserva}, {self.funcion.pelicula.titulo}, asientos:{self.asientos}, total: {self.montot}")

    def aplicpromocion(self,promocion):#modific
        if promocion.esvalida(self.usuario):
            self.montot=promocion.aplicdescuento(self.montot)
            print(f"Descuento aplicado, total: {self.montot}")

        else:
            print("promoción no valida")

    def __str__(self):
        return (f"ID:{self.idreserva}, "f"Nombre:{self.usuario}, "f"función:{self.funcion}, "f"estado:{self.estado}, "f"total:{self.montot}")
