from abc import ABC,abstractmethod


class Usuario(ABC):
    def __init__(self,codigo,nombre):
        self.codigo=codigo
        self.nombre=nombre
        self.prestamos = []

    
    def __str__ (self):
        return f"Codigo: {self.codigo} Nombre: {self.nombre} Tipo: {self.tipo}"

    @abstractmethod
    def puedePrestar (self):
        pass

    @abstractmethod
    def eliminarPrestamo(self,codigo):
        pass
    @abstractmethod    
    def consultarPrestamosUsu(self):
        pass
    @abstractmethod 
    def mostrarPrestamos(self):
        pass
    
    @abstractmethod 
    def consultar_prestamo(self):
        pass
          

class Estudiante(Usuario):
    def __init__ (self,codigo,nombre,programa):
        super().__init__(codigo,nombre)
        self.programa = programa
        #nmaximoPrestamos = 0

    def __str__(self):
        return f"Codigo: {self.codigo}, nombre: {self.nombre} programa: {self.programa}"
    
    def puedePrestar (self):
        return True
    
    def eliminarPrestamo(self,recurso):
        for i, prest in enumerate (self.prestamos):
            if prest.recurso.codigo == recurso.codigo:
                pos = i
            self.prestamos.pop(pos)

    def consultarPrestamosUsu(self):
        if len (self.prestamos)>0:
            for prestamo in self.prestamos:
                print (prestamo) 
        else:
            print("El usuario no tiene prestamos")      
            
    def consultar_prestamo(self,codigoP):
        if len (self.prestamos)>0:
            for prestamo in self.prestamos:
                if prestamo.codigo == codigoP:
                    return prestamo
            return None
        else:
            print("El usuario no tiene prestamos")            

    
    def mostrarPrestamos(self):
        for prestamo in self.prestamos:
            print(f"Recurso: {prestamo.recurso.nombre}, Codigo: {prestamo.recurso.codigo} ")


class Docente(Usuario):
    def __init__ (self,codigo,nombre,tipod,programa):
        super().__init__(codigo,nombre)
        self.programa = programa
        self.tipod = tipod
        if self.tipod ==1:
            self.maximoPrestamos = 4
        elif self.tipod == 2:
            self.maximoPrestamos = 2    

    def __str__(self):
        return f"Codigo: {self.codigo}, nombre: {self.nombre} Tipo:{self.tipod} programa: {self.programa}"    
    
    def puedePrestar (self):
        if len (self.prestamos)<self.maximoPrestamos:
            return True
        else:
            return False
        
    def eliminarPrestamo(self,recurso):
        for i, prest in enumerate (self.prestamos):
            if prest.recurso.codigo == recurso.codigo:
                pos = i
            self.prestamos.pop(pos)

    def consultarPrestamosUsu(self):
        if len (self.prestamos)>0:
            for prestamo in self.prestamos:
                print (prestamo) 
        else:
            print("El usuario no tiene prestamos")       
    
    def consultar_prestamo(self,codigoP):
        if len (self.prestamos)>0:
            for prestamo in self.prestamos:
                if prestamo.codigo == codigoP:
                    return prestamo
            return None
        else:
            print("El usuario no tiene prestamos")               
    
    def mostrarPrestamos(self):
        for prestamo in self.prestamos:
            print(f"Recurso: {prestamo.recurso.nombre}, Codigo: {prestamo.recurso.codigo} ")
        

class Trabajador(Usuario):
    def __init__ (self,codigo,nombre,tipot):
        super().__init__(codigo,nombre)
        self.tipot = tipot
        self.maximoPrestamos = 2

    def __str__(self):
        return f"Codigo: {self.codigo}, nombre: {self.nombre} Tipo:{self.tipot}"  
    
    def puedePrestar (self):
        if len (self.prestamos)<self.maximoPrestamos:
            return True
        else:
            return False
        
    def eliminarPrestamo(self,recurso):
        for i, prest in enumerate (self.prestamos):
            if prest.recurso.codigo == recurso.codigo:
                pos = i
            self.prestamos.pop(pos)

    def consultarPrestamosUsu(self):
        if len (self.prestamos)>0:
            for prestamo in self.prestamos:
                print (prestamo) 
        else:
            print("El usuario no tiene prestamos")       
            
    def consultar_prestamo(self,codigoP):
        if len (self.prestamos)>0:
            for prestamo in self.prestamos:
                if prestamo.codigo == codigoP:
                    return prestamo
            return None
        else:
            print("El usuario no tiene prestamos")            
            
    def mostrarPrestamos(self):
        for prestamo in self.prestamos:
            print(f"Recurso: {prestamo.recurso.nombre}, Codigo: {prestamo.recurso.codigo} ")
        