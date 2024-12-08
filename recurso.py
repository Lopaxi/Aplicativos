class Recursos:
    def __init__(self,codigo,nombre):
        self.codigo=codigo
        self.nombre=nombre
        self.disponibilidad= "si"


    def __str__(self):
        return  f"codigo: {self.codigo},  nombre: {self.nombre}, disponibilidad: {self.disponibilidad}"
    

    def setDisponibilidad (self,newdis):
        self.disponibilidad = newdis

    def estadoRecurso (self):
        if self.disponibilidad == "si":
            print("El recurso esta disponible")
        else:
            print("El recurso no esta disponible")   