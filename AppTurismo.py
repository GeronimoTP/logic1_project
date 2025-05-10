#Importamos la funcion de arreglos
import numpy as np
# Importamos funciones las cuales nos sirven para hacer verificacion de errores al ingreso de datos
import funciones
#Importamos la clase Usuario para el uso de sus metodos y atributos
from Usuario import Usuario
#Importamos la clase Hotel para el uso de sus metodos y atributos
from Hotel import Hotel
#Importamos la clase Habitacion para el uso de sus metodos y atributos
from Habitacion import Habitacion 
#Importamos la clase Reserva para el uso de sus metodos y atributos
from Reserva import Reserva
#Importamos la clase Vuelo para el uso de sus metodos y atributos
from Vuelo import Vuelo
#Importamos la funcion datetime para el uso de horas y fechas 
from datetime import datetime
import os


class AppTurismo:
    """"
    Esta es la clase principal, la que hace las veces del programa y la que provee la interfaz de usuario.

    ATRIBUTOS
    cont_usuarios: Contador de que indica cuantos usuarios se han registrado en el sistema
    cont_hoteles: Contador que indica cuantos hoteles se han registrado en el sistema
    cont_vuelos: Contador que indica cuantos vuelos se han registrado en el sistema
    cont_reservas: Contador que indica cuantas reservas se han registrado en el sistema
    arreglo_usuarios: Arreglo que almacena los usuarios del sistema
    arreglo_hoteles: Arreglo que almacena los hoteles del sistema
    arreglo_vuelos: Arreglo que almacena los vuelos del sistema
    arreglo_reservas: Arreglo que almacena las reservas del sistema
    usuario_autenticado: Variable que almacena el usuario que esta autenticado en el sistema

    CONSTANTES
    MAX_USUARIOS: Contiene el numero maximo de usuarios que se pueden registrar en el sistema
    MAX_RESERVAS: Contiene el numero maximo de reservas que se pueden registrar en el sistema
    MAX_HOTELES: Contiene el numero maximo de hoteles que se pueden registrar en el sistema
    MAX_VUELOS: Contiene el numero maximo de vuelos que se pueden registrar en el sistema



    """

    # Atributos
    cont_usuarios = int
    cont_hoteles = int
    cont_vuelos = int
    cont_reservas = int
    arreglo_usuarios = np.ndarray
    arreglo_hoteles = np.ndarray
    arreglo_vuelos = np.ndarray
    arreglo_reservas = np.ndarray
    usuario_autenticado = Usuario
    
    
    
    # Constantes
    MAX_USUARIOS = 30
    MAX_RESERVAS = 30
    MAX_HOTELES = 30
    MAX_VUELOS = 30

    # Metodo constructor de la clase
    def __init__(self):

        """
        Este metodo constructor va a cargar los archivos de datos que contienen los datos almacenados de la aplicacion

        """
        self.arreglo_usuarios = np.full(self.MAX_USUARIOS, fill_value = None, dtype = object)
        self.arreglo_hoteles = np.full(self.MAX_HOTELES, fill_value = None, dtype = object)
        self.arreglo_vuelos = np.full(self.MAX_VUELOS, fill_value = None, dtype = object)
        self.arreglo_reservas = np.full(self.MAX_RESERVAS, fill_value = None, dtype = object)
        self.cont_reservas = 0
        self.cont_vuelos = 0
        self.cont_hoteles = 0
        self.cont_usuarios = 0 

        # Cargamos los datos
        self.arreglo_usuarios, self.cont_usuarios = self.cargar_datos(Usuario.ARCHIVO_USUARIOS, self.MAX_USUARIOS)
        self.arreglo_vuelos, self.cont_vuelos = self.cargar_datos(Vuelo.ARCHIVO_VUELOS, self.MAX_VUELOS)
        self.arreglo_hoteles, self.cont_hoteles = self.cargar_datos(Hotel.ARCHIVO_HOTELES, self.MAX_HOTELES)
        self.arreglo_reservas, self.cont_reservas = self.cargar_datos(Reserva.ARCHIVO_RESERVAS, self.MAX_RESERVAS)

        
        # Si no hay usuarios, creamos un usuario SuperAdmin por defecto
        if (self.cont_usuarios == 0):
            self.arreglo_usuarios[0] = Usuario(nombre_usuario = "SuperAdmin", numero_documento_usuario = 123456789, contraseña_usuario = "SuperAdmin", tipo_usuario = 3 )
            self.cont_usuarios = 1 # Si el SuperAdmin es el primer usuario, se inicializa el contador de usuarios en 1
        
        # Se indica que no hay usuario autenticado
        self.usuario_autenticado = None 
        
        
    # Este metodo carga los datos 
    def cargar_datos(self, archivo, num_max_datos):
        """
        Este método carga los datos de un archivo, en un arreglo específico

        PARAMS
        archivo = URL relativa del archivo a abrir
        num_max_datos = indica el tamaño máximo de datos que almacena el arreglo

        RETORNOS
        datos = arreglo con los datos cargados
        num_datos = cantidad de datos cargados en el arreglo
        """
        try:
            datos = np.load(archivo, allow_pickle=True)
            i = 0
            while (datos[i] != None):
                i += 1
            return datos, i
        except (FileNotFoundError, EOFError):
            print ("No se pudo cargar el archivo ...") 
            datos = np.full((num_max_datos), fill_value=None, dtype=object)
            return datos, 0
    
    # Este metodo guarda los datos
    def guardar_datos(self, datos, archivo):
        """
        Este método almacena los datos de un arreglo en un archivo

        PARAMS
        datos = arreglo Numpy con los datos a alamcenar
        archivo = URL relativa del archivo en el que se almacenarán los datos

        RETURNS
        True si almacena los datos correctamente en el archivo
        False si no logra almacenar los datos en el archivo 
        
        """
        try:
            np.save(archivo, datos)
            return True
        except (FileNotFoundError, EOFError):
            return False

    
    # Este metodo da solucion al requerimiento registar usuario
    def registrar_usuario(self):

        """
        Este metodo crea y agrega un nuevo usuario al arreglo de usuarios

        PARAMETROS
        Ninguno

        RETORNO
        True si el registro del usuario es correcto, False en caso contrario
        """
        
        if (self.cont_usuarios < self.MAX_USUARIOS): # Se verifica que exista espacio para un nuevo registro
            # Crea un usuario nuevo y se piden sus datos
            usuario = Usuario 
            usuario = Usuario()
            usuario.pedir_datos_usuario()
            # Se almacena el usuario creado en el arreglo y aumenta el contador de usuarios registrados en 1
            self.arreglo_usuarios[self.cont_usuarios] = usuario
            self.cont_usuarios += 1

            # Actualizamos los datos
            if (self.guardar_datos(self.arreglo_usuarios, Usuario.ARCHIVO_USUARIOS)): 
                print("\nSe actualizó el archivo de usuarios")
            else:
                print("\nNo se pudo guardar el archivo de usuarios")

            return True
        
        else:
            print("No hay espacio disponible para hacer un registro.")
            return False

    # Este metodo da solucion al requerimiento registrar vuelo
    def registrar_vuelo(self):

        """
        Este metodo crea y agrega un nuevo vuelo al arreglo de vuelos

        PARAMETROS
        Ninguno

        Retorno
        Vacio
        """
        
        if (self.cont_vuelos < self.MAX_VUELOS): # Se verifica que exista espacio para un nuevo registro
            # Crea un vuelo nuevo y se piden sus datos
            vuelo = Vuelo
            vuelo = Vuelo()
            vuelo.pedir_datos_vuelo()
            vuelo.numero_vuelo = self.cont_vuelos # El numero de vuelo se asigna de acuerdo al orden de registro
            # Se almacena el vuelo creado en el arreglo y aumenta el contador de vuelos registrados en 1
            self.arreglo_vuelos[self.cont_vuelos] = vuelo
            self.cont_vuelos += 1

            # Actualizamos los datos
            if (self.guardar_datos(self.arreglo_vuelos, Vuelo.ARCHIVO_VUELOS)):
                print("\nSe actualizó el archivo de vuelo")
            else:
                print("\nNo se pudo guardar el archivo de vuelos")
            
            print("\nVuelo registrado correctamente.\nATENCION: Recuerde que el NUMERO DEL VUELO se asignara de acuerdo al orden de registro, empezando desde 0.\nEl numero del vuelo es: ", vuelo.numero_vuelo)
        else:
            print("\nNo hay espacio disponible para hacer un registro.")

    # Este metodo da solucion al requerimiento registrar vuelo
    def registrar_hotel(self):

        """
        Este metodo crea y agrega un nuevo hotel al arreglo de hoteles
        
        PARAMETROS
        Ninguno

        Retorno
        Vacio
        """

        if (self.cont_hoteles < self.MAX_HOTELES): # Se verifica que exista espacio para un nuevo registro
            # Crea un nuevo hotel y se piden sus datos
            hotel = Hotel
            hotel = Hotel()
            hotel.pedir_datos_hotel()
            hotel.id_hotel = self.cont_hoteles # # El ID de hotel se asigna de acuerdo al orden de registro
            # Se almacena el hotel creado en el arreglo y aumenta el contador de hoteles registrados en 1
            self.arreglo_hoteles[self.cont_hoteles] = hotel
            self.cont_hoteles += 1

            #Actualizamos los datos
            if (self.guardar_datos(self.arreglo_hoteles, Hotel.ARCHIVO_HOTELES)):
                print("\nSe actualizó el archivo de hoteles")
            else:   
                print("\nNo se pudo guardar el archivo de hoteles")
            
            print("\nHotel registrado con exito.\nATENCION: Recuerde que el ID del hotel se asignara de acuerdo al orden de registro, empezando desde 0.\nEl id del hotel es ", hotel.id_hotel)
        else:
            print("\nNo hay espacio disponible para hacer un registro.")

    # Este metodo da solucion al requerimiento promover categoria cliente
    def promover_categoria_cliente(self):

        """
        Este metodo permite a un empleado promover la categoria de un cliente

        PARAMETROS
        Ninguno
        
        RETORNO
        Vacio
        """
        
        documento = input("\nIngrese el numero documento del cliente que quiere consultar: ")
        while(funciones.validar_entero_mayor_0(documento)): # Se valida el documento a buscar y se pide hasta que se ingrese bien
            documento = input("\nIngrese el numero documento del cliente que quiere consultar: ")
        documento = int(documento) # Se deja el documento a buscar convertido en tipo de dato entero

        for i in range(0, self.cont_usuarios, 1):
            if (documento == self.arreglo_usuarios[i].numero_documento_usuario): # Se busca el numero de documento en el arreglo de usuarios
                if (self.arreglo_usuarios[i].tipo_usuario == 1):
                    while (True):
                        self.arreglo_usuarios[i].tipo_cliente = input("\nIngrese la categoria a la cual desea promover el cliente.\n1.Regular\n2.Plata\n3.Oro\n4.Platino\nRespuesta: ")
                        while (funciones.validar_entero_mayor_0(self.arreglo_usuarios[i].tipo_cliente)): # Se valida el numero ingresado y se pide hasta que se ingrese bien
                            self.arreglo_usuarios[i].tipo_cliente = input("\nIngrese la categoria a la cual desea promover el cliente.\n1.Regular\n2.Plata\n3.Oro\n4.Platino\nRespuesta: ")
                        self.arreglo_usuarios[i].tipo_cliente = int(self.arreglo_usuarios[i].tipo_cliente) # Se deja la categoria convertida en tipo de dato entero
                        if (self.arreglo_usuarios[i].tipo_cliente > 4):
                            print("\nIngresaste una opcion invalida. Intentalo de nuevo.")
                        else:
                            break
                
                    match(self.arreglo_usuarios[i].tipo_cliente):
                        case 1:
                            self.arreglo_usuarios[i].tipo_cliente = "Regular"
                        case 2:
                            self.arreglo_usuarios[i].tipo_cliente = "Plata"
                        case 3:
                            self.arreglo_usuarios[i].tipo_cliente = "Oro"
                        case 4: 
                            self.arreglo_usuarios[i].tipo_cliente = "Platino"
                    
                    # Actualizamos los datos                   
                    if (self.guardar_datos(self.arreglo_usuarios, Usuario.ARCHIVO_USUARIOS)):
                        print("\nSe actualizó el archivo de usuarios")
                    else:
                        print("\nNo se pudo guardar el archivo de usuarios")
                                
                    print("\nCambio registrado exitosamente!")
                    return 
        # Si llega a este punto, fuera del ciclo, es porque el cliente no fue encontrado    
            print("\nEl usuario consultado no existe.")
                
    # Este metodo da solucion al requerimiento autenticar usuario
    def autenticar_usuario(self):

        """
        Este metodo permite a un usuario autenticarse con numero de documento y contraseña para ingresar al sistema

        PARAMETROS
        Ninguno

        RETORNO
        True si el usuario ingresa autenticado a la aplicacion correctamente, False en caso contrario
        """

        numero_documento_usuario_buscado = input("\nIngrese su numero de documento: ")
        while(funciones.validar_entero_mayor_0(numero_documento_usuario_buscado)): # Se valida el numero de documento buscado y se pide hasta que se ingrese bien
            numero_documento_usuario_buscado = input("\nIngrese su numero de documento: ")
        numero_documento_usuario_buscado = int(numero_documento_usuario_buscado) # Se deja el numero de documento buscado convertido en tipo de dato entero

        contraseña_buscada = input("\nIngrese la contraseña: ")
        while(funciones.validar_no_vacio(contraseña_buscada)): # Se valida la contraseña buscada y se pide hasta que se ingrese bien (Que no este vacio)
            contraseña_buscada = input("\nIngrese la contraseña: ")
        
        
        for i in range(self.cont_usuarios):
            if (self.arreglo_usuarios[i].numero_documento_usuario == numero_documento_usuario_buscado): # Se busca el numero de documento en el arreglo de usuarios
                if(self.arreglo_usuarios[i].contrasena_usuario == contraseña_buscada): # Se busca la contraseña en el arreglo de usuarios
                    
                    
                    self.usuario_autenticado = self.arreglo_usuarios[i] # Se almacena el usuario encontrado en la variable usuario autenticado
                    print("\nHas ingresado correctamente!")

                    return True 
                else:
                    print("\nLa contraseña no coincide. Intentalo de nuevo.")
                    return False
        # Si llega a este punto, fuera del ciclo, el usuario no fue encontrado    
        print(f"\nEl usuario con el id {numero_documento_usuario_buscado} no esta registrado. Intentalo de nuevo.")
        return False
        
    # Este metodo da solucion al requerimiento consultar informacion cliente
    def consultar_informacion_cliente(self, cliente):

        """
        Este metodo permite consultar la informacion de un cliente y sus reservas activas

        PARAMETROS
        cliente: Hace referencia al cliente del cual se quiere consultar su informacion y reservas activas

        RETORNO
        True si el cliente tiene reservas activas, False en caso contrario
        """
        
        if (cliente.tipo_usuario == 1): # Si el usuario es de tipo cliente, se procede de esta manera
            info_cliente = ""
            reservas_cliente =""
            
            info_cliente += "Nombre: " + cliente.nombre_usuario + "\n" + cliente.tipo_documento_usuario + ": " + str(cliente.numero_documento_usuario) + "\n" + "Telefono: " + str(cliente.telefono_usuario) + "\n" + "Correo: " + (cliente.correo_usuario) + "\n" + "Tipo de cliente: " + (cliente.tipo_cliente) + "\n" + "Contacto de emergencia: " + (cliente.nombre_contacto_emergencia_usuario) + "\n" + "Numero de telefono del contacto de emergencia: " + (str(cliente.telefono_contacto_emergencia_usuario))

            for i in range (0, self.cont_reservas, 1):
                if (self.arreglo_reservas[i].titular_reserva == cliente.numero_documento_usuario): # Se buscan las reservas que tengan como titular al cliente
                    if (self.arreglo_reservas[i].fecha_salida > (datetime.now().date())): # Se valida que sean reservas activas (fecha posterior)
                        reservas_cliente += "\nID de la reserva: " + str(self.arreglo_reservas[i].id_reserva) + "\nNumero de personas en la reserva: " + str(self.arreglo_reservas[i].numero_personas) + "\n" + "Ciudad de partida: " + self.arreglo_reservas[i].ciudad_partida_reserva + "\n" + "Ciudad de destino: " + self.arreglo_reservas[i].ciudad_destino_reserva + "\n" + "Fecha de salida: " + str(self.arreglo_reservas[i].fecha_salida) + "\n" + "Fecha de regreso: " + str(self.arreglo_reservas[i].fecha_regreso) + "\n" + "Numero de vuelo reservado de ida: " + str(self.arreglo_reservas[i].numero_vuelo_ida) + "\n" + "Numero de vuelo reservado de vuelta: " + str(self.arreglo_reservas[i].numero_vuelo_vuelta) + "\n" + "Nombre del hotel reservado: " + self.arreglo_reservas[i].nombre_hotel_reserva + "\n"

        
            print("\nInformacion del cliente: " + "\n" + info_cliente)
            if (reservas_cliente != ""):
                print("\nReservas activas del cliente: " + "\n" + reservas_cliente)
                return True
                
            else: 
                print("\nEl cliente no tiene reservas activas.")
                return False

    # Este metodo da solucion al requerimiento consultar habitaciones disponibles
    def consultar_habitaciones_disponibles(self, hotel, fecha1, fecha2, imprimir):

        """
        Este metodo permite consultar las habitaciones disponibles de un hotel seleccionado en un intervalo de tiempo

        PARAMETROS
        hotel: Hace referencia al hotel cuya disponibilidad se quiere conocer
        imprimir: Hace referencia a un booleano, para que imprima las habitaciones disponibles (True), o solo retorne un booleano si quiere saber si hay habitaciones disponibles (False) 
        fecha1: Hace referencia a la fecha inicial del intervalo
        fecha2: Hace referencia a la fecha final del intervalo


        RETORNO
        True si hay habitaciones disponibles en el hotel seleccionado, False en caso contrario
        """
        
                    
        listado_habitaciones_disponibles = ""
        for i in range (0, len(self.arreglo_hoteles[hotel.id_hotel].arreglo_habitaciones), 1): #Este ciclo recorre las habitaciones del hotel seleccionado
            bandera = True
            for k in range (0, self.cont_reservas, 1):  #Este ciclo reccore las reservas realizadas, y las compara con la informacion de la habitacion i. 
                if (hotel.id_hotel == self.arreglo_reservas[k].id_hotel_reserva):
                    if (hotel.arreglo_habitaciones[i].numero_habitacion == self.arreglo_reservas[k].numero_habitacion_reserva): #Si el numero de la habitacion i coincide con la habitacion reservada en la reserva k, verifica:
                        if(fecha1 < self.arreglo_reservas[k].fecha_salida and fecha2 < self.arreglo_reservas[k].fecha_salida): #Si tanto fecha1 como fecha2 son antes de la fecha de salida de la reserva, significa que esa habitacion no esta reservada en ese intervalo en la reserva evaluada. Por tanto, continua con la siguiente iteración
                            continue 
                        else:
                            if (fecha1 > self.arreglo_reservas[k].fecha_regreso and fecha2 > self.arreglo_reservas[k].fecha_regreso): #Si tanto fecha1 como fecha2 son despues de la fecha de llegada de la reserva, signfica que la habitacion no esta reservada en ese intervalo en la reserva evaluada. Continua con la siguiente iteración.
                                continue
                            else: 
                                bandera = False #Si ninguna de las condiciones anteriores se cumple, es decir, si fecha1 o fecha2 estan entre la fecha de salida y fecha de llegada de la reserva, significa que esta reservada en ese intervalo de tiempo. Cambiamos el valor de la bandera
                                break
                

                    
            if (bandera): #Si al terminar el ciclo interno, la bandera sigue en True, signfica que no esta reservada y se agrega al listado.
                listado_habitaciones_disponibles += "\nHabitacion " + str(hotel.arreglo_habitaciones[i].numero_habitacion) + ": " + hotel.arreglo_habitaciones[i].descripcion_habitacion + "\n" + "Capacidad: " + str(hotel.arreglo_habitaciones[i].capacidad_habitacion) + " Personas" + "\n"
                
        
        if (listado_habitaciones_disponibles == ""): 
            if (imprimir):
                print("\nNo hay habitaciones disponibles en el hotel.")
                return False
            else:
                return False
                
        else:
            if (imprimir):
                print("\nLista de habitaciones disponibles:\n" + listado_habitaciones_disponibles)
                return True
            else:
                return True
        
    
    # Este metodo da solucion al requerimiento crear reserva
    def crear_reserva(self, cliente):

        """
        Este metodo permite crear una reserva y agregarla al arreglo de reservas 

        PARAMETROS
        cliente: Hace referencia al cliente registrado y autenticado

        RETORNO
        Vacio
        """
        reserva = Reserva
        reserva = Reserva()
        reserva.pedir_datos_reserva(cliente) #Se piden los datos para verificar si la reserva es viable.
        bandera = False 
        if (self.cont_reservas < self.MAX_RESERVAS):
            for i in range(0, self.cont_vuelos, 1):

                if (reserva.ciudad_destino_reserva == self.arreglo_vuelos[i].ciudad_destino and reserva.ciudad_partida_reserva == self.arreglo_vuelos[i].ciudad_origen and reserva.numero_personas <= self.arreglo_vuelos[i].cupos_vuelo and reserva.fecha_salida == self.arreglo_vuelos[i].fecha_salida_vuelo):
                    # ^^ Se verifica que la ciudad de destino, origen, fecha de salida y cupos del vuelo sean favorables con respecto a los datos de la reserva. Se guarda el numero de vuelo de ida en la reserva.
                    
                    reserva.numero_vuelo_ida = self.arreglo_vuelos[i].numero_vuelo 
                    for j in range (0, self.cont_vuelos, 1):
            
                        if(reserva.ciudad_destino_reserva == self.arreglo_vuelos[j].ciudad_origen and reserva.ciudad_partida_reserva == self.arreglo_vuelos[j].ciudad_destino and reserva.numero_personas <= self.arreglo_vuelos[j].cupos_vuelo and reserva.fecha_regreso == self.arreglo_vuelos[j].fecha_salida_vuelo):
                            #^^ Vuelve a recorrer el arreglo de vuelos, y se verifica que la ciudad de destino de la reserva sea la ciudad de partida del vuelo, y la ciudad de salida de la reserva sea el destino del vuelo. Vuelve a verificarse los cupos y las fechas. 
                            reserva.numero_vuelo_vuelta = self.arreglo_vuelos[j].numero_vuelo
                            bandera = True
                            break #Guarda el numero de vuelo de regreso en la reserva, y se cambia el estado de la bandera para indicar que se puede seguir al siguiente paso.
                    if (bandera):
                        break


            
            if (bandera): #Si la bandera es True significa que encontraron vuelos. Por tanto, sigue con el siguiente paso. Si la bandera es falsa, se imprime que no hay vuelos disponibles, y se corta la funcion.
                
                while(bandera):
                    k = 1
                    listado_hoteles = ""
                    for i in range (0, self.cont_hoteles, 1):
                        if (reserva.ciudad_destino_reserva == self.arreglo_hoteles[i].ciudad_hotel and cliente.tipo_cliente == self.arreglo_hoteles[i].categoria_hotel): #Si la ciudad de destino de la reserva es igual a la ciudad donde esta el hotel, y las categorias del cliente y del hotel son iguales, se agrega al listado.
                            if (self.consultar_habitaciones_disponibles(self.arreglo_hoteles[i], reserva.fecha_salida, reserva.fecha_regreso, False)):
                                listado_hoteles += str(k) + ". " + self.arreglo_hoteles[i].nombre_hotel + "       ID: " + str(self.arreglo_hoteles[i].id_hotel) + "\n"
                                k += 1


                    if (listado_hoteles == ""): 
                        print("\nNo hay hoteles disponibles en la ciudad. Lo sentimos!")
                        return 
                    else:
                        print ("\nHoteles en la ciudad:\n"+ listado_hoteles)
                        hotel_escogido = input("\nIngrese el numero de identificacion del hotel dentro de la lista: ")
                        while(funciones.validar_id(hotel_escogido, self.cont_hoteles)): #Se valida el ID ingresado, y se solicita hasta que lo ingrese bien.
                            hotel_escogido = input("\nIngrese el numero de identificacion del hotel dentro de la lista: ")
                        hotel_escogido = int(hotel_escogido) #Convertimos el ID en un entero.
                        try: 
                            
                            if (self.arreglo_hoteles[hotel_escogido].categoria_hotel == cliente.tipo_cliente and self.arreglo_hoteles[hotel_escogido].ciudad_hotel == reserva.ciudad_destino_reserva):
                                ##^Se verifica nuevamente que la categoria del hotel y el cliente, y las ciudades de la reserva y hotel, coincidan. 
                                # De lo contrario, se le dice al cliente que ingreso un hotel por fuera de la lista. Volvemos a generar el listado, y se vuelve a solicitar ID. 
                                
                                reserva.id_hotel_reserva = hotel_escogido
                                if (self.consultar_habitaciones_disponibles(self.arreglo_hoteles[hotel_escogido], reserva.fecha_salida, reserva.fecha_regreso, bandera)):
                                    """El metodo de arriba, muestra la lista de habitaciones disponibles, y ademas 
                                    retorna True si hay habitaciones disponibles, y False si no las hay.
                                    Por ende, si la condicion de arriba no se cumple, se imprime que el hotel no tiene habitaciones
                                    disponibles y retorna al menu principal"""
                                    
                                    while(bandera):
                                        habitacion_reserva = input("\nIngrese el numero de la habitacion dentro de la lista que quiere reservar: ")
                                        while(funciones.validar_id(habitacion_reserva, len(self.arreglo_hoteles[hotel_escogido].arreglo_habitaciones ) -1)): #Validamos el numero de la habitacion.
                                            habitacion_reserva = input("\nIngrese el numero de la habitacion dentro de la lista que quiere reservar: ")
                                        habitacion_reserva = int(habitacion_reserva)
                                    
                                    
                                        try:
                                            
                                            if (self.arreglo_hoteles[hotel_escogido].arreglo_habitaciones[habitacion_reserva].numero_habitacion == habitacion_reserva): #Como los IDS de cada clase corresponden a la posicion en el arreglo en que se almacenan, verificamos que coincida el numero de la habitacion con la habitacion escogida.
                                                bandera = False
                                                for y in range (0, self.cont_reservas, 1):
                                                    if (self.arreglo_reservas[y].id_hotel_reserva == self.arreglo_hoteles[hotel_escogido].id_hotel):
                                                        if (self.arreglo_reservas[y].numero_habitacion_reserva == habitacion_reserva): #Este arreglo recorre las reservas para verificar que si sea posible la reserva de la habitacion elegida.
                                                            if (self.arreglo_reservas[y].fecha_salida > reserva.fecha_salida and self.arreglo_reservas[y].fecha_salida > reserva.fecha_regreso):
                                                                bandera = False 
                                                            else: 
                                                                if (self.arreglo_reservas[y].fecha_regreso < reserva.fecha_regreso and self.arreglo_reservas[y].fecha_regreso < reserva.fecha_salida):
                                                                    bandera = False
                                                                    
                                                                else:
                                                                    bandera = True #La bandera se deja en True para que vuelva a repetir el ciclo de solicitar el numero de la habitacion.
                                                                    break
                                                
                                                        else:
                                                            bandera = False
                                                    else: 
                                                        bandera = False 
                                                if (bandera):
                                                    print("\nIngresaste una habitacion que no esta disponible. Selecciona una habitacion que este dentro de la lista.")
                                                    continue
                                                                
                                                            
                                                else: #Si la bandera es falsa, es decir la habitacion esta libre en las fechas de la reserva, entonces:
                                                    if (self.arreglo_hoteles[hotel_escogido].arreglo_habitaciones[habitacion_reserva].capacidad_habitacion >= reserva.numero_personas): #Se verifica que el numero de personas sea menor o igual a la capacidad de la habitacion escogida. #De lo contrario, se solicita que ingrese otro numero de habitacion
                                                        #Finalmente, se guarda la habitacion, el nombre del hotel, el id de la reserva, en la reserva realizada. Y se le restan los cupos a los aviones escogidos para la reserva con base al numero de personas en ella.
                                                        reserva.numero_habitacion_reserva = habitacion_reserva
                                                        reserva.nombre_hotel_reserva = self.arreglo_hoteles[hotel_escogido].nombre_hotel
                                                        reserva.id_reserva = self.cont_reservas
                                                        self.arreglo_reservas[self.cont_reservas] = reserva
                                                        self.cont_reservas += 1
                                                        self.arreglo_vuelos[reserva.numero_vuelo_ida].cupos_vuelo -= reserva.numero_personas # Restamos a los vuelos de 
                                                        self.arreglo_vuelos[reserva.numero_vuelo_vuelta].cupos_vuelo -= reserva.numero_personas

                                                        if (self.guardar_datos(self.arreglo_reservas, Reserva.ARCHIVO_RESERVAS)):
                                                            print("\nSe actualizó el archivo de reservas")
                                                        else:
                                                            print("\nNo se pudo guardar el archivo de reservas")
                                                        
                                                        if (self.guardar_datos(self.arreglo_vuelos, Vuelo.ARCHIVO_VUELOS)):
                                                            print("\nSe actualizó el archivo de vuelos")
                                                        else:
                                                            print("\nNo se pudo guardar el archivo de vuelos")
                                                          
                                                        print("\nReserva exitosa!")
                                                        print("\nPara realizar consultas con respecto a la reserva, EL ID DE LA RESERVA ES ", reserva.id_reserva)
                                                        self.generar_factura(reserva)
                                                    else:
                                                        print("\nEscogiste una habitacion que no tiene capacidad suficiente para las personas de la reserva. ")
                                                        return #Cambiamos el valor de la bandera para que vuelva a ingresar en el ciclo "While (bandera)" interno.
                                                        

                                                    
                                                    
                                            else:
                                                print("\nEscogiste una habitacion que no esta disponible. Selecciona una habitacion que este dentro de la lista. ")
                                                bandera = True
                                                continue
                                                
                                        
                                        except ValueError:
                                            print("\nIngresaste una habitacion invalida. Intentalo de nuevo.")
                                            continue
                                else:
                                    print("\nVolviendo al menu principal.")
                                    return
                                    
                                    
                                    
                                        
                            else:
                                print("\nIngresaste un hotel invalido. Selecciona un hotel que este dentro de la lista.")            
                                continue
                        except ValueError:
                            print("\\nIngresaste un hotel invalido. Intentalo de nuevo.")
                                
            else: 
                print("\nNo hay vuelos disponibles para las fechas dispuestas. ")
                return               
    
    # Este metodo da solucion al requerimiento consultar habitaciones reservadas
    def consultar_habitaciones_reservadas(self):
        """
        Este metodo permite consultar las habitaciones reservadas de un hotel

        PARAMETROS
        Ninguno

        RETORNO
        Vacio

        """
        
        listado_hoteles = ""
        for i in range(0, self.cont_hoteles, 1):
            listado_hoteles += "Nombre: " + self.arreglo_hoteles[i].nombre_hotel + "\nID: " + str(self.arreglo_hoteles[i].id_hotel) + "\n" #Generamos el listado de hoteles con ID, para solicitarle el que quiere consultar.
        if(listado_hoteles != ""):
            print("\nListado hoteles: " + "\n" + listado_hoteles)
            
            hotel = input("\nIngrese el ID del hotel cuya lista quiere generar: ")
            while(funciones.validar_id(hotel, self.cont_hoteles)): # Se valida el ID del hotel y se pide hasta que se ingrese bien
                print("\nListado hoteles: " + "\n" + listado_hoteles)
                hotel = input("\nIngrese el ID del hotel cuya lista quiere generar: ")
            hotel = int(hotel) # Se deja el ID del hotel convertido en tipo de dato entero
            
            
            listado_habitaciones_reservadas = ""
            for i in range (0, self.cont_reservas, 1):
                if (self.arreglo_reservas[i].id_hotel_reserva == self.arreglo_hoteles[hotel].id_hotel): # Se busca el ID del hotel seleccionado en el arreglo de reservas.
                    for j in range (0, len(self.arreglo_hoteles[hotel].arreglo_habitaciones), 1):
                        if (self.arreglo_reservas[i].numero_habitacion_reserva == j): #Ahora se recorre el arreglo de las reservas, y si el numero de la habitacion de la reserva coincide con el numero de la habitacion j, se realiza la siguiente verificacion:
                            if (self.arreglo_reservas[i].fecha_salida >= datetime.now().date() or self.arreglo_reservas[i].fecha_regreso >= datetime.now().date()): #Si la fecha de salida de la reserva o la fecha de regreso de la reserva es igual o despues a la fecha en que se realiza la verificacion, entonces se agrega al listado.
                                listado_habitaciones_reservadas += " \nTitular de la reserva: " + str(self.arreglo_reservas[i].titular_reserva) + "\n" + "Habitacion " + str(j) + " reservada desde " + str(self.arreglo_reservas[i].fecha_salida) + " Hasta " + str(self.arreglo_reservas[i].fecha_regreso) + "\n" 
                    
            if (listado_habitaciones_reservadas == ""): 
                print("\nNo hay habitaciones reservadas en el hotel.")
            else: 
                print("\nListado de habitaciones reservadas: Hotel ", self.arreglo_hoteles[hotel].nombre_hotel)
                print(listado_habitaciones_reservadas)
        else: print("\nNo hay hoteles registrados. ")
    
    
    # Este metodo da solucion al requerimiento generar lista habitaciones hotel
    def generar_lista_habitaciones_hotel(self):
        """
        Este metodo permite generar la lista de habitaciones de un hotel

        PARAMETROS
        Ninguno

        RETORNO
        Vacio

        """
        
        listado_hoteles = ""
        for i in range(0, self.cont_hoteles, 1):
            listado_hoteles += "Nombre: " + self.arreglo_hoteles[i].nombre_hotel + "\nID: " + str(self.arreglo_hoteles[i].id_hotel) + "\n"
        if (listado_hoteles != ""):
            print("\nListado hoteles: " + "\n" +  listado_hoteles)
            hotel = input("\nIngrese el ID del hotel cuya lista quiere generar: ")
            while(funciones.validar_id(hotel, self.cont_hoteles)): # Se valida el id del hotel y se pide hasta que se ingrese bien
                print("Listado hoteles: " + "\n" +  listado_hoteles)
                hotel = input("\nIngrese el ID del hotel cuya lista quiere generar: ")
            hotel = int(hotel) # Se deja el Id del hotel convertido en tipo de dato entero
            listado_habitaciones = ""
            for i in range (0, len(self.arreglo_hoteles[hotel].arreglo_habitaciones), 1): #Se recorre el arreglo de habitaciones del hotel
                listado_habitaciones += "Habitacion #" + str(self.arreglo_hoteles[hotel].arreglo_habitaciones[i].numero_habitacion) + "  Descripcion: " + self.arreglo_hoteles[hotel].arreglo_habitaciones[i].descripcion_habitacion + "\n" + "Capacidad: " + str(self.arreglo_hoteles[hotel].arreglo_habitaciones[i].capacidad_habitacion)+ " personas"+ "\n" + "Precio por noche: " + str(self.arreglo_hoteles[hotel].arreglo_habitaciones[i].precio_noche_habitacion) + "COP" + "\n" + "\n"
            if (listado_habitaciones != ""):
                print("Listado de habitaciones" + "\n" + listado_habitaciones )
            else:
                print("\nNo hay habitaciones dentro del hotel seleccionado.")
        else: print("\nNo hay hoteles registrados. ")

    # Este metodo da solucion al requerimiento consultar disponibilidad vuelo
    def consultar_disponibilidad_vuelo(self):
        """
        Este metodo permite consultar la disponibilidad de un vuelo (Si aun tiene cupos disponibles)

        PARAMETROS
        Ninguno

        RETORNO
        Vacio
        """

    
        listado_vuelos = ""
        for i in range(0, self.cont_vuelos, 1):
            listado_vuelos += "Numero de vuelo: " + str(self.arreglo_vuelos[i].numero_vuelo) + "\n"

        if (listado_vuelos != ""):
            print("Listado de Vuelos: " + "\n" + listado_vuelos)

            vuelo = input("\nIngrese el numero del vuelo del cual desea consultar la disponibilidad: ")
            while (funciones.validar_id(vuelo, self.cont_vuelos)): # Se valida el numero del vuelo y se pide hasta que se ingrese bien
                print("Listado de Vuelos: " + "\n" + listado_vuelos)
                vuelo = input("\nIngrese el ID del vuelo del cual desea consultar la disponibilidad: ")
            vuelo = int(vuelo) # Se deja el numero de vuelo convertido en tipo de dato entero
            if (self.arreglo_vuelos[vuelo].cupos_vuelo > 0 ): # Se verifica que el vuelo tenga cupos 
                print (f"\nEl vuelo tiene {self.arreglo_vuelos[vuelo].cupos_vuelo} puestos disponibles. ")
            else:
                print("\nEl vuelo no tiene ningun puesto disponible.")
        else: print("No hay vuelos registrados. ")

    # Este metodo da solucion al requerimiento generar historial reservas
    def generar_historial_reservas(self):
        """
        Este metodo permite generar un historial de reservas del sistema

        PARAMETROS
        Ninguno

        RETORNO
        Vacio
        """
        
        historial_reservas = ""
        fecha = input("\nIngrese la fecha desde la cual quiere consultar las reservas (AA-MM-DD): ")
        while (funciones.validar_fecha(fecha)): # Se valida la fecha y se pide hasta que se ingrese bien
            fecha = input("\nIngrese la fecha desde la cual quiere consultar las reservas (AA-MM-DD): ")
        fecha = datetime.strptime(fecha, "%Y-%m-%d").date() # Se deja la fecha convertida en tipo de dato date (SOLO FECHA)

        
        
        for i in range(0, self.cont_reservas, 1):
            if (fecha <= self.arreglo_reservas[i].fecha_salida): # Se recorre el arreglo de reservas buscando las que tengan una fecha de salida mayor o igual a la fecha ingresada
                num_dias = self.arreglo_reservas[i].fecha_regreso - self.arreglo_reservas[i].fecha_salida # Se calcula el numero de dias que dura la reserva
                # Se calcula el costo de cada reserva existente
                costo = self.arreglo_vuelos[self.arreglo_reservas[i].numero_vuelo_ida].costo_vuelo + self.arreglo_vuelos[self.arreglo_reservas[i].numero_vuelo_vuelta].costo_vuelo + (num_dias.days) * self.arreglo_hoteles[self.arreglo_reservas[i].id_hotel_reserva].arreglo_habitaciones[self.arreglo_reservas[i].numero_habitacion_reserva].precio_noche_habitacion #num_days sirve para, de la resta anterior, sacar solamente los dias.
                iva = (costo) * 0.19 # Se calcula el IVA 
                costo_total = costo + iva
                historial_reservas +=  "\n" + "ID de la reserva: " + str(self.arreglo_reservas[i].id_reserva) + "\nNumero de personas en la reserva: " + str(self.arreglo_reservas[i].numero_personas) + "\n" + "Ciudad de partida: " + self.arreglo_reservas[i].ciudad_partida_reserva + "\n" + "Ciudad de destino: " + self.arreglo_reservas[i].ciudad_destino_reserva + "\n" + "Fecha de salida: " + str(self.arreglo_reservas[i].fecha_salida) + "\n" + "Fecha de regreso: " + str(self.arreglo_reservas[i].fecha_regreso) + "\n" + "Numero de vuelo reservado de ida: " + str(self.arreglo_reservas[i].numero_vuelo_ida) + "\n" + "Numero de vuelo reservado de vuelta: " + str(self.arreglo_reservas[i].numero_vuelo_vuelta) + "\n" + "Nombre del hotel reservado: " + self.arreglo_reservas[i].nombre_hotel_reserva + "\nCosto total de la reserva: " + str(costo_total) + "\nIVA pagado en la reserva: " + str(iva) + "\n"
                
        
        if (historial_reservas == ""):
            print("\nNo hay reservas realizadas desde la fecha que ingresaste. ")
        
        else:
            print("\nHistorial de reservas:\n" + historial_reservas)


    # Este metodo da solucion al requerimiento generar factura
    def generar_factura(self, reserva):
        """
        Este metodo permite generar la factura de una reserva activa

        PARAMETROS
        reserva: Hace referencia a la reserva activa del cliente de la cual se quiere generar la factura

        RETORNO
        Vacio
        """
        if (reserva.fecha_salida <= datetime.now().date() or reserva.fecha_regreso <= datetime.now().date()): # Se verifica que la reserva sea un reserva activa
            print("\nSolo puedes consultar facturas de reservas activas. Intentalo de nuevo.")
            return False
        else:
            factura = ""
            num_dias = reserva.fecha_regreso - reserva.fecha_salida
            costo_sin_iva = self.arreglo_vuelos[reserva.numero_vuelo_ida].costo_vuelo + self.arreglo_vuelos[reserva.numero_vuelo_vuelta].costo_vuelo + (num_dias.days) * self.arreglo_hoteles[reserva.id_hotel_reserva].arreglo_habitaciones[reserva.numero_habitacion_reserva].precio_noche_habitacion
            costo_total = (costo_sin_iva * 0.19) + costo_sin_iva
            factura += "\nTitular de la reserva: " + str(reserva.titular_reserva) +"\nNumero de personas: " + str(reserva.numero_personas) + "\nHotel: " + reserva.nombre_hotel_reserva + ", habitacion # " + str(reserva.numero_habitacion_reserva) + "\nCosto por noche: " + str(self.arreglo_hoteles[reserva.id_hotel_reserva].arreglo_habitaciones[reserva.numero_habitacion_reserva].precio_noche_habitacion) + "\n" + "Numero de vuelo de ida: " + str(reserva.numero_vuelo_ida) + "\n"+ "Precio vuelo de ida: " + str(self.arreglo_vuelos[reserva.numero_vuelo_ida].costo_vuelo) + "\n" + "Numero vuelo vuelta: " + str(reserva.numero_vuelo_vuelta) + "\n" + "Precio vuelo de vuelta: " + str(self.arreglo_vuelos[reserva.numero_vuelo_vuelta].costo_vuelo) + "\n" 
            print(factura)
            print("\nSubtotal: ", costo_sin_iva, "COP")
            print("\nTotal a pagar: ", costo_total, "COP")
            return True
    
    # Este metodo da solucion al requerimiento cancelar reserva
    def cancelar_reserva(self, usuario):
        """
        Este metodo permite cancelar una reserva activa

        PARAMETROS
        usuario: Hace referencia al usuario registrado y autenticado del cual se desea cancelar la reserva

        RETORNO
        Vacio
        """
        
            
        if (usuario.tipo_usuario == 1): # Si el usuario es tipo cliente se procede asi
            if (self.consultar_informacion_cliente(usuario)): # Se verifica que exista informacion y reservas del cliente
                reserva = input("Ingrese el ID de la reserva que quiere cancelar: ")
                while (funciones.validar_id(reserva, self.cont_reservas)): # Se valida el ID de la reserva y se pide hasta que se ingrese bien
                    self.consultar_informacion_cliente(usuario)
                    reserva = input("Ingrese el ID de la reserva que quiere cancelar: ")
                reserva = int(reserva) # Se deja el Id de la reserva convertido en tipo de dato entero
                if (self.arreglo_reservas[reserva].id_reserva == reserva):
                    self.arreglo_vuelos[self.arreglo_reservas[reserva].numero_vuelo_ida].cupos_vuelo += self.arreglo_reservas[reserva].numero_personas 
                    self.arreglo_vuelos[self.arreglo_reservas[reserva].numero_vuelo_vuelta].cupos_vuelo += self.arreglo_reservas[reserva].numero_personas 

                    
                    self.arreglo_reservas[reserva] = None # Se iguala la reserva a eliminar a vacio
                    for i in range (reserva + 1, self.cont_reservas): # Se corren las reservas en su arreglo hacia la izquierda
                        
                        self.arreglo_reservas[i-1] = self.arreglo_reservas[i]
                        self.arreglo_reservas[i-1].id_reserva = i-1

                    self.cont_reservas -= 1
                    
                    if (self.guardar_datos(self.arreglo_reservas, Reserva.ARCHIVO_RESERVAS)):
                        print("\nSe actualizó el archivo de reservas")
                    else:
                        print("\nNo se pudo guardar el archivo de reservas")
                    
                    if (self.guardar_datos(self.arreglo_vuelos, Vuelo.ARCHIVO_VUELOS)):
                        print("\nSe actualizó el archivo de vuelos")
                    else:
                        print("\nNo se pudo guardar el archivo de vuelos")
                
                    print("Cancelacion exitosa! ")
                
            else:
                print("La cancelacion no se pudo realizar.")
            
           
                    
                
    
    # Este metodo muestra el menu del cliente
    def mostrar_menu_cliente(self):
    
        opc = 1
        while(opc != 5):
        
            print("\n**************MENÚ DE OPCIONES**************")
            print("\n1. Reservar un paquete turístico")
            print("\n2. Consultar factura de una reserva activa")
            print("\n3. Consultar la informacion de sus reservas activas.")
            print("\n4. Cancelar una reserva activa")
            print("\n5. Salir de la APP")
            opc = input("Su opcion: ")
            while(funciones.validar_entero_mayor_0(opc)): # Se valida la opcion ingresada y se pide hasta que se ingrese bien
                    opc= input("Su opcion: ")
            opc = int(opc) # Se deja la opcion convertida en tipo de dato entero
            match (opc):
                case 1:
                    self.crear_reserva(self.usuario_autenticado) 
                case 2: 
                        
                        if (self.consultar_informacion_cliente(self.usuario_autenticado)):
                            factura_a_generar = input("Ingrese el id de la reserva: ")
                            while (funciones.validar_id(factura_a_generar, self.cont_reservas)): # Se valida el Id de la reserva y se pide hasta que se ingrese bien
                                self.consultar_informacion_cliente(self.usuario_autenticado)
                                factura_a_generar = input("Ingrese el id de la reserva: ")    
                            factura_a_generar = int(factura_a_generar) # Se deja el Id de la reserva convertido en tipo de dato entero
                            self.generar_factura(self.arreglo_reservas[factura_a_generar]) # Se genera la factura de la reserva en la posicion del arreglo de acuerdo al ID ingresado
                        else:
                            print("No se pudo generar la factura")
                        
                        
                case 3:
                    self.consultar_informacion_cliente(self.usuario_autenticado)
                case 4:
                    self.cancelar_reserva(self.usuario_autenticado)
                case 5:
                    print("\n**********Hasta pronto!**********")
                case _:
                    print("Ingresaste una opcion invalida. Intentalo de nuevo.")

    # Este metodo muestra el menu del empleado
    def mostrar_menu_empleado(self):
        opc = 1
        while(opc !=11 ):
            print("\n**************MENÚ DE OPCIONES EMPLEADO*************")
            print("1. Registrar un cliente")
            print("2. Promover categoría de un cliente")
            print("3. Generar lista con los datos de las habitaciones de un hotel")
            print("4. Generar lista de las habitaciones reservadas de un hotel")
            print("5. Generar lista de las habitaciones disponibles de un hotel")
            print("6. Consultar la información de un cliente ")
            print("7. Consultar disponibilidad de un vuelo")
            print("8. Generar historial de reservas")
            print("9. Crear una reserva de un cliente")
            print("10. Cancelar una reserva de un cliente")
            print("11. Salir de la APP")
            opc  = input("Su opción: ")
            while(funciones.validar_entero_mayor_0(opc)): # Se valida la opcion ingresada y se pide hasta que se ingrese bien
                opc  = input("Su opción: ")
            opc = int(opc) # Se deja la opcion convertida a tipo de dato entero
            match (opc):
                case 1:
                    if (self.registrar_usuario()):
                        self.cont_usuarios +=1

                        if (self.guardar_datos(self.arreglo_usuarios, Usuario.ARCHIVO_USUARIOS)):
                            print("\nSe actualizó el archivo de usuarios")
                        else:
                            print("\nNo se pudo guardar el archivo de usuarios")

                        print("\nUsuario registrado exitosamente.")
                    else:
                        print("No se pudo realizar el registro del usuario")
                    
                case 2:
                    self.promover_categoria_cliente()
                case 3:
                    self.generar_lista_habitaciones_hotel()
                case 4: 
                    self.consultar_habitaciones_reservadas()
                case 5:
                    listado_hoteles = ""
                    for i in range(0, self.cont_hoteles, 1):
                        listado_hoteles += "Nombre: " + self.arreglo_hoteles[i].nombre_hotel + "\nID: " + str(self.arreglo_hoteles[i].id_hotel) + "\n"

                    if (listado_hoteles != ""):
                        print("\nListado hoteles: " + "\n" + listado_hoteles)
                        id_hotel = input("\nIngrese el ID del hotel cuya lista quiere generar: ")
                        while(funciones.validar_id(id_hotel, self.cont_hoteles)): # Se valida el ID del hotel y se pide hasta que se ingrese bien
                           id_hotel = input("\nIngrese el ID del hotel cuya lista quiere generar: ")
                        id_hotel = int(id_hotel) # Se deja el ID del hotel convertido en tipo de dato entero
                        hotel = self.arreglo_hoteles[id_hotel]
                        fecha1 = input("\nIngrese la fecha desde la que se quiere verificar disponibilidad (formato AÑO-MES-DIA): ")
                        while(True):
                            while (funciones.validar_fecha(fecha1)):
                                fecha1 = input("\nIngrese la fecha desde la que se quiere verificar disponibilidad (formato AÑO-MES-DIA): ")
                            fecha1 = datetime.strptime(fecha1, "%Y-%m-%d").date()
                            fecha_actual = datetime.now()
                            if (fecha1 <= fecha_actual.date()):
                                print("\nIngresaste una fecha anterior o igual a hoy. Vuelve a intentarlo")
                                fecha1 = input("\nIngrese la fecha desde la que se quiere verificar disponibilidad (formato AÑO-MES-DIA): ")
                            else:
                                break 
                        fecha2 = input("\nIngrese la fecha hasta la que se quiere verificar disponibilidad (formato AÑO-MES-DIA): ")
                        while (True):
                            while(funciones.validar_fecha(fecha2)): # Se valida la fecha de regreso y se pide hasta que se ingrese bien
                                fecha2 = input("\nIngrese la fecha hasta la que se quiere verificar disponibilidad (formato AÑO-MES-DIA): ")
                            fecha2 = datetime.strptime(fecha2, "%Y-%m-%d").date() # Se deja la fecha de regreso convetida en tipo de dato date (SOLO FECHA)
                            if (fecha2 <= fecha1): # Se valida que la fecha de regreso no sea menor o igual a la fecha de salida y se pide hasta que se ingrese bien
                                print("\nIngresaste una fecha incorrecta. Intentalo de nuevo. ")
                                fecha2 = input("\nIngrese la fecha hasta la que se quiere verificar disponibilidad (formato AÑO-MES-DIA): ")
                            else:
                                break

                        self.consultar_habitaciones_disponibles(hotel, fecha1,fecha2, True)
                    else:
                        print("\nNO hay hoteles registrados.")
                        return
                case 6: 
                    try:
                        num_cliente = input("\nIngrese el numero de documento del cliente a buscar: ")
                        while (funciones.validar_entero_mayor_0(num_cliente)): # Se valida el numero de documento y se pide hasta que se ingrese bien
                            num_cliente = input("\nIngrese el numero de documento del cliente a buscar: ")
                        num_cliente = int(num_cliente) # Se deja el numero de documento convertido en tipo de dato entero
                        cliente = None # Se iguala el parametro a Vacio-None
                        for i in range (0, self.cont_usuarios, 1): 
                            if (self.arreglo_usuarios[i].numero_documento_usuario == num_cliente): # Se busca al cliente
                                cliente = self.arreglo_usuarios[i] # Se almacena al cliente en el parametro
                                break
                        if (cliente != None): 
                            self.consultar_informacion_cliente(cliente)
                        else:
                            print("\nEl cliente buscado no existe. ")
                    except ValueError:
                        print("")
                        
                case 7:
                    self.consultar_disponibilidad_vuelo()
                case 8:
                    self.generar_historial_reservas()
                case 9:
                    cliente = None # El parametro cambia a Vacio-None
                    documento_cliente = input("Ingrese el numero de documento del cliente a quien se le generara la reserva: ")
                    while (funciones.validar_entero_mayor_0(documento_cliente)): # Se valida el numero de documento y se pide hasta que se ingrese bien
                        documento_cliente = input("Ingrese el numero de documento del cliente a quien se le generara la reserva: ")
                    documento_cliente = int(documento_cliente) # Se deja el numero de documento convertido a tipo de dato entero
                    for i in range (0, self.cont_usuarios, 1):
                        if (documento_cliente == self.arreglo_usuarios[i].numero_documento_usuario): # Se busca el numero de documento en el arreglo de usuarios
                            if (self.arreglo_usuarios[i].tipo_usuario == 1): # Se verifica que el usuario encontrado si sea un cliente
                                cliente = self.arreglo_usuarios[i] # Se cambia el parametro a el cliente encontrado
                    
                    if (cliente != None):
                        self.crear_reserva(cliente)

                    else:
                        print("El cliente consultado no existe.\nVolviendo al menu principal.")
                case 10:
                    usuario = None 
                    documento = input("\nIngrese el numero de documento del cliente: ")
                    while(funciones.validar_entero_mayor_0(documento)): # Se valida el numero de documento y se pide hasta que se ingrese bien
                        documento = input("\nIngrese el numero de documento del cliente: ")
                    documento = int(documento) # Se deja el numero de documento convertido en tipo de dato entero
                    for i in range (0, self.cont_usuarios, 1):
                        if (self.arreglo_usuarios[i].numero_documento_usuario == documento): # Se busca el numero de documento en el arreglo de usuarios
                            usuario = self.arreglo_usuarios[i] # Se almacena en la variable el cliente encontrado
                    if (usuario == None):
                        print("El usuario buscado no existe.\nLa cancelacion no se pudo realizar. ")
                    else:
                        self.cancelar_reserva(usuario)

                case 11:
                    print("**************Hasta pronto!**************")
                case _:
                    print("Ingresaste una opcion invalida. Intentalo de nuevo.")
    
    
    # Este metodo muestra el menu del administrador
    def mostrar_menu_administrador(self):
        opc = 1
        while(opc != 5 ):
            print("\n**************MENÚ DE OPCIONES ADMINISTRADOR*************")
            print("1. Registrar un empleado")
            print("2. Registrar un administrador")
            print("3. Registrar un vuelo")
            print("4. Registrar un hotel")
            print("5. Salir de la APP")
            opc = input("Su opcion: ")
            while (funciones.validar_entero_mayor_0(opc)): # Se valida la opcion ingresada y se pide hasta que se ingrese bien
                opc = input("Su opcion: ")
            opc = int(opc) # Se deja la opcion convertida en tipo de dato entero
            match (opc):
                case 1:
                    if (self.registrar_usuario()):
                        self.arreglo_usuarios[self.cont_usuarios-1].tipo_usuario = 2 # Cuando se registra un empleado, se le asigna su tipo de usuario
                        if (self.guardar_datos(self.arreglo_usuarios, Usuario.ARCHIVO_USUARIOS)):
                            print("\nSe actualizó el archivo de usuarios")
                        else:
                            print("\nNo se pudo guardar el archivo de usuarios")
                        
                        print("\nUsuario registrado exitosamente.")
                    else:
                        print("\nNo se pudo realizar el registro del usuario.")
                case 2:
                    if (self.registrar_usuario()):
                        self.arreglo_usuarios[self.cont_usuarios-1].tipo_usuario = 3 # Cuando se registra un Administrador, se le asigna su tipo de usuario

                        if (self.guardar_datos(self.arreglo_usuarios, Usuario.ARCHIVO_USUARIOS)):
                            print("\nSe actualizó el archivo de usuarios")
                        else:
                            print("\nNo se pudo guardar el archivo de usuarios")
                        
                        print("\nUsuario registrado exitosamente.")
                    else:
                        print("\nNo se pudo realizar el registro del usuario.")

                case 3:
                    self.registrar_vuelo()
                case 4:
                    self.registrar_hotel()
                case 5:
                    print("**************Hasta pronto!**************")
                    return
                case _:
                    print("Ingresaste una opcion invalida. Intentalo de nuevo.")
    
    # Este metodo es el que da inicio a la aplicacion
    def principal(self):
        opc=1
        while(opc != 3):
        
            print("\n***********************Bienvenido a Volamos por Colombia!***********************")
            print("\nElija una opcion: \n1. Aunteticarse\n2. Registrarse\n3. Salir de la APP")
            opc = input("Tu opcion: ")
            while(funciones.validar_entero_mayor_0(opc)): # Se valida la opcion ingresada y se pide hasta que se ingrese bien
                print("\nElija una opcion: \n1. Aunteticarse\n2. Registrarse\n3. Salir de la APP")
                opc = input("Tu opcion: ")
            opc = int(opc) # Se deja la opcion convertida en tipo de dato entero
            match (opc): 
                case 1:
                    if (self.autenticar_usuario()):
                        
                        match (self.usuario_autenticado.tipo_usuario):
                            case 1:
                                self.mostrar_menu_cliente()
                            case 2:
                                self.mostrar_menu_empleado()
                            case 3:
                                self.mostrar_menu_administrador()
                    else:
                        continue
                case 2:
                    if (self.registrar_usuario()):
                        print("\nUsuario registrado correctamente.")
                    else:
                        print("\nNo se pudo realizar el registro del usuario.")
                
                case 3:
                    print("\n***********Hasta pronto***********")
                    return
                case _:
                    print("Ingresaste una opcion invalida. Intentalo de nuevo.")

            # Sirve para limpiar la pantalla
            input("Presione enter para continuar... ")
            os.system("clear" if os.name =="posix" else "cls")
                    
                            