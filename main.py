# Cosas nuevas
# 1) lower()-- para transformar en minuscula
# 2) from __future__ import print_function-- sirve para usar el metodo print en py 2 y 3
# 3) import os -- Sirve en este caso para incluir os.system("cls")

# Agenda telefonica

from __future__ import print_function

saltoLinea = "\n"
extensionArchivo = ".txt"

import os  # Se incluye para usar el limpa pantalla
import csv # Para trabajar con archivos csv
import time # Obtener la fecha y la hora del sistema

# FUNCIONES- CREAR, ESCRIBIR LEER ARCHIVO
# Crear archivo
def crearArchivo(nombre, extension):
    archivo = open(nombre + extension, "w")
    archivo.close()


# Escribir en archivo
def escribirArchivo(nombre, apellido, numero, email, extension):
    # Persona
    archivo = open(nombre + extension, "a")
    archivo.write(nombre + saltoLinea)
    archivo.write(apellido + saltoLinea)
    archivo.write(numero + saltoLinea)
    archivo.write(email)
    archivo.close()
    # Contactos totales
    archivoContactos = open("contactos" + extension, "a")
    archivoContactos.write(nombre + saltoLinea)
    archivoContactos.close()


# Leer el archivo
def leerArchivo(nombre, extension):
    archivo = open(nombre + extension, "r")
    contacto = archivo.readlines()  # Almacenando cada linea en la lista

# Buscar archivos
def validarExistensia(parametroBusqueda):
    
    archivoContactos = open("contactos" + extensionArchivo, "r")
    lista = listaContactos()
    archivoContactos.close()
    parametroBusqueda = parametroBusqueda + "\n"
    if parametroBusqueda in lista:
        print("Contacto encontrado")
        return True
    else:
        print("Sin resultados")
        return False

#Sirve para buscar un nombre el la lista de contactos y retornar su posiion o indice(como si estuviese en una lista)
#La funcion index retorna la posicion de un elemento en la lista
def posicionNombreEnLista(nombre):
    contactos = listaContactos()
    indice = contactos.index(nombre)
    return indice


# Eliminar contacto
def eliminarArchivoContacto(nombre, extension):
    # Eliminar el archivo
    os.remove(nombre + extension)


# Eliminar elemento de la lsita de contactos
def eliminarContactoLista(indice):
    lista = listaContactos()
    indice = indice - 1
    del (lista[indice])

    # reescribir archivo
    archivoContactos = open("contactos" + extensionArchivo, "w")  # "w" sobreescribe el archivo
    for elemento in lista:
        archivoContactos.write(elemento)
    archivoContactos.close()


# Lista de todos los contactos
def listaContactos():
    archivoContactos = open("contactos" + extensionArchivo, "r")
    listaContactos = archivoContactos.readlines()
    archivoContactos.close()
    return listaContactos  # Se debe manipular como una lista, lista= listaContactos()

##Enviar un mensaje
def guardarMensaje(destinatario,mensaje):
    #Crear nuevo dialecto
    csv.register_dialect("dialectoMensajes",delimiter= "|")
    #Abrir manejador de archivo en modo escritura
    archivo = open ("mensajes.csv","a")
    #Menejador de archivo csv en escritura
    archivoCSV = csv.writer(archivo, dialect="dialectoMensajes")
    #Obtener la fecha del sistema
    fechayHora = time.strftime("%c")
    #Lista con los campos
    listaCampos = [destinatario,mensaje,fechayHora]
    archivoCSV.writerow(listaCampos)
    

#Ver todos los mensajes que se han enviado.
def verMensajesEnviados():
    
    #Crear nuevo dialecto
    csv.register_dialect("newDialecto",delimiter= "|")
    #Abrir manejador de archivo en modo lectura
    archivo = open("mensajes.csv","r")
    #Manejador de archivo csv en modo lectura
    archivoCSV = csv.DictReader(archivo, dialect = "newDialecto")
    
    listaDicc = list(archivoCSV)
    
    i = 0
    print("A continuacion le mostramos todos los mensajes enviados.")
    while i < len(listaDicc):
        j = i + 1
        print ("----------------------------------------------------")
        print ("\n-Mensaje numero --> %d"%(j))
        print ("*Mensaje: ")
        print (listaDicc[i]["mensaje"])
        print ("\n*Destinatario: ")
        print (listaDicc[i]["destinatario"])
        print ("\n*Fecha y Hora :")
        print (listaDicc[i]["horayFecha"])
        print ("----------------------------------------------------")
        i+=1
        print("\n\n")
    
#Eliminar mensajes.
#Sirve para guardar las llamadas realizadas.
def guardarLlamada(destinatario):
    #Crear nuevo dialecto
    csv.register_dialect("dialectoLlamadas",delimiter= "|")
    #Abrir manejador de archivo en modo escritura
    archivo = open ("llamadas.csv","a")
    #Menejador de archivo csv en escritura
    archivoCSV = csv.writer(archivo, dialect="dialectoLlamadas")
    #Obtener la fecha del sistema
    fechayHora = time.strftime("%c")
    #Lista de los campos
    listaCampos = [destinatario,fechayHora]
    archivoCSV.writerow(listaCampos)
    #Cerrar el archivo
    archivo.close()

#Sirve para ver el registro de todas las llamadas que se han realizado.
def verLlamadas():
    
    #Crear nuevo dialecto
    csv.register_dialect("newDialecto",delimiter= "|")
    #Abrir manejador de archivo en modo lectura
    archivo = open("llamadas.csv","r")
    #Manejador de archivo csv en modo lectura
    archivoCSV = csv.DictReader(archivo, dialect = "newDialecto")
    
    listaDicc = list(archivoCSV)
    
    i = 0
    print("A continuacion le mostramos todos los mensajes enviados.")
    while i < len(listaDicc):
        j = i + 1
        print ("----------------------------------------------------")
        print ("\n-Llamada numero --> %d"%(j))
        print ("\n*Destinatario: ")
        print (listaDicc[i]["destinatario"])
        print ("\n*Fecha y Hora :")
        print (listaDicc[i]["horayFecha"])
        print ("----------------------------------------------------")
        i+=1
        print("\n\n")
listaContactos()

#Ver un contacto en especifico
def verContacto(nombre):

    contacto = open(nombre + extensionArchivo, "r")
    cadaCampo = contacto.readlines()
    contacto.close()

    return cadaCampo #Se debe manipular como una lista, contacto= contacto()

#Modificar un campo del contacto
#opc va a ser el numero del campo, sabiendo que poseemos 4 campos
#nombreContacto sera el nombre del contacto que va a modificar

def modificarCampo():

    #Para saber cual de los contacos va a modificar
    nombre = (raw_input("\nPor favor ingrese el nombre del contacto: ").lower())
    print("\n\n--> Los contactos poseen los siguinetes campos: ")
    print("\n\n1) Nombre\t\t2) Apellido")
    print("\n\n3) Numero\t\t4) E-mail")
    indice = (int(raw_input("\nIngrese la opcion: ")))
    indice -= 1
    #Para manejar las posiciones en la lista
    lista = listaContactos()
    # Ver cada campo del contacto.
    camposLista = verContacto(nombre)
    
    #Nombre
    if indice == 0:

        # Eliminar el contacto al que se le cambiara el nombre.
        os.remove(nombre + extensionArchivo)

        print("\nA continuacion le mostramos los campos de este contacto...")

        for campo in camposLista:
            print( saltoLinea + campo )

        camposLista[indice] = "" #Eliminamos el campo nombre en la posicion 0

        nombreMasSalto = nombre + saltoLinea

        posicion = posicionNombreEnLista(nombreMasSalto)

        lista[posicion] = "" #Eliminamos el nombre de la lista de los contactos

        nuevoNombre = (raw_input("\nPor favor ingrese el nuevo nombre: ").lower())

        camposLista[indice] = nuevoNombre + saltoLinea #Almacenamos el nuevo nombre en la posicion 0
        lista[posicion] = nuevoNombre + saltoLinea

        #Reescribir el archivo donde estan almacenados todos los contactos
        listaTodosContactos = open("contactos" + extensionArchivo,"w")

        for nombre in lista:
            listaTodosContactos.write(nombre)

        listaTodosContactos.close()
        #Reescribir el archivo del contacto especifico
        camposContacto = open(nuevoNombre + extensionArchivo, "w")

        for campo in camposLista:

            camposContacto.write(campo)

        camposContacto.close()


    #Apellido
    elif indice == 1:

        print("\nA continuacion le mostramos los campos de este contacto...")

        for campo in camposLista:
            print(saltoLinea + campo)

        camposLista[indice] = ""#Eliminamos el campo apellido
        nuevoApellido = (raw_input("Por favor ingrese el nuevo apellido: "))
        nuevoApellido += saltoLinea
        camposLista[indice] = nuevoApellido

        # Reescribir el archivo del contacto especifico
        camposContacto = open(nombre + extensionArchivo, "w")

        for campo in camposLista:
            camposContacto.write(campo)

        camposContacto.close()

    #Numero
    elif indice == 2:
        print("\nA continuacion le mostramos los campos de este contacto...")

        for campo in camposLista:
            print(saltoLinea + campo)

        camposLista[indice] = ""  # Eliminamos el campo numero de telefono
        nuevoNumero = (raw_input("Por favor ingrese el nuevo numero: "))
        nuevoNumero += saltoLinea
        camposLista[indice] = nuevoNumero

        # Reescribir el archivo del contacto especifico
        camposContacto = open(nombre + extensionArchivo, "w")

        for campo in camposLista:
            camposContacto.write(campo)

        camposContacto.close()

    #E-mail
    elif indice == 3:
        print("\nA continuacion le mostramos los campos de este contacto...")

        for campo in camposLista:
            print(saltoLinea + campo)

        camposLista[indice] = ""  # Eliminamos el campo e-mail
        nuevoEmail = (raw_input("Por favor ingrese el nuevo E-mail: "))
        nuevoEmail += saltoLinea
        camposLista[indice] = nuevoEmail

        # Reescribir el archivo del contacto especifico
        camposContacto = open(nombre + extensionArchivo, "w")

        for campo in camposLista:
            camposContacto.write(campo)

        camposContacto.close()

#---------------------------------------------------------------------------------------------------------------

ciclo = True
while ciclo == True:

    os.system('cls')  # Limpia la pantalla para win.! En linux seria os.system('clear')

    # Menu
    print("""
                ////////////////////////////////////////////////////////
                /---------->Bienvenido a tu agenta personal<----------/
                                    //V 1.0//
                ////////////////////////////////////////////////////////
          
            --------------------------------------------------------------
				    > Menu <

            1) Agregar un nuevo contacto\t2) Eliminar un contacto

            3) Actualizar un contacto\t\t4) Ver un contacto

            5) Buscar un contacto\t\t6) Mensajes

            7) Llamadas\t\t\t\t8) Salir

    """)
    # Recojer opcion
    opc = (int(raw_input("Introduzca su opcion: ")))

    # comparar si es 8, para matar el ciclo y salir
    if opc == 8:
        break

    # Comprobar que sea distinto de alguna opcion para decirle que se equivoco
    elif opc != 1 and opc != 2 and opc != 3 and opc != 4 and opc != 5 and opc != 6 and opc != 7:

        print("\nOpcion invalida")

        # Comprobar si quiere ir al menu principal o salir
        ciclo = (int(raw_input("Ingrese el numero 0 para ir al menu anterior o 8 para salir : ")))

        if ciclo == 8:
            break
# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
    # Primera Funcion -- Agregar un nuevo contacto--------------------------------------------------------------
    elif opc == 1:

        os.system('cls')  # Limpia para win en linux seria os.system('clear')
        print(
            "\n**ATENCION - Si el nombre de usuario que vas a agregar ya esta registrado entonces todos los campos que vas a llenar aqui, van a sustituir los del contacto que ya esta agregado.")
        print("**CONSEJO - Si el nombre ya existe, agregale una letra o palabra que lo diferencie del que ya existe.")

        print("\n1) Si deseas ver la lista de los contactos existentes.")
        print("\n2) Si es un contacto que sabes que no existe.")
        print("\n3) Si deseas volver al menu principal.")

        opc1 = (int(raw_input("\nIngrese la opcion: ")))

        # Verificar la lista de los contactos
        if opc1 == 1:

            os.system('cls')  # Limpia para win en linux seria os.system('clear')
            print ("--> Lista de los contactos")
            lista = listaContactos()
            for i, contacto in enumerate(lista):
                i += 1
                print("\n %d) %s" % (i, contacto))

            print("--> Selecione: ")
            print("\n1) Agregar un nuevo contacto.")
            print("\n2) Volver al menu principal.")
            print("\n3) Salir.")
            opc2 = (int(raw_input("\nIngrese la opcion: ")))

            #Agregar contacto
            if opc2 == 1:

                print ("\n--> Agregando nuevo contacto")
                nombre = (raw_input('\nIntroduzca el nombre: ').lower())
                apellido = (raw_input('\nIntroduzca el apellido: ').lower())
                numero = (raw_input('\nIntroduzca el numero: '))
                email = (raw_input('\nIntroduzca el E-mail: ').lower())

                # llamada de las funciones
                crearArchivo(nombre, extensionArchivo)
                escribirArchivo(nombre, apellido, numero, email, extensionArchivo)
                leerArchivo(nombre, extensionArchivo)

            # Volver Menu principal
            elif opc2 == 2:
                continue
            #Salir del programa
            elif opc2 == 3:
                break

        # Agregar contacto directamente
        elif opc1 == 2:

            print ("\n--> Agregando nuevo contacto")
            nombre = (raw_input('\nIntroduzca el nombre: ').lower())
            apellido = (raw_input('\nIntroduzca el apellido: ').lower())
            numero = (raw_input('\nIntroduzca el numero: '))
            email = (raw_input('\nIntroducza el E-mail: ').lower())
            # llamada de las funciones
            crearArchivo(nombre, extensionArchivo)
            escribirArchivo(nombre, apellido, numero, email, extensionArchivo)
            leerArchivo(nombre, extensionArchivo)

        # Volver Menu principal
        elif opc1 == 3:
            continue


    #Segunda Funcion -- Eliminar un contacto--------------------------------------------------------------------
    elif opc == 2:

        os.system('cls')  # Limpia para win en linux seria os.system('clear')
        print("\n--> Escoja su opcion:")
        print("\n1) Si desea ver la lista de todos los contactos.")
        print("\n2) Ingrese nombre para ver si existe un contacto con ese nombre.")
        print("\n3) Ir al menu principal.")
        print("\n4) Salir.")
        opc1 = (int(raw_input("\nIngrese el numero de su opcion: ")))

        # Mostrar la lista de los contactos, para que escoja cual eliminar
        if opc1 == 1:

            lista = listaContactos()

            for i, contacto in enumerate(lista):
                i += 1
                print("\n %d) %s" % (i, contacto))

            print("\nOpciones:")
            print("\n1) Si eliminar un contacto.")
            print("\n2) Si quiere ir al menu principal.")
            print("\n3) Salir.")
            opc2 = (int(raw_input("\nIngrese la opcion: ")))

            # Eliminar el archivo
            if opc2 == 1:

                nombre = (raw_input('\nIntroduzca el nombre del contacto a eliminar: ').lower())
                indice = (int(raw_input("Ingrese por favor, la enumeracion del contacto para confirmar: ")))
                eliminarArchivoContacto(nombre, extensionArchivo)
                eliminarContactoLista(indice)

            # Volver al menu principal
            elif opc2 == 2:
                continue
            #Salir
            elif opc2 == 3:
                break

        # Busqueda del contacto por nombre
        elif opc1 == 2:

            nombre = (raw_input('\nIntroduzca el nombre: ').lower())
            validarExistensia(nombre)
            # Para frenar el ciclo y se pueda apresiar la impresion de los datos
            raw_input("Presiona enter para continuar")
        elif opc1 == 3:
            continue
        elif opc1 == 4:
            break

    #Tercera Funcion- Actualizar un contacto--------------------------------------------------------------------
    elif opc == 3:

        os.system('cls')  # Limpia para win en linux seria os.system('clear')
        print("\nA continuacion podra modificar cualquier campo del contacto.")
        print("***Atencion, si el cotacto no existe ocurrira un error y el programa se cerrara.")
        print("\n1) Desea ver antes la lista de los contactos.")
        print("\n2) Sabe que el cotacto existe y lo desea actualizar.")
        print("\n3) Ir al menu principal.")
        print("\n4) Salir.")
        opc1 = (int(raw_input("\nIngrese la opcion: ")))
        if opc1 == 1:
            lista = listaContactos()
            print()
            
            for i, contacto in enumerate(lista):
                i += 1
                print ("\n %d) %s" % (i,contacto))
                
            print("\n1) Si desea actualizar un cotacto ahora.")
            print("\n2) Ir al menu principal.")
            print("\n3) Salir.")
            
            opc2 = (int(raw_input("\nIngrese la opcion: ")))
            
            if opc2 == 1:
                modificarCampo()
            elif opc2 == 2:
                continue
            elif opc2 == 3:
                break
                
        elif opc1 == 2:
            modificarCampo()
        
        elif opc1 == 3:
            continue
        elif opc1 == 4:
            break
    #Cuarta Funcion- Ver un contacto
    elif opc == 4:
        os.system("cls")
        nombre = (raw_input("Ingrese el nombre para ver el contacto: ").lower())
        print()
        campos = verContacto(nombre)
        for campo in campos:
            print(campo)

        print("\n1) Ver otro contacto.")
        print("\n2) Ir al menu principal")
        print("\n3) Salir.")
        opc1=(int(raw_input("\nIngrese la opcion: ")))

        if opc1 == 1:
            os.system("cls")

            nombre1 = (raw_input("Ingrese el nombre para ver el contacto: ").lower())
            print()
            lista = verContacto(nombre1)

            for campo in lista:
                print(campo)

            print("\n1) Ir al menu principal")
            print("\n2) Salir.")
            
            opc2 = (int(raw_input("\nIngrese la opcion: ")))

            if opc2 == 1:
                continue
            elif opc2 == 2:
                break
                
        elif opc1 == 2:
            continue #Para terminar la iteracion y pasar a la siguiente.
        
        elif opc1 == 3:
            break
    #Quinta Funcion- Buscar un cotacto.
    elif opc == 5:
        
        os.system("cls")
        
        print("Vamos a buscar un contacto...")
        nombre = (raw_input("\nPor favor nombre para buscarlo: "))
        
        lista = listaContactos()
        #Buscar si el nombre es un contacto o no, si lo es, se le muestra el contacto.
        
        nombreConSalto = nombre + "\n"
        if nombreConSalto in lista:
            campos = verContacto(nombre)
            print("\nBusqueda exitosa.!!")
            print("\nA continuacion le mostramos el contacto.")
            print()
            for campo in campos:
                print(campo)

            print("\n1) Ir al menu principal.")
            print("\n2) Salir.")
            opc1 = (int(raw_input("\nIngrese la opcion: ")))
            
            if opc1 == 1:
                continue
            elif opc1 == 2:
                break
        else:
            print("\nBusqueda infructuosa.!!")
            
            print("\n1) Ir al menu principal.")
            print("\n2) Salir.")
            opc1 = (int(raw_input("\nIngrese la opcion: ")))
            
            if opc1 == 1:
                continue
            elif opc1 == 2:
                break
    
    
    #Sesta Funcion- Enviar un SMS
    elif opc == 6:
        
        os.system("cls")
        print ("Bienvenido a la mensajeria instantanea.")
        print ("\n1) Nuevo mensaje.")
        print ("\n2) Enviados")
        print ("\n3) Ir al menu principal.")
        print ("\n4) Salir.")
        opc1 = (int(raw_input("\nIngrese la opcion: ")))
        
        ##Enviar un mensaje nuevo.
        if opc1 == 1:
            
            os.system("cls")
            print ("1) Enviar a un contacto.")
            print ("\n2) Enviar a un numero desconosido.")
            print ("\n3) Ir al menu principal.")
            print ("\n4) Salir.")
            opc2 = (int(raw_input("\nIngrese la opcion: ")))
            
            #Enviar mensaje a un contacto existente en la agenda
            if opc2 == 1:
                
                os.system("cls")
                print ("A continuacion le mostramos la lista de los contactos: ")
                lista = listaContactos()
                
                for i, contacto in enumerate(lista):
                    i += 1
                    print("\n %d) %s" % (i, contacto))
                num = (int(raw_input("\nIngrese el numero que representa el contacto: ")))
                indiceNombre = num - 1
                
                contactoNombre = lista[indiceNombre].split("\n")
                contactoNombre = contactoNombre[0]
                
                mensaje = (raw_input("\nPor favor Ingrese el mensaje: "))
                
                guardarMensaje(contactoNombre,mensaje)
                
                os.system("cls")
                
                print("\n-->Mensaje enviado con exito.")
                print ("\n\n1) Enviar otro mensaje.")
                print ("\n2) Ir al menu principal.")
                print ("\n3) Salir.")
                opc3 = (int(raw_input("\nIngrese la opcion: ")))
                
                #Enviar otro mensaje
                if opc3 == 1:
                    os.system("cls")
                    print ("A continuacion le mostramos la lista de los contactos: ")
                    lista = listaContactos()
                
                    for i, contacto in enumerate(lista):
                        i += 1
                        print("\n %d) %s" % (i, contacto))
                    num = (int(raw_input("\nIngrese el numero que representa el contacto: ")))
                    indiceNombre = num - 1
                
                    contactoNombre = lista[indiceNombre].split("\n")
                    contactoNombre = contactoNombre[0]
                
                    mensaje = (raw_input("Por favor Ingrese el mensaje: "))
                
                    guardarMensaje(contactoNombre,mensaje)
                    
                    os.system("cls")
                    
                    print("\n-->Mensaje enviado con exito.")
                    print ("\n\n1) Ir al menu principal.")
                    print ("\n2) Salir.")
                    opc4 = (int(raw_input("\nIngrese la opcion: ")))
                    if opc4 == 1:
                        continue
                    elif opc4 == 2:
                        break
                
            #Enviar un numero inexistente en la agenda
                elif opc3 == 2:
                    continue
                elif opc3 == 3:
                    break
                    
                    
            #Enviar un mensaje a un numero no existenete en la agenda.
            
            elif opc2 == 2:
                
                os.system("cls")
                print("Por favor ingrese los siguientes datos para enviar su mensaje.")
                numero = (str(raw_input("\nIngres el numero telefonico: ")))
                mensaje = (raw_input("\nPor favor Ingrese el mensaje: "))
                guardarMensaje(numero,mensaje)
                
                print("\n-->Mensaje enviado con exito.")
                print ("\n\n1) Enviar otro mensaje.")
                print ("\n2) Ir al menu principal.")
                print ("\n3) Salir.")
                opc3 = (int(raw_input("\nIngrese la opcion: ")))
                
                #Enviar otro mensaje
                if opc3 == 1:
                    os.system("cls")
                    print("Por favor ingrese los siguientes datos para enviar su mensaje.")
                    numero = (str(raw_input("\nIngres el numero telefonico: ")))
                    mensaje = (raw_input("\nPor favor Ingrese el mensaje: "))
                    guardarMensaje(numero,mensaje)
                
                    print("\n-->Mensaje enviado con exito.")
                    print ("\n\n1) Ir al menu principal.")
                    print ("\n1) Salir.")
                    opc4 = (int(raw_input("\nIngrese la opcion: ")))
                    
                    if opc4 == 1:
                        continue
                    elif opc4 == 2:
                        break
                
                elif opc3 == 2:
                    continue
                elif opc3 == 3:
                    break
                    
                
            elif opc2 == 3:
                continue
            elif opc2 == 4:
                break
                
        ##Mostrar los mensajes enviados.
        elif opc1 == 2:
            os.system("cls")
            verMensajesEnviados()
            print ("\n\n1) Ir al menu principal.")
            print ("\n2) Salir.")
            opc2 = (int(raw_input("\nIngrese la opcion: ")))
            if opc2 == 1:
                continue
            elif opc2 == 2:
                break
            
        elif opc1 == 3:
            continue
        elif opc1 == 4:
            break
    #Septima Funcion- Llamar
    elif opc == 7:
        os.system("cls")
        print ("Bienvenido al gestor de llamadas.")
        print ("\n1) Realizar una llamada.")
        print ("\n2) Ver el registro de llamadas realizadas.")
        print ("\n3) Ir al menu principal.")
        print ("\n4) Salir.")
        
        opc1 = (int(raw_input("\nIngrese la opcion: ")))
        
        #Realizar un nueva llamada.
        if opc1 == 1:
            os.system("cls")
            print("1) Llamar a un contacto.")
            print("\n2) Llamar a un numero desconocido.")
            print("\n3) Ir al menu principal.")
            print("\n4) Salir.")
            
            opc2 = (int(raw_input("\nIngrese la opcion: ")))
            
            #Llamar un contacto.
            if opc2 == 1:
                os.system("cls")
                print ("A continuacion le mostramos la lista de los contactos: ")
                lista = listaContactos()
                
                for i, contacto in enumerate(lista):
                    i += 1
                    print("\n %d) %s" % (i, contacto))
                num = (int(raw_input("\nIngrese el numero que representa el contacto: ")))
                indiceNombre = num - 1
                
                contactoNombre = lista[indiceNombre].split("\n")
                contactoNombre = contactoNombre[0]
                
                guardarLlamada(contactoNombre)
                
                os.system("cls")
                
                print("\n-->Llamada realizada con exito.")
                print ("\n\n1) Realizar otra llamada.")
                print ("\n2) Ir al menu principal.")
                print ("\n3) Salir.")
                opc3 = (int(raw_input("\nIngrese la opcion: ")))
                
                #Realizar otra llamada
                if opc3 == 1:
                    os.system("cls")
                    print ("A continuacion le mostramos la lista de los contactos: ")
                    lista = listaContactos()
                
                    for i, contacto in enumerate(lista):
                        i += 1
                        print("\n %d) %s" % (i, contacto))
                    num = (int(raw_input("\nIngrese el numero que representa el contacto: ")))
                    indiceNombre = num - 1
                
                    contactoNombre = lista[indiceNombre].split("\n")
                    contactoNombre = contactoNombre[0]
                
                    guardarLlamada(contactoNombre)
                    
                    os.system("cls")
                    
                    print("\n-->Llamada realizada con exito.")
                    print ("\n1) Ir al menu principal.")
                    print ("\n2) Salir.")
                    opc4 = (int(raw_input("\nIngrese la opcion: ")))
                    #Ir al menu principal
                    if opc4 == 2:
                        continue
                    #Salir
                    elif opc4 == 3:
                        break
        #Ver el registro de llamadas realizadas.
                #Ir al menu principal
                elif opc3 == 2:
                    continue
                #Salir
                elif opc3 == 3:
                    break
                
        #Ver el registro de las llamdas realizadas
        elif opc1 == 2:
            os.system("cls")
            verLlamadas()
            print("\n1) Ir al menu principal.")
            print("\n2) Salir.")
            opc1 = (int(raw_input("\nIngrese la opcion: ")))
            if opc1 == 1:
                continue
            elif opc1 == 2:
                break
        #Ir al menu principal
        elif opc1 == 3:
            continue
        elif opc1 == 4:
            break      