# Keiner castillo cod: 224034048 & Manuel Castillo cod: 224034077



from leer import *
from programaPrincipal import*
from central import *
import pickle

central = Central([],[])

def grabarArchSerializable(central):
    archivo=open("archivoSerializable","wb")
    pickle.dump(central,archivo)
    archivo.close()
    print("Archivo grabado correctamente")

def leerArchSerializable():
    try:
        archivo=open("archivoSerializable","rb")
        central=pickle.load(archivo) 
        archivo.close()
        print("Archivo leido correctamente")
        return central
    except FileNotFoundError:
        print("El archvio no fue encontrado por favor cree una central")
        return Central ([],[])


def menuPrincipal():
    central=leerArchSerializable()
    while True:
        print("Bienvendio al menu Principal")
        print("----------------------------")
        print("1.Manejo de usuarios")
        print("2.Manejo de recursos")
        print("3.Manejo de prestamos y devoluciones")
        print("4.Menu informes")
        print("5.Salir")
        

        op=leerInt("Dijite una opcion: -> ")
        if op==1:
            menuManejoUsuarios(central)
        elif op==2:
            menuManejoRecursos(central)
        elif op==3:
            menuMnejoPrestamosyDev(central)

        elif op ==4: 
            menuInformes(central)
        
        elif op==5:
            grabarArchSerializable(central)
            print("Hasta Luego")
            break

        else:
            print("dijite una opcion valida") 

       

def menuManejoRecursos(central):
    while True:
        print("Menu manejo de recursos")
        print("----------------------------")
        print("1.Adicionar recurso")
        print("2.Modificar recurso")
        print("3.Eliminar recurso")
        print("4.Consultar recurso")
        print("5.Volver al menu principal")

        op=leerInt("Dijite una opcion: -> ")
        if op==1:
            central.adicionarRecurso()
            pass
        elif op==2:
            central.modificarRecurso()
        
        elif op==3:
            central.eliminarRecurso()

        elif op==4:
            central.ConsultarRecurso()

        elif op==5:
            print("Volver al menu principal")
            break
        else:
            print("dijite una opcion valida")
                

def menuManejoUsuarios(central):
    while True:
        print("Menu manejo de recursos")
        print("----------------------------")
        print("1.Adicionar usuario")
        print("2.Eliminarr usuario")
        print("3.Consultar usuario")
        print("4.Modificar usuario")
        print("5.Volver al menu principal")

        op=leerInt("Dijite una opcion: -> ")
        if op==1:
            central.adicionarUsuario()
            
        elif op==2:
            central.eliminarUsuario()
           
        elif op==3:
             central.ConsultarUsuario()
        
        elif op==4:
             central.modificarUsuario()

        elif op==5:
            print("Hasta Luego")
            break
            
        else:
            print("dijite una opcion valida")

def menuMnejoPrestamosyDev(central):
    while True:
        print("Menu manejo de prestamos y devoluciones")
        print("----------------------------")
        print("1.Realizar prestamo")
        print("2.Consultar prestamo")
        print("3.Realizar devolución")
        print("4.Consultar prestamos usuarios")
        print("5.Volver al menu principal")

        op=leerInt("Dijite una opcion: -> ")
        if op==1:
            central.realizarPrestamo()
            
        elif op==2:
            central.consultarPrestamo()
            
        elif op==3:
            central.devolucionRecurso()
            

        elif op==4:
            central.consultarPrestamosUsuario()

        elif op==5:
            print("Hasta Luego")
            break
        else:
            print("dijite una opcion valida")

def menuInformes(central):  
    while True:
        print("Menu informes")
        print("----------------------------")
        print("1.Total prestamos")
        print("2.Total prestamos por usuario")
        print("3.Estado de un recurso")
        print("4.Volver al menu principal")

        op=leerInt("Dijite una opcion: -> ")
        if op==1:
            central.totalPrestamos()
            
        elif op==2:
            central.totalPrestamosPorU()
            
        elif op==3:
            central.estadoRecursou()
                
        elif op==4:
            print("Hasta Luego")
            break
        else:
            print("dijite una opcion valida")      

def main():
    menuPrincipal()

if __name__ == '__main__' :
    main()
