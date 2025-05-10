# Importamos funciones las cuales nos sirven para hacer verificacion de errores al ingreso de datos
import funciones 

class Habitacion:

    """
    Esta clase almacena la informacion de una habitacion que es:
    Capacidad
    Numero
    Descripcion
    Precio por noche
    
    ATRIBUTOS
    capacidad_habitacion: Es el numero de personas que pueden ocupar la habitacion
    numero_habitacion: Es el numero de la habitacion, asignado de acuerdo al orden de registro, iniciando en 0
    descripcion_habitacion: Hace referencia a un corto texto descriptivo de la habitacion
    precio_noche_habitacion: Es el precio por noche de la habitacion

    """
    # Atributos
    capacidad_habitacion = int
    numero_habitacion = int
    descripcion_habitacion = str
    precio_noche_habitacion = float

    

    # Metodo constructor de la clase
    def __init__(self, capacidad_habitacion = 0, numero_habitacion = 0, descripcion_habitacion = "", precio_noche_habitacion = 0.0):
        self.capacidad_habitacion = capacidad_habitacion
        self.numero_habitacion = numero_habitacion
        self.descripcion_habitacion = descripcion_habitacion
        self.precio_noche_habitacion = precio_noche_habitacion
         
        
    # Este metodo pide por consola los datos para el registro de una habitacion 
    def pedir_datos_habitacion(self, i):

        # Se pide la capacidad de la habitacion
        self.capacidad_habitacion = input(f"\nIngrese la capacidad de la habitacion {i}: ")
        while (funciones.validar_entero_mayor_0(self.capacidad_habitacion)): # Se valida la capacidad de la habitacion y se pide hasta que se ingrese bien
            self.capacidad_habitacion = input(f"\nIngrese la capacidad de la habitacion {i} : ")
        self.capacidad_habitacion = int(self.capacidad_habitacion) # Se deja la capacidad de la habitacion convertida en tipo de dato entero

        # Se pide la descripcion de la habitacion
        self.descripcion_habitacion = input(f"\nIngrese la descripcion de la habitacion {i}: ")
        while (funciones.validar_cadena_caracteres(self.descripcion_habitacion)): # Se valida la descripcion de la habitacion y se pide hasta que se ingrese bien
            self.descripcion_habitacion = input(f"\nIngrese la descripcion de la habitacion {i}: ")

        # Se pide el precio por noche de la habitacion
        self.precio_noche_habitacion = input(f"\nIngrese el precio por noche de la habitacion {i} (SOLO ingrese punto en caso de ser decimal. No ingrese puntos de 1000 ni comas.): ")
        while(funciones.validar_real_mayorigual_0(self.precio_noche_habitacion)): # Se valida el precio por noche de la habitacion y se pide hasta que se ingrese bien
            self.precio_noche_habitacion = input(f"\nIngrese el precio por noche de la habitacion {i} (SOLO ingrese punto en caso de ser decimal. No ingrese puntos de 1000 ni comas.): ")
        self.precio_noche_habitacion = float(self.precio_noche_habitacion) # Se deja el precio por noche de la habitacion convertido en tipo de dato real

    


            
        


