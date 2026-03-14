from cafeteria import Cliente, Empleado,Productobase, Bebida,Postre,Pedido,Inventario


def menuempleado():
    print("1.Actualizar inventario")
    print("2.Cambiar estado pedido")
    
def menUs():
    print("1.Realizar pedido")
    print("2.Consulta historial")
    print("3.Canjear puntos")
    

bebidas=[
Bebida(13,"latte",45,"mediano",Bebida.TEMP.Caliente,["leche deslactosada"]),
Bebida(14,"expresso",45,"grande",Bebida.TEMP.Fria,[]),
Bebida(15,"americano",45,"mediano",Bebida.TEMP.Caliente,["vainilla"]),
Bebida(16,"Jugo",45,"chico",Bebida.TEMP.Fria,["azucar"]),
Bebida(17,"cappuccino",45,"mediano",Bebida.TEMP.Caliente,["nuez"]),
Bebida(18,"Té",45,"chico",Bebida.TEMP.Caliente,["miel"]),
Bebida(19,"malteada",45,"grande",Bebida.TEMP.Fria,["leche deslactosada"]),
Bebida(20,"soda",45,"mediano",Bebida.TEMP.Fria,["popote"]),
Bebida(21,"Té helado",45,"chico",Bebida.TEMP.Fria,["licor"]),
Bebida(23,"macchiato",45,"grande",Bebida.TEMP.Fria,["chocolate"]),
]
for a in bebidas:
    print(a)
bebidas[1].agregarextra("vainilla")
print(bebidas[2].calcularpreciofinal())


postres=[
Postre(34,"galleta",57,True,False),
Postre(35,"gomitas",7,True,True),
Postre(36,"pastel pequeño",72,True,False),
Postre(37,"galleta de avena",21,True,False),
Postre(38,"muffin",23,True,False),
Postre(39,"flan",43,True,True),
Postre(78,"brownie",20,True,False),
Postre(12,"tarta",21,True,False),
Postre(23,"tiramisu",10,True,False),
Postre(63,"helado",29,True,True),
]
for b in postres:
    print(b)


inventarios=[
Inventario({"vainilla":4,"azucar":2,"leche deslactpdada":1}),
Inventario({"coco":4,"azucar":3,"leche deslactosada":0}),
Inventario({"miel":4}),
Inventario({"popote":4}),
Inventario({"leche deslactosada":4}),
Inventario({"azucar":4}),
Inventario({"nuez":4}),
Inventario({"licor":4}),
Inventario({"chocolate":4}),
Inventario({"canela":4}),
]
for c in inventarios:
    print(c)
inventarios[1].reducirstock("coco",2)
inventarios[1].notificarfaltante("leche deslactosada")

pedidos=[
Pedido(12,[bebidas[0]],Pedido.ESTADO.Pendiente,16),
Pedido(13,[postres[1]],Pedido.ESTADO.Pendiente,17),
Pedido(14,[bebidas[2]],Pedido.ESTADO.Pendiente,56),
Pedido(15,[bebidas[3]],Pedido.ESTADO.Pendiente,34),
Pedido(16,[postres[4]],Pedido.ESTADO.Pendiente,79),
Pedido(17,[postres[5]],Pedido.ESTADO.Pendiente,123),
Pedido(18,[postres[6]],Pedido.ESTADO.Pendiente,57),
Pedido(19,[bebidas[7]],Pedido.ESTADO.Pendiente,135),
Pedido(20,[bebidas[8]],Pedido.ESTADO.Pendiente,75),
Pedido(21,[postres[9]],Pedido.ESTADO.Pendiente,34),
]
for d in pedidos:
    print(d)
print(pedidos[2].calculartotal())
print(pedidos[3].validarstock(inventarios[0]))

clientes=[
Cliente(212,"Fernando","fernando@gmail.com",7,None),
Cliente(213,"Alejandro","ale@gmail.com",62,None),
Cliente(214,"Roberto","robert@gmail.com",7,None),
Cliente(215,"Estela","esti@gmail.com",92,None),
Cliente(216,"Marisol","mari@gmail.com",22,None),
Cliente(217,"Maria","mar@gmail.com",12,None),
Cliente(218,"Sol","sol@gmail.com",20,None),
Cliente(219,"Ana","ana@gmail.com",20,None),
Cliente(224,"Karen","karen@gmail.com",48,None),
Cliente(865,"Pedro","pedroo@gmail.com",193,None),
]
for e in clientes:
    print(e)
clientes[0].realizarpedido(pedidos[1])
clientes[0].consultahistorial()
clientes[0].canjearpuntos(2)

empleado1=[
Empleado(12,"Juan","juan@gmail.com",Empleado.ROL.Barista),
Empleado(13,"Joseph","jo@gmail.com",Empleado.ROL.Mesero),
Empleado(14,"Jaime","jaime@gmail.com",Empleado.ROL.Barista),
Empleado(15,"Jeremy","jere@gmail.com",Empleado.ROL.Barista),
Empleado(16,"Josue","jos@gmail.com",Empleado.ROL.Mesero),
Empleado(17,"Jimena","jimena@gmail.com",Empleado.ROL.Mesero),
Empleado(18,"Josefina","jos@gmail.com",Empleado.ROL.Mesero),
Empleado(19,"Carmen","carn@gmail.com",Empleado.ROL.Gerente),
Empleado(20,"Estefania","estefi@gmail.com",Empleado.ROL.Gerente),
Empleado(11,"Liliana","lili@gmail.com",Empleado.ROL.Gerente),
]
for f in empleado1:
    print(f)
empleado1[1].actualizarinven(inventarios[1],"canela",7)
empleado1[1].cambiarestadopedido(pedidos[1],Pedido.ESTADO.Preparando)



while True:
    print("1.Usuario")
    print("2.Empleado")

    opcion=input("Selecciona una opcion")

    if opcion=="1":
        while True:
            menUs()
            opcion2=input("Seleccione 1,2 o 3")

            if opcion2=="1":
                while True:
                    print("1.Bebida" \
                    "2.Postre")
                    eleccion=input("Seleccione 1 o 2")

                    if eleccion=="1":  
                        nombre=input("nombre de bebida: ")
                        tamaño=input("tamaño:pequeño,grade,mediano")
                        temperatura=input("temperatura:Fria? si/no")
                        if temperatura=="si":
                            t=Bebida.TEMP.Fria
                        else:
                            t=Bebida.TEMP.Caliente
                        
                        while True:
                            extra=input("agregar extra o enter para no agregar extra")
                            if not extra:
                                break
                            
                            pedidobebida=Bebida(pedidos[0].idpedido,nombre,pedidos[0].total,tamaño,t,[])
                            pedidobebida.agregarextra(extra)
                            print(f"{pedidobebida}")
                        npedido=Pedido(pedidos[0].idpedido,[pedidobebida],pedidos[0].ESTADO,pedidos[0].total)
                        clientes[0].realizarpedido(npedido) 
                    elif eleccion=="2":
                        nombre=input("nombre del postre")
                        pedidopostre=Postre(postres[0].idproducto,nombre,postres[0].preciobase,postres[0].esvegano,postres[0].singluten)
                        print(f"{pedidopostre}")
                        clientes[0].realizarpedido(pedidos[0])
                    elif eleccion=="s":
                        break

            elif opcion2=="2":
                clientes[0].consultahistorial()
                
            elif opcion2=="3":
                clientes[0].canjearpuntos(4)
                    
            elif opcion2=="s":
                break
            else:
                print("Elige una de las opciones")

    elif opcion=="2":
        while True:
            menuempleado()
            opcion3=input("Seleccione 1 o 2")
            
            if opcion3=="1":
                ingrediente=input("ingrediente: ")
                cantidad=int(input("cantidad: "))
                empleado1[0].actualizarinven(inventarios[0],ingrediente,cantidad)
            elif opcion3=="2":
                estado=input("nuevo estado:")
                nuevoestado=Pedido.ESTADO[estado]
                empleado1[0].cambiarestadopedido(pedidos[0],nuevoestado)
            elif opcion3=="s":
                break
    elif opcion=="s":
        break
    else:
        print("eliga una opcion válida")
