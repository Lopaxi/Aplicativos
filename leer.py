def leerInt (cadena):
    while True:
        try:
            dato = int(input(cadena))
            return dato
        except ValueError:
            print('El valor introducido no es correccto, por favor digite un numero entero: ')  
            
            
def leerFloat (cadena):
    while True:
        try:
            dato = float (input(cadena))
            return dato
        except ValueError:
            print('El valor introducido no es correccto, por favor digite un numero real: ')              
            
            
def leerString (cadena):
    dato = input(cadena)
    return dato