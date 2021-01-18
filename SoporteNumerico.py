def numero_en_rango(numero, limiteinferior, limitesuperior):
    while numero not in range(limiteinferior, limitesuperior+1):
        print("Error")
        numero = int(input("Introduzca el numero: " + "Debe estar entre: "+ str(limiteinferior) + " y " + str(limitesuperior)))
    return numero


def corroborar_division(numerador, denominador):
    if denominador == 0:
         print("error")
         division = None
    else:
        division = numerador / denominador
    return division


def es_primo(numero):
    primo = True
    if numero < 0:
        print("Introdujo un numero negativo")
        print("Si desea trabajar con el valor absoluto de ese numero")
        opc = int(input("Introduzca 1, sino introduzca cualquier otro numero: "))
        if opc == 1:
            numero = - numero
        else:
            return "Selecciono no trabajar con esta funcion"

    if numero == 1 or numero == 0:
        primo = False
        return primo
    elif numero == 2:
        return primo

    elif numero % 2 == 0:
        primo = False
        return primo
    else:
        mitad = numero ** 0.5
        divisor = 2
        while divisor <= mitad:
            resto = numero % divisor
            if resto == 0:
                primo = False
            return primo
            divisor += 1
        return primo


def divisores(numero):
    base = 0
    numero_primo = 0
    cantidad_primos = 0
    lista_de_primos = []
    while numero_primo < numero:
        if es_primo(base):
            numero_primo = base
            cantidad_primos += 1
            lista_de_primos.append(numero_primo)
        base += 1

    divisores = []
    for valor in lista_de_primos:
        while numero % valor == 0:
            divisores.append(valor)
            numero = numero // valor
    return divisores


def contador_divisores(listas_de_divisores):
    divisores_contados = []
    for numero in range(len(listas_de_divisores)):
        primo = listas_de_divisores[numero]
        contador = 0
        for numero in listas_de_divisores:
            if numero == primo:
                contador += 1
        if contador == 1:
            elemento = primo
        else:
            elemento = str(primo) + "^" + str(contador)
        if elemento not in divisores_contados:
            divisores_contados.append(elemento)
    return divisores_contados


def simplificar(numerador,denominador):

    lista_numerador = divisores(numerador)
    lista_denominador = divisores(denominador)
    longitud_numerador = len(lista_numerador)
    longitud_denominador = len(lista_denominador)
    if longitud_numerador > longitud_denominador:
        cantidad_de_vueltas = longitud_denominador
    else:
        cantidad_de_vueltas = longitud_numerador
    for indice in range(cantidad_de_vueltas):
        if lista_numerador[indice] == lista_denominador[indice]:
            lista_numerador.remove(lista_numerador[indice])
            lista_denominador.remove(lista_denominador[indice])

    numerador = denominador = 1
    for valor in lista_numerador:
        numerador *= valor

    for valor in lista_denominador:
        denominador *= valor

    if denominador == 1:
        fraccion = str(numerador)
    else:
        fraccion = str(numerador) + "/" + str(denominador)

    return fraccion

