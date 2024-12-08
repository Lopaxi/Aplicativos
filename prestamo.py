from leer import*
class Prestamo:
    def __init__(self,usuario,recurso,codigo):
        self.usuario=usuario
        self.recurso=recurso
        self.codigo = codigo

    def __str__(self):
        return f"Usuario: {self.usuario.nombre}, Recurso prestado: {self.recurso.nombre}, codigo del prestamo: {self.codigo}"    
    
    
        

   