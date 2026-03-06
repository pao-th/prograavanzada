import csv
import os

class Usuario():
    lista=[]

    ruta_csv=r"C:/Users/DELL/Downloads/DESARROLLO DE APLICACIONES/progra/pao/personas.csv"

    def __init__(self,name,age,food):
        self.nombre=name
        self.edad=age
        self.comida=food
        if self not in Usuario.lista:
            Usuario.lista.append(self)

    def mostrardatos(self):
        return f"El usuario {self.nombre} tiene {self.edad} y le gusta {self.comida}"
    
    @classmethod
    def mostrarlista(cls):
        for u in Usuario.lista:
            print(u.mostrardatos())

    @classmethod
    def guardarusuario(cls):
        campo=["nombre","edad","comida"]

        directorio=os.path.dirname(cls.ruta_csv)
        if not os.path.exists(directorio):
            try:
                os.makedirs(directorio)
                print(f"directorio creadp: {directorio}")
            except Exception as e:
                print(f"eror al crear el directorio: {e}")
                return False
        
        with open(cls.ruta_csv,"w", newline='', encoding="utf-8") as f:
            escritor=csv.DictWriter(f,fieldnames=campo, delimiter=",")
            escritor.writeheader()
            for u in cls.lista:
                escritor.writerow({"nombre": u.nombre,"edad": u.edad,"comida": u.comida})
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
            























































































