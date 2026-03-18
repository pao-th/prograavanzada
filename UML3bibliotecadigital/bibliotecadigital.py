
class Material():
    def __init__(self,idmaterial,titulo,añopublicacion,disponible:bool):
        self.idmaterial=idmaterial
        self.titulo=titulo
        self.añopublicacion=añopublicacion
        self.disponible=disponible

class Libro(Material):
    def __init__(self, idmaterial, titulo, añopublicacion, disponible,autor,ISBN,genero):
        super().__init__(idmaterial, titulo, añopublicacion, disponible)
        self.autor=autor
        self.ISBN=ISBN
        self.genero=genero

    def __str__(self):
            return (f"ID:{self.idmaterial}, "f"titulo:{self.titulo}, "f"año de publicación:{self.añopublicacion}, "f"disponible:{self.disponible}, "f"ISBN:{self.ISBN}, "f"genero:{self.genero}")
    
    __repr__=__str__

class Revista(Material):
    def __init__(self, idmaterial, titulo, añopublicacion, disponible,edicion,periocidad):
        super().__init__(idmaterial, titulo, añopublicacion, disponible)
        self.edicion=edicion
        self.periocidad=periocidad

    def __str__(self):
            return (f"ID:{self.idmaterial}, "f"titulo:{self.titulo}, "f"año de publicación:{self.añopublicacion}, "f"disponible:{self.disponible}, "f"edición:{self.edicion}, "f"periocidad:{self.periocidad}")
    
    __repr__=__str__

class Materialdigital(Material):
    def __init__(self, idmaterial, titulo, añopublicacion, disponible,tipoarchivo,urldescarga,tamañoMB):
        super().__init__(idmaterial, titulo, añopublicacion, disponible)
        self.tipoarchivo=tipoarchivo
        self.urldescarga=urldescarga
        self.tamañoMB=tamañoMB

    def __str__(self):
            return (f"ID:{self.idmaterial}, "f"título:{self.titulo}, "f"año de publicación:{self.añopublicacion}, "f"disponible:{self.disponible}, "f"tipo de archivo:{self.tipoarchivo}, "f"url:{self.urldescarga} ,"f"tamaño:{self.tamañoMB}")
    
    __repr__=__str__

class Persona():
    def __init__(self,nombre):
        self.nombre=nombre

class Usuario(Persona):
    def __init__(self,nombre,limiteprestamos,listactiva:list):
        super().__init__(nombre)
        self.limiteprestamos=limiteprestamos
        self.listactiva=listactiva

    def __str__(self):
        return (f"nombre:{self.nombre}, "f"limite de prestamos:{self.limiteprestamos}, "f"lista:{self.listactiva}")


class Bibliotecario(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def gestionarprestamo(self,us:Usuario,material:Material):
        if material.disponible and len(us.listactiva) < us.limiteprestamos:
            p=Prestamo(len(us.listactiva)+1,None,None,us,material)
            us.listactiva.append(p)
            print(f"prestamo del libro: {material.titulo} a nombre de {us.nombre} ")
            material.disponible=False
        else:
            print("libro no disponible")


    def trasnsmaterial(self,sucursaldestino:Sucursal,material:Material):
        self.sucursaldestino=sucursaldestino
        self.material=material
        sucursaldestino.catalogoprincipal.append(material)
        print(f"Transferencia del material {material.titulo} a {sucursaldestino.nombre}")

    def __str__(self):
            return (f"nombre:{self.nombre}")


class Sucursal():
    def __init__(self,idsucursal,nombre,catalagoprincipal:list[Material]):
        self.idsucursal=idsucursal
        self.nombre=nombre
        self.catalogoprincipal=catalagoprincipal

    def __str__(self):
            return (f"ID de sucursal:{self.idsucursal}, "f"nombre:{self.nombre}, "f"catalogo:{self.catalogoprincipal}")


class Prestamo():
    def __init__(self,idprestamo,fechainicio,fechadevolucion,usuario:Usuario,material:Material):
        self.idprestamo=idprestamo
        self.fechainicio=fechainicio
        self.fechadevolucion=fechadevolucion
        self.usuario=usuario
        self.material=material

    def __str__(self):
            return (f"ID:{self.idprestamo}, "f"fecha de inicio:{self.fechainicio}, "f"fecha de devolución:{self.fechadevolucion}, "f"usuario:{self.usuario}, "f"material:{self.material} ")


class Penalizacion():
    def __init__(self,monto,motivo,pagada:False):
        self.monto=monto
        self.motivo=motivo
        self.pagada=pagada

    def calcularmutlta(self,diaspendientes):
        self.monto=diaspendientes*50
        return self.monto

    def bloquearusuario(self,us:Usuario):
        us.limiteprestamos=0
        print(f"limite de prestamos alcanzados")

class Catalago():
    def __init__(self):
         pass
    
    def buscarpautor(autor,sucursales:list[Sucursal]):
        porautor=[]
        for a in sucursales:
            for b in a.catalogoprincipal:
                if isinstance(b,Libro) and b.autor==autor:
                    porautor.append(b)
        return porautor

    def buscarsucursales(titulo,sucursales:list[Sucursal]):
        ensucursales=[]
        for c in sucursales:
            for d in c.catalogoprincipal:
                if d.titulo.lower()==titulo.lower():
                    ensucursales.append(d)
        return ensucursales
    
    
