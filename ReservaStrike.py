reservas = {}

def reservar_zapatillas():
    global reservas
    if len(reservas) >= 20:
        print("No quedan más reservas disponibles.")
        return
    print("\n-- Reservar Zapatillas --")
    nombre = input("Nombre del comprador: ")
    if nombre in reservas:
        print("Error: ese nombre ya tiene una reserva.")
        return
    clave = input("Digite la palabra secreta para confirmar la reserva: ")
    if clave != "EstoyEnListaDeReserva":
        print("Error: palabra clave incorrecta. Reserva no realizada.")
        return
    reservas[nombre] = 1
    print(f"Reserva realizada exitosamente para {nombre}.")

def buscar_reserva():
    global reservas
    print("\n-- Buscar Zapatillas Reservadas --")
    nombre = input("Nombre del comprador a buscar: ")
    if nombre not in reservas:
        print("No se encontró ninguna reserva con ese nombre.")
        return
    cantidad = reservas[nombre]
    tipo = "VIP" if cantidad == 2 else "estándar"
    print(f"Reserva encontrada: {nombre} - {cantidad} par(es) ({tipo}).")
    if cantidad == 1:
        vip = input("¿Desea pagar adicional para VIP y reservar 2 pares? (s/n): ").lower()
        if vip == "s":
            reservas[nombre] = 2
            print(f"Reserva actualizada a VIP. Ahora {nombre} tiene 2 pares reservados.")
        else:
            print("Manteniendo reserva actual.")

def cancelar_reserva():
    global reservas
    print("\n-- Cancelar Reserva --")
    nombre = input("Nombre del comprador a cancelar reserva: ")
    if nombre not in reservas:
        print("No se encontró ninguna reserva con ese nombre.")
        return
    del reservas[nombre]
    print(f"La reserva de {nombre} ha sido cancelada.")

def menu_principal():
    while True:
        print("\nTOTEM AUTOATENCIÓN RESERVA STRIKE")
        print("1.- Reservar zapatillas")
        print("2.- Buscar zapatillas reservadas")
        print("3.- Cancelar reserva")
        print("4.- Salir")
        opcion = input("Seleccione una opción (1-4): ")
        if opcion == "1":
            reservar_zapatillas()
        elif opcion == "2":
            buscar_reserva()
        elif opcion == "3":
            cancelar_reserva()
        elif opcion == "4":
            print("\nPrograma terminado...")
            break
        else:
            print("\nDebe ingresar una opción válida!!")

menu_principal()
