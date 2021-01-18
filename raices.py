from SoporteFunciones import *
from Sistemadeecuaciones import *
from SoporteNumerico import numero_en_rango


opcion = -1
while opcion != 5:
    print("Menu de opciones")
    print("1- trabajar con cuadratica")
    print("2- trabajar con lineal")
    print("3_ trabajar con un polinomio")
    print("4_ trabajar con sistema de ecuaciones")
    print("5_ salir")
    opcion = int(input("Introduzca una opcion: "))
    opcion = numero_en_rango(opcion, 1, 5)
    if opcion == 1:
        eleccion = -1
        while eleccion != 4:
            print("Menu")
            print("1_ discriminante")
            print("2_ raices")
            print("3_ vertice")
            print("4_ volver al menu principal")
            eleccion = int(input("Introduzca una opcion: "))
            eleccion = numero_en_rango(eleccion, 1, 4)
            a = float(input("Introduzca x2: "))
            b = float(input("Introduzca x: "))
            c = float(input("Introduzca k: "))
            if eleccion == 1:
                print(discriminante(a, b, c))
            elif eleccion == 2:
                print(baskara(a, b, c))
            elif eleccion == 3:
                print("El vertice es: ")
                print(vertice(a, b, c))
    elif opcion == 2:
        x1 = float(input("x1: "))
        y1 = float(input("y1: "))
        x2 = float(input("x2: "))
        y2 = float(input("y2: "))
        A = x1, y1
        B = x2, y2
        y = construccion_funcion_x2puntos(A, B)
        print(y)
        a = float(input("Pendiente: "))
        b = float(input("Ordenada al origen: "))
        print(cortes(a, b))
    elif opcion == 3:
        a = 1
        if int(input("Introduzca si a distinto de cero oprima cualquier numero menos cero: ")) != 0:
            a = float(input("a: "))
        if int(input("Si son dos raices distintas, presione 2: ")) == 2:
            x1 = float(input("Introduce la 1 raiz: "))
            x2 = float(input("Introduce la 2 raiz: "))
        else:
            x1 = x2 = float(input("Introduzca la raiz: "))
        print(construccion_cuadratica(x1, x2, a=a))
    elif opcion == 4:
        eleccion = - 1
        while eleccion != 3:
            print("Menu de opciones")
            print("1_despejar y")
            print("2_dar solucion a pares ordenados")
            print("3_ volver al menu principal")
            eleccion = int(input("Introduzca una opcion: "))
            if eleccion == 1:
                y = float(input("Ingrese y: "))
                x = float(input("Ingrese x: "))
                k = float(input("Ingrese k: "))
                print(despejar_y(y, x, k))
            elif eleccion == 2:
                print("Coloca el formato de la primer ecuacion")
                print("1_ y = x + a")
                print("2_ y + x = a")
                print("3_ y + a = x")
                print("4_ y + x + a = 0")
                if int(input("Si los formatos son distintos, presione 1")) == 1:
                    formato1 = int(input("Introduzca el formato de la primer ecuacion: "))
                    formato1 = numero_en_rango(formato1, 1, 4)
                    formato2 = int(input("Introduzca el formato de la segunda ecuacion: "))
                    formato2 = numero_en_rango(formato2, 1, 4)
                else:
                    formato1 = int(input("Introduzca el formato de las ecuaciones: "))
                    formato1 = numero_en_rango(formato1, 1, 4)
                    formato2 = formato1
                y1 = float(input("Ingrese y1: "))
                x1 = float(input("Ingrese x1: "))
                k1 = float(input("Ingrese k1: "))
                y2 = float(input("Ingrese y2: "))
                x2 = float(input("Ingrese x2: "))
                k2 = float(input("Ingrese k2: "))

                ecuacion_1 = [y1, x1, k1]
                ecuacion_2 = [y2, x2, k2]
                print(sistema_de_ecuacion(ecuacion_1, ecuacion_2, formato1=formato1, formato2=formato2))
print("Gracias por usar este programa")
