# Variables de registro
Identificacion = {}
Días_semana = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sabado","Domingo"]
Puntarenas = {}
SanCarlos = {}
Guanacaste = {}
Hotel = {}
Hotel_seleccionado = {}
continuar = 1
horarios_checkin = []
horarios_checkout = []
# Datos de los hoteles

Posicion = 0
file = open("Hoteles.txt","r")
Datos = file.read()
Especificaciones = Datos.split("&")
for i in Especificaciones:
    # Puntarenas
    if i == "P,capacidad":
        Puntarenas = int(Especificaciones[Posicion + 1])
    # San Carlos
    if i == "S,capacidad":
        SanCarlos = int(Especificaciones[Posicion + 1])
    # Guanacaste
    if i == "G,capacidad":
        Guanacaste = int(Especificaciones[Posicion + 1])
    Posicion += 1
file.close()
Posicion = 0

# Función para el módulo de hospedaje
def modulo_registros(Puntarenas,SanCarlos,Guanacaste,continuar):
    while continuar == 0:
        print("1 - Hotel Paraíso, Puntarenas\n2 - Hotel Paraíso, San Carlos\n3 - Hotel Paraíso, Guanacaste")
        opcion = int(input("Seleccione el Hotel para el registro: "))
        if opcion == 1 and Puntarenas > 0:
            print("Capacidad del hotel: 120 habitaciones\nCantidad máxima de personas por habitación: 4 \nCantidad de habitaciones disponibles en este momento:", Puntarenas)
            Hotel = "Puntarenas"
            continuar = 1
        elif opcion == 2 and SanCarlos > 0:
            print("Capacidad del hotel: 60 habitaciones\nCantidad máxima de personas por habitación: 2 \nCantidad de habitaciones disponibles en este momento:", SanCarlos)
            Hotel = "San Carlos"
            continuar = 1
        elif opcion == 3 and Guanacaste > 0:
            print("Capacidad del hotel: 100 habitaciones\nCantidad máxima de personas por habitación: 4 \nCantidad de habitaciones disponibles en este momento:", Guanacaste)
            Hotel = "Guanacaste"
            continuar = 1
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
    Edad = int(input("Edad: "))
    if Edad < 18:
        print("Debes de ser mayor de edad para poder realizar un registro, pide ayuda de un adulto para poder seguir adelante")
        return
    FormaDePago = input("Forma de pago (efectivo, transferencia, tarjeta de crédito): ")
    if Hotel == "Puntarenas" or Hotel == "Guanacaste":
        while continuar == 1:
            n_acompañantes = int(input("¿Cuántas personas lo acompañan? "))
            if n_acompañantes > 3:
                print("El limite máximo de personas en este hotel es de 4 personas por habitación, inserte otra cantidad:")
            else:
                continuar = 0
    if Hotel == "San Carlos":
        while continuar == 1:
            n_acompañantes = int(input("¿Cuántas personas lo acompañan? "))
            if n_acompañantes > 1:
                print("El limite máximo de personas en este hotel es de 2 personas por habitación, inserte otra cantidad:")
            else:
                continuar = 0
    for i in range(n_acompañantes):
        print("Datos del acompañante", i + 1)
        Datos_acompañantes.append([0]*3)
        Datos_acompañantes[i][0] = input("Nombre del acompañante: ")
        Datos_acompañantes[i][1] = input("Número de identificación: ")
        Datos_acompañantes[i][2] = input("Edad: ")
    if Hotel == "Puntarenas":
        file = open("Registros_Puntarenas.txt","a")
    if Hotel == "San Carlos":
        file = open("Registros_San Carlos.txt","a")
    if Hotel == "Guanacaste":
        file = open("Registros_Guanacaste.txt","a")
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
    file.write(str(Edad))
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
    print("¡Registro de información exitoso!")
    return(Hotel,Identificacion)
# Función para el módulo de reservas
personas_por_habitación_hotel = [4,2,4]

Hotel_Puntarenas = []
Hotel_SanCarlos = []
Hotel_Guanacaste = []

costo_findesemana = 35000
costo_entresemana = 25000
total_fines_semana = 0
total_entre_semana = 0
subtotal = 0
descuento = 0
total_con_descuento = 0
monto_total = 0

fechas_seleccionadas = []
valores_factura = []
checkin_Puntarenas =[]
checkout_Puntarenas = []
checkin_SanCarlos =[]
checkout_SanCarlos = []
checkin_Guanacaste =[]
checkout_Guanacaste = []

matriz_checkin = [checkin_Puntarenas,checkin_SanCarlos,checkin_Guanacaste]
matriz_checkout = [checkout_Puntarenas,checkout_SanCarlos,checkout_Guanacaste]

def consulta_disponibilidad(): #esta es para consultar una fecha específica 

    seguir= "1"
    while seguir == "1":

        hotel = int(input("Ingrese el hotel en el que desea consultar disponibilidad:\n1 - Hotel Paraíso, Puntarenas\n2 - Hotel Paraíso, San Carlos\n3 - Hotel Paraíso, Guanacaste  \n"))

        while hotel not in [1,2,3]:

            print("Opción de hotel no válida, ingrese el hotel nuevamente")
            hotel = input("Ingrese el hotel en el que desea consultar disponibilidad:\n1 - Hotel Paraíso, Puntarenas\n2 - Hotel Paraíso, San Carlos\n3 - Hotel Paraíso, Guanacaste  \n")

        fecha = input("Ingrese la fecha en la que desea realizar su hospedaje Formato(aaaa-mm-dd) \n" )

        fecha = fecha.split("-")

        fecha_entero = []

        for elemento in fecha:
            fecha_entero.append(int(elemento))
    
        valor_buscado = fecha_a_serie(fecha_entero[0],fecha_entero[1],fecha_entero[2])

        
        encontrado = False
        if hotel == 1:
            for disponibilidad in Hotel_Puntarenas:
                if valor_buscado == disponibilidad[0]:
                    print("La disponibilidad para ese día es de ", 120 - disponibilidad[1]," habitaciones")
                    encontrado = True
            if not encontrado:
                    print("La disponibilidad para ese día es de 120 habitaciones")
                    
        elif hotel == 2:
            for disponibilidad in Hotel_SanCarlos:
                 if valor_buscado == disponibilidad[0]:
                    print("La disponibilidad para ese día es de ", 60 - disponibilidad[1]," habitaciones")
                    encontrado = True
            if not encontrado:
                    print("La disponibilidad para ese día es de 60 habitaciones")
        else:
            if hotel == 1:
                 if valor_buscado == disponibilidad[0]:
                    print("La disponibilidad para ese día es de ", 100 - disponibilidad[1]," habitaciones")
                    encontrado = True
            if not encontrado:
                    print("La disponibilidad para ese día es de 100 habitaciones")
        
        seguir = str(input("Si desea consultar otro día digite 1, sino digite cualquier otra tecla "))


def es_bisiesto(year): #Cálcula si un día es bisiesto
    bisiesto = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    return bisiesto

def fecha_a_serie(año,mes,día):
 # Crea una serie continua basada en una fecha en la que se cuenta el número de días desde una fecha base 
    año_base = (2000, 1, 1)
    fecha_actual = (año, mes, día)
    diferencia_años = fecha_actual[0] - año_base[0]
    
    suma_bisiestos = 0

    for año in range(año_base[0], fecha_actual[0]):
        
        if es_bisiesto(año):
            
            suma_bisiestos += 1
    numero_serial = (diferencia_años * 365) + suma_bisiestos + fecha_actual[2]
    
    meses_dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30] #El vector llega hasta noviembre, no tiene sentido agrega diciembre
    if es_bisiesto(fecha_actual[0]):
        meses_dias[1] = 29
   
    for dias_mes in meses_dias[:fecha_actual[1]-1]:
        numero_serial += dias_mes

    return numero_serial

def serie_a_fechas(serie):
#Pasa la serie que creamos de nuevo a formato fecha
    
    fecha_base = (1900, 1, 1) 
    
    diferencia_días = serie 
    año = fecha_base[0]
    
    while True:
        días_en_año = 366 
        if es_bisiesto(año):
            días_en_año = 366 
            
        else:
            días_en_año =365
            
        if diferencia_días >= días_en_año:
            diferencia_días -= días_en_año
            año += 1
        else:
            break
    
    meses_días = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    if es_bisiesto(año):
        meses_días[1] = 29
    
    mes = 1
    for días_en_mes in meses_días:
        if diferencia_días > días_en_mes:
            diferencia_días -= días_en_mes
            mes += 1
        else:
            break
    
    día = diferencia_días 
    return (año, mes, día)

def es_fin_de_semana(aaaa, mm, dd): #Determina si un día es fin de semana o no, devuelve un booleano
    #Fórmula de Zeller
    a = int((14 - mm) / 12)
    y = aaaa - a
    m = int(mm + (12 * a) - 2)
    d = int(dd + y + int(y/4) - int(y/100) + int(y/400)+((31*m) / 12)) % 7
    return d == 0 or d == 6

def contar_fines_entre_semana(fechas_seleccionadas):
    #Cuenta el número de días en fin de semana o entre semana y retorna el conteo
    fines_de_semana = 0
    entre_semana = 0
    for fecha in fechas_seleccionadas:
        if es_fin_de_semana(fecha[0],fecha[1],fecha[2]) == True:
            fines_de_semana += 1
        else:
            entre_semana += 1
    return fines_de_semana, entre_semana
            

def validar_fechas(fecha_inicio, días_reserva,habitaciones, reserva_hotel):
    #Valida si el total de días seleccionados está disponible
    suma_días_disponibles = 0
    

    for fechas_seleccionadas in range(fecha_inicio, fecha_inicio + días_reserva):

    
        disponible = False
        if reserva_hotel == 1:
        
             for disponibilidad in Hotel_Puntarenas:
                if fechas_seleccionadas == disponibilidad[0] and (120 - disponibilidad[1]) >= habitaciones:
                    suma_días_disponibles += 1
                    disponible = True
                    break
    
        if not disponible:
            suma_días_disponibles += 1
                
        elif reserva_hotel == 2:
            for disponibilidad in Hotel_SanCarlos:
                  if fechas_seleccionadas == disponibilidad[0] and (60 - disponibilidad[1]) >= habitaciones:
                    suma_días_disponibles += 1
                    disponible = True
                    break
    
            if not disponible:
                suma_días_disponibles += 1
                
        elif reserva_hotel == 3:
            for disponibilidad in Hotel_Guanacaste:
                  if fechas_seleccionadas == disponibilidad[0] and (100 - disponibilidad[1]) >= habitaciones:
                    suma_días_disponibles += 1
                    disponible = True
                    break
    
            if not disponible:
                suma_días_disponibles += 1

        if suma_días_disponibles < días_reserva:

            return False
        else:
            return True 

def calcular_habitaciones(número_personas, reserva_hotel):
    #A partir de el número de personas calcula la cantidad de habitaciones necesarias
    buscar_hotel = reserva_hotel - 1 #Usamos el número de hotel como índice

    n_persona = personas_por_habitación_hotel[buscar_hotel] #Buscamos el número de habitación en el arreglo

    
    num = número_personas // n_persona #Sacamos el entero de la división
    if(num % n_persona > 0): #Si hay residuo entonces sumamos, dado que esas personas tendrán que estar en otra habitación aunque la capacidad de la habitación es mayor
        num += 1
    
    return num

    
def calcular_montos(días_reserva, fines_semana,entre_semana, número_personas, costo_entresemana,costo_findesemana):
    #Cálcula todos los monts, descuentos y precios por fines de semana y entre semana y totales con impuesto
    #Se almacenan en variables para incluirlo en la factura
    total_fines_semana = fines_semana * costo_findesemana *número_personas
    total_entre_semana = entre_semana * costo_findesemana * número_personas
    subtotal = total_fines_semana + total_entre_semana
    if número_personas >= 5:
        descuento = 0.2
    else:
        descuento = 0
    total_con_descuento = subtotal * (1 - descuento)
    IVA = 0.13
    monto_total = total_con_descuento * (1+ IVA)
    return total_fines_semana, total_entre_semana,subtotal, descuento,total_con_descuento, monto_total

    
    
def hospedaje():
    #Realiza todo el proceso de reserva y check in/ check out
    reserva_hotel = int(input("Ingrese el hotel en el que desea consultar disponibilidad:\n1 - Hotel Paraíso, Puntarenas\n2 - Hotel Paraíso, San Carlos\n3 - Hotel Paraíso, Guanacaste  \n"))

    while reserva_hotel not in [1,2,3]:

        print("Opción de hotel no válida, ingrese el hotel nuevamente")
        reserva_hotel = input("Ingrese el hotel en el que desea hospedarse:\n1 - Hotel Paraíso, Puntarenas\n2 - Hotel Paraíso, San Carlos\n3 - Hotel Paraíso, Guanacaste  \n")

    fecha_reserva = input("Ingrese la fecha en la que desea realizar su hospedaje (formato aaaa-mm-dd) \n" )

    días_reserva = int(input("Ingrese el número de días que desea hospedarse: "))

    while días_reserva < 1:

        print("Número de días no válido")
        días_reserva = int(input("Ingrese el número de días que desea hospedarse: "))

    número_personas = int(input("Ingrese el número de personas que van a hospedarse: "))

    fecha_reserva = fecha_reserva.split("-")

    fecha_enteros_reserva = []

    for elemento in fecha_reserva:
        fecha_enteros_reserva.append(int(elemento))
    
    fecha_inicio = fecha_a_serie(fecha_enteros_reserva[0],fecha_enteros_reserva[1],fecha_enteros_reserva[2])

    habitaciones = calcular_habitaciones(número_personas, reserva_hotel)
                                    
    repetir_proceso = validar_fechas(fecha_inicio, habitaciones,días_reserva,reserva_hotel)
                                    

    while repetir_proceso == True:

        print("No todos los días están disponibles para reservar. Por favor seleccione otras fechas u otro Hotel")

        reserva_hotel = input("Ingrese el hotel en el que desea consultar disponibilidad:\n1 - Hotel Paraíso, Puntarenas\n2 - Hotel Paraíso, San Carlos\n3 - Hotel Paraíso, Guanacaste  \n")

        while reserva_hotel not in [1,2,3]:

            print("Opción de hotel no válida, ingrese el hotel nuevamente")
            reserva_hotel = input("Ingrese el hotel en el que desea hospedarse:\n1 - Hotel Paraíso, Puntarenas\n2 - Hotel Paraíso, San Carlos\n3 - Hotel Paraíso, Guanacaste  \n")

        fecha_reserva = input("Ingrese la fecha en la que desea realizar su hospedaje Formato(aaaa-mm-dd) \n" )

        días_reserva = int(input("Ingrese el número de días que desea hospedarse: "))

    while días_reserva < 1:

        print("Número de días no válido")
        días_reserva = int(input("Ingrese el número de días que desea hospedarse: "))

        número_personas = int(input("Ingrese el número de personas que van a hospedarse: "))

        fecha_reserva = fecha_reserva.split("-")

        fecha_enteros_reserva = []

        for elemento in fecha_reserva:
            fecha_entero_reserva.append(int(elemento))
    
        fecha_inicio = fecha_a_serie(fecha_entero_reserva[0],fecha_entero_reserva[1],fecha_entero_reserva[2])

        habitaciones = calcular_habitaciones(número_personas, reserva_hotel)

        repetir_proceso  = validar_fechas(fecha_inicio, habitaciones,días_reserva,reserva_hotel)

   
    
    for fecha_seleccionada in range(fecha_inicio, fecha_inicio + días_reserva):

        encontrado = False
        
        if reserva_hotel == 1:
                                        
            for disponibilidad in Hotel_Puntarenas:
                if fecha_seleccionada == disponibilidad[0]:
                    disponibilidad[1] += habitaciones
                    encontrado = True
            if not encontrado:
                Hotel_Puntarenas.append([fecha_seleccionada,habitaciones])

        elif reserva_hotel == 2:
                                        
            for disponibilidad in Hotel_SanCarlos:
                if fecha_seleccionada == disponibilidad[0]:
                    disponibilidad[1] += habitaciones
                    encontrado = True
            if not encontrado:
                Hotel_Puntarenas.append([fecha_seleccionada,habitaciones])

        else:

            for disponibilidad in Hotel_Guanacaste:
                if fecha_seleccionada == disponibilidad[0]:
                    disponibilidad[1] += habitaciones
                    encontrado = True
            if not encontrado:
                Hotel_Puntarenas.append([fecha_seleccionada,habitaciones])

    for fecha in range(fecha_inicio, fecha_inicio+días_reserva):
        fechas_seleccionadas.append(serie_a_fechas(fecha))

    print("¡Su reserva se realizó con éxito!")

    fines_de_semana, entre_semana = contar_fines_entre_semana(fechas_seleccionadas)

    print("Ha seleccionado ", fines_de_semana, " días de fin de semana y ", entre_semana, " días entre semana")

    total_fines_semana, total_entre_semana,subtotal, descuento,total_con_descuento, monto_total= calcular_montos(días_reserva, fines_de_semana, entre_semana, número_personas, costo_entresemana,costo_findesemana)

    
    print("El total por los días entre semana es ", total_entre_semana, " y el total por fines de semana es de ", total_fines_semana,"\nEl subtotal es de ", subtotal,"\nEl descuento corresponde a ", descuento * 100, "%", "\nel total con descuento es " ,total_con_descuento, "\nEl monto final a pagar (incluyendo IVA) es :", monto_total)

    horario_checkin_checkout(fecha_inicio, días_reserva, reserva_hotel, 1 )
    horario_checkin_checkout(fecha_inicio, días_reserva, reserva_hotel, 2 )
    
def horario_checkin_checkout(fecha_inicio, días_reserva, hotel, tipo ):
    #Despliega el checkin o check out. Es para no repetir código
    if tipo == 1:
        generar_checkin(hotel,fecha_inicio)
    else:
        generar_checkout(hotel,fecha_inicio+días_reserva)

def generar_checkin(reserva_hotel, fecha_reserva):
    #Realiza la validación de las horas de checkin y reserva la hora de checkin
    horarios = matriz_checkin[reserva_hotel-1]
    disponible = False
    valido = False
    
    #validar que la persona tenga cupo en la hora
    while not valido:
        hora_checkin = consultar_horas_check_in_out(["Ingrese la hora a la que desea hacer check in:","1 - 2","2 - 2:30","3 - 3","4 - 3:30","5 - 4","6 - 4:30","7 - 5"])
        serie = str(fecha_reserva)+ "-" + str(hora_checkin)
        if len(matriz_checkin[reserva_hotel-1]) > 0:
            for disponibilidad in matriz_checkin[reserva_hotel-1]:
                if serie == disponibilidad[0]:
                    if(disponibilidad[1]) < 20: # hay campos para registro
                        valido = True
                        disponible = True
                    else: # no quedan campos
                        print("La hora escogida no está disponible.")
                        disponible = True
            if not disponible: # fecha no existe en el registro
                valido = True
            else: # reseteamos para que pueda escoger otra hora
                disponible = False
        else: # no hay registros de fechas
            valido = True

    # Una vez hecha la validación se suma al horario si la serie está o se agrega la serie sino se encuentra 
    disponible = False
    for disponibilidad in matriz_checkin[reserva_hotel-1]:
        if serie == disponibilidad[0]:
            if(disponibilidad[1]) < 20:
                disponibilidad[1] += 1
                disponible = True
                break                
    if not disponible:
        matriz_checkin[reserva_hotel-1].append([serie,1])


def generar_checkout(reserva_hotel, fecha_reserva):
    #Lo mismo que la de checkin pero para check out
    horarios = matriz_checkout[reserva_hotel-1]
    disponible = False
    valido = False
    
    #validar que la persona tenga cupo en la hora
    while not valido:
        hora_checkout = consultar_horas_check_in_out(["Ingrese la hora a la que desea hacer check out:","1 - 11:30","2 - 12","3 - 12:30","4 - 1","5 - 1:30","6 - 2"])
        serie = str(fecha_reserva)+ "-" + str(hora_checkout)
        if len(matriz_checkout[reserva_hotel-1]) > 0:
            for disponibilidad in matriz_checkout[reserva_hotel-1]:
                if serie == disponibilidad[0]:
                    if(disponibilidad[1]) < 20: # hay campos para registro
                        valido = True
                        disponible = True
                    else: # no quedan campos
                        print("La hora escogida no está disponible.")
                        disponible = True
            if not disponible: # fecha no existe en el registro
                valido = True
            else: # reseteamos para que pueda escoger otra hora
                disponible = False
        else: # no hay registros de fechas
            valido = True

    # Una vez hecha la validación se suma al horario si la serie está o se agrega la serie sino se encuentra
    disponible = False
    #hora_checkout = consultar_horas_check_in_out(["Ingrese la hora a la que desea hacer check out:","1 - 11:30","2 - 12","3 - 12:30","4 - 1","5 - 1:30","6 - 2"])
    #serie = str(fecha_reserva)+ "-" + str(hora_checkout)
    for disponibilidad in matriz_checkout[reserva_hotel-1]:
        if serie == disponibilidad[0]:
            if(disponibilidad[1]) < 20:
                disponibilidad[1] += 1
                disponible = True
                break               
    if not disponible:
        matriz_checkout[reserva_hotel-1].append([serie,1])


def consultar_horas_check_in_out(mensaje):
    #Despliega un menú con las horas de checkin y checkout
    for x in mensaje:
        print(x)
    hora_checkin = int(input())
    while hora_checkin < 0 or hora_checkin > 7:
        print("La opción ingresada no es válida.")
        for x in mensaje:
            print(x)
        hora_checkin = int(input())
    return hora_checkin

# Función para el módulo de facturación
def modulo_facturacion():
    # Implementa la lógica del módulo de facturación aquí
    pass

# Función para el módulo de reportes
def modulo_reportes():
    # Implementa la lógica del módulo de reportes aquí
    pass

#file = open("Hoteles.txt")
#for i in Especificaciones:
#    if Hotel == "Puntarenas":
#        if i == "P,capacidad":
#            Puntarenas -= 1
#            Especificaciones[Posicion + 1] = Puntarenas
#    if Hotel == "San Carlos":
#        if i == "S,capacidad":
#            SanCarlos -= 1
#            Especificaciones[Posicion + 1] = SanCarlos
#    if Hotel == "Guanacaste":
#        if i == "G,capacidad":
#            Guanacaste -= 1
#            Especificaciones[Posicion + 1] = Guanacaste
#    Posicion += 1
#file.close()



    
while continuar == 1:
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    if usuario == "admin" and contraseña == "Adm112":
        continuar = 0
        print("Inicio de sesión exitoso.\n")
        while continuar == 0:
            print("Bienvenido al menú:")
            print("1. Módulo de Registros")
            print("2. Módulo de Reservas")
            print("3. Módulo de Facturación")
            print("4. Módulo de Reportes")
            print("5. Salir")
            opcion = int(input("Selecciona una opción: "))
             
            if opcion == 1:
                Hotel,Identificacion = modulo_registros(Puntarenas,SanCarlos,Guanacaste,continuar)
                if Hotel == "Puntarenas":
                    Hotel_seleccionado = 1
                if Hotel == "San Carlos":
                    Hotel_seleccionado = 2
                if Hotel == "Guanacaste":
                    Hotel_seleccionado = 3
            elif opcion == 2:
                hospedaje()
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

