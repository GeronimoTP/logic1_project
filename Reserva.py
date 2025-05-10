#Importamos la funcion datetime para el uso de horas y fechas 
from datetime import datetime
# Importamos funciones las cuales nos sirven para hacer verificacion de errores al ingreso de datos
import funciones

class Reserva:

    """
    Esta clase almacena la informacion de una reserva de un paquete turistico que es:
    Titular de la reserva
    Numero de personas
    Ciudad de partida
    Ciudad de destino
    Fecha de salida
    Fecha de regreso
    Numero del vuelo de ida
    Numero del vuelo de regreso
    Nombre del hotel
    ID del hotel
    Numero de la habitacion
    ID de la reserva

    ATRIBUTOS
    titular_reserva: Es el numero de documento del cliente que hace la reserva del paquete turistico
    numero_personas: Es l numero de personas incluidos en el paquete turistico
    ciudad_partida_reserva: Es la ciudad de partida del paquete turistico
    ciudad_destino_reserva: Es la ciudad de destino del paquete turistico
    fecha_salida: Es la fecha de salida seleccionada por el cliente
    fecha_regreso: Es la fecha de regreso seleccioanada por el cliente
    numero_vuelo_ida: Es el numero del vuelo de ida seleccionado por el cliente
    numero_vuelo_vuelta: Es el numero del vuelo de vuelta seleccionado por el cliente
    nombre_hotel_reserva: Es el nombre del hotel seleccionado por el cliente
    id_hotel_reserva: Es el identificador del hotel seleccionado por el cliente
    numero_habitacion_reserva: Es el numero de la habitacion seleccionada por el cliente
    id_reserva: Es el identificador de la reserva, asignado de acuerdo al orden de registro, iniciando desde 0

    """
    #Atributos
    titular_reserva = int or str 
    numero_personas = int
    ciudad_partida_reserva = str
    ciudad_destino_reserva = str
    fecha_salida = datetime
    fecha_regreso = datetime
    numero_vuelo_ida = int
    numero_vuelo_vuelta = int
    nombre_hotel_reserva = str
    id_hotel_reserva = int
    numero_habitacion_reserva = int
    id_reserva = int
    #Constantes
    ARCHIVO_RESERVAS = "datos_reserva.npy"

    # Metodo constructor de la clase: Por defecto cada reserva tiene una persona
    def __init__(self, titular_reserva = 0, numero_personas = 1, ciudad_partida_reserva = "", ciudad_destino_reserva = "", fecha_salida = None, fecha_regreso = None, numero_vuelo_ida = 0, numero_vuelo_vuelta = 0, nombre_hotel_reserva = "", numero_habitacion_reserva = 0, id_hotel_reserva = 0, id_reserva = 0):
        self.titular_reserva = titular_reserva
        self.numero_personas = numero_personas
        self.ciudad_partida_reserva = ciudad_partida_reserva
        self.ciudad_destino_reserva = ciudad_destino_reserva
        self.fecha_salida = fecha_salida
        self.fecha_regreso = fecha_regreso
        self.numero_vuelo_ida = numero_vuelo_ida
        self.numero_vuelo_vuelta = numero_vuelo_vuelta
        self.nombre_hotel_reserva = nombre_hotel_reserva
        self.numero_habitacion_reserva = numero_habitacion_reserva
        self.id_reserva = id_reserva
        self.id_hotel_reserva = id_hotel_reserva
    
    # Este metodo pide por consola los datos para registrar una reserva
    def pedir_datos_reserva(self, cliente):
        while(True):
            try:
                # Se pide el numero de personas de la reserva
                self.numero_personas = int(input("\nIngrese el numero de personas incluidas en el paquete (de 1 a 4): "))
                if (self.numero_personas <= 0 or self.numero_personas > 4): # Se valida el numero de personas y se pide hasta que se ingrese bien
                    print("\nIngresaste un numero de personas invalido. Intentalo de nuevo. ")
                else:
                    break
            except ValueError:
                print("\nIngresaste un caracter invalido. Intentalo de nuevo.")
        
        # Se pide la ciudad de partida de la reserva
        self.ciudad_partida_reserva = input("\nIngrese la ciudad de partida: ")
        while (funciones.validar_cadena_caracteres(self.ciudad_partida_reserva)): # Se valida la ciudad de partida y se pide hasta que se ingrese bien
            self.ciudad_partida_reserva = input("\nIngrese la ciudad de partida: ")

        
        # Se pide la ciudad de destino de la reserva
        self.ciudad_destino_reserva = input("\nIngrese la ciudad de destino: ")
        while (funciones.validar_cadena_caracteres(self.ciudad_destino_reserva)): # Se valida la ciudad de destino y se pide hasta que se ingrese bien
            self.ciudad_destino_reserva = input("\nIngrese la ciudad de destino: ")
        
        # Se pide la fecha de salida de la reserva
        self.fecha_salida = input("\nIngrese la fecha de salida (formato AÑO-MES-DIA): ")
        while(True):
            while (funciones.validar_fecha(self.fecha_salida)): # Se valida la fecha de salida y se pide hasta que se ingrese bien
                self.fecha_salida = input("\nIngrese la fecha de salida (formato AÑO-MES-DIA): ")
            self.fecha_salida = datetime.strptime(self.fecha_salida, "%Y-%m-%d").date() # Se deja la fecha de salida convertida en tipo de dato date (SOLO FECHA)
            fecha_actual = datetime.now() # Se crea una variable que almacena la fecha actual
            if (self.fecha_salida <= fecha_actual.date()): # Se valida que la fecha de salida no sea menor o igual la fecha actual y se pide hasta que se ingrese bien 
                print("\nIngresaste una fecha de salida anterior o igual a hoy. Vuelve a intentarlo")
                self.fecha_salida = input("\nIngrese la fecha de salida (formato AÑO-MES-DIA): ")
            else:
                break 
        
        # Se pide la fecha de regreso de la reserva
        self.fecha_regreso = input("\nIngrese la fecha de regreso (formato AÑO-MES-DIA): ")
        while (True):
            while(funciones.validar_fecha(self.fecha_regreso)): # Se valida la fecha de regreso y se pide hasta que se ingrese bien
                self.fecha_regreso = input("\nIngrese la fecha de regreso (formato AÑO-MES-DIA): ")
            self.fecha_regreso = datetime.strptime(self.fecha_regreso, "%Y-%m-%d").date() # Se deja la fecha de regreso convetida en tipo de dato date (SOLO FECHA)
            if (self.fecha_regreso <= self.fecha_salida): # Se valida que la fecha de regreso no sea menor o igual a la fecha de salida y se pide hasta que se ingrese bien
                print("\nIngresaste una fecha incorrecta. Intentalo de nuevo. ")
                self.fecha_regreso = input("\nIngrese la fecha de llegada: ")
            else:
                break
        # Se asigna el titular de la reserva al numero de documento del cliente
        self.titular_reserva = cliente.numero_documento_usuario
        
        

        
            


            



        





