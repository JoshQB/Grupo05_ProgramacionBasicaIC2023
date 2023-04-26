# Ingenieria en sistemas de la computacion
# curso: Programacion basica
# Entrega final
# Grupo 5
# Autores: BARRIENTOS ACUÑA KENNETH ANDREY / QUESADA BONILLA JOSEPH DAVID 
# Profesor: CAMACHO MORA ALVARO DIONISIO

# coding=utf-8

from getpass import getpass
import os
import random
import shutil

errores = 0

def leerArchivo(documento):
    # Abre el archivo en modo de lectura ('r') y lo asigna a la variable 'archivo'. El 'with' asegura que el archivo se cierre correctamente después de su uso.
    with open(documento, 'r') as archivo:
        # Lee todas las líneas del archivo y las guarda en una lista llamada 'lineas'.
        lineas = archivo.readlines()  
        # Crea una nueva lista llamada 'lineas_sin_salto' que contiene las líneas leídas del archivo, pero sin los caracteres de salto de línea al final de cada línea, utilizando el método 'strip()' para eliminar esos caracteres.
        lineas_sin_salto = [linea.strip() for linea in lineas]
        # Devuelve la lista 'lineas_sin_salto' que contiene las líneas del archivo sin caracteres de salto de línea al final.
        return lineas_sin_salto  

    
def escribirArchivoSaldos(moneda, monto, documento):
    if not os.path.exists(documento):  # Verifica si el archivo no existe en el sistema de archivos.
        with open(documento, 'w') as archivo:  # Si el archivo no existe, lo crea en modo de escritura ('w') y lo asigna a la variable 'archivo'.
            archivo.write("Hola")  # Escribe la palabra "Hola" en el archivo.

    texto = ['Colones\n', '0\n', 'Dolares\n', '0\n', 'Bitcoin\n', '0\n']  # Crea una lista llamada 'texto' que contiene líneas de texto con nombres de monedas y montos iniciales en 0, con caracteres de salto de línea al final.

    if(moneda == 1):  # Si la moneda es igual a 1 (representando colones).
        texto[1] = str(monto) + "\n"  # Actualiza el valor del monto en la posición 1 de la lista 'texto' 
    if(moneda == 2):  # Si la moneda es igual a 2 (representando dólares).
        texto[3] = str(monto) + "\n"  # Actualiza el valor del monto en la posición 3 de la lista 'texto' 
    if(moneda == 3):  # Si la moneda es igual a 3 (representando bitcoins).
        texto[5] = str(monto) + "\n"  # Actualiza el valor del monto en la posición 5 de la lista 'texto' 

    with open(documento, 'w') as archivo:  # Abre el archivo en modo de escritura ('w') y lo asigna a la variable 'archivo', sobrescribiendo su contenido existente.
        for linea in texto:  # Recorre cada línea en la lista 'texto'.
            archivo.write(linea)  # Escribe cada línea en el archivo.

def reescribirArchivoSaldo(montoC, montoD, montoB, documento):
    if not os.path.exists(documento):  # Verifica si el archivo no existe en el sistema de archivos.
        with open(documento, 'w') as archivo:  # Si el archivo no existe, lo crea en modo de escritura ('w') y lo asigna a la variable 'archivo'.
            archivo.write("Hola")  # Escribe la palabra "Hola" en el archivo.

    texto = ['Colones\n', '0\n', 'Dolares\n', '0\n', 'Bitcoin\n', '0\n']  # Crea una lista llamada 'texto' que contiene líneas de texto con nombres de monedas y montos iniciales en 0, con caracteres de salto de línea al final.

    texto[1] = str(montoC) + "\n"  # Actualiza el valor del monto de colones en la posición 1 de la lista 'texto' 
    texto[3] = str(montoD) + "\n"  # Actualiza el valor del monto de dólares en la posición 3 de la lista 'texto' 
    texto[5] = str(montoB) + "\n"  # Actualiza el valor del monto de bitcoins en la posición 5 de la lista 'texto' 

    with open(documento, 'w') as archivo:  # Abre el archivo en modo de escritura ('w') y lo asigna a la variable 'archivo', sobrescribiendo su contenido existente.
        for linea in texto:  # Recorre cada línea en la lista 'texto'.
            archivo.write(linea)  # Escribe cada línea en el archivo.



def reescribirArchivoUsuarios(usuarios,cedula):
    with open("usuarios_pines.txt", 'w') as archivo:
            archivo.write(usuarios[0]+"\n")

    indice_usuario = usuarios.index(cedula)
    del usuarios[indice_usuario:indice_usuario+4]
    print (usuarios)
    for i in range(1,len(usuarios)):
        dato = usuarios[i]
        if(i < len(usuarios)-1):
            with open("usuarios_pines.txt", mode="a") as archivo:
                    archivo.write(dato + "\n")
            
        else:
            with open("usuarios_pines.txt", mode="a") as archivo:
                archivo.write(dato)
                        


#Esta funcion se usa realizar el primer deposito de un nuevo usuario
def depositoRegistro(divisas):
    divisas = leerArchivo(divisas)
    global errores
    monto = 0
    depositoValido = False
    moneda = 0
    print("\n------------------------------------------------------------------")
    print("\n                     ---- Cuentas disponibles ----\n")
    print("1. Colones")
    print("2. Dolares")
    print("3. Bitcoin")

    print("\n------------------------------------------------------------------")
    
    opcion = input("Seleccione a cual cuenta desea acreditar el deposito: ")
    
    if opcion == "1":
        print("\n------------------------------------------------------------------\n")
        print("Ha seleccionado la cuenta de Colones.\n")
        monto = float(input("Digite el monto que desea ingresar: "))
        if(monto >= 100000):
            depositoValido = True
            moneda = 1
            return depositoValido,moneda,monto
        else:
            errores += 1
            print("Debe ser un monto igual o mayor a 100000 colones.\n")
        
    elif opcion == "2":
        print("Ha seleccionado la cuenta de Dolares.")
        monto = float(input("Digite el monto que desea ingresar: "))
        monto2 = monto*float(divisas[1])
        if(monto2 >= 100000):
            depositoValido = True
            moneda = 2
            return depositoValido,moneda,monto
        else:
            errores += 1
            print("Debe ser un monto igual o mayor a 100000 colones.\n")
        
    elif opcion == "3":
        print("Ha seleccionado la cuenta de Bitcoin.")
        monto = float(input("Digite el monto que desea ingresar: "))
        monto2 = monto*float(divisas[0])
        if(monto2 >= 100000):
            depositoValido = True
            moneda = 3
            return depositoValido,moneda,monto
        else:
            errores += 1
            print("Debe ser un monto igual o mayor a 100000 colones.\n")

    else:
        print("Opción inválida. Por favor seleccione una opción del 1 al 3.")

    return depositoValido,moneda,monto

def crearServicios(ruta_carpeta):
    contador = 0 # Inicializa un contador en 0 para llevar el registro de cuántos servicios activos se han creado
    servicios = ['Agua','Electricidad','Telefonia','Internet','Impuestos','Colegios Profesionales','Tarjeta de credito']
    for i in range(len(servicios)):
        ruta = str(i+1) + ".txt"
        ruta_archivo = os.path.join(ruta_carpeta, ruta)  # Une la ruta de la carpeta con el nombre del archivo generado para obtener la ruta completa del archivo.
        with open(ruta_archivo, 'w') as archivo:
            archivo.write(servicios[i]+"\n")
            #Les ponemos probabilidad para asegurarnos que sean almenos 3 activos
            if(contador<3):
                valores = [0,1]
                probabilidades = [0.3,0.7]
            else:
                valores = [0,1]
                probabilidades = [0.5,0.5]
            valorAleatorio = random.choices(valores, weights=probabilidades)[0]
            if(valorAleatorio == 1):
                contador += 1
            archivo.write(str(valorAleatorio)+ "\n")
            valorAleatorioMonto = random.randint(1000,100000)  # Genera un valor aleatorio para el monto del servicio
            archivo.write(str(valorAleatorioMonto))

                
#Funcion para registrar nuevos usuarios
def registrarUsario():
    usuarios = []
    existe = False
    #Cantidad de errores permitidos
    global errores
    #Booleano para saber si es valido el primero deposito
    #Si errores es mayor a 3 se sale
    while(errores < 3):
        cedula = input("Ingrese el numero de cedula: ")
        #verifica que la cedula no tenga mas de 9 digitos
        if(len(cedula)>9):
            print("ERROR, el numero de cedula no puede tener mas de nueve digitos")
            errores += 1
        #verifica que la cedula no tenga menos de 9 digitos
        elif(len(cedula)<9):
            print("ERROR, el numero de cedula no puede tener menos de nueve digitos")
            errores += 1
        #Aqui leemos el archivo de texto y lo transformamos a una lista cada linea
        usuarios = leerArchivo('usuarios_pines.txt')
        for linea in usuarios:
            #verificamos que el usuario exista
            if(linea == cedula):
                existe = True
        if(existe):
             errores += 1
             existe = False
             print("ERROR, el usuario ya se encuentra registrado, intente nuevamente")
        elif(len(cedula)==9 and existe == False):
             nombre = input("Ingrese su nombre: ")
             while True:
                pin_ingresado = getpass('Ingrese su PIN de 4 dígitos: ')
                #verificamos que el pin tegna 4 digitos
                if(len(pin_ingresado)==4):
                    pin_segundo = getpass('Ingrese nuevamente el PIN: ')
                    if pin_ingresado == pin_segundo:
                        print('PIN correcto\n\n')
                        print("Para poder registrar al usuario se debe de realizar un deposito de minimo 100.000 colones\n")
                        errores = 0
                        while(errores < 3):
                            depositoValido,moneda,monto = depositoRegistro('tipos_de_cambio.txt')
                            if(depositoValido):
                                #Con esto creamos la carpeta con el numero de cedula
                                ruta_carpeta = os.path.join(os.getcwd(), cedula)
                                os.mkdir(cedula) 
                                #Carpeta para el saldo de las cuentas
                                ruta_archivoSaldos = os.path.join(ruta_carpeta, 'Saldos')
                                ruta_archivoSaldos2 =  os.path.join(ruta_archivoSaldos, 'Saldos.txt')
                                os.mkdir(ruta_archivoSaldos) 
                                #Carpeta para los servicios                          
                                ruta_archivoServicios = os.path.join(ruta_carpeta, 'Servicios')
                                os.mkdir(ruta_archivoServicios) 
                                escribirArchivoSaldos(moneda,monto,ruta_archivoSaldos2)
                                crearServicios(ruta_archivoServicios)
                                #Estas lineas son para agregar al nuevo usuario
                                with open("usuarios_pines.txt", mode="a") as archivo:
                                    archivo.write("\n" + cedula + "\n")
                                    archivo.write(nombre + "\n")
                                    archivo.write(pin_segundo)
                                    return 0
                        break
                    else:
                        print('ERROR, Los PIN no coinciden. Vuelva a intentarlo.')
                        print("Continuemos")
                else:
                    print("ERROR, el PIN debe contener 4 digitos")
        

    errores = 0
    return 0


def retirarDinero(cedula):
    global errores
    errores = 0
    #Aqui escogemos la carpeta que vamos a usar
    ruta_carpeta = os.path.join(os.getcwd(), cedula)
    ruta_archivoSaldos = os.path.join(ruta_carpeta, 'Saldos')
    ruta_archivoSaldos2 =  os.path.join(ruta_archivoSaldos, 'Saldos.txt')
    #Aqui esta la lista con los saldos de las cuentas
    saldo = leerArchivo(ruta_archivoSaldos2)

    print("\n------------------------------------------------------------------")
    print("\n                     ---- Cuentas disponibles ----\n")
    print("1. Colones")
    print("2. Dolares")
    print("3. Bitcoin")

    print("\n------------------------------------------------------------------")
    
    opcion = input("Seleccione a cual cuenta desea realizarle el retiro: ")
    
    if opcion == "1":
        print("\n------------------------------------------------------------------\n")
        print("Ha seleccionado la cuenta de Colones.\n")
        while(errores < 3):
            monto = float(input("Digite el monto que desea retirar: "))
            if(monto <= float(saldo[1])):
                saldoNuevo = str(float(saldo[1]) - monto)
                print("Se retiro el dinero exitosamente\n")
                print("Su saldo actual es de: " + saldoNuevo)
                reescribirArchivoSaldo(saldoNuevo,saldo[3],saldo[5],ruta_archivoSaldos2)
                return 0
            else:
                errores += 1
                print("Saldo insuficiente, ingrese un monto valido.\n")
        return 0
        
    elif opcion == "2":
        print("\n------------------------------------------------------------------\n")
        print("Ha seleccionado la cuenta de Dolares.\n")
        while(errores < 3):
            monto = float(input("Digite el monto que desea retirar: "))
            if(monto <= float(saldo[3])):
                saldoNuevo = str(float(saldo[3]) - monto)
                print("Se retiro el dinero exitosamente\n")
                print("Su saldo actual es de: " + saldoNuevo)
                reescribirArchivoSaldo(saldo[1],saldoNuevo,saldo[5],ruta_archivoSaldos2)
                return 0
            else:
                errores += 1
                print("Saldo insuficiente, ingrese un monto valido.\n")
        return 0
        
    elif opcion == "3":
        print("\n------------------------------------------------------------------\n")
        print("Ha seleccionado la cuenta de Bitcoins.\n")
        while(errores < 3):
            monto = float(input("Digite el monto que desea retirar: "))
            if(monto <= float(saldo[5])):
                saldoNuevo = str(float(saldo[5]) - monto)
                print("Se retiro el dinero exitosamente\n")
                print("Su saldo actual es de: " + saldoNuevo)
                reescribirArchivoSaldo(saldo[1],saldo[3],saldoNuevo,ruta_archivoSaldos2)
                return 0
            else:
                errores += 1
                print("Saldo insuficiente, ingrese un monto valido.\n")
        return 0

    else:
        print("Opción inválida. Por favor seleccione una opción del 1 al 3.")

def depositarDinero(cedula):
    global errores
    errores = 0
    #Aqui escogemos la carpeta que vamos a usar
    ruta_carpeta = os.path.join(os.getcwd(), cedula)
    ruta_archivoSaldos = os.path.join(ruta_carpeta, 'Saldos')
    ruta_archivoSaldos2 =  os.path.join(ruta_archivoSaldos, 'Saldos.txt')
    #Aqui esta la lista con los saldos de las cuentas
    saldo = leerArchivo(ruta_archivoSaldos2)


    print("\n------------------------------------------------------------------")
    print("\n                     ---- Cuentas disponibles ----\n")
    print("1. Colones")
    print("2. Dolares")
    print("3. Bitcoin")

    print("\n------------------------------------------------------------------")
    
    opcion = input("Seleccione a cual cuenta desea realizarle el deposito: ")
    
    if opcion == "1":
        print("\n------------------------------------------------------------------\n")
        print("Ha seleccionado la cuenta de Colones.\n")
        while(errores < 3):
            monto = float(input("Digite el monto que desea depositar: "))
            if(monto > 0):
                saldoNuevo = str(float(saldo[1]) + monto)
                print("Se retiro el dinero exitosamente\n")
                print("Su saldo actual es de: " + saldoNuevo)
                reescribirArchivoSaldo(saldoNuevo,saldo[3],saldo[5],ruta_archivoSaldos2)
                return 0
            else:
                errores += 1
                print("Ingrese un valor positivo mayor que cero.\n")
        return 0
        
    elif opcion == "2":
        print("\n------------------------------------------------------------------\n")
        print("Ha seleccionado la cuenta de Dolares.\n")
        while(errores < 3):
            monto = float(input("Digite el monto que desea depositar: "))
            if(monto > 0):
                saldoNuevo = str(float(saldo[3]) + monto)
                print("Se deposito el dinero exitosamente\n")
                print("Su saldo actual es de: " + saldoNuevo)
                reescribirArchivoSaldo(saldo[1],saldoNuevo,saldo[5],ruta_archivoSaldos2)
                return 0
            else:
                errores += 1
                print("Ingrese un valor positivo mayor que cero.\n")
        return 0
        
    elif opcion == "3":
        print("\n------------------------------------------------------------------\n")
        print("Ha seleccionado la cuenta de Bitcoins.\n")
        while(errores < 3):
            monto = float(input("Digite el monto que desea depositar: "))
            if(monto > 0):
                saldoNuevo = str(float(saldo[5]) + monto)
                print("Se deposito el dinero exitosamente\n")
                print("Su saldo actual es de: " + saldoNuevo)
                reescribirArchivoSaldo(saldo[1],saldo[3],saldoNuevo,ruta_archivoSaldos2)
                return 0
            else:
                errores += 1
                print("Ingrese un valor positivo mayor que cero.\n")
        return 0

    else:
        print("Opción inválida. Por favor seleccione una opción del 1 al 3.")    

def verSaldo(cedula):
    #Aqui escogemos la carpeta que vamos a usar
    ruta_carpeta = os.path.join(os.getcwd(), cedula)
    ruta_archivoSaldos = os.path.join(ruta_carpeta, 'Saldos')
    ruta_archivoSaldos2 =  os.path.join(ruta_archivoSaldos, 'Saldos.txt')
    #Aqui esta la lista con los saldos de las cuentas
    saldo = leerArchivo(ruta_archivoSaldos2)

    print("\n------------------------------------------------------------------")
    print("\n                     ---- Saldos disponibles disponibles ----\n")
    print("1. Colones: " + saldo[1])
    print("2. Dolares: " + saldo[3])
    print("3. Bitcoin: " + saldo[5])


def pagarServiciosAux(cedula,saldo):
    #Aqui se selecciona la carpeta con los saldos
    ruta_carpeta = os.path.join(os.getcwd(), cedula)
    ruta_archivoSaldos = os.path.join(ruta_carpeta, 'Saldos')
    ruta_archivoSaldos2 =  os.path.join(ruta_archivoSaldos, 'Saldos.txt')
    #Aqui estan los saldos de la cuenta entre 1,3,5
    saldosCuenta = leerArchivo(ruta_archivoSaldos2)
    #Aqui estan las divisas
    divisas = leerArchivo('tipos_de_cambio.txt')
    cambioBitcoin = divisas[6]
    montoBitcoin = float(saldo)/float(cambioBitcoin)
    cambioDolar = divisas[7]
    montoDolar = float(saldo)/float(cambioDolar)
    while True:
            print("Seleccione con la cuenta que desea pagar: ")
            print("1. Colones")
            print("2. Dolares")
            print("3. Bitcoin")
        
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                if(float(saldo) <= float(saldosCuenta[1])):
                    nuevoSaldo = float(saldosCuenta[1]) - float(saldo)
                    reescribirArchivoSaldo(str(nuevoSaldo),saldosCuenta[3],saldosCuenta[5],ruta_archivoSaldos2)
                    print("Se realizo el pago exitosamente\n")
                    return True,nuevoSaldo
                else:
                    print("El saldo en la cuenta seleccionada no es suficiente")
                    return False,0

            elif opcion == "2":
                if(float(montoDolar) <= float(saldosCuenta[3])):
                    nuevoSaldo = float(saldosCuenta[3]) - float(montoDolar)
                    reescribirArchivoSaldo(saldosCuenta[1],str(nuevoSaldo),saldosCuenta[5],ruta_archivoSaldos2)
                    print("Se realizo el pago exitosamente\n")
                    return True,nuevoSaldo
                else:
                    print("El saldo en la cuenta seleccionada no es suficiente")
                    return False,0
            elif opcion == "3":
                if(float(montoBitcoin) <= float(saldosCuenta[5])):
                    nuevoSaldo = float(saldosCuenta[5]) - float(montoBitcoin)
                    reescribirArchivoSaldo(saldosCuenta[1],saldosCuenta[3],str(nuevoSaldo),ruta_archivoSaldos2)
                    print("Se realizo el pago exitosamente\n")
                    return True,nuevoSaldo
                else:
                    print("El saldo en la cuenta seleccionada no es suficiente")
                    return False,0

#Aqui se modifica el archivo de servicios una vez pague
def pagar(rutaArchivo,servicioBase,cedula):
    for i in range(7):
        ruta = str(i+1) + ".txt"
        ruta_archivoSaldos2 =  os.path.join(rutaArchivo, ruta)
        servicio = leerArchivo(ruta_archivoSaldos2)
        if(servicio[0] == servicioBase):
            if(servicio[1] == '1'):
                print("El saldo a pagar es: " + servicio[2] + " colones")
                finalizado,monto = pagarServiciosAux(cedula,servicio[2])
                if(finalizado):
                    with open(ruta_archivoSaldos2, 'w') as archivo:
                        archivo.write(servicio[0]+"\n")
                        archivo.write(str(0)+ "\n")
                        archivo.write(str(0))
                        return 0
            else:
                print("El servicio se encuentra inactivo, volviendo al menu de servicios...")
                return 0   



def pagarServicios(cedula):
    ruta_carpeta = os.path.join(os.getcwd(), cedula)
    ruta_archivoSaldos = os.path.join(ruta_carpeta, 'Servicios')
    while True:
        while True:
            finalizado = False
            print("----------------------------------------\n")
            print("Bienvenido al menú de servicios\n")
            print("Seleccione el servicio que desea pagar: ")
            print("1. Electricidad")
            print("2. Agua")
            print("3. Telefonía")
            print("4. Internet")
            print("5. Impuestos")
            print("6. Colegios Profesionales")
            print("7. Tarjeta de crédito")
            print("8. Salir\n")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                pagar(ruta_archivoSaldos,'Electricidad',cedula)
                return 0
            elif opcion == "2":
                pagar(ruta_archivoSaldos,'Agua',cedula)
                return 0
            elif opcion == "3":
                pagar(ruta_archivoSaldos,'Telefonia',cedula)
                return 0
            elif opcion == "4":
                pagar(ruta_archivoSaldos,'Internet',cedula)
                return 0
            elif opcion == "5":
                pagar(ruta_archivoSaldos,'Impuestos',cedula)
                return 0
            elif opcion == "6":
                pagar(ruta_archivoSaldos,'Colegios Profesionales',cedula)
                return 0
            elif opcion == "7":
                pagar(ruta_archivoSaldos,'Tarjeta de credito',cedula)
                return 0
            elif opcion == "8":
                # Salir del programa
                print("Gracias por utilizar nuestros servicios")
                return 0
            else:
                print("Opción inválida, por favor seleccione una opción del menú")



def compraDivisas(ruta_archivoSaldos2, cuentaOrigen, cuentaDestino):
    saldos = leerArchivo(ruta_archivoSaldos2)
    divisas = leerArchivo('tipos_de_cambio.txt')

    #Tipos de cambio
    #Compra de colones
    colonXbitcoin = float(divisas[6])
    colonXdolar = float(divisas[7])
    #Compra de bitcoin
    bitcoinXcolones = float(divisas[8])
    bitcoinXdolar = float(divisas[9])
    #Compra de dolares
    dolarXcolones = float(divisas[10])
    dolarXbitcoin = float(divisas[11])

    #Saldos dsponibles
    saldoColones = saldos[1]
    saldoDolares = saldos[3]
    saldoBitcoins = saldos[5]

    compra = float(input("Digite la cantidad que desea comprar: "))

    #Compra de colones
    if(cuentaDestino == 1):
        if(cuentaOrigen == 2):
            compraAux = compra/colonXdolar
            if(float(compraAux) <= float(saldoDolares)):
                    compra += float(saldoColones)
                    nuevoSaldo = float(saldoDolares) - float(compraAux)
                    reescribirArchivoSaldo(str(compra),str(nuevoSaldo),saldoBitcoins,ruta_archivoSaldos2)
                    print("Se realizo la compra exitosamente\n")
            else:
                print("No posee saldo suficiente para realizar la compra")
        elif(cuentaOrigen == 3):
            compraAux = compra/colonXbitcoin
            if(float(compraAux) <= float(saldoBitcoins)):
                    compra += float(saldoColones)
                    nuevoSaldo = float(saldoBitcoins) - float(compraAux)
                    reescribirArchivoSaldo(str(compra),saldoDolares,str(nuevoSaldo),ruta_archivoSaldos2)
                    print("Se realizo la compra exitosamente\n")
            else:
                print("No posee saldo suficiente para realizar la compra")

    #Compra de dolares
    elif(cuentaDestino == 2):
        if(cuentaOrigen == 1):
            compraAux = compra*dolarXcolones
            if(float(compraAux) <= float(saldoColones)):
                    compra += float(saldoDolares)
                    nuevoSaldo = float(saldoColones) - float(compraAux)
                    reescribirArchivoSaldo(str(nuevoSaldo),str(compra),saldoBitcoins,ruta_archivoSaldos2)
                    print("Se realizo la compra exitosamente\n")
            else:
                print("No posee saldo suficiente para realizar la compra")
        elif(cuentaOrigen == 3):
            compraAux = compra*dolarXbitcoin
            if(float(compraAux) <= float(saldoBitcoins)):
                    compra += float(saldoDolares)
                    nuevoSaldo = float(saldoBitcoins) - float(compraAux)
                    reescribirArchivoSaldo(saldoColones,str(compra),str(nuevoSaldo),ruta_archivoSaldos2)
                    print("Se realizo la compra exitosamente\n")
            else:
                print("No posee saldo suficiente para realizar la compra")


    #Compra de bitcoins
    elif(cuentaDestino == 3):
        if(cuentaOrigen == 1):
            compraAux = compra*bitcoinXcolones
            if(float(compraAux) <= float(saldoColones)):
                    compra += float(saldoBitcoins)
                    nuevoSaldo = float(saldoColones) - float(compraAux)
                    reescribirArchivoSaldo(str(nuevoSaldo),saldoDolares,str(compra),ruta_archivoSaldos2)
                    print("Se realizo la compra exitosamente\n")
            else:
                print("No posee saldo suficiente para realizar la compra")

        elif(cuentaOrigen == 2):
            compraAux = compra*bitcoinXdolar
            if(float(compraAux) <= float(saldoDolares)):
                    compra += float(saldoBitcoins)
                    nuevoSaldo = float(saldoDolares) - float(compraAux)
                    reescribirArchivoSaldo(str(nuevoSaldo),saldoColones,str(compra),ruta_archivoSaldos2)
                    print("Se realizo la compra exitosamente\n")
            else:
                print("No posee saldo suficiente para realizar la compra")



def ventaDivisas(ruta_archivoSaldos2,cuentaOrigen, cuentaDestino):
    saldos = leerArchivo(ruta_archivoSaldos2)
    divisas = leerArchivo('tipos_de_cambio.txt')

    #Tipos de cambio
    #Compra de colones
    colonXbitcoin = float(divisas[0])
    colonXdolar = float(divisas[1])
    #Compra de bitcoin
    bitcoinXcolones = float(divisas[2])
    bitcoinXdolar = float(divisas[3])
    #Compra de dolares
    dolarXcolones = float(divisas[4])
    dolarXbitcoin = float(divisas[5])

    #Saldos dsponibles
    saldoColones = saldos[1]
    saldoDolares = saldos[3]
    saldoBitcoins = saldos[5]

    venta = float(input("Digite la cantidad que desea vender: "))


    #Venta de colones
    if(cuentaDestino == 1):
        if(cuentaOrigen == 2):
            ventaAux = venta/colonXdolar
            if(float(venta) <= float(saldoColones)):
                    ventaAux += float(saldoDolares)
                    nuevoSaldo = float(saldoColones) - float(venta)
                    reescribirArchivoSaldo(str(nuevoSaldo),str(ventaAux),saldoBitcoins,ruta_archivoSaldos2)
                    print("Se realizo la venta exitosamente\n")
            else:
                print("No posee saldo suficiente para realizar la venta")
        elif(cuentaOrigen == 3):
            ventaAux = venta/colonXbitcoin
            if(float(venta) <= float(saldoColones)):
                    ventaAux += float(saldoBitcoins)
                    nuevoSaldo = float(saldoColones) - float(venta)
                    reescribirArchivoSaldo(str(nuevoSaldo),saldoDolares,str(ventaAux),ruta_archivoSaldos2)
                    print("Se realizo la venta exitosamente\n")
            else:
                print("No posee saldo suficiente para realizar la venta")

    #Venta de dolares
    elif(cuentaDestino == 2):
        if(cuentaOrigen == 1):
            ventaAux = venta*dolarXcolones
            if(float(venta) <= float(saldoDolares)):
                    ventaAux += float(saldoColones)
                    nuevoSaldo = float(saldoDolares) - float(venta)
                    reescribirArchivoSaldo(str(ventaAux),str(nuevoSaldo),saldoBitcoins,ruta_archivoSaldos2)
                    print("Se realizo la venta exitosamente\n")
            else:
                print("No posee saldo suficiente para realizar la venta")
        elif(cuentaOrigen == 3):
            ventaAux = venta*dolarXbitcoin
            if(float(venta) <= float(saldoDolares)):
                    ventaAux += float(saldoBitcoins)
                    nuevoSaldo = float(saldoDolares) - float(venta)
                    reescribirArchivoSaldo(saldoColones,str(nuevoSaldo),str(ventaAux),ruta_archivoSaldos2)
                    print("Se realizo la venta exitosamente\n")
            else:
                print("No posee saldo suficiente para realizar la venta")


    #Venta de bitcoins
    elif(cuentaDestino == 3):
        if(cuentaOrigen == 1):
            ventaAux = venta*bitcoinXcolones
            if(float(venta) <= float(saldoBitcoins)):
                    ventaAux += float(saldoColones)
                    nuevoSaldo = float(saldoBitcoins) - float(venta)
                    reescribirArchivoSaldo(str(ventaAux),saldoDolares,str(nuevoSaldo),ruta_archivoSaldos2)
                    print("Se realizo la venta exitosamente\n")
            else:
                print("No posee saldo suficiente para realizar la venta")

        elif(cuentaOrigen == 2):
            ventaAux = venta*bitcoinXdolar
            if(float(venta) <= float(saldoDolares)):
                    ventaAux += float(saldoBitcoins)
                    nuevoSaldo = float(saldoDolares) - float(venta)
                    reescribirArchivoSaldo(saldoColones,str(ventaAux),str(nuevoSaldo),ruta_archivoSaldos2)
                    print("Se realizo la venta exitosamente\n")
            else:
                print("No posee saldo suficiente para realizar la venta")




def compraVentaDivisas(cedula):
    ruta_carpeta = os.path.join(os.getcwd(), cedula)
    ruta_archivoSaldos = os.path.join(ruta_carpeta, 'Saldos')
    ruta_archivoSaldos2 =  os.path.join(ruta_archivoSaldos, 'Saldos.txt')
    while True:
            print("----------------------------------------\n")
            print("Bienvenido al menú de compra y venta de divisas\n")
            print("Seleccione el servicio que desea pagar: ")
            print("1. Compra de colones")
            print("2. Venta de colones")
            print("3. Compra de dolares")
            print("4. Venta de dolares")
            print("5. Compra de bitcoin")
            print("6. Venta de bitcoin")
            print("7. Salir\n")

            opcion = input("Seleccione una opción: ")

            #Cuentas, 1 = Colones, 2 = Dolares, 3 = Bitcoin
            if opcion == "1":
                cuentaDestino = 1
                print("Seleccione la cuenta con la cual desea comprar: ")
                print("1. Dolares")
                print("2. Bitcoin")
                entrada = input("Seleccione una opcion: ")
                if(entrada == "1"):
                    cuentaOrigen = 2
                elif(entrada == "2"):
                    cuentaOrigen = 3
                compraDivisas(ruta_archivoSaldos2,cuentaOrigen,cuentaDestino)
                return 0
            

            elif opcion == "2":
                cuentaDestino = 1
                print("Seleccione la cuenta a la cual depositar la venta: ")
                print("1. Dolares")
                print("2. Bitcoin")
                entrada = input("Seleccione una opcion: ")
                if(entrada == "1"):
                    cuentaOrigen = 2
                elif(entrada == "2"):
                    cuentaOrigen = 3
                ventaDivisas(ruta_archivoSaldos2,cuentaOrigen,cuentaDestino)
                return 0
            

            elif opcion == "3":
                cuentaDestino = 2
                print("Seleccione la cuenta con la cual desea comprar: ")
                print("1. Colones")
                print("2. Bitcoin")
                entrada = input("Seleccione una opcion: ")
                if(entrada == "1"):
                    cuentaOrigen = 1
                elif(entrada == "2"):
                    cuentaOrigen = 3
                compraDivisas(ruta_archivoSaldos2,cuentaOrigen,cuentaDestino)
                return 0
            

            elif opcion == "4":
                cuentaDestino = 2
                print("Seleccione la cuenta a la cual depositar la venta: ")
                print("1. Colones")
                print("2. Bitcoin")
                entrada = input("Seleccione una opcion: ")
                if(entrada == "1"):
                    cuentaOrigen = 1
                elif(entrada == "2"):
                    cuentaOrigen = 3
                ventaDivisas(ruta_archivoSaldos2,cuentaOrigen,cuentaDestino)
                return 0
            

            elif opcion == "5":
                cuentaDestino = 3
                print("Seleccione la cuenta con la cual desea comprar: ")
                print("1. Colones")
                print("2. Dolares")
                entrada = input("Seleccione una opcion: ")
                if(entrada == "1"):
                    cuentaOrigen = 1
                elif(entrada == "2"):
                    cuentaOrigen = 2
                compraDivisas(ruta_archivoSaldos2,cuentaOrigen,cuentaDestino)
                return 0
            

            elif opcion == "6":
                cuentaDestino = 3
                print("Seleccione la cuenta a la cual depositar la venta: ")
                print("1. Colones")
                print("2. Dolares")
                entrada = input("Seleccione una opcion: ")
                if(entrada == "1"):
                    cuentaOrigen = 1
                elif(entrada == "2"):
                    cuentaOrigen = 2
                ventaDivisas(ruta_archivoSaldos2,cuentaOrigen,cuentaDestino)
                return 0
            

            elif opcion == "7":
                print("¡Gracias por utilizar nuestros servicios! ¡Hasta pronto!")
                return 0 


def eliminarCuenta(cedula,pin):
    pin_ingresado = getpass('Ingrese su PIN: ')
    if(pin_ingresado == pin):
        if os.path.exists(cedula):
            shutil.rmtree(cedula)
            usuarios = leerArchivo("usuarios_pines.txt")
            reescribirArchivoUsuarios(usuarios,cedula)
            print("Se ha eliminado correctamente el usuario")
            return 0
        else:
            print("Ese numero de cedula no esta registrado")
    else:
        print("El pin ingresado es incorrecto, volviendo al menu anterior")

def eliminarCuentaAdmi(cedula):
    if os.path.exists(cedula):
        shutil.rmtree(cedula)
        usuarios = leerArchivo("usuarios_pines.txt")
        reescribirArchivoUsuarios(usuarios,cedula)
        print("Se ha eliminado correctamente el usuario")
        return 0
    else:
        print("Ese numero de cedula no esta registrado")



def usuarioRegistrado():
    global errores
    errores = 0
    erroresPin = 0
    #Primero cargamos la informacion de las personas registradas
    listaUsuarios = leerArchivo("usuarios_pines.txt")
    if(len(listaUsuarios) < 4):
        print("No hay ningun usuario registrado")
        return 0
    while(errores<3):
        existe = False
        cedula = input("Ingrese el numero de cedula: ")
        for i in range(len(listaUsuarios)):
                #verificamos que el usuario exista
                if(listaUsuarios[i] == cedula):
                    cedulaActual = listaUsuarios[i]
                    nombre = listaUsuarios[i+1]
                    pin = listaUsuarios[i+2]
                    existe = True
        if(existe):
            while(erroresPin < 3):
                pin_ingresado = getpass('Ingrese su PIN: ')
                if(pin_ingresado == pin):
                    usuarioRegistroAux(cedulaActual,nombre,pin)
                    return 0
                else:
                    print("Error, el pin ingresado no es correcto, intente nuevamente")
                    erroresPin += 1
            print("Se excedio el numero de intentos para ingresar el PIN")
            return 0
        else:
            errores += 1
            print("La cedula ingresada no se encuentra registrada ")
    print("Se excedio el numero maximo de intentos, volviendo al menu principal")
    return 0


def usuarioRegistroAux(cedula,nombre,pin):
    while True:
        print("\n----------------------------------------------------")
        print("\n---Bienvenido al Menu de usuario " + nombre + "---")
        print("1. Retirar dinero")
        print("2. Depositar dinero")
        print("3. Ver saldo actual")
        print("4. Pagar servicios")
        print("5. Compra/Venta de Divisas")
        print("6. Eliminar usuario")
        print("7. Salir")
        
        opcion = input("\nPor favor, seleccione una opción: ")

        if opcion == "1":
            retirarDinero(cedula)
        elif opcion == "2":
            depositarDinero(cedula)
        elif opcion == "3":
            verSaldo(cedula)
        elif opcion == "4":
            pagarServicios(cedula)
        elif opcion == "5":
            compraVentaDivisas(cedula)
        elif opcion == "6":
            eliminarCuenta(cedula,pin)
            return 0
        elif opcion == "7":
            print("¡Gracias por utilizar nuestros servicios! ¡Hasta pronto!")
            return 0 
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


def modificarTipo():
    divisas = leerArchivo('tipos_de_cambio.txt')


    print("\nBienvenido al sistema de cambio de divisas\n")
    print("1. Compra de colones")
    print("2. Venta de colones")
    print("3. Compra de bitcoin")
    print("4. Venta de bitcoins")
    print("5. Compra de dolar")
    print("6. Venta de dolar")
    print("7. Salir")


    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        print("1. De colon a bitcoin")
        print("2. De colon a dolar")
        entrada = input("Seleccione una opcion: ")
        if(entrada == "1"):
            entrada2 = input("Digite la nueva divisa: ")
            divisas[6] = entrada2
            print ("Se realizo el cambio correctamente")
        elif(entrada == "2"):
            entrada2 = input("Digite la nueva divisa: ")
            divisas[7] = entrada2
            print ("Se realizo el cambio correctamente")

    elif opcion == "2":
        print("1. De colon a bitcoin")
        print("2. De colon a dolar")
        entrada = input("Seleccione una opcion: ")
        if(entrada == "1"):
            entrada2 = input("Digite la nueva divisa: ")
            divisas[0] = entrada2
            print ("Se realizo el cambio correctamente")
        elif(entrada == "2"):
            entrada2 = input("Digite la nueva divisa: ")
            divisas[1] = entrada2
            print ("Se realizo el cambio correctamente")


    elif opcion == "3":
        print("1. De bitcoin a colones")
        print("2. De bitcoin a dolar")
        entrada = input("Seleccione una opcion: ")
        if(entrada == "1"):
            entrada2 = input("Digite la nueva divisa: ")
            divisas[8] = entrada2
            print ("Se realizo el cambio correctamente")
        elif(entrada == "2"):
            entrada2 = input("Digite la nueva divisa: ")
            divisas[9] = entrada2
            print ("Se realizo el cambio correctamente")


    elif opcion == "4":
        print("1. De bitcoin a colones")
        print("2. De bitcoin a dolar")
        entrada = input("Seleccione una opcion: ")
        if(entrada == "1"):
            entrada2 = input("Digite la nueva divisa: ")
            divisas[2] = entrada2
            print ("Se realizo el cambio correctamente")
        elif(entrada == "2"):
            entrada2 = input("Digite la nueva divisa: ")
            divisas[3] = entrada2
            print ("Se realizo el cambio correctamente")


    elif opcion == "5":
        print("1. De dolares a colones")
        print("2. De dolares a bitcoin")
        entrada = input("Seleccione una opcion: ")
        if(entrada == "1"):
            entrada2 = input("Digite la nueva divisa: ")
            divisas[10] = entrada2
            print ("Se realizo el cambio correctamente")
        elif(entrada == "2"):
            entrada2 = input("Digite la nueva divisa: ")
            divisas[11] = entrada2
            print ("Se realizo el cambio correctamente")


    elif opcion == "6":
        print("1. De dolares a colones")
        print("2. De dolares a bitcoin")
        entrada = input("Seleccione una opcion: ")
        if(entrada == "1"):
            entrada2 = input("Digite la nueva divisa: ")
            divisas[4] = entrada2
            print ("Se realizo el cambio correctamente")
        elif(entrada == "2"):
            entrada2 = input("Digite la nueva divisa: ")
            divisas[5] = entrada2
            print ("Se realizo el cambio correctamente")

    elif opcion == "7":
        print("Saliendo...")
        return 0
    else:
        print("Opción inválida, por favor seleccione otra.")

    with open("tipos_de_cambio.txt", 'w') as archivo:
        for linea in divisas:
            archivo.write(linea + "\n")

def configuracionAvanzada():
    print("Para ingresar, ingrese el pin de administrador: ")
    datos = leerArchivo('usuarios_pines.txt')
    pin = datos[0]
    pin_ingresado = getpass('Ingrese el PIN: ')
    if(pin == pin_ingresado):
        while True:
            print("\n------ Configuración avanzada ------\n")
            print("1. Eliminar usuario")
            print("2. Modificar tipo de cambio")
            print("3. Salir\n")

            opcion = input("Ingrese la opción deseada: ")

            if opcion == "1":
                usuario = input("Por favor ingrese la cedula del usuario que desea eliminar: ")
                eliminarCuentaAdmi(usuario)
            elif opcion == "2":
                modificarTipo()
            elif opcion == "3":
                print("Saliendo...")
                break
            else:
                print("Opción inválida, intente de nuevo.")
    else:
        print("El pin ingresado es incorrecto")
        return 0



if __name__ == "__main__":
    while True:
        print("\n\n\n------------------------------------------------------------------")
        print("\n                     ---- Menú Principal ----")
        print("\n1. Registrar nuevo usuario")
        print("2. Usuario Registrado")
        print("3. Configuración Avanzada")
        print("4. Salir")

        print("\n------------------------------------------------------------------")
        
        opcion = input("Ingrese el número de la opción que desea ejecutar: ")
        
        if opcion == "1":
            print("Ha seleccionado la opción de registrar un nuevo usuario.")
            print("\n------------------------------------------------------------------\n")
            registrarUsario()
        elif opcion == "2":
            print("Ha seleccionado la opción de usuario registrado.")
            print("\n------------------------------------------------------------------\n")
            usuarioRegistrado()
        elif opcion == "3":
            configuracionAvanzada()
            print("Ha seleccionado la opción de configuración avanzada.")
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor seleccione una opción del 1 al 4.")
        
