import tkinter as tk
from tkinter import messagebox

def nuevo_archivo():
    messagebox.showinfo("informacion","creaste un nuevo archivo")
def abrir_archivo():
    messagebox.showinfo("informacion","abriste archivo")
def guardar_archivo():
    messagebox.showinfo("informacion","guardaste un nuevo archivo")
def cortar():
    messagebox.showinfo("informacion","cortaste")
def pegar():
    messagebox.showinfo("informacion","pegaste un texto")

ventana=tk.Tk()
ventana.title("uso de menú")
ventana.geometry("400x400")

barramenu=tk.Menu(ventana)

menu_archivo=tk.Menu(barramenu,tearoff=0)
menu_archivo.add_command(label="Nuevo",command=nuevo_archivo)
menu_archivo.add_command(label="abrir",command=abrir_archivo)
menu_archivo.add_command(label="guardar",command=guardar_archivo)

menu_edicion=tk.Menu(barramenu,tearoff=0)
menu_archivo.add_command(label="cortar",command=cortar)
menu_archivo.add_command(label="pegar",command=pegar)


barramenu.add_cascade(label="archivo", menu=menu_archivo)
barramenu.add_cascade(label="edicion", menu=menu_archivo)

ventana.confi(menu=barramenu)

ventana.mainloop()