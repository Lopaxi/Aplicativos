from leer import*
from usuario import*
from recurso import*
from prestamo import*

class Central:
    def __init__(self,recursos,usuarios):
        self.recursos=recursos
        self.usuarios=usuarios
        self.nprestmo = 0
        

    def validarCodigo (self,codigo):
        for usuario in self.usuarios:
            if usuario.codigo == codigo:
                return codigo
        return None    
    
    
    def validarCodigoR (self,codigo):
        for recurso in self.recursos:
            if recurso.codigo == codigo:
                return codigo
        return None    

    def adicionarUsuario(self):
        while True:   
            print("Regitrar usuario")
            codigo = leerInt("Por favor digiite el codigo: ")
            cod = self.validarCodigo(codigo)
            if cod == None:
                print("Usted es:")
                print("1.Estudiante")
                print("2.Docente")
                print("3.Trabajador")
                op = leerInt("Digite una opcion: ")
                if op == 1:
                    nombre = leerString("Por favor digiite el nombre: ")
                    programa = leerString("Por favor digiite el programa: ")
                    usuario = Estudiante (codigo,nombre,programa)
                    self.usuarios.append(usuario)
                    print("Usuario registrado con exito")
                    print(usuario)
                    break
                elif op==2:
                    nombre = leerString("Por favor digiite el nombre: ")
                    programa = leerString("Por favor digiite el programa: ")
                    tipo = leerInt ("Elija tipo de docente 1.TC - 2.HC: ")
                    usuario = Docente (codigo,nombre,tipo,programa)
                    self.usuarios.append(usuario)
                    print("Usuario registrado con exito")
                    print(usuario)
                    break
                elif op==3:
                    nombre = leerString("Por favor digiite el nombre: ")
                    tipot = leerInt ("Elija tipo de trabajador 1.Administrativo - 2.Academico: ")
                    usuario = Trabajador (codigo,nombre,tipot)
                    self.usuarios.append(usuario)
                    print("Usuario registrado con exito")
                    print(usuario)
                    break

            else:
                print("El codigo ya existe..")    

    def eliminarUsuario (self):
        print("Eliminar usuario")
        codigo = leerInt("Digite el codigo de usuario a eliminar: ")
        usua = self.buscarUsuario(codigo)
        if usua != None:
            for i,usu in enumerate(self.usuarios):
                if usu.codigo == codigo:
                    pos= i
                    self.usuarios.pop(pos)
                    print(f"Usuario {usu.nombre} codigo : {usu.codigo} fue eliminado")
                    self.mostrarUsuarios()
        else:
            print("El usuario no existe")     


    def modificarUsuario (self):
        print("Modificar usuario")
        codigo = leerInt("Ingresa el codigo del usuario: ")
        usuario = self.buscarUsuario(codigo)
        if usuario != None:
            print(usuario)
            if isinstance (usuario,Estudiante):
                print("Que deseas modificar...")
                print ("1.Nombre")
                print ("2.Codigo")
                print ("3.Programa")
                op = leerInt("Digita una opcion: ")
                if op == 1:
                    usuario.nombre = leerString("Digita el nuevo nombre: ")
                    print("Nombre actualizado con exito")
                    print(usuario)
                elif op == 2:
                    usuario.codigo = leerInt("Digita el nuevo codigo: ")
                    print("codigo actualizado con exito")
                    print(usuario)
                
                elif op == 3:
                    usuario.programa = leerString("Digita el nuevo programa: ")
                    print("Programa actualizado con exito")
                    print(usuario)

                else:
                    print("Opcion no valida") 

            if isinstance (usuario,Docente):
                print("Que deseas modificar...")
                print ("1.Nombre")
                print ("2.Codigo")
                print ("3.Programa")
                print("4.Tipo de docente")
                op = leerInt("Digita una opcion: ")
                if op == 1:
                    usuario.nombre = leerString("Digita el nuevo nombre: ")
                    print("Nombre actualizado con exito")
                    print(usuario)
                elif op == 2:
                    usuario.codigo = leerInt("Digita el nuevo codigo: ")
                    print("codigo actualizado con exito")
                    print(usuario)
                
                elif op == 3:
                    usuario.programa = leerString("Digita el nuevo programa: ")
                    print("Programa actualizado con exito")
                    print(usuario)   
                elif op == 4:
                    usuario.tipod = leerInt("Digita el nuevo tipo de docente 1.TC / 2.HC: ")
                    print("Tipo actualizado con exito")
                    print(usuario) 
                else:
                    print("Opcion no valida")     

            if isinstance (usuario,Trabajador):
                print("Que deseas modificar...")
                print ("1.Nombre")
                print ("2.Codigo")
                print ("3.Tipo de Trabajador")
                op = leerInt("Digita una opcion: ")
                if op == 1:
                    usuario.nombre = leerString("Digita el nuevo nombre: ")
                    print("Nombre actualizado con exito")
                    print(usuario)
                elif op == 2:
                    usuario.codigo = leerInt("Digita el nuevo codigo: ")
                    print("codigo actualizado con exito")
                    print(usuario)
                  
                elif op == 3:
                    usuario.tipot = leerInt("Digita el nuevo tipo de trabajador 1.Adm / 2.Acd: ")
                    print("Tipo actualizado con exito")
                    print(usuario)                    
                
                else:
                    print("Opcion no valida")    

        else:
            print("El usuario no existe")    

               

    def ConsultarUsuario(self):
        codigo = leerInt("Digita el codigo del usuario: ")
        for usu in self.usuarios:
            if usu.codigo == codigo:
                print (usu) 
                return
        print("El ususario no existe")   


    def mostrarUsuarios (self):
        print("Mostrando Usuarios")
        for usu in self.usuarios:
            print(usu)    
        
               

    def buscarUsuario(self,codigo):
        for usu in self.usuarios:
            if usu.codigo == codigo:
                return usu
        return None    


########################################################################################################################


    def adicionarRecurso(self):
        while True:   
            print("Adicionar recurso")
            codigo = leerInt("Por favor digiite el codigo del recurso: ")
            cod = self.validarCodigoR(codigo)
            if cod == None:
                nombre = leerString("Por favor digiite el nombre del recurso: ")
                recurso = Recursos (codigo,nombre)
                self.recursos.append(recurso)
                print(f"Recurso {nombre} registrado con exito")
                break
            else:
                print("El recurso ya existe..") 


    def eliminarRecurso (self):
        print("Eliminar recurso")
        self.mostrarRecursos()
        codigo = leerInt("Digite el codigo del recurso a eliminar: ")
        recurso = self.buscarRecurso(codigo)
        if recurso != None:
            for i,rec in enumerate(self.recursos):
                if rec.codigo == codigo:
                    pos= i
                    self.recursos.pop(pos)
                    print(f"Recurso {rec.nombre} codigo : {rec.codigo} fue eliminado")
                    self.mostrarRecursos()
        else:
            print("El recurso no existe") 

    
    def modificarRecurso (self):
        print("Modificar Recurso")
        codigo = leerInt("Ingresa el codigo del recurso: ")
        recurso = self.buscarRecurso(codigo)
        if recurso != None:
            print(recurso)
            print("Que deseas modificar...")
            print ("1.Nombre")
            print ("2.Codigo")
            op = leerInt("Digita una opcion: ")
            if op == 1:
                recurso.nombre = leerString("Digite el nuevo nombre para el recurso: ")
                print("Nombre del recurso modificado con exito")
                print(recurso)
            elif op == 2:
                recurso.codigo = leerInt("Digite el nuevo codigo para el recurso: ")  
                print("Codigo del recurso modificado con exito")
                print(recurso)
            else:
                print("Opcion no valida")    
        else:
            print("El recurso no existe")
                      

    def mostrarRecursos(self):
        print("Mostrando recursos")
        for recurso in self.recursos:
            print(recurso)


    def ConsultarRecurso(self):
        codigo = leerInt("Digita el codigo del recurso: ")
        for rec in self.recursos:
            if rec.codigo == codigo:
                print (rec) 
                return
        print("El recurso no existe")            
        
    
    def buscarRecurso(self,codigo):
        for rec in self.recursos:
            if rec.codigo == codigo:
                return rec
        return None 


#########################################################################################################################


    def realizarPrestamo(self):
        print("Un saludo, vamos a realizar un prestamo")
        codigo = leerInt("Por favor digita tu codigo: ")
        usuario = self.buscarUsuario(codigo)
        if usuario != None:
            if usuario.puedePrestar() == True:
                self.mostrarRecursos()
                codigoR = leerInt("Digita el codigo del recurso: ")
                recurso = self.buscarRecurso(codigoR)
                if recurso != None:
                    if recurso.disponibilidad == "si":
                            print("Prestamo exitoso")
                            codp =self.nprestmo = self.nprestmo+1
                            prestamo = Prestamo(usuario,recurso,codp)
                            recurso.setDisponibilidad("no")
                            usuario.prestamos.append(prestamo)
                            print(prestamo)
                                
                    else:
                        print("El recurso no esta disponible")
                else:
                    print("El recurso no existe")
            else:
                print("El usuario ha excedido el limite de prestamos ")        
        else:
            print("El usuario no existe")                     

    def devolucionRecurso(self):
        print("Devolucion de recursos")
        codigo = leerInt("Por favor digita tu codigo: ")
        usuario = self.buscarUsuario(codigo)
        if usuario != None:
            usuario.mostrarPrestamos()
            codigoR = leerInt("Digita el codigo del recurso que vas a devolver: ")
            recurso = self.buscarRecurso(codigoR)
            if recurso != None:
                if recurso.disponibilidad == "no":
                        print("Devolucion exitosa")
                        recurso.setDisponibilidad("si")
                        usuario.eliminarPrestamo (recurso)
                else:
                    print("El recurso ya fue devuelto")
            else:
                print("El recurso no existe")

        else:
            print("El usuario no esta registrado")


    def consultarPrestamosUsuario (self):
        print("Consultar prestamos usuario")
        codigo = leerInt("Por favor digita tu codigo: ")
        usuario = self.buscarUsuario(codigo)
        if usuario != None:
            usuario.consultarPrestamosUsu()
        else:
            print("Usuario no resgistrado")  
            
    def consultarPrestamo (self):
        print("Consultar prestamo")
        codigo = leerInt("Por favor digita tu codigo: ")
        usuario = self.buscarUsuario(codigo)
        if usuario != None:
            codigoP = leerInt("Por favor digita  el codigo del prestamo : ")
            prest = usuario.consultar_prestamo(codigoP)
            if prest != None:
                print(prest)
            else:
                print("El prestamo no existe")    
            
        else:
            print("Usuario no resgistrado")          
           

####################################################################################################################


    def totalPrestamos (self):
        total =0
        for usu in self.usuarios:
            total+= len(usu.prestamos)
        print(f"El total de prestamos es {total}")   

    def totalPrestamosPorUsus (self):
        total =0
        for usu in self.usuarios:
            total+= len(usu.prestamos)
            print(f"El total de prestamos de {usu.nombre} es: {total}") 

    def totalPrestamosPorU (self):
        codigo = leerInt("Por favor digita tu codigo: ")
        usuario = self.buscarUsuario(codigo)
        if usuario != None:
            total = len(usuario.prestamos)
            print(f"El total de prestamos de {usuario.nombre} es: {total}")                 



    def estadoRecursou (self):
        codigo = leerInt ("codigo del recurso: ")
        recurso = self.buscarRecurso(codigo)
        if recurso!= None:
            disp = recurso.disponibilidad
            print(f"El recurso {disp} esta disponible")
        else:
            print("El recurso no esta registrado")    


     
