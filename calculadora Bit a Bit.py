def mostrar_menu():
    print("Calculadora Bit a Bit")
    print("1. AND (&)")
    print("2. OR (|)")
    print("3. XOR (^)")
    print("0. Salir")

def calculadora():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
#podemos salir de la calculadora si ya realizamos la operacion
        if opcion == '0':
            print("Saliendo...")
            break

        if opcion in ['1', '2', '3']:
             
            try:
                Numa = int(input("Número A (entero): "))
                Numb = int(input("Número B (entero): "))

                if opcion == '1':
                    resultado = Numa & Numb
                    simbolo = '&'
                elif opcion == '2':
                    resultado = Numa | Numb
                    simbolo = '|'
                elif opcion == '3':
                    resultado = Numa ^ Numb
                    simbolo = '^'

                print(f"{Numa} {simbolo} {Numb} = {resultado} (binario: {bin(resultado)})")

            except ValueError:
                print(" Ingresa solo números enteros.")
        else:
            print(" Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    calculadora()