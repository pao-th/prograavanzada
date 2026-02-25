import tkinter as tk
from tkinter import messagebox

def opcion():
    if var.get()==1:
        messagebox.showinfo("estado", "te gustan los tacos")
    elif var.get()==2:
        messagebox.showinfo("estado", "te gustan las chanclas")
    elif var.get()==3:
        messagebox.showinfo("estado", "te gustan las milanesas")
    elif var.get()==4:
        messagebox.showinfo("estado", "te gustam la pizza")
    else:
        messagebox.showinfo("estado", "seleccina una opcion")

   
ven2=tk.Tk()
ven2.title("uso de radio button")
ven2.geometry("400x400")
etiqueta2=tk.Label(ven2,text="¿cual es tu comida favortita?")
etiqueta2.pack(pady=20)

var=tk.IntVar()
rad1=tk.Radiobutton(ven2, text="tacos", variable=var, value=1)
rad1.pack()
rad2=tk.Radiobutton(ven2, text="chanclas", variable=var, value=2)
rad2.pack()
rad3=tk.Radiobutton(ven2, text="milanesas", variable=var, value=3)
rad3.pack()
rad4=tk.Radiobutton(ven2, text="pizza", variable=var, value=4)
rad4.pack()

boton=tk.Button(ven2,text="verificar", command=opcion)
boton.pack(pady=30)

ven2.mainloop()