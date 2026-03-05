from sistemacine import *


def menuempleado(empleado):
    if empleado.rol==Empleado.ROL.Admin:
        print("1.Agregar funcion")
    
    print("2.Agregar promoción")
    print("3.Marcar entrada")
    
def menUs():
    print("1.inicia sesion")
    print("2.Crea reserva")
    print("3.Cancelar reserva")
    print("4.Consulta promociones")


usuariosp=[
Usuario(1234,"Roberto","roberto@gamil.com","222147597",8),
Usuario(8682,"Juan","juan@gamil.com","222134547",6),
Usuario(8572,"Pedro","pedro@gamil.com","228264597",12),
Usuario(9123,"Miguel","miguel@gamil.com","23447597",30),
Usuario(1456,"Sebastian","sebastian@gamil.com","29047597",10),
Usuario(1278,"Rodrigo","rodrigo@gamil.com","222140397",6),
Usuario(1236,"Ricardo","ricardo@gamil.com","2221097",0),
Usuario(5555,"Ramirez","ramirez@gamil.com","22107597",70),
Usuario(4444,"Daniel","daniel@gamil.com","20147597",80),
Usuario(2222,"Marcos","marcos@gamil.com","2007597",50),
]
for a in usuariosp:
    print(a)

print(usuariosp[1].login())
print(usuariosp[2].logout())
print(usuariosp[3].actualizardatos(1348,"Pedro","pedro@gmail.com", 63466874))


empleadop=[
Empleado("León","leon@gmail.com","274658697", Empleado.ROL.Taquillero,5375,"9:00-00:00"),
Empleado("Miguel","lopez@gmail.com","5688609",Empleado.ROL.Admin,2580,"7:00-22:00"),
Empleado("Lalo","leon@gmail.com","274658697", Empleado.ROL.Limpieza,5375,"9:00-00:00"),
Empleado("Esteban","leon@gmail.com","274658697", Empleado.ROL.Taquillero,5375,"9:00-00:00"),
Empleado("Moises","leon@gmail.com","274658697", Empleado.ROL.Taquillero,5375,"9:00-00:00"),
Empleado("Lazaro","leon@gmail.com","274658697", Empleado.ROL.Taquillero,5375,"9:00-00:00"),
Empleado("Pablo","leon@gmail.com","274658697", Empleado.ROL.Taquillero,5375,"9:00-00:00"),
Empleado("Pedro","leon@gmail.com","274658697", Empleado.ROL.Taquillero,5375,"9:00-00:00"),
Empleado("Juan","leon@gmail.com","274658697", Empleado.ROL.Taquillero,5375,"9:00-00:00"),
Empleado("Angel","lopez@gmail.com","5688609",Empleado.ROL.Admin,2580,"7:00-22:00"),
]

for b in empleadop:
    print(b)
print(empleadop[0].marcarentrada())

espaciop=[
Espacio(23,"Sala1","Planta baja"),
Espacio(24,"Sala2","Planta baja"),
Espacio(25,"Sala3","Planta baja"),
Espacio(26,"Sala 4","Planta baja"),
Espacio(27,"Sala5","Planta baja"),
Espacio(28,"Sala6","Primer piso"),
Espacio(29,"Sala7","Primer piso"),
Espacio(30,"Sala8","Primer piso"),
Espacio(31,"Sala9","Primer piso"),
Espacio(32,"Sala10","Primer piso"),
]
for c in espaciop:
    print(c)
print(espaciop[1].verificardispo())
print(espaciop[1].limpiarespacio())

salap=[
Sala(894,"Sala 01", "Planta baja", 50,Sala.TIPO.DosD,esvip=False),
Sala(894,"Sala 02", "Planta baja", 50,Sala.TIPO.TresD,esvip=True),
Sala(894,"Sala 03", "Planta baja", 50,Sala.TIPO.TresD,esvip=False),
Sala(894,"Sala 04", "Planta baja", 50,Sala.TIPO.TresD,esvip=False),
Sala(894,"Sala 05", "Planta baja", 50,Sala.TIPO.IMAX,esvip=False),
Sala(894,"Sala 06", "Primer piso", 50,Sala.TIPO.DosD,esvip=True),
Sala(894,"Sala 07", "Primer piso", 50,Sala.TIPO.DosD,esvip=True),
Sala(894,"Sala 08", "Primer piso", 50,Sala.TIPO.IMAX,esvip=True),
Sala(894,"Sala 09", "Primer piso", 50,Sala.TIPO.IMAX,esvip=True),
Sala(894,"Sala 10", "Primer piso", 50,Sala.TIPO.IMAX,esvip=True),
]
for d in salap:
    print(d)
print(salap[1].ajustaraforo(40))
print(salap[1].obtenertipoS())

comidap=[
Comida(12,"Bebidas","Planta baja",["Refresco","Ice mango","Ice cereza"],{"Refresco":20, "Ice mango":20,"Ice cereza":20}),
Comida(12,"Palomitas","Planta baja",["caramelo","naturales","mantequilla"],{"caramelo":20, "naturales":20,"mantequilla":20}),
Comida(12,"Helado","Planta baja",["fresa","vainilla","chocolate"],{"fresa":20, "vainilla":20,"chocolate":20}),
Comida(12,"Chicles","Planta baja",["de menta","de hiervabuena"],{"menta":20,"hiervabuena":20}),
Comida(12,"Yoghurt","Planta baja",["blanco","amargo","semiamargo"],{"blanco":20, "amargo":20,"semiamargo":20}),
Comida(12,"Papas","Planta baja",["blanco","amargo","semiamargo"],{"blanco":20, "amargo":20,"semiamargo":20}),
Comida(12,"Nachos","Planta baja",["blanco","amargo","semiamargo"],{"blanco":20, "amargo":20,"semiamargo":20}),
Comida(12,"Hotdogs","Planta baja",["blanco","amargo","semiamargo"],{"blanco":20, "amargo":20,"semiamargo":20}),
Comida(12,"Chetos","Planta baja",["blanco","amargo","semiamargo"],{"blanco":20, "amargo":20,"semiamargo":20}),
Comida(12,"Envase","Planta baja",["blanco","amargo","semiamargo"],{"blanco":20, "amargo":20,"semiamargo":20})

]
for e in comidap:
    print(e)
print(comidap[1].actualizarinventario("Refresco",0))
print(comidap[1].venderproducto("Refresco"))

peliculap=[
Pelicula("La llorona", "55 minutos", "todo público", "Ciencia ficción"),
Pelicula("Deadpool", "65 minutos", "mayores de 16", "Acción"),
Pelicula("Cenicienta", "50 minutos", "todo público", "Infantil"),
Pelicula("Blancanieves", "55 minutos", "todo público", "Infantil"),
Pelicula("El conjuro 1", "90 minutos", "mayores de 16", "Terror"),
Pelicula("El conjuro 2", "95 minutos", "mayores de 16", "Terror"),
Pelicula("Rapidos y furiosos", "90 minutos", "todo público", "Ciencia ficción"),
Pelicula("Rapidos y furiosos 2", "50 minutos", "todo público", "Ciencia ficción"),
Pelicula("Cars", "65 minutos", "todo público", "Infantil"),
Pelicula("Cars 2", "70 minutos", "todo público", "Infantil"),
]
for f in peliculap:
    print(f)
print(peliculap[0].esapta())
print(peliculap[1].esapta())
print(peliculap[0].obsinopsis("sigue a una trabajadora social en 1973 que ignora advertencias y pone a sus hijos en riesgo frente al espíritu folclórico"))

funcionp=[
Funcion(535,peliculap[0],salap[0],"4:00",200),
Funcion(535,peliculap[1],salap[1],"5:00",300),
Funcion(535,peliculap[2],salap[2],"6:30",230),
Funcion(535,peliculap[3],salap[3],"1:00",180),
Funcion(535,peliculap[4],salap[4],"4:00",400),
Funcion(535,peliculap[5],salap[5],"10:00",300),
Funcion(535,peliculap[6],salap[6],"20:00",890),
Funcion(535,peliculap[7],salap[7],"22:00",230),
Funcion(535,peliculap[8],salap[8],"23:00",532),
Funcion(535,peliculap[9],salap[9],"22:10",237)
]
for g in funcionp:
    print(g)
print(funcionp[1].calcasientoslib(1,20))
print(funcionp[1].obtdetallduncion())

promocionp=[
Promocion(10,"Estudiante",10,30),
Promocion(20,"3ra edad",10,30),
Promocion(30,"Primavera",10,30),
Promocion(40,"Día de la mujer",10,30),
Promocion(50,"Día de las madres",10,30),
Promocion(60,"San Valentin",10,30),
Promocion(70,"Verano",10,30),
Promocion(80,"Invierno",10,30),
Promocion(90,"Promo de jueves",10,30),
Promocion(95,"",10,30)
]
for j in promocionp:
    print(j)
print(promocionp[0].aplicdescuento(400))
print(promocionp[0].esvalida(usuariosp[0]))

reservap=[
Reserva(589,usuariosp[1], funcionp[0],2,Reserva.ESTADO.Pagada,funcionp[0].preciobase*2),
Reserva(559,usuariosp[0], funcionp[1],4,Reserva.ESTADO.Pendiente,funcionp[1].preciobase*4),
Reserva(539,usuariosp[2], funcionp[2],3,Reserva.ESTADO.Pagada,funcionp[2].preciobase*3),
Reserva(129,usuariosp[3], funcionp[3],9,Reserva.ESTADO.Promocion,funcionp[3].preciobase*9),
Reserva(873,usuariosp[4], funcionp[4],6,Reserva.ESTADO.Pendiente,funcionp[4].preciobase*6),
Reserva(987,usuariosp[5], funcionp[5],4,Reserva.ESTADO.Pagada,funcionp[5].preciobase*4),
Reserva(543,usuariosp[6], funcionp[6],7,Reserva.ESTADO.Promocion,funcionp[6].preciobase*7),
Reserva(0,usuariosp[7], funcionp[7],3,Reserva.ESTADO.Pagada,funcionp[7].preciobase*3),
Reserva(523,usuariosp[8], funcionp[8],1,Reserva.ESTADO.Pendiente,funcionp[8].preciobase*8),
Reserva(523,usuariosp[9], funcionp[9],5,Reserva.ESTADO.Pagada,funcionp[9].preciobase*5),

]
for k in reservap:
    print(k)
print(reservap[0].aplicpromocion(promocionp[0]))
print(reservap[0].confpago())
print(reservap[0].genticket())


while True:
    print("1.Usuario")
    print("2.Empleado")
    print("3.Administrador")
    opcion=input("Selecciona una opcion")

    if opcion=="1":
        while True:
            menUs()
            opcion2=input("Seleccione 1,2,3 o 4")

            if opcion2=="1":
                usuariosp[1].login()
            elif opcion2=="2":
                
                asiento=(input("¿Qué asientos desea?(escriba con comas)"))
                asientoe=(asiento.split(","))
                si=usuariosp[1].creserva(funcionp[0], asientoe)
                if si:
                    cantidad=len(asientoe)
                    reserva1=Reserva(589,usuariosp[1], funcionp[0],asiento,Reserva.ESTADO.Pagada,funcionp[0].preciobase*cantidad)
                    reserva1.genticket()#ag
                    reserva1.confpago()#ag
                else:
                    print("no se puede generar ticket  con asientos ocupados")

            elif opcion2=="3":
                usuariosp[1].cancelareserva(funcionp[0])
                reserva1=None

            elif opcion2=="4":
                usuariosp[1].consultapromo()
                cod=input("ingrese el codigo de descuento")
                if cod=="10" and promocionp[0].esvalida:
                    promo=promocionp[0]
                    reserva1.aplicpromocion(promo)
                else:
                    print("Código no válido o la fecha de la promoción ya expiró")
                    
            elif opcion2=="s":
                break
            else:
                print("Elige una de las opciones")

    elif opcion=="2":
        emplead=empleadop[0]
        while True:
            menuempleado(emplead)
            opcion3=input("Seleccione 2 o 3")
            if opcion3=="2":
                codigo=input("Escriba el código")
                descripcion=input("Escriba la descripcion)")
                porcen=input("Solo escriba el número del porcentaje")
                fecha=input("Escriba fecha (solo un número)")
                npromo=Promocion(codigo, descripcion,porcen, fecha)
                print(f"Listo, descuento con código: {codigo} agregado, {npromo}")
                
            elif opcion3=="3":
                emplead.marcarentrada()
            elif opcion3=="s":
                break

    elif opcion=="3":
        empleado=empleadop[1]
        while True:
            menuempleado(empleado)
            opcion3=input("Selecciona 1,2,3")
            if opcion3=="1":
                if empleado.rol==Empleado.ROL.Admin:
                    empleado.gestionarfunciones(funcionp[0])
                else:
                    print("Esta opción no es válida para usted")
            elif opcion3=="2":
                codigo=input("Escriba el código")
                descripcion=input("Escriba la descripción")
                porcen=input("Solo escriba el número del porcentaje")
                fecha=input("Escriba fecha (solo un número)")
                npromo=Promocion(codigo, descripcion,porcen, fecha)
                print(f"Listo {npromo}")
            elif opcion3=="3":
                empleado.marcarentrada()
            elif opcion3=="s":
                break

    elif opcion=="s":
        break
    else:
        print("eliga una opcion válida")


    
