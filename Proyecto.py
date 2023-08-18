# Variables de registro
Nombre = {}
Identificacion = {}
Pais = {}
Provincia = {}
Canton = {}
Distrito = {}
Direccion = {}
Edad = {}
FormaDePago = {}
Datos_acompañantes = []
Días_semana = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sabado","Domingo"]
Puntarenas = {}
SanCarlos = {}
Guanacaste = {}
Hotel = {}
horarios_checkin = []
horarios_checkout = []
# Datos de los hoteles
# Puntarenas
Posicion = 0
file = open("Hoteles.txt","r")
Datos = file.read()
Especificaciones = Datos.split("&")
for i in Especificaciones:
    if i == "P,capacidad":
        Puntarenas = int(Especificaciones[Posicion + 1])
    if i == "S,capacidad":
        SanCarlos = int(Especificaciones[Posicion + 1])
    if i == "G,capacidad":
        Guanacaste = int(Especificaciones[Posicion + 1])
    Posicion += 1
file.close()

# Función para el módulo de hospedaje
def modulo_registros(Puntarenas,SanCarlos,Guanacaste,continuar):
    while continuar == 1:
        print("1 - Hotel Paraíso, Puntarenas\n2 - Hotel Paraíso, San Carlos\n3 - Hotel Paraíso, Guanacaste")
        opcion = int(input("Seleccione el Hotel para el registro: "))
        if opcion == 1 and Puntarenas > 0:
            print("Capacidad del hotel: 120 habitaciones\nCantidad máxima de personas por habitación: 4 \nCantidad de habitaciones disponibles en este momento:", Puntarenas)
            Hotel = "Puntarenas"
            continuar = 0
        elif opcion == 2 and SanCarlos > 0:
            print("Capacidad del hotel: 60 habitaciones\nCantidad máxima de personas por habitación: 2 \nCantidad de habitaciones disponibles en este momento:", SanCarlos)
            Hotel = "San Carlos"
            continuar = 0
        elif opcion == 3 and Guanacaste > 0:
            print("Capacidad del hotel: 100 habitaciones\nCantidad máxima de personas por habitación: 4 \nCantidad de habitaciones disponibles en este momento:", Guanacaste)
            Hotel = "Guanacaste"
            continuar = 0
        else:
            print("No hay habitaciones disponibles en el hotel que eligió, seleccione otro.")
    Nombre = input("Nombre del cliente: ")
    Identificacion = input("Número de identificación: ")
    Identificador = Identificacion + ":&"
    Pais = input("País: ")
    Provincia = input("Provincia: ")
    Canton = input("Cantón: ")
    Distrito = input("Distrito: ")
    Direccion = input("Otras especificaciones de dirección: ")
    Edad = input("Edad: ")
    FormaDePago = input("Forma de pago (efectivo, transferencia, tarjeta de crédito): ")
    n_acompañantes = int(input("¿Cuántas personas lo acompañan? "))
    for i in range(n_acompañantes):
        print("Datos del acompañante", i + 1)
        Datos_acompañantes.append([0]*3)
        Datos_acompañantes[i][0] = input("Nombre del acompañante: ")
        Datos_acompañantes[i][1] = input("Número de identificación: ")
        Datos_acompañantes[i][2] = input("Edad: ")
    file = open("Registros.txt","a")
    file.write("&Número de cliente")
    file.write(Identificador)
    file.write(Identificacion)
    file.write("&Nombre del cliente")
    file.write(Identificador)
    file.write(Nombre)
    file.write("&Número de identificación")
    file.write(Identificador)
    file.write(Identificacion)
    file.write("&País")
    file.write(Identificador)
    file.write(Pais)
    file.write("&Provincia")
    file.write(Identificador)
    file.write(Provincia)
    file.write("&Cantón")
    file.write(Identificador)
    file.write(Canton)
    file.write("&Distrito")
    file.write(Identificador)
    file.write(Distrito)
    file.write("&Hotel")
    file.write(Identificador)
    file.write(Hotel)
    file.write("&Otras especificaciones de dirección")
    file.write(Identificador)
    file.write(Direccion)
    file.write("&Edad")
    file.write(Identificador)
    file.write(Edad)
    file.write("&Forma de pago (efectivo, transferencia, tarjeta de crédito)")
    file.write(Identificador)
    file.write(FormaDePago)
    file.write("&Numero de acompañantes")
    file.write(Identificador)
    file.write(str(n_acompañantes))
    for i in range(n_acompañantes):
        file.write("&Nombre del acompañante")
        file.write(Identificador)
        file.write(Datos_acompañantes[i][0])
        file.write("&Número de identificación:")
        file.write(Identificador)
        file.write(Datos_acompañantes[i][1])
        file.write("&Edad:")
        file.write(Identificador)
        file.write(Datos_acompañantes[i][2])
    file.write("\n")
    file.close()
# Función para el módulo de reservas


# Función para el módulo de facturación
def modulo_facturacion():
    # Implementa la lógica del módulo de facturación aquí
    pass

# Función para el módulo de reportes
def modulo_reportes():
    # Implementa la lógica del módulo de reportes aquí
    pass

# Función para el menú principal
def menu():
    continuar = 1
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    if usuario == "admin" and contraseña == "Adm112":
        print("Inicio de sesión exitoso.\n")
        while continuar == 1:
            print("Bienvenido al menú:")
            print("1. Módulo de Registros")
            print("2. Módulo de Reservas")
            print("3. Módulo de Facturación")
            print("4. Módulo de Reportes")
            print("5. Salir")
            opcion = int(input("Selecciona una opción: "))
             
            if opcion == 1:
                modulo_registros(Puntarenas,SanCarlos,Guanacaste,continuar)
            elif opcion == 2:
                modulo_reservas()
            elif opcion == 3:
                modulo_facturacion()
            elif opcion == 4:
                modulo_reportes()
            elif opcion == 5:
                print("Sesión finalizada.")
                break
            else:
                print("Opción inválida. Por favor, elija una opción válida.")
    else:
        print("Credenciales incorrectas. Vuelve a intentarlo.")

# Llamada a la función principal del menú
menu()
