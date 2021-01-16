# Función Suma: Dado un vector v retorna la suma intermedias
def suma(v):
    l = len(v)
    if l == 0:
        return []
    elif l == 1:
        return v
    else:
        s = []
        for i in range(l):
            for j in range(l):
                if j == i+1:
                    s.append(v[i]+v[j])
        return s

# Funcion tringuloPascal: Dado un numero k retorna los indices de los coficientes de cada termino del binomio de Newton elevado a la k-esima potencia
def trianguloPascal(k):
    # Definimos k con 0 y 1 como casos base
    if k == 0:
        return [1]
    elif k == 1:
        return [1,2,1]
    else:
	# Definimos el caso recursivo
        return [1]+suma(trianguloPascal(k-1))+[1]


def menu():
    k = int(input("Ingrese el numero del ladrillo: "))
    v = trianguloPascal(k)
    print(v)
menu()
