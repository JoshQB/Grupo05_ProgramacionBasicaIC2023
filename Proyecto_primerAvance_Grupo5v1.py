# Ingenieria en sistemas de la computacion
# curso: Programacion basica
# primer avance
# Grupo 5
# Autores: QUESADA BONILLA JOSEPH DAVID / MANZANARES NUÑEZ DAVID EUGENIO / BARRIENTOS ACUÑA KENNETH ANDREY
# Profesor: CAMACHO MORA ALVARO DIONISIO
usuarios = []

def registrar_usuario():
     # solicitud de datos para el usuario
        new_user = input ("por favor ingrese su Nombre\n")
        # validar que la cedula sea de 9 dijitos
        while True:
            num_cedula = input ("Por favor escriba su numero de cedula, el numero de cedula tiene que ser de 9 dijitos\n")
            if not len(num_cedula) != 9:
                print ("")
                break
            else: 
                print("Error, El numero de cedula tiene que ser de 9 dígitos!\n")
        # validar que la pin sea de 4 dijitos
        while True: 
            new_pin = input ("Por favor ingrese un numero Pin, el numero Pin tiene un maximo de 4 dígitos\n")
            if not len(new_pin) != 4: 
                print ("")
                break
            else:
                print("Error, El numero Pin tiene que ser unicamente de 4 dígitos\n")
        
        while True:
            print ("Para continuar con el registro, se necesita realizar un deposito minimo de 100 000 colones, 184,72 Dolares o 0,0069 BTC (Bitcoin)\n")
            
             
            while True:
                opcion = 0
                opcion:int = input ("Que opcion desea realizar, (1) colones, (2) Dolares, (3) Bitcoin\n") 

                if opcion == 1:
                    print ("************ Deposito en Colones ****************\n")
                    deposito = float(input("Cuanto desea depositar ? Nota: el deposito minimo para el registro es de 100 000 colones.\n"))
                    deposito_minimo_colones:int = 100000
                    if deposito >= deposito_minimo_colones:
                        print("deposito realizado con exito.\n")
                    else:
                        print("Error, el deposito minimo tiene que ser de 100 000 colones.\n")

                elif opcion == 2:
                    print ("************ Deposito en Dolares ****************\n")
                    deposito = float(input("Cuanto desea depositar ? Nota: el deposito minimo para el registro es de 184,72 Dolares.\n"))
                    deposito_minimo_dolares = 184,72
                    if deposito >= deposito_minimo_dolares:
                        print("deposito realizado con exito.\n")
                    else:
                        print("Error, el deposito minimo tiene que ser de 184,72 Dolares.\n")
                    break
                else:
                    print(" ")
        usuarios.append([new_user, num_cedula, new_pin, deposito])
        print("Usuario creado con exito\n")
        print("*************************************************\n")
def sub_menu ():
    print("\nMenú:")
    print("*************************************************************")
    print("*1. Retirar dinero                                          *")
    print("*2. Depositar dinero                                        *")
    print("*3. Ver saldo actual                                        *")
    print("*4. Pagar servicios                                         *")
    print("*5. Compra/Venta de Divisas                                 *")
    print("*6. Eliminar usuario                                        *")
    print("*7. Salir                                                   *")
    print("*************************************************************\n")
    opcion = 0
    while True:
        opcion = int (input ("Que desea realizar? \n"))
        if opcion == 1:
            print ("------------- Retirar dinero -------------\n")
            print ("Saldo actual: ", usuario[3])
            saldo_retiro = int (input ("Cuanto dienero desea retirar ? "))
            
            if not saldo_retiro >= saldo:
                usuario[3] = saldo - saldo_retiro
                print("Retiro realizado con exito")
                print("Saldo actual: ",usuario[3])
                print("\n")
            else:
                print ("Error, no puede retirar una sifra mayor a la del saldo actual")
                
        elif opcion == 2:
            print ("------------- Depositar dinero -------------\n")
            print ("Saldo actual: ", usuario[3])
            deposito = int (input ("Cuanto dienero desea depositar ? "))
            usuario[3] = usuario[3] + deposito
            print("Deposito realizado con exito\n")
            
        elif opcion == 3:
            print ("------------- Ver saldo actual -------------\n")
            print("Saldo actual: ", usuario[3])
            print("\n")
        elif opcion == 4:
            print ("------------- Pagar servicios  -------------\n")
        elif opcion == 5:
            print ("------------- Compra/Venta de Divisas -------------\n")
        elif opcion == 6:
            print ("------------- Eliminar usuariol -------------\n")
        elif opcion == 7:
            print("Saliendo del sistema...")
            break
        else:
            print("opcion invalida...")

def loggin():
    # inicio de la validacion de datos pora el Loggin
    num_cedula = input ("por favor escriba su cedula\n")
    intentos = 0
    while intentos < 3:
        new_pin = input ("Por favor escriba su numero PIN\n")
            
        for usuario in usuarios:
            if  num_cedula == usuario[1] and new_pin == usuario[2]:
                print("Inicio de sesión exitoso\n")
                print ("Bienvenido, ", usuario[0]) 
                print ("Saldo actual: ", usuario[3])
                sub_menu 
                return True

        intentos += 1 
        print("Cedula o PIN incorrectos. Intentos restantes: ", 3 - intentos)

    print("Ha excedido el número máximo de intentos de inicio de sesión.")
    return False 
        
    # fin del loggin 

def mostrar_usuarios():
    for usuario in usuarios:
        print("Nombre de usuario:", usuario[0])
        print("cedula:", usuario[1])
        print("pin:", usuario[2])
        print("deposito", usuario[3])
        print("-------------------")



# 1- bienvenida y menu principal
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

        loggin()

    elif opcion == 3:
        mostrar_usuarios()
        print("Configuracion Avanzada")

    # salir del programa 
    elif opcion == 4:
        print("Gracias por usar nuestro ATM, que tenga un buen dia")   
        break
    else:              
        print("opcion invalida")