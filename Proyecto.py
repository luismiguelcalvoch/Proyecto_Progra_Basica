# Variables de registro
nombres = []
n_identificaciones = []
paises = []
cantones = []
distritos = []
direcciones = []
edades = []
formasDePago = []
hospedajes = []
horarios_checkin = []
horarios_checkout = []
# Datos de los hoteles
hoteles = {
    "Puntarenas": {
        "capacidad": 120,
        "max_huespedes_por_habitacion": 4,
        "tarifa_semana": 100,
        "tarifa_fin_de_semana": 120,
    },
    "San Carlos": {
        "capacidad": 60,
        "max_huespedes_por_habitacion": 2,
        "tarifa_semana": 80,
        "tarifa_fin_de_semana": 100,
    },
    "Guanacaste": {
        "capacidad": 100,
        "max_huespedes_por_habitacion": 4,
        "tarifa_semana": 90,
        "tarifa_fin_de_semana": 110,
    },
}

# Función para el módulo de hospedaje
def modulo_registros():
    nombreDeCliente = input("Nombre del cliente: ")
    identificacion = input("Número de identificación: ")
    pais = input("País: ")
    canton = input("Cantón: ")
    distrito = input("Distrito: ")
    direccion = input("Otras especificaciones de dirección: ")
    edad = input("Edad: ")
    formaDePago = input("Forma de pago (efectivo, transferencia, tarjeta de crédito): ")

    # Agregar datos a las listas
    nombres.append(nombreDeCliente)
    n_identificaciones.append(identificacion)
    paises.append(pais)
    cantones.append(canton)
    distritos.append(distrito)
    direcciones.append(direccion)
    edades.append(edad)
    formasDePago.append(formaDePago)

    n_acompañantes = int(input("Cuántas personas lo acompañan: "))
    for i in range(n_acompañantes):
        print("Datos del acompañante", i + 1)
        nombre_acompañante = input("Nombre del acompañante: ")
        identificacion_acompañante = input("Número de identificación: ")
        edad_acompañante = input("Edad: ")

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
                modulo_registros()
            elif opcion == 2:
                modulo_reservas()
            elif opcion == 3:
                modulo_facturacion()
            elif opcion == 4:
                modulo_reportes()
            elif opcion == 5:
                continuar = 0
                print("Sesión finalizada.")
            else:
                print("Opción inválida. Por favor, elija una opción válida.")
    else:
        print("Credenciales incorrectas. Vuelve a intentarlo.")

# Llamada a la función principal del menú
menu()
