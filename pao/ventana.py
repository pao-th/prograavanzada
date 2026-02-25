import tkinter as tk
from tkinter import messagebox
def estatus():
    if var.get()==1:
        messagebox.showinfo("estado", "checkbutton seleccionado")
    else:
        messagebox.showinfo("estado", "checkbutton no esta seleccionado")

ven=tk.Tk()
ven.title("VEN1")
ven.geometry("400x400")
etiqueta=tk.Label(ven,text="holaaa")
etiqueta.pack(pady=20)

var=tk.IntVar()
bcheck=tk.Checkbutton(ven,text="elegir opocion", variable=var)
bcheck.pack(pady=10)

boton1=tk.Button(ven,text="verificar estatus", command=estatus)
boton1.pack()

ven.mainloop()