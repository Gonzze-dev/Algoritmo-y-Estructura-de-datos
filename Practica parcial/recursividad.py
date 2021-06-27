# EJERCICIO 19
def funcion(n):
    if n == 1:
        return 2
    elif n >= 2:
        return n + 1/funcion(n-1)

# EJERCICIO 20

def busqueda_Secuencial(arreglo, elementoABuscar):
    if len(arreglo) < 1:
        return None
    else:
        if arreglo[-1] == elementoABuscar:
            return len(arreglo)-1

        return busqueda_Secuencial(arreglo[:-1], elementoABuscar)

def resolverTorreDeHanoi(cantDiscos, origen, destino, auxiliar):
        if(cantDiscos == 1):
            destino.append(origen.pop())
        else:
            resolverTorreDeHanoi(cantDiscos - 1, origen, auxiliar, destino)
            destino.append(origen.pop())
            resolverTorreDeHanoi(cantDiscos - 1, auxiliar, destino, origen)

#EJERCICIO 24  
def ejercicio24():
    origen = []
    auxiliar = []
    destino = []

    for i in range(0,5):
        origen.append(i)

    print(origen)

    resolverTorreDeHanoi(len(origen), origen, destino, auxiliar)

    print("\n", destino)

#EJERCICIO 12

def euclidesMCD(numero_a, numero_b, resto=None):
    if(numero_a == 0):
        return numero_b
    if(numero_b == 0):
        return numero_a
    if(numero_a == numero_b):
        return numero_a

    if (numero_a % numero_b == 0):
        print(resto)
        return resto
    else:
        return euclidesMCD(numero_b,numero_a % numero_b, numero_a % numero_b)

#EJERCICIO 13
def euclidesMCM(numero_a, numero_b):
    return (numero_a*numero_b)/euclidesMCD(numero_a, numero_b)

#EJERCICIO 14
def sumarDigitosDeUnNumero(numero):
    if (len(str(numero)) == 1):
        return numero
    else:
        cantDigitos = len(str(numero))
        digito = ((numero % (10**cantDigitos)) - (numero % (10**(cantDigitos-1)))) // 10**(cantDigitos-1)

        return digito + sumarDigitosDeUnNumero(numero%(10**(cantDigitos-1)))

#EJERCICIO (no me acuerdo el numero)
def recorrerMatriz(matriz, x=0, y=0):
    if x < len(matriz):
        if(y < len(matriz[x])):
            print(matriz[x][y])
            recorrerMatriz(matriz, x, y+1)
        elif(y >= len(matriz[x])):
            y = 0
            recorrerMatriz(matriz, x+1, y)

Pn = 54
Qn = 24
for i in range(1,200):
    if (Pn % i == 0) and (Qn % i == 0):
        print(i)
