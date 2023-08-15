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
        Puntarenas = Especificaciones[Posicion + 1]
    if i == "S,capacidad":
        SanCarlos = Especificaciones[Posicion + 1]
    if i == "G,capacidad":
        Guanacaste = Especificaciones[Posicion + 1]
    Posicion += 1

# Función para el módulo de hospedaje
def modulo_registros(Puntarenas,SanCarlos,Guanacaste):
        print("1 - Hotel Paraíso, Puntarenas\n2 - Hotel Paraíso, San Carlos\n3 - Hotel Paraíso, Guanacaste")
        opcion = int(input("Seleccione el Hotel para el registro: "))
        if opcion == 1:
            print("Capacidad del hotel: 120 habitaciones\nCantidad máxima de personas por habitación: 4 \nCantidad de habitaciones disponibles en este momento:", Puntarenas)
        if opcion == 2:
            print("Capacidad del hotel: 60 habitaciones\nCantidad máxima de personas por habitación: 2 \nCantidad de habitaciones disponibles en este momento:", SanCarlos)
        if opcion == 3:
            print("Capacidad del hotel: 100 habitaciones\nCantidad máxima de personas por habitación: 4 \nCantidad de habitaciones disponibles en este momento:", Guanacaste)
        Nombre = input("Nombre del cliente: ")
        Identificacion = input("Número de identificación: ")
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
            Datos_acompañantes[i][0] = input("Nombre del acompañante: ")
            Datos_acompañantes[i][1] = input("Número de identificación: ")
            Datos_acompañantes[i][2] = input("Edad: ")
# Función para el módulo de reservas
def modulo_reservas():
    def calcular_monto_total(hotel, dias, num_huespedes, es_fin_de_semana):
        tarifa_por_persona = hoteles[hotel]["tarifa_fin_de_semana"] if es_fin_de_semana else hoteles[hotel]["tarifa_semana"]
        monto_total = tarifa_por_persona * dias * num_huespedes
        iva = monto_total * 0.13
        monto_total_con_iva = monto_total + iva
        return monto_total, iva, monto_total_con_iva
    
    def verificar_disponibilidad(hotel, dias, num_huespedes):
        capacidad_hotel = hoteles[hotel]["capacidad"]
        max_huespedes_por_habitacion = hoteles[hotel]["max_huespedes_por_habitacion"]
        total_habitaciones_necesarias = (num_huespedes + max_huespedes_por_habitacion - 1) // max_huespedes_por_habitacion
        return total_habitaciones_necesarias <= capacidad_hotel

    def reservar_hospedaje():
        hotel = input("Ingrese el nombre del hotel (Puntarenas, San Carlos, Guanacaste): ")
        dias = int(input("Ingrese la cantidad de días del hospedaje: "))
        num_huespedes = int(input("Ingrese la cantidad de huéspedes: "))
        es_fin_de_semana = input("¿La reserva incluye fin de semana? (Sí/No): ").lower() == "sí"

        if hotel in hoteles:
            if verificar_disponibilidad(hotel, dias, num_huespedes):
                monto_total, iva, monto_total_con_iva = calcular_monto_total(hotel, dias, num_huespedes, es_fin_de_semana)
                print("\nResumen de la reserva:")
                print(f"Hotel: {hotel}")
                print(f"Días del hospedaje: {dias}")
                print(f"Número de huéspedes: {num_huespedes}")
                print(f"Monto a pagar por persona por noche: ${'%.2f' % (monto_total / (dias * num_huespedes))}")
                print(f"Monto total: ${'%.2f' % monto_total}")
                print(f"IVA (13%): ${'%.2f' % iva}")
                print(f"Monto total con IVA: ${'%.2f' % monto_total_con_iva}")
            else:
                print("Lo sentimos, no hay disponibilidad en el hotel para la cantidad de huéspedes.")
        else:
            print("El hotel ingresado no está registrado en el sistema.")
    reservar_hospedaje()
    
        
        
                

    

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
                modulo_registros(Puntarenas,SanCarlos,Guanacaste)
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
