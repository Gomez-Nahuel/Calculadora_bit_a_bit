from colorama import Fore, Style
from functions import compuerta_and, compuerta_or, compuerta_xor, convertir_a_binario, convertir_a_decimal

def mostrar_menu():
    print(Fore.YELLOW + " --------------------------- ")
    print("")
    print("Calculadora Bit a Bit")
    print("")
    print(Fore.BLACK + "1. AND (&)")
    print("2. OR (|)")
    print("3. XOR (^)")
    print("0. Salir")
    print(Fore.YELLOW + " --------------------------- ")

def calculadora():
    opcion = ""
    while opcion != '0':
        mostrar_menu()
        opcion = input("Elige una opción: ")
        print(" --------------------------- ")
        if opcion == '0':
            print("🔄 Saliendo del programa ")
            print("")
        if opcion in ['1', '2', '3']:
            try:
                decimalNumA = int(input("Número A (entero): "))
                decimalNumB = int(input("Número B (entero): "))
                binarioNumA = convertir_a_binario(decimalNumA)
                binarioNumB = convertir_a_binario(decimalNumB)

                if opcion == '1':
                    resultado = compuerta_and(binarioNumA, binarioNumB)
                    simbolo = '&'
                    data = """
# Compuerta AND = Produce una salida de 1 (verdadero) solo si todas las entradas son 1.
Es como decir `Ambas condiciones deben cumplirse`
                    """
                elif opcion == '2':
                    resultado = compuerta_or(binarioNumA, binarioNumB)
                    simbolo = '|'
                    data = """
# Compuerta OR = Genera una salida de 1 si al menos una de las entradas es 1.
Es como decir `Una u otra condición puede cumplirse`
                        """
                elif opcion == '3':
                    resultado = compuerta_xor(binarioNumA, binarioNumB)
                    simbolo = '^'
                    data = """
# Compuerta XOR = La salida es 1 únicamente si las entradas son diferentes (una es 1 y la otra 0).
Es como decir `Solo una condición puede cumplirse, pero no ambas`
                    """
                print(" --------------------------- ")
                print(Fore.GREEN + f"{data}")
                print(f"Operación en decimal: {decimalNumA} [{binarioNumA}] {simbolo} {decimalNumB} [{binarioNumB}] = {convertir_a_decimal(resultado)} [{resultado}].")
                print(Style.RESET_ALL + "")
            except ValueError:
                print(" --------------------------- ")
                print(" Ingresa solo números enteros.")
        else:
            print(" --------------------------- ")
            print(" Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    calculadora()