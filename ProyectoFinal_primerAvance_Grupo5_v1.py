# Ingenieria en sistemas de la computacion
# curso: Programacion basica
# primer avance
# Grupo 5
# Autores: QUESADA BONILLA JOSEPH DAVID / MANZANARES NUÑEZ DAVID EUGENIO / BARRIENTOS ACUÑA KENNETH ANDREY
# Profesor: CAMACHO MORA ALVARO DIONISIO


# 1- bienvenida y menu principal
opcion = 0
def menu():

    print ("****************************************************")
    print ("*                   Bienvenido                     *")
    print ("*                Global Bank Inc                   *")
    print ("*        (1) Nuevo Usuario (2) ingresar            *")
    print ("*          (3) Configuracion Avanzada              *")
    print ("*                  (4) salir                       *")
    print ("****************************************************\n") 

# inicio de While para el menu
while True:    
    menu()

    opcion = int (input("Que opcion desea realizar?\n"))
    # inicio del regsitro de usuario
    if opcion == 1:
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

        print("Usuario creado con exito\n")
        
    # fin del registro de usuario

    elif opcion == 2: 

        # inicio de la validacion de datos pora el Loggin
        cedula = input ("por favor escriba su cedula\n")
        if cedula != num_cedula:
            print ("El numero de cedula, no coincide con el de ningun usuario registrado")
        elif cedula == num_cedula:
            intentos = 3 
            # inicio del for para validar que no se exeda la cantidad de intentos para poder ingresar 
            for i in range(intentos):
                pin = input ("Por favor escriba su numero PIN\n")
                if pin == new_pin:
                    print ("Bienvenido, ", new_user)    
                    break
                else: 
                    print("El numero PIN es incorrecto!")
                
                if i < intentos - 3:
                    print("por favor, vuelver a escribir el numero PIM.\n")
            if pin != new_pin:
                print("Has alcanzado el numero maximo de intentos")
        # fin del loggin

    elif opcion == 3:
        print("Configuracion Avanzada")

    # salir del programa 
    elif opcion == 4:
        print("Gracias por usar nuestro ATM, que tenga un buen dia")   
        break
    else:              
        print("opcion invalida")
