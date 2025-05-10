# Importamos funciones las cuales nos sirven para hacer verificacion de errores al ingreso de datos
import funciones
#Importamos la clase habitacion para el uso de sus metodos y atributos
from Habitacion import Habitacion
#Importamos la funcion de arreglos 
import numpy as np
 
class Hotel:

    """
    Esta clase almacena la informacion de un hotel que es:
    ID
    Nombre 
    Ciudad
    Direccion
    Telefono
    Correo 
    Categoria
    Numero de habitaciones
    
    ATRIBUTOS
    id_hotel: Es el identificador del hotel, asignado de acuerdo al orden de registro, iniciando en 0
    nombre_hotel: Es el nombre del hotel
    ciudad_hotel: Es la ciudad de ubicacion del hotel
    direccion_hotel: Es la direccion del hotel
    telefono_hotel: Es el numero de telefono del hotel
    correo_hotel: Es el correo electronico del hotel
    categoria_hotel: Es la categoria del hotel
    numero_habitaciones: Es el numero de habitaciones del hotel
    arreglo_habitaciones: Es un arreglo que contiene las habitaciones registradas del hotel

    """


    # Atributos
    id_hotel = int
    nombre_hotel = str
    ciudad_hotel = str
    direccion_hotel = str
    telefono_hotel = int
    correo_hotel = str
    categoria_hotel = int
    numero_habitaciones = int
    arreglo_habitaciones = np.ndarray
    # Constantes
    ARCHIVO_HOTELES = "dato_hotel.npy"
    
    # Metodo constructor de la clase: Por defecto la categoria de cualquier hotel es regular
    def __init__(self, id_hotel = 0, nombre_hotel = "", ciudad_hotel = "", direccion_hotel = "", telefono_hotel = 0, correo_hotel = "", categoria_hotel = 1, numero_habitaciones = 0, arreglo_habitaciones = None):
        self.id_hotel = id_hotel
        self.nombre_hotel = nombre_hotel
        self.ciudad_hotel = ciudad_hotel
        self.direccion_hotel = direccion_hotel
        self.telefono_hotel = telefono_hotel
        self.correo_hotel = correo_hotel
        self.categoria_hotel = categoria_hotel
        self.numero_habitaciones = numero_habitaciones
        self.arreglo_habitaciones = arreglo_habitaciones



    

    # Este metodo pide por consola los datos para el registro del hotel
    def pedir_datos_hotel(self):

        # Se pide el nombre del hotel
        self.nombre_hotel = input("\nIngrese el nombre del hotel: ")
        while (funciones.validar_cadena_caracteres(self.nombre_hotel)): # Se valida el nombre del hotel y se pide hasta que se ingrese bien
            self.nombre_hotel = input("\nIngrese el nombre del hotel: ")
        
        # Se pide la ciudad del hotel
        self.ciudad_hotel = input("\nIngrese la ciudad donde esta ubicada el hotel: ")
        while (funciones.validar_cadena_caracteres(self.ciudad_hotel)): # Se valida la ciudad del hotel y se pide hasta que se ingrese bien
            self.ciudad_hotel = input("\nIngrese la ciudad donde esta ubicada el hotel: ")

        #Se pide la direccion del hotel
        self.direccion_hotel = input("\nIngrese la direccion del hotel: ")
        while (funciones.validar_cadena_caracteres(self.direccion_hotel)): # Se valida la direccion del hotel y se pide hasta que se ingrese bien
            self.direccion_hotel = input("\nIngrese la direccion del hotel: ")
        
        # Se pide el numero de telefono del hotel
        self.telefono_hotel = input("\nIngrese el telefono del hotel: ")
        while(funciones.validar_longitud(self.telefono_hotel)): # Se valida el numero de telefono del hotel y se pide hasta que se ingrese bien
            self.telefono_hotel = input("\nIngrese el telefono del hotel: ")
        self.telefono_hotel = int(self.telefono_hotel) # Se deja el numero de telefono del hotel convertido en tipo de dato entero
        
        # Se pide el correo electronico del hotel
        self.correo_hotel = input("\nIngrese el correo electronico del hotel: ")
        while (funciones.validar_cadena_caracteres(self.correo_hotel)): # Se valida el correo electronico del hotel y se pide hasta que se ingrese bien
            self.correo_hotel = input("\nIngrese el correo electronico del hotel: ")
        
        while (True):
            #Se pide la categoria del hotel
            self.categoria_hotel = (input("\nIngrese la categoria del hotel\n1. Regular\n2. Plata\n3. Oro\n4. Platino\nRespuesta: "))
            while(funciones.validar_entero_mayor_0(self.categoria_hotel)): # Se valida el numero ingresado para la categoria del hotel y se pide hasta que se ingrese bien
                self.categoria_hotel = (input("\nIngrese la categoria del hotel\n1. Regular\n2. Plata\n3. Oro\n4. Platino\nRespuesta: "))
            self.categoria_hotel = int(self.categoria_hotel)
            if (self.categoria_hotel > 4):
                print("\nIngresaste una opcion invalida. Intentalo de nuevo.")
            else:
                match(self.categoria_hotel):
                    case 1:
                        self.categoria_hotel = "Regular"
                        break
                    case 2:
                        self.categoria_hotel = "Plata"
                        break
                    case 3:
                        self.categoria_hotel = "Oro"
                        break
                    case 4:
                        self.categoria_hotel = "Platino"
                        break
                
                
                
                        
                    
           
        # Se pide el numero de habitaciones del hotel
        self.numero_habitaciones = (input("\nIngrese el numero de habitaciones que tiene el hotel: "))
        while (funciones.validar_entero_mayor_0(self.numero_habitaciones)): # Se valida el numero de habitaciones y se pide hasta que se ingrese bien
            self.numero_habitaciones = int(input("\nIngrese el numero de habitaciones que tiene el hotel: "))
        self.numero_habitaciones = int(self.numero_habitaciones) # Se deja el numero de habitaciones convertido en tipo de dato entero

        # Creo un arreglo para almacenar las habitaciones
        self.arreglo_habitaciones = np.full((self.numero_habitaciones), fill_value = None, dtype= object)
        for i in range(0, self.numero_habitaciones): # Se crean habitaciones de acuerdo al numero de habitaciones
            # Crea una habitacion nueva y pide sus datos
            habitacion = Habitacion
            habitacion = Habitacion()
            habitacion.pedir_datos_habitacion(i)
            habitacion.numero_habitacion = i # El numero de la habitacion se asigna en el orden de registro
            # Almacena la habitacion creada en el arreglo de habitaciones del hotel
            self.arreglo_habitaciones[i] = habitacion

            print("Habitacion registrada exitosamente! Recuerde que el numero de la habitacion corresponde al orden en que las registra.\nNumero Habitacion: ", i)

            if (i == self.numero_habitaciones -1):
                print("\nRegistro de habitaciones exitoso!. ")

        
            
            
        

            

                
               

            
            
        
        
        
        
        
            



        
        
    
    
