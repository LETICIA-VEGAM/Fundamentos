def nuevoTema(tema: str): 
    print(f"\n-----{tema}-----\n")


if __name__ == "__main__":

    nuevoTema("Operadores aritméticos")
    print("Operador Suma, 5 + 6 =", 5 + 6)
    print("Operador Resta, 9 - 8 =", 9 - 8)
    print("Operador Multiplicación, 8 * 3 =", 8 * 3)
    print("Operador División, 12 / 6 =", 12 / 6)

    #Este es un comentario de una sola línea.
    ''' Este es un comentario de varias lineas'''

    nuevoTema("Operadores Lógicos")
    print("True and True:", True and True)
    #1. Hacer las tablas de verdad
    #2. 1 Ejemplo de cada operador de comparación
    nuevoTema("Operadores de comparación")
    print("5 == 6:", 5 == 6)

    nuevoTema("Variables")
    variable1 = 10
    _variable2 = 6.2547
    variable3 = "pepe"
    nombreVariable = 8
    nombre_variable = 34.2
    print(variable1, _variable2, variable3, nombreVariable, nombre_variable)

    a, b, c = 5, 10.8, "Hola"
    print(a)
    print(b)
    print(c)

    #Ejemplo de variable dinámica
    nombre_variable = "Adios"
    print(nombre_variable)

    nuevoTema("Enteros")
    w = 105
    x = 1234567897654321
    y = .58
    z = 0b00110011
    h = 0xFF

    print(w, type(w))
    print(x, type(x))
    print(y, type(y))
    print(z, type(z))
    print(h, type(h))

    nuevoTema("Flotantes")
    x = 1234.56
    print(x, type(x))
    y = -0.2584
    print(y, type(y))

    nuevoTema("Números complejos")
    x = -46j
    y = 12 + 45j
    z = 2j
    print(x, type(x))
    print(y, type(y))
    print(z, type(z))
    print(c, type(c))

    nuevoTema("Booleanos")
    x = True
    print(x, type(x))
    