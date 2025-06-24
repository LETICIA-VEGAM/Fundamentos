def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def calculadora():
    print("Calculadora Básica en Python")
    print("Operaciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = input("Elige una operación (1/2/3/4): ")

    if opcion in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Error: Entrada inválida. Por favor ingresa números.")
            return

        if opcion == '1':
            resultado = sumar(num1, num2)
        elif opcion == '2':
            resultado = restar(num1, num2)
        elif opcion == '3':
            resultado = multiplicar(num1, num2)
        elif opcion == '4':
            resultado = dividir(num1, num2)

        print(f"Resultado: {resultado}")
    else:
        print("Opción inválida. Intenta de nuevo.")
    # Ejecutar la calculadora
calculadora()     