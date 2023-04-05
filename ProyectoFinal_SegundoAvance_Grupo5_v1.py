# Ingenieria en sistemas de la computacion
# curso: Programacion basica
# Segundo avance
# Grupo 5
# Autores: QUESADA BONILLA JOSEPH DAVID 
# Profesor: CAMACHO MORA ALVARO DIONISIO

import os
# funcion registro usuario 
def registrar_usuario():
    # arreglo para los usuarios
    usuarios = []
    # inicio de while true para el registro de usuario
    while True:
        #solicitud de nombre de usuario, cedula y numero Pin
        nombre = input("Ingrese su nombre de usuario: ")
        # al solicitar el numero de cedula se tiene que validar que sea de 9 dijitos, al igual que el numero pin, que tiene que ser de 4 dijitos
        cedula = input("Ingrese su número de cédula (9 dígitos): ")
        # se utiliza el while para validar que el numero de cedula y el pin correspondan a los dijitos necesarios
        while len(cedula) != 9:
            print("El número de cédula debe tener 9 dígitos.")
            cedula = input("Ingrese su número de cédula (9 dígitos): ")
        pin = input("Ingrese su número PIN (4 dígitos): ")
        while len(pin) != 4:
            print("El número PIN debe tener 4 dígitos.")
            pin = input("Ingrese su número PIN (4 dígitos): ")

        # para el regiustro se necesita un deposito minimo, en colones, dolares o en Bitcoin
        while True:
            print("Para continuar con el registro, se necesita un deposito minimo, ya sea en colones, dolares o en bitcoin\n")
            print("Elija la moneda del depósito mínimo:")
            print("1. Colones")
            print("2. Dólares")
            print("3. Bitcoin")
            # se solicita al usuario cual obcion desea realizar
            opcion = input("Ingrese el número de la opción elegida: ")
            # inicio deposito en colones
            if opcion == "1":
                moneda = "colones"
                # se solicita el monto que desea depositar
                deposito_minimo = input("Ingrese el monto del depósito mínimo en colones: ")
                if float(deposito_minimo) < 100000:
                    print("El depósito mínimo en colones debe ser de 100 000 colones.")
                    continue
                break
                # fin deposito en colones

                # inicio deposito en dolares
            elif opcion == "2":
                moneda = "dólares"
                # se solicita el monto que desea depositar
                deposito_minimo = input("Ingrese el monto del depósito mínimo en dólares: ")
                if float(deposito_minimo) < 187.72:
                    print("El depósito mínimo en dólares debe ser de 187.72 dólares.")
                    continue
                break
                # fin deposito en dolares

                # inicio deposito en BIT
            elif opcion == "3":
                moneda = "bitcoin"
                # se solicita el monto que desea depositar
                deposito_minimo = input("Ingrese el monto del depósito mínimo en bitcoin: ")
                if float(deposito_minimo) < 0.0069:
                    print("El depósito mínimo en bitcoin debe ser de 0.0069 BTC.")
                    continue
                break

                # fin deposito en BIT
            else:
                print("Opción inválida. Intente de nuevo.")

        # se guardan lo solicitado en el arreglo bidimencional y un archivo plano        
        usuarios.append([cedula, nombre, pin, deposito_minimo, moneda])
        with open('usuarios.txt', 'w') as f:
            for usuario in usuarios:
                f.write(f"{usuario[0]},{usuario[1]},{usuario[2]},{usuario[3]},{usuario[4]}\n")
        print(f"Usuario {nombre} registrado con éxito.")
        break


def ver_saldo_actual(cedula):
    # Abre el archivo "usuarios.txt" en modo lectura
    with open('usuarios.txt', 'r') as f:
        
        # Crea una lista de listas, donde cada sublista representa un usuario y contiene su información
        usuarios = [line.strip().split(',') for line in f.readlines()]
        
        # Recorre la lista de usuarios

    # Si encuentra el usuario con el nombre ingresado, guarda su saldo en las diferentes monedas
    for usuario in usuarios:
        if usuario[0] == cedula:
            saldo_colones = float(usuario[3]) if usuario[4] == "colones" else 0
            saldo_dolares = float(usuario[3]) if usuario[4] == "dólares" else 0
            saldo_bitcoin = float(usuario[3]) if usuario[4] == "bitcoin" else 0
            break

    # Imprime el saldo actual del usuario en cada moneda
    print("***************************************************")

    print(f"\nSaldo actual en colones: {saldo_colones}")
    print(f"Saldo actual en dólares: {saldo_dolares}")
    print(f"Saldo actual en bitcoin: {saldo_bitcoin}\n")

    print("***************************************************")

def menu_principal():
    # Abre el archivo "usuarios.txt" en modo lectura
    with open('usuarios.txt', 'r') as f:
        usuarios = [line.strip().split(',') for line in f.readlines()]
    
    max_intentos = 3  # Máximo de intentos permitidos
    intentos = 0  # Número actual de intentos
    
    # inicio del bucle para solicitar los datos del inicio de sesion
    while intentos < max_intentos:
        # solicitud de el numero de cedula del usuario y el pin
        cedula = input("Ingrese su número de cédula: ")
        pin = input("Ingrese su número PIN: ")

        usuario_valido = False
        for usuario in usuarios:
            if usuario[0] == cedula and usuario[2] == pin:
                print("Bienvenido, ", usuario[1])
                usuario_valido = True
                 # menu para el menu priuncipal 
                while True:
                    print("\nMenú principal:")
                    print("1. Retirar dinero")
                    print("2. Depositar dinero")
                    print("3. Ver saldo actual")
                    print("4. Pagar servicios")
                    print("5. Compra/Venta de Divisas")
                    print("6. Eliminar usuario")
                    print("7. Salir")
                    opcion = input("Ingrese el número de la opción elegida: \n")
                    if opcion == "1":
                        print("retirar_dinero")
                    elif opcion == "2":
                        print("depositar dinero")
                    elif opcion == "3":
                        ver_saldo_actual(cedula)
                    elif opcion == "4":
                        print("Pagar servicios")
                    elif opcion == "5":
                        print("Compra/Venta de Divisas")
                    elif opcion == "6":
                        print ("eliminar usuario")
                    elif opcion == "7":
                        print ("Saliendo del menu principal...\n")
                    break
        
        if usuario_valido:
            break  # Sal del ciclo si las credenciales son válidas

        intentos += 1
        intentos_restantes = max_intentos - intentos
        
        if intentos_restantes > 0:
            print(f"Cédula o PIN incorrecto. Tiene {intentos_restantes} intentos restantes.")
        else:
            print("Ha excedido el número máximo de intentos. Intente más tarde.")
            break


def menu():

    print ("****************************************************")
    print ("*                   Bienvenido                     *")
    print ("*                Global Bank Inc                   *")
    print ("*        (1) Nuevo Usuario (2) ingresar            *")
    print ("*          (3) Configuracion Avanzada              *")
    print ("*                  (4) salir                       *")
    print ("****************************************************\n") 

# inicio de While para el menu
opcion = 0
while True:    
    menu()

    opcion = int (input("Que opcion desea realizar?\n"))
    # inicio del regsitro de usuario
    if opcion == 1:

       registrar_usuario()     
        
    # fin del registro de usuario

    elif opcion == 2: 

        menu_principal()

    elif opcion == 3:

        print("Configuracion Avanzada")

    # salir del programa 
    elif opcion == 4:

        print("Gracias por usar nuestro ATM, que tenga un buen dia")   
        break
    else:         

        print("opcion invalida")
