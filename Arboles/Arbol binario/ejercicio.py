from TDA_Arbol_Binario import Arbol
from random import randint

arbolNumeros = Arbol()

#EJERCICIO Contar Ocurrencias
def contarOcurrencias(arbol, dato):
    contador = 0

    if(arbol.info is not None):
        if(dato == arbol.info):
            contador += 1
        if(arbol.izq is not None):
            contador += contarOcurrencias(arbol.izq, dato)
        if(arbol.der is not None):
            contador += contarOcurrencias(arbol.der, dato)

    return contador

def ejercicioContarOcurrencias():
    numero = 5
    for i in range(0, 100):
        arbolNumeros.insertar_nodo(randint(1,10))

    print("La cantidad de ocurrencias del numero '", numero, "' es de:", contarOcurrencias(arbolNumeros, numero))

#EJERCICIO Contar pares e impares
def contarParesEImpares(arbol):
    contPares, contImpares = 0, 0

    if(arbol.info is not None):
        if(arbol.info % 2 == 0):
            contPares += 1
        else:
            contImpares += 1
        if(arbol.izq is not None):
            par, impar = contarParesEImpares(arbol.izq)
            contPares += par
            contImpares += impar
        if(arbol.der is not None):
            par, impar = contarParesEImpares(arbol.der)
            contPares += par
            contImpares += impar

    return contPares, contImpares

def ejercicioContarParesImpares():
    for i in range(0, 100):
        arbolNumeros.insertar_nodo(randint(1,10))

    cantidadPares, cantidadImpares = contarParesEImpares(arbolNumeros)
    print("La cantidad de numeros pares en el arbol es de: ", cantidadPares)
    print("La cantidad de numeros impares en el arbol es de: ", cantidadImpares)

ejercicioContarParesImpares()