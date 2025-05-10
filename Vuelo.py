# Importamos funciones las cuales nos sirven para hacer verificacion de errores al ingreso de datos
import funciones
#Importamos la funcion datetime para el uso de horas y fechas 
from datetime import datetime 


class Vuelo:

    """
    Esta clase almacena la informacion de un vuelo que es:
    Numero de vuelo
    Ciudad de origen
    Ciudad de destino
    Costo del vuelo
    Hora de salida
    Capacidad maxima del vuelo
    Nombre del piloto
    Fecha de salida del vuelo
    Cupos del vuelo

    ATRIBUTOS
    numero_vuelo: Es el numero del vuelo, asignado de acuerdo al orden de registro, iniciando en 0
    ciudad_origen: Es la ciudad de origen del vuelo 
    ciudad_destino: Es la ciudad de destino del vuelo
    costo_vuelo: Es el costo del vuelo
    hora_salida:  Es la hora de salida del vuelo de su ciudad de origen a la ciudad de destino
    capacidad_maxima_vuelo: Es el numero maximo de cupos que tiene el vuelo
    nombre_piloto: Es el nombre del piloto del vuelo correspondiente
    fecha_salida_vuelo: Es la fecha de salida del vuelo de su ciudad de origen a su ciudad de destino
    cupos_vuelo: Hace referencia a los cupos disponibles que aun tiene el vuelo
    """
    # Atributos
    numero_vuelo = int 
    ciudad_origen = str
    ciudad_destino = str
    costo_vuelo = float
    capacidad_maxima_vuelo = int
    nombre_piloto = str
    fecha_salida_vuelo = datetime
    cupos_vuelo = int
    #Constantes
    
    ARCHIVO_VUELOS = "datos_vuelo.npy"

    # Metodo constructor de la clase
    def __init__(self, numero_vuelo =0, ciudad_origen = "", ciudad_destino = "", costo_vuelo = 0.0, capacidad_maxima_vuelo = 0, nombre_piloto = ""):
        self.numero_vuelo = numero_vuelo 
        self.ciudad_origen = ciudad_origen
        self.ciudad_destino = ciudad_destino
        self.costo_vuelo = costo_vuelo
        self.capacidad_maxima_vuelo = capacidad_maxima_vuelo
        self.nombre_piloto = nombre_piloto

    # Este metodo pide por consola los datos para el registro del vuelo
    def pedir_datos_vuelo(self):
        
        # Se pide la ciudad de origen del vuelo
        self.ciudad_origen = input("\nIngrese la ciudad de origen del vuelo: ")        
        while (funciones.validar_cadena_caracteres(self.ciudad_origen)): # Se valida la ciudad de origen del vuelo y se pide hasta que se ingrese bien
            self.ciudad_origen = input("\nIngrese la ciudad de origen del vuelo: ")

        # Se pide la ciudad de destino del vuelo
        self.ciudad_destino = input("\nIngrese la ciudad de destino del vuelo: ")    
        while (funciones.validar_cadena_caracteres(self.ciudad_destino)): # Se valida la ciudad de destino del vuelo y se pide hasta que se ingrese bien
                self.ciudad_destino = input("\nIngrese la ciudad de destino del vuelo: ")

        # Se pide la fecha de salida del vuelo
        self.fecha_salida_vuelo = input("\nIngrese la fecha de salida del vuelo (formato AÑO-MES-DIA): ")
        while(True):
            while (funciones.validar_fecha(self.fecha_salida_vuelo)):
                self.fecha_salida_vuelo = input("\nIngrese la fecha de salida del vuelo (formato AÑO-MES-DIA): ")
            self.fecha_salida_vuelo = datetime.strptime(self.fecha_salida_vuelo, "%Y-%m-%d").date()
            fecha_actual = datetime.now()
            if (self.fecha_salida_vuelo <= fecha_actual.date()):
                print("\nIngresaste una fecha de salida anterior o igual a hoy. Vuelve a intentarlo")
                self.fecha_salida = input("\nIngrese la fecha de salida del vuelo (formato AÑO-MES-DIA): ")
            else:
                break 
        
        # Se pide el costo del vuelo
        self.costo_vuelo = input("\nIngrese el costo del vuelo (SOLO ingrese punto en caso de ser decimal. No ingrese puntos de 1000 ni comas.): ")
        while (funciones.validar_real_mayorigual_0(self.costo_vuelo)):# Se valida el costo del vuelo y se pide hasta que se ingrese bien
            self.costo_vuelo = input("\nIngrese el costo del vuelo(SOLO ingrese punto en caso de ser decimal. No ingrese puntos de 1000 ni comas.): ")
        self.costo_vuelo = float(self.costo_vuelo) # Se deja el costo del vuelo convertido en tipo de dato real

        # Se pide la capacidad maxima del vuelo
        self.capacidad_maxima_vuelo = input("\nIngrese la capacidad máxima de pasajeros que puede tener el vuelo: ")
        while(funciones.validar_entero_mayor_0(self.capacidad_maxima_vuelo)): # Se valida la capacidad maxima del vuelo y se pide hasta que se ingrese bien
            self.capacidad_maxima_vuelo = input("\nIngrese la capacidad máxima de pasajeros que puede tener el vuelo: ")
        self.capacidad_maxima_vuelo = int(self.capacidad_maxima_vuelo) # Se deja la capacidad maxima del vuelo convertida en tipo de dato entero

        # Se pide el nombre del piloto del vuelo
        self.nombre_piloto = input("\nIngrese el nombre del piloto: ")
        while (funciones.validar_cadena_caracteres(self.nombre_piloto)): # Se valida el nombre del piloto y se pide hasta que se ingrese bien
            self.nombre_piloto = input("\nIngrese el nombre del piloto: ")

        # Inicialmente los cupos del vuelo es igual a la capacidad maxima del vuelo
        self.cupos_vuelo = self.capacidad_maxima_vuelo 

        


                
        










        












        
            

        

    


        
        
        



            
            
    


    
