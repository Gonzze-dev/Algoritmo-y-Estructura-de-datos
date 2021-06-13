# 6,7,15,22 de la guia
from tdaLista import Lista
from random import randint

#EJERCICIO 2
def eliminarVocalesDeUnaLista(palabra):
    objLista = Lista()

    vocales = ['a', 'e', 'i', 'o', 'u']

    for caracter in palabra:
        objLista.insertar(caracter.lower());   

    for vocal in vocales:
        aux = objLista.eliminar(vocal)
        while(aux is not None):
            aux = objLista.eliminar(vocal)

    return objLista

def ejercicio2():
    objLista = Lista()

    palabra = "hOla gente como estan"

    objLista = eliminarVocalesDeUnaLista(palabra)
    objLista.barrido()

#EJERCICIO 3

def esPar(numero):
    if (numero % 2 == 0):
        return True
    else:
        return False

def dividirListaEnDosYDevolverUnaConLosNumerosParesYOtraConLosImpares(objLista):
    listaConNumerosPares = Lista()
    listaConNumerosImpares = Lista()
    numero = 0

    for i in range(0, round(objLista.tamanio()/2)):
        numero = objLista.obtener_elemento(i)

        if (esPar(numero)):
            listaConNumerosPares.insertar(numero)

    for i in range(round(objLista.tamanio()/2), objLista.tamanio()):
        numero = objLista.obtener_elemento(i)

        if (not esPar(numero)):
            listaConNumerosImpares.insertar(numero)

    return listaConNumerosPares, listaConNumerosImpares

def ejercicio3():
    objLista = Lista()
    listaConNumerosImpares = Lista()
    listaConNumerosPares = Lista()
    
    for i in range(0, 30):
        objLista.insertar(randint(1,20))

    listaConNumerosPares, listaConNumerosImpares = dividirListaEnDosYDevolverUnaConLosNumerosParesYOtraConLosImpares(objLista)

    print("Pares")
    listaConNumerosPares.barrido()

    print("\nImpares")
    listaConNumerosImpares.barrido()
    
def esPrimo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True

#EJERCICIO 5
def sacarNumerosPrimosDeUnaLista(objLista):
    numero = 0
    i = 0

    while (i < objLista.tamanio()):

        numero = objLista.obtener_elemento(i)

        if(esPrimo(numero)):
            while(numero is not None):
                numero = objLista.eliminar(numero)
        
        i += 1

def ejercicio5():
    objLista = Lista()
    
    for i in range(0, 30):
        objLista.insertar(randint(1,20))
    
    sacarNumerosPrimosDeUnaLista(objLista)

    objLista.barrido()
