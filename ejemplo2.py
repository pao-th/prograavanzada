import tkinter as tk

def ventanaprincipal():
    global ventana
    ventana=tk.Tk()
    ventana.title("...")
    ventana.geometry("500x500")
    ventana.config(bg="lightyellow")

    etiqueta=tk.Label(ventana,text="hola")
    etiqueta.pack()

    boton=tk.Button(ventana,text="ventana2",command=ventana_2)
    boton.pack(pady=20)

    boton=tk.Button(ventana,text="ventana3",command=ventana_3)
    boton.pack(pady=20)

    boton=tk.Button(ventana,text="ventana4",command=ventana_4)
    boton.pack(pady=20)

    boton=tk.Button(ventana,text="ventana5",command=ventana_5)
    boton.pack(pady=20)

    ventana.mainloop()

def destruirventana(ventanactual):
    ventanactual.destroy()
    ventanaprincipal()

def ventana_2():
    ventana.destroy()

    ventana2=tk.Tk()
    ventana2.title("2daventana")
    ventana2.geometry("500x500")
    ventana2.config(bg="lightyellow")

    etiqueta=tk.Label(ventana2,text="2")
    etiqueta.pack()

    boton=tk.Button(ventana2,text="ventanaprincipal", command=lambda:destruirventana(ventana2))
    boton.pack(pady=20)

    ventana2.mainloop()

def ventana_3():
    ventana.destroy()

    ventana3=tk.Tk()
    ventana3.title("3raventana")
    ventana3.geometry("500x500")
    ventana3.config(bg="lightyellow")

    etiqueta=tk.Label(ventana3,text="3")
    etiqueta.pack()

    boton=tk.Button(ventana3,text="ventanaprincipal", command=lambda:destruirventana(ventana3))
    boton.pack(pady=20)

    ventana3.mainloop()

def ventana_4():
    ventana.destroy()

    ventana4=tk.Tk()
    ventana4.title("4taventana")
    ventana4.geometry("500x500")
    ventana4.config(bg="lightyellow")

    etiqueta=tk.Label(ventana4,text="4")
    etiqueta.pack()

    boton=tk.Button(ventana4,text="ventanaprincipal", command=lambda:destruirventana(ventana4))
    boton.pack(pady=20)

    ventana4.mainloop()

def ventana_5():
    ventana.destroy()

    ventana5=tk.Tk()
    ventana5.title("5taventana")
    ventana5.geometry("500x500")
    ventana5.config(bg="lightyellow")

    etiqueta=tk.Label(ventana5,text="5")
    etiqueta.pack()

    boton=tk.Button(ventana5,text="ventanaprincipal", command=lambda:destruirventana(ventana5))
    boton.pack(pady=20)

    ventana5.mainloop()

ventanaprincipal()