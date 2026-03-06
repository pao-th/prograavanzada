import tkinter as tk
from backend import*
from tkinter import messagebox

def ventanaprincipal():
    ventana=tk.Tk()
    ventana.title("Login")
    ventana.geometry("400x400")

    etiqueta=tk.Label(ventana,text="nombre")
    etiqueta.pack()
    entrada=tk.Entry(ventana,width=40)
    entrada.pack(pady=15)

    etiqueta2=tk.Label(ventana,text="edad")
    etiqueta2.pack()
    entrada2=tk.Entry(ventana,width=40)
    entrada2.pack(pady=15)

    etiqueta3=tk.Label(ventana,text="comida favorita")
    etiqueta3.pack()
    entrada3=tk.Entry(ventana,width=40)
    entrada3.pack(pady=15)

    def registrar():
        name=entrada.get()
        age=entrada2.get()
        food=entrada3.get()
        newuser=Usuario(name,age,food)
        entrada.delete(0,tk.END)
        entrada2.delete(0,tk.END)
        entrada3.delete(0,tk.END)
        messagebox.showinfo("registro de usuario", "resgistro exitoo")



    boton=tk.Button(ventana,text="registrar",command=registrar)
    boton.pack(pady=15)
    def mostrar():
        Usuario.mostrarlista()

    boton2=tk.Button(ventana,text="mostarr lista",command=mostrar)
    boton2.pack(pady=15)

    def alcerrar():
        print("guardando datos")
        Usuario.guardarusuario()
        ventana.destroy()
    ventana.protocol("WM_DELETE_WINDOW",alcerrar)

 
    ventana.mainloop()

ventanaprincipal()