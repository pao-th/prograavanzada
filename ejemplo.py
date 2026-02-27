import tkinter as tk

root=tk.Tk()
root.title("ejemplo de grid")
root.geometry("500x200")
root.config(bg="blue")

etiqueta=tk.Label(root,text="Nombre: ",bg="blue",fg="white",font=("Arial",16,"bold"))
etiqueta.grid(row=0,column=0,padx=5, pady=5,sticky="w")
entrada=tk.Entry(root,width=60)
entrada.grid(row=0,column=1,padx=5,pady=5)

tk.Label(root,text="correo").grid(row=1,column=0,padx=5,pady=5,sticky="w")
entrada2=tk.Entry(root,width=45)
entrada2.grid(row=1,column=1,padx=5,pady=5,sticky="w")

tk.Button(root,text="enciar").grid(row=2,column=0,columnspan=2,pady=10)

root.mainloop()