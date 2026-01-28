def mostrar_menu():
    print("\n=== Sistema de Gestión Nequi ===")
    print("1. Cargar saldo")
    print("2. Pagar")
    print("3. Transferir dinero")
    print("4. Mostrar saldo")
    print("5. Salir")


def cargar_saldo(saldo):
    try:
        monto = float(input("Ingrese el monto a cargar: "))
        if monto <= 0:
            print("Error: La platica debe ser por arriba de 0 michicato.")
            return saldo
        saldo += monto
        print(f"miraaalo, ya tienes platica. Nuevo saldo: ${saldo:.2f}")
        return saldo
    except ValueError:
        print("Error: bruto.")
        return saldo


def pagar(saldo):
    try:
        monto = float(input("Ingrese el monto a pagandini: "))
        if monto <= 0:
            print("Error: Animal,el monto debe ser mayor a 0.")
            return saldo
        if monto > saldo:
            print("No le alcanza, vaya busque platica.")
            return saldo
        saldo -= monto
        print(f"Bien, ta lisssto. Te quedan: ${saldo:.2f}")
        return saldo
    except ValueError:
        print("Error: bruto.")
        return saldo


def transferir(saldo):
    celular = input("Ingrese el número de celular del destinatario (10 dígitos): ")

    if not (celular.isdigit() and len(celular) == 10):
        print("Error: el número de celular debe tener exactamente 10 dígitos,ponga bien el dedo.")
        return saldo

    try:
        monto = float(input("Ingrese el monto a transferir: "))
        if monto <= 0:
            print("Error: ya te lo he dicho,el monto debe ser mayor a 0.")
            return saldo
        if monto > saldo:
            print("tamos paila, no hay platica.")
            return saldo

        saldo -= monto
        print(f"Transferencia exitosa a {celular}. Saldo restante: ${saldo:.2f}")
        return saldo

    except ValueError:
        print("Error: este monto NO VA!!,es invalido.")
        return saldo


def main():
    saldo = 0.0

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            saldo = cargar_saldo(saldo)
        elif opcion == "2":
            saldo = pagar(saldo)
        elif opcion == "3":
            saldo = transferir(saldo)
        elif opcion == "4":
            print(f"Saldo actual: ${saldo:.2f}")
        elif opcion == "5":
            print("Nos abrimos del sistema. Chaolin.")
            break
        else:
            print("nombeee asi no. Aprenda a leer el menú.")


if __name__ == "__main__":
    main()