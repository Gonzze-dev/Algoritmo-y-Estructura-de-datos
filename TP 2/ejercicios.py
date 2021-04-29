from pila import Pila
from random import randint

#EJERCICIO 1

def retornar_Numero_De_Ocurrencias(datos_pila, n):
    contador = 0

    while(not datos_pila.pila_vacia()):

        if (n == datos_pila.desapilar()):
            contador += 1

    return contador

def ejercicio_1():
    obj_pila = Pila()

    for i in range(0, 100):
        num = randint(1, 10)
        obj_pila.apilar(num)

    numero = int(input('ingrese un numero: '))
    
    print(retornar_Numero_De_Ocurrencias(obj_pila, numero))
    
#EJERCICIO 2

def sacar_Impares_De_Pila(datos_pila):
    aux_Pila = Pila()

    while(not datos_pila.pila_vacia()):
        elemento = datos_pila.desapilar()

        if (elemento % 2 == 0):
            aux_Pila.apilar(elemento)

    return aux_Pila

def ejercicio_2():
    obj_Pila = Pila()

    for i in range(0, 100):
        num = randint(1, 10)
        obj_Pila.apilar(num)
    
    obj_Pila = sacar_Impares_De_Pila(obj_Pila)

    for i in range(0, obj_Pila.tamanio()):
        print(obj_Pila.desapilar())

#EJERCICIO 3

def sacar_Ocurrencias_De_La_Pila(datos_pila):
    aux_Pila = Pila()
    aux_Conjunto = list()

    while(not datos_pila.pila_vacia()):
        elemento = datos_pila.desapilar()

        if (not (elemento in aux_Pila)):
            aux_Conjunto.append(elemento)
            aux_Pila.apilar(elemento)
    
    return aux_Pila

def ejercicio_3():
    obj_Pila = Pila()

    for i in range(0, 100):
        num = randint(1, 10)
        obj_Pila.apilar(num)

    obj_Pila = sacar_Ocurrencias_De_La_Pila(obj_Pila)
    
#EJERCICIO 4

def invertir_Pila(pila_a_invertir):
    aux_Pila = Pila()

    while(not pila_a_invertir.pila_vacia()):
        aux_Pila.apilar(pila_a_invertir.desapilar())

    return aux_Pila

def ejercicio_4():
    obj_Pila = Pila()

    for i in range(0, 20):
        num = randint(1, 10)
        obj_Pila.apilar(num)
    
    obj_Pila.apilar(102)
    obj_Pila = invertir_Pila(obj_Pila)

#EJERCICIO 5

def invertir_Pila_Sin_Perder_Elementos(pila_a_invertir):
    pila_Inversa = Pila()
    aux_Pila = Pila()

    #me da la pila invertida
    while(not pila_a_invertir.pila_vacia()):
        elemento = pila_a_invertir.desapilar()
        pila_Inversa.apilar(elemento)
        aux_Pila.apilar(elemento)

    #le devuelvo los elementos que desapile a la pila original
    while(not aux_Pila.pila_vacia()):
        pila_a_invertir.apilar(aux_Pila.desapilar())

    return pila_Inversa

def es_Palindromo(palabra_pila):
    pila_Inversa = Pila()
    pila_Inversa = invertir_Pila_Sin_Perder_Elementos(palabra_pila)

    while((not palabra_pila.pila_vacia()) and (palabra_pila.elemento_cima() == pila_Inversa.elemento_cima())):
        palabra_pila.desapilar()
        pila_Inversa.desapilar()
    
    if(palabra_pila.pila_vacia()):
        return True
    else:
        return False

def ejercicio_5():
    obj_Pila = Pila()
    palabra = input('Ingrese una palabra: ')

    for letra in palabra:
        obj_Pila.apilar(letra)

    print(es_Palindromo(obj_Pila))

#EJERCICIO 6

def existe_Leila_O_Boba_En_Pila(personajes_star_wars):

    Estado = None
    aux_Pila = Pila()

    while((not personajes_star_wars.pila_vacia()) and (not (personajes_star_wars.elemento_cima() in ('Boba Fet', 'Leia Organa')))):
        aux_Pila.apilar(personajes_star_wars.desapilar())

    if (personajes_star_wars.pila_vacia()):
        Estado = False
    else:
        Estado = True
    
    while(not aux_Pila.pila_vacia()):
        personajes_star_wars.apilar(aux_Pila.desapilar())
    
    return Estado

def ejericcio_6():
    obj_Pila = Pila()
    obj_Pila2 = Pila()
    obj_Pila3 = Pila()

    obj_Pila.apilar('Boba Fet')
    obj_Pila.apilar('Leia Organa')
    obj_Pila.apilar('Darth Vader')
    obj_Pila.apilar('Yoda')
    obj_Pila.apilar('Chewbacca')
    obj_Pila.apilar('Obi-Wan Kenobi')
    obj_Pila.apilar('R2-D2')
    obj_Pila.apilar('C3PO')

    obj_Pila2.apilar('Leia Organa')
    obj_Pila2.apilar('Darth Vader')
    obj_Pila2.apilar('Yoda')
    obj_Pila2.apilar('Chewbacca')
    obj_Pila2.apilar('Obi-Wan Kenobi')
    obj_Pila2.apilar('R2-D2')
    obj_Pila2.apilar('C3PO')

    obj_Pila3.apilar('Darth Vader')
    obj_Pila3.apilar('Yoda')
    obj_Pila3.apilar('Chewbacca')
    obj_Pila3.apilar('Obi-Wan Kenobi')
    obj_Pila3.apilar('R2-D2')
    obj_Pila3.apilar('C3PO')

    print(existe_Leila_O_Boba_En_Pila(obj_Pila))

ejericcio_6()
