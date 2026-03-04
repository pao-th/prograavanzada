import tkinter as tk
from PIL import Image, ImageTk


def ventanaprincipal():
    global ventana
    ventana=tk.Tk()
    ventana.title("Reino Animal")
    ventana.geometry("500x500")
    ventana.config(bg="lightgreen")

    imagen=Image.open("reinoanimal.jpg")
    imagen=imagen.resize((400,200))
    imagen_tk=ImageTk.PhotoImage(imagen)
    label_imagen=tk.Label(ventana,image=imagen_tk)
    label_imagen.pack(pady=20)

    etiqueta=tk.Label(ventana,text="REINO ANIMAL")
    etiqueta.pack()

    var=tk.IntVar()
    rad1=tk.Radiobutton(ventana,text="Elefante",variable=var,value=1)
    rad1.pack()

    rad2=tk.Radiobutton(ventana,text="Jirafa",variable=var,value=2)
    rad2.pack()

    rad3=tk.Radiobutton(ventana,text="Castor",variable=var,value=3)
    rad3.pack()

    rad4=tk.Radiobutton(ventana,text="León",variable=var,value=4)
    rad4.pack()

    def ventanas():
        variable=var.get()
        if variable==1:
            ventana_2()
        elif variable==2:
            ventana_3()
        elif variable==3:
            ventana_4()
        elif variable==4:
            ventana_5()


    boton=tk.Button(ventana,text="seleccionar",command=ventanas)
    boton.pack(pady=20)

    ventana.mainloop()



def destruirventana(ventanactual):
    ventanactual.destroy()
    ventanaprincipal()

def ventana_2():
    ventana.destroy()

    ventana2=tk.Tk()
    ventana2.title("elefante")
    ventana2.geometry("700x700")
    ventana2.config(bg="lightyellow")

    etiqueta=tk.Label(ventana2,text="ELEFANTE",bg="gray",font=("Algerian",24,"bold"))#c
    etiqueta.pack(pady=10)

    frame=tk.Frame()#c
    frame.pack(pady=20)#c

    imagen=Image.open("elefante.jpg")
    imagen=imagen.resize((400,200))
    imagen_tk=ImageTk.PhotoImage(imagen)
    label_imagen=tk.Label(frame,image=imagen_tk)
    label_imagen.grid(row=0,column=0,padx=5,pady=5)#c
    #label_imagen.pack(pady=20)

    etiqueta2=tk.Label(frame,text="Los elefantes o elefántidos son una familia de mamíferos placentarios." \
    " Y son lindos",wraplength=200,justify="left")
    etiqueta2.grid(row=0,column=1,padx=5,pady=5)
    #etiqueta2.pack()


    boton=tk.Button(ventana2,text="ventana principal", command=lambda:destruirventana(ventana2))
    boton.pack(pady=20)

    ventana2.mainloop()

def ventana_3():
    ventana.destroy()

    ventana3=tk.Tk()
    ventana3.title("jirafa")
    ventana3.geometry("500x500")
    ventana3.config(bg="lightyellow")

    etiqueta=tk.Label(ventana3,text="JIRAFA")
    etiqueta.pack()

    imagen=Image.open("jirafa.jpg")
    imagen=imagen.resize((400,200))
    imagen_tk=ImageTk.PhotoImage(imagen)
    label_imagen=tk.Label(ventana3,image=imagen_tk)
    label_imagen.pack(pady=20)

    etiqueta2=tk.Label(ventana3,text="Es la más alta de todas las especies de animales terrestres existentes")
    etiqueta2.pack()


    boton=tk.Button(ventana3,text="ventana principal", command=lambda:destruirventana(ventana3))
    boton.pack(pady=20)

    ventana3.mainloop()

def ventana_4():
    ventana.destroy()

    ventana4=tk.Tk()
    ventana4.title("castor")
    ventana4.geometry("500x500")
    ventana4.config(bg="lightyellow")

    etiqueta=tk.Label(ventana4,text="CASTOR")
    etiqueta.pack()

    imagen=Image.open("castor.jpg")
    imagen=imagen.resize((400,200))
    imagen_tk=ImageTk.PhotoImage(imagen)
    label_imagen=tk.Label(ventana4,image=imagen_tk)
    label_imagen.pack(pady=20)

    etiqueta2=tk.Label(ventana4,text="roedores semiacuáticos robustos, famosos por ser ingenieros del ecosistema")
    etiqueta2.pack()


    boton=tk.Button(ventana4,text="ventana principal", command=lambda:destruirventana(ventana4))
    boton.pack(pady=20)

    ventana4.mainloop()

def ventana_5():
    ventana.destroy()

    ventana5=tk.Tk()
    ventana5.title("leom")
    ventana5.geometry("500x500")
    ventana5.config(bg="lightyellow")

    etiqueta=tk.Label(ventana5,text="León")
    etiqueta.pack()

    imagen=Image.open("leon.jpg")
    imagen=imagen.resize((400,200))
    imagen_tk=ImageTk.PhotoImage(imagen)
    label_imagen=tk.Label(ventana5,image=imagen_tk)
    label_imagen.pack(pady=20)

    etiqueta2=tk.Label(ventana5,text="mamífero carnívoro de la familia de los félidos y una de las cinco especies del género Panthera")
    etiqueta2.pack()


    boton=tk.Button(ventana5,text="ventana principal", command=lambda:destruirventana(ventana5))
    boton.pack(pady=20)

    ventana5.mainloop()

ventanaprincipal()
