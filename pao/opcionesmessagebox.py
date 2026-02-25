import tkinter as tk
from tkinter import messagebox

def ventana():
    if var.get()==1:
        messagebox.showinfo("venatana de informacion", "aca puedes escribir info del usuario")
    elif var.get()==2:
        messagebox.showwarning("ventana de advertencia", "esta es una advertencia")
    elif var.get()==3:
        messagebox.showerror("ventana de error", "has cometido un error")
    elif var.get()==4:
        respuesta=messagebox.askyesno("ventana de opcion", "te gusta esta clase")
        if respuesta:
            messagebox.showinfo("ventana de respuesta","más te vale")
        else:
            messagebox.showinfo("ventana de repuesta", "por eso vas a reprobar")
    elif var.get()==5:
        respuesta=messagebox.askokcancel("ventana de opcion", "das tu alma a esta clase?")
        if respuesta:
            messagebox.showinfo("ventana de respuesta","por eso vas a sacar 10")
        else:
            messagebox.showinfo("ventana de repuesta", "por eso repruebas")
    else:
        messagebox.showinfo("ventana de respuesta", "elige una opcion")



ven3=tk.Tk()
ven3.title("tipos de messagebox")
ven3.geometry("400x400")
ven3.config(bg="lightblue")
etiqueta2=tk.Label(ven3,text="TIPOS DE MESSAGEBOX")
etiqueta2.pack(pady=20)

var=tk.IntVar()
rad1=tk.Radiobutton(ven3, text="mostrar informacion", variable=var, value=1)
rad1.pack()
rad2=tk.Radiobutton(ven3, text="advertencia", variable=var, value=2)
rad2.pack()
rad3=tk.Radiobutton(ven3, text="error", variable=var, value=3)
rad3.pack()
rad4=tk.Radiobutton(ven3, text="pregunta si o no", variable=var, value=4)
rad4.pack()
rad5=tk.Radiobutton(ven3, text="pregunta aceptar o cancelar", variable=var, value=5)
rad5.pack()

boton=tk.Button(ven3,text="verificar", command=ventana)
boton.pack(pady=30)

ven3.mainloop()