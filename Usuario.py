
# Importamos funciones las cuales nos sirven para hacer verificacion de errores al ingreso de datos
import funciones

class Usuario:

    """
    Esta clase almacena la informacion de un usuario que es:
    Nombre
    Tipo de documento
    Numero de documento
    Telefono
    Correo
    Nombre de contacto de emergencia
    Telefono de contacto de emergencia
    Contraseña
    Ademas hay 2 atributos ocultos para el manejo de perfiles del usuario 

    ATRIBUTOS
    nombre_usuario: Es el nombre del usuario
    tipo_documento_usuario: Entre Cedula de Ciudadania, Tarjeta de identidad, Cedula de extranjeria o Pasaporte
    numero_documento_usuario: El numero de documento del usuario de acuerdo a su tipo de documento el cual tambien permite autenticarse en el sistema
    telefono_usuario: Es el numero de telefono del usuario
    correo_usuario: Es la direccion de correo electronico del usuario
    tipo_usuario: Hace referencia al tipo de usuario de acuerdo a los perfiles
    tipo_cliente: Hace referencia a la categoria del cliente
    nombre_contacto_emergencia_usuario: Es el nombre de un contacto de emergencia que asigna el usuario
    telefono_contacto_emergencia_usua: Es el numero de telefono del contacto de emergencia que el usuario registro
    contrasena_usuario: Es la contraseña registrada por el usuario para acceder al sistema, con una longitud minima de 6 y maxima de 16 caracteres

    CONSTANTES

    TIPO_CLIENTE: Contiene la constante que identifica a un usuario con el perfil cliente
    TIPO_EMPLEADO: Contiene la constante que identifica a un usuario con el perfil empleado
    TIPO_ADMINISTRADOR: Contiene la constante que identifica a un usuario con el perfil administrador
    """

    # Atributos
    nombre_usuario = str
    tipo_documento_usuario = str
    numero_documento_usuario = int
    telefono_usuario = int
    correo_usuario = str
    tipo_usuario = int
    tipo_cliente = str
    nombre_contacto_emergencia_usuario = str
    telefono_contacto_emergencia_usuario = int
    contrasena_usuario = str

    # Constantes
    TIPO_CLIENTE = 1
    TIPO_EMPLEADO = 2
    TIPO_ADMIN = 3
    ARCHIVO_USUARIOS = "datos_usuario.npy"
    

    

    # Metodo constructor de la clase: Por defecto el perfil de cualquier usuario es cliente y la categoria regular
    def __init__(self, nombre_usuario = "", tipo_documento_usuario = 0, numero_documento_usuario = 0, telefono_usuario = 0, correo_usuario = "", tipo_usuario = 1, tipo_cliente = "Regular", nombre_contacto_emergencia_usuario = "", telefono_contacto_emergencia_usuario = 0, contraseña_usuario = ""):
        
        self.nombre_usuario = nombre_usuario
        self.tipo_documento_usuario = tipo_documento_usuario
        self.numero_documento_usuario = numero_documento_usuario
        self.telefono_usuario = telefono_usuario
        self.correo_usuario = correo_usuario
        self.tipo_cliente = tipo_cliente
        self.nombre_contacto_emergencia_usuario = nombre_contacto_emergencia_usuario
        self.telefono_contacto_emergencia_usuario = telefono_contacto_emergencia_usuario
        self.tipo_usuario = tipo_usuario
        self.contrasena_usuario = contraseña_usuario

    # Este metodo pide por consola los datos para el registro del usuario
    def pedir_datos_usuario(self):

        # Se pide el nombre del usuario
        self.nombre_usuario = input("\nIngrese su nombre completo: ")
        while(funciones.validar_cadena_caracteres(self.nombre_usuario)): # Se valida el nombre y se pide el hasta que se ingrese bien
            self.nombre_usuario = input("\nIngrese su nombre completo: ")
        
        while (True):
            try:  
                # Se pide el tipo de documento del usuario
                self.tipo_documento_usuario = int(input("\nIngrese el tipo de documento de identidad\n \n1.Cedula de Ciudadania \n2.Tarjeta de Identidad \n3.Cedula de Extranjeria \n4.Pasaporte\nRespuesta: "))
                match(self.tipo_documento_usuario):
                    case 1:
                        self.tipo_documento_usuario = "CC"
                        break
                    case 2:
                        self.tipo_documento_usuario = "TI"
                        break
                    case 3: 
                        self.tipo_documento_usuario = "CE"
                        break
                    case 4:
                        self.tipo_documento_usuario = "Pasaporte"
                        break
                    case _: 
                        print("\nIngresaste una opcion no valida. Intentalo de nuevo\n")
                        
            except ValueError:
                print("\nHaz ingresado un caracterer invalido. Inténtalo de nuevo\n")
                

        while(True):

            #Se pide el numero de documento de acuerdo al tipo de documento
            if (self.tipo_documento_usuario == "Pasaporte"): # Si el usuario ingresa Pasaporte, se solicita que ingrese los numeros dentro del pasaporte en el orden correspondiente.
                self.numero_documento_usuario = (input("\nIngrese los numeros dentro de su codigo de pasaporte en el orden correspondiente: "))
                while (funciones.validar_entero_mayor_0(self.numero_documento_usuario)):
                    self.numero_documento_usuario = (input("\nIngrese los numeros dentro de su codigo de pasaporte en el orden correspondiente: "))
                self.numero_documento_usuario = int(self.numero_documento_usuario)

                break
            
            else:
                self.numero_documento_usuario = (input("\nIngrese su numero de documento: "))
                while(funciones.validar_entero_mayor_0(self.numero_documento_usuario)): # Se valida el numero del documento y se pide hasta que se ingrese bien
                    self.numero_documento_usuario = (input("\nIngrese su numero de documento: "))
                self.numero_documento_usuario = int(self.numero_documento_usuario) # Se deja el numero de documento convertido en tipo de dato entero
                
                break   
            
        # Se pide el numero de telefono del usuario
        self.telefono_usuario = input("\nIngrese su número de telefono: ")
        while (funciones.validar_longitud(self.telefono_usuario)): # Se valida el numero de telefono y se pide hasta que se ingrese bien
            self.telefono_usuario = input("\nIngrese su número de telefono: ")
        self.telefono_usuario = int(self.telefono_usuario) # Se deja el numero de telefono convertido en tipo de dato entero
            
        # Se pide el correo electronico del usuario
        self.correo_usuario = input("\nIngrese su correo electronico: ")     
        while (funciones.validar_cadena_caracteres(self.correo_usuario)): # Se valida el correo electronico y se pide hasta que se ingrese bien
            self.correo_usuario = input("\nIngrese su correo electronico: ")
        
        # Se pide el nombre de contacto de emergencia del usuario
        self.nombre_contacto_emergencia_usuario = input("\nIngrese el nombre de un contacto de emergencia: ")    
        while (funciones.validar_cadena_caracteres(self.nombre_contacto_emergencia_usuario)): # Se valida el nombre de contacto de emergencia y se pide hasta que se ingrese bien
            self.nombre_contacto_emergencia_usuario = input("\nIngrese el nombre de un contacto de emergencia: ")
                    
        # Se pide el numero de telefono del contacto de emergencia del usuario  
        self.telefono_contacto_emergencia_usuario = (input("\nIngrese el telefono de su contacto de emergencia: "))
        while (funciones.validar_longitud(self.telefono_contacto_emergencia_usuario)): # Se valida el numero de telefono del contacto de emergencia y se pide hasta que se ingrese bien
            self.telefono_contacto_emergencia_usuario = (input("\nIngrese el telefono de su contacto de emergencia: "))
        self.telefono_contacto_emergencia_usuario = int(self.telefono_contacto_emergencia_usuario) #Se deja el telefono del contacto de emegerncia convertido en tipo de dato entero
        
        while(True):

            # Se pide la contraseña del usuario de minimo 6 caracteres y maximo 16
            self.contrasena_usuario = input("\nIngrese la contraseña con la que va a ingresar al sistema. Tenga en cuenta que debe tener un minimo de 6 caracteres, y un maximo de 16.\nContraseña: ")
            while(funciones.validar_no_vacio(self.contrasena_usuario)): #Se valida la contraseña y se pide hasta que se ingrese bien
                self.contrasena_usuario = input("\nIngrese la contraseña con la que va a ingresar al sistema. Tenga en cuenta que debe tener un minimo de 6 caracteres, y maximo 16 caracteres.\nContraseña: ")
            if (6 <= len(self.contrasena_usuario) and len(self.contrasena_usuario) <= 16 ): # Se valida la condicion de longitud de la contraseña
                print("\nContraseña registrada correctamente.")
                break
            else: # Se separa el error de longitud de la contraseña
                if (len(self.contrasena_usuario) < 6): 
                    print("\nLa contraseña ingresada es demasiado corta. Intentalo de nuevo.")
                else:
                    if (len(self.contrasena_usuario )  > 16):
                        print("\nLa contraseña ingresada es demasiado larga. Intentalo de nuevo.")
            
        
        
        

        
                



        

                
               
                


                
                



        



        








