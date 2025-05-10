#Importamos la funcion datetime para el uso de horas y fechas 
from datetime import datetime

# Esta funcion valida que la cadena no este vacia y no sean numeros
# Retorna False si el dato es correcto, True en caso contrario
def validar_cadena_caracteres(dato):
    bandera = True
    if (dato==""):
            print("\nNo ingresaste ningún caracter. Intentalo de nuevo.")
            return bandera
    else: 
        if (dato.isdigit()):
                print("\nIngresaste un caracter invalido. Intentalo de nuevo.")
                return bandera
        else:
               bandera = False
               return bandera

# Esta funcion valida que el numero entero ingresado no sea vacio y no sea menor o igual a 0 
# Retorna False si el valor es correcto, True en caso contrario
def validar_entero_mayor_0(valor):

    if (valor == ""):
         print("\nNo ingresaste ningún valor. Inténtalo de nuevo.")
         return True
    else:
        try:
            valor = int(valor)
            if (valor <= 0):
                print("\nIngresaste 0 o un valor negativo. Intentelo de nuevo")
                return True
            else:
                return False
        except ValueError:
            print("\nIngresaste un caracter invalido. Intentalo de nuevo. ")
            return True

# Esta funcion valida que el numero entero ingresado no sea vacio y no sea menor a 0
# Retorna False si el valor es correcto, True en caso contrario
def validar_entero_mayorigual_0(valor):
    bandera = True
    if (valor == ""):
        print("\nNo ingresaste ningún valor. Inténtalo de nuevo.")
        return bandera
    
    try:
        
        valor = int(valor)
        if (valor < 0):
          print("\nIngresaste un valor negativo. Intentelo de nuevo")
          return bandera
        else:
             bandera = False
             return bandera
    except ValueError:
         print("\nIngresaste un caracter invalido. Intentalo de nuevo. ")
         return bandera

# Esta funcion valida que el numero real ingresado no sea vacio y no sea menor a 0   
# Retorna False si el valor es correcto, True en caso contrario
def validar_real_mayorigual_0(valor):
    bandera = True
    if (valor == ""):
        print("\nNo ingresaste ningún valor. Inténtalo de nuevo.")
        return bandera
    
    try:
        
        valor = float(valor)
        if (valor < 0):
          print("\nIngresaste un valor negativo. Intentelo de nuevo")
          return bandera
        else:
             bandera = False
             return bandera
    except ValueError:
         print("\nIngresaste un caracter invalido. Intentalo de nuevo. ")
         return bandera

# Esta funcion valida que la fecha ingresada no este en un formato diferente el requerido
# Retorna False si la fecha es correcta, True en caso contrario
def validar_fecha(fecha):
    bandera = True
    try:
        fecha = datetime.strptime( fecha, "%Y-%m-%d")
        bandera = False
        return bandera

    except ValueError:
        print("\nIngresaste la fecha en formato incorrecto. Intentalo de nuevo")
        return bandera

# Esta funcion valida que la cadena ingresada no sea vacia
# Retorna False si el dato es correcto, True en caso contrario
def validar_no_vacio(dato):
    bandera = True
    if (dato == ""):
        print("No has ingresado ningun dato. Intentalo de nuevo.")
        return bandera
    else:
        bandera = False
        return bandera

# Esta funcion valida especificamente que la longitud de los numeros telefonicos sea igual a 10 y no se ingresen enteros menores a 0
# Retorna False si el valor es correcto, True en caso contrario
def validar_longitud(valor):

    if not(validar_entero_mayor_0(valor)):
        if (len(valor) != 10):
            print("El numero de telefono no es correcto. Intentelo de nuevo")
            return True
        else:
            return False
    else:
        print("El numero de telefono no es correcto. Intentelo de nuevo")
        return True


    
# Esta funcion valida que el identificador (ID) ingresado no sea menor a 0
# Tiene un parametro (max) que sera un contador, verificando que el ID no sea mayor al contador
# Retorna False si el dato es correcto, True en caso contrario
def validar_id(dato, max):
    
    if not(validar_entero_mayorigual_0(dato)):
        dato = int(dato)
    
        if (dato < max):
            return False
        else:
            print("Ingresaste un ID invalido. Intentalo de nuevo.")
            
            return True
    else: 
        return True
