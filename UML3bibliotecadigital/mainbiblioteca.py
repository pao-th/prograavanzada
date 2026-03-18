from bibliotecadigital import*

libros=[
Libro(12,"Ana Frank","1947",True,"Ana Frank", 1234,"autobiografia"),
Libro(13,"Caperucita roja","1934",True,"Desconocido", 1566,"infantil"),
Libro(14,"Don Quijote de la Mancha","1924",True,"Miguel de Cervantes", 1567,"Novela"),
Libro(15,"La odisea","siglo VIII",True,"Homero", 1294,"Poema"),
Libro(16,"Cien años de soledad","1967",True,"Gabriel García", 1474,"Realismo mágico"),
Libro(17,"Orgullo y prejuicio","1813",True,"Jane Austen", 3464,"Novela romántica"),
Libro(18,"El principito","1943",True,"Antoine de Saint", 9842,"Infantil"),
Libro(19,"1984","1949",True,"George Orwell", 4234,"Ficción política"),
Libro(20,"El resplandor","1977",True,"Stephen King", 9834,"Terror psicologico"),
Libro(21,"Rayuela","1947",True,"Julio Cortazar", 0,"Surrealismo"),
]
for a in libros:
    print(a)

revistas=[
Revista(123,"Escandolos","2026",True,12,"bimestral"),
Revista(124,"National Geographic","2025",True,2,"bimestral"),
Revista(125,"Time","2025",True,6,"bimestral"),
Revista(126,"Vogue","2024",True,9,"bimestral"),
Revista(127,"Forbes","2024",True,2,"bimestral"),
Revista(128,"Muy interesante","2023",True,8,"bimestral"),
Revista(129,"The economist","2024",True,12,"bimestral"),
Revista(103,"Proceso","2025",True,11,"bimestral"),
Revista(130,"Teconología","2026",True,20,"bimestral"),
Revista(131,"Moda","2026",True,5,"bimestral"),

]
for b in revistas:
    print(b)

matdigitales=[
Materialdigital(34,"Mapa de México","2026",True,"PDF","www.mapadigital.com","34MB"),
Materialdigital(34,"Cenicienta (audiolibro)","2026",True,"PDF","www.audiolibro1.com","3MB"),
Materialdigital(34,"Amarte (audiolibro)","2025",True,"PDF","www.audiolibro2.com","4MB"),
Materialdigital(34,"Mapa de Puebla","2022",True,"PDF","www.mapadigital.com","35MB"),
Materialdigital(34,"Obesidad en México TESIS","2023",True,"PDF","www.tesis.com","37MB"),
Materialdigital(34,"Periódico Hoy","2021",True,"PDF","www.periodicosdigitales.com","20MB"),
Materialdigital(34,"Fotografías de Puebla antigua","2024",True,"PDF","www.fotografias1.com","10MB"),
Materialdigital(34,"Fotografías de México","2026",True,"PDF","www.fotografias2.com","33MB"),
Materialdigital(34,"Mapa del mundo","2025",True,"PDF","www.mapadigital.com","7MB"),
Materialdigital(34,"Revistas cientificas","2025",True,"PDF","www.revistasd.com","46MB"),

]
for c in matdigitales:
    print(c)

usuarios=[
Usuario("Juan",23,[]),
Usuario("Nancy",23,[]),
Usuario("Esteban",23,[]),
Usuario("Jose",23,[]),
Usuario("Jimena",23,[]),
Usuario("Julio",23,[]),
Usuario("Julia",23,[]),
Usuario("Julian",23,[]),
Usuario("Jorge",23,[]),
Usuario("Ximena",23,[]),

]
for d in usuarios:
    print(d)



sucursales=[
Sucursal(123,"Zona centro",[matdigitales[0],libros[0],revistas[0]]),
Sucursal(123,"La dorada",[matdigitales[1],libros[2],revistas[3]]),
Sucursal(123,"Zona Puebla",[matdigitales[3],libros[3],revistas[4]]),
Sucursal(123,"Zona Huejotzingo",[matdigitales[4],libros[7],revistas[6]]),
Sucursal(123,"Zona Cholula",[matdigitales[6],libros[6],revistas[9]]),
Sucursal(123,"En plaza comercial (El pasea)",[matdigitales[8],libros[8],revistas[8]]),
Sucursal(123,"Zona Paseo Bravo",[matdigitales[5],libros[5],revistas[5]]),
Sucursal(123,"Sucursal El Ratón",[matdigitales[7],libros[1],revistas[4]]),
Sucursal(123,"Sucursal Tlaxcala",[matdigitales[2],libros[4],revistas[2]]),
Sucursal(123,"Sucursal de Hidalgo",[matdigitales[4],libros[6],revistas[1]]),

]
for f in sucursales:
    print(f)

bibliotecarios=[
Bibliotecario("Jesus"),
Bibliotecario("Marcos"),
Bibliotecario("Miguel"),
Bibliotecario("Jazmín"),
Bibliotecario("Elisa"),
Bibliotecario("Ambesa"),
Bibliotecario("Ana"),
Bibliotecario("Alex"),
Bibliotecario("Monse"),
Bibliotecario("Emmanuel"),

]
for e in bibliotecarios:
    print(e)
bibliotecarios[1].gestionarprestamo(usuarios[2],libros[3])
bibliotecarios[2].trasnsmaterial(sucursales[3],matdigitales[3])


while True:
    print("1.Gestionar prestamos")
    print("2.Transferir material")
    print("3.Buscar por autor")
    print("4.Buscar en las sucursales")
    print("5.Penalizar")


    opcion=input("Selecciona una opcion")

    if opcion=="1":
        bibliotecarios[0].gestionarprestamo(usuarios[0],libros[0])

    elif opcion=="2":
        bibliotecarios[0].trasnsmaterial(sucursales[0],matdigitales[0])

    elif opcion=="3":
        autor=input("Escriba el nombre del autor que desea buscar")
        r=Catalago.buscarpautor(autor,sucursales)
        for x in r:
            print(x)

    elif opcion=="4":
       titulo=input("Escriba el título que desea buscar")
       re=Catalago.buscarsucursales(titulo,sucursales)
       for y in re:
           print(y)

    elif opcion=="5":
        p=Penalizacion(0,"retraso",False)
        p.calcularmutlta(12)
        p.bloquearusuario(usuarios[0])

    elif opcion=="s":
        break
    else:
        print("eliga una opcion válida")

