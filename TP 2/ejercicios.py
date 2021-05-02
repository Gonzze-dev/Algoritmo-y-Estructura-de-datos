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

#EJERCICIO 12

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

def ejericcio_12():
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
    print(existe_Leila_O_Boba_En_Pila(obj_Pila2))
    print(existe_Leila_O_Boba_En_Pila(obj_Pila3))

#EJERCICIO 14

def insertar_El_Numero_Menor_al_Mayor_En_Pila(obj_Pila_A_Insertar_Numero, numero):

    obj_Numeros_Mayores_Pila = Pila()

    #Si se ingresa mas de 1 numero entro aqui
    if (not obj_Pila_A_Insertar_Numero.pila_vacia()):
        
        #Si es mayor lo inserto de una
        if (numero >= obj_Pila_A_Insertar_Numero.elemento_cima()):
            obj_Pila_A_Insertar_Numero.apilar(numero)

        else:

            # Evaluo todos los menores al numero incluyendo los iguales y los apilo
            # En la pila auxiliar obj_Numeros_Mayores_Pila
            # Despues cuando se rompa el bucle doy por hecho que llego a que
            # Numero es mayor al elemento de la cima o que no encontro ninguno

            while((not obj_Pila_A_Insertar_Numero.pila_vacia()) and (numero < obj_Pila_A_Insertar_Numero.elemento_cima())):
                elemento = obj_Pila_A_Insertar_Numero.desapilar()
                obj_Numeros_Mayores_Pila.apilar(elemento)
            
            obj_Pila_A_Insertar_Numero.apilar(numero)

            #Coloco todos los numeros que eran mayores al numero ingresado
            while(not obj_Numeros_Mayores_Pila.pila_vacia()):
                obj_Pila_A_Insertar_Numero.apilar(obj_Numeros_Mayores_Pila.desapilar())
            
    else:
        #Si no hay nada le inserto el primer numero esto para cuando se hace el primer bucle
        obj_Pila_A_Insertar_Numero.apilar(numero)

def ejercicio_14():

    obj_Pila = Pila()
    opcion = 'y'
    numero = None
    elemento = None

    while(opcion == 'y'):
        numero = int(input('Ingrese un numero: '))

        insertar_El_Numero_Menor_al_Mayor_En_Pila(obj_Pila, numero)

        opcion = input('¿Volver a ingresar un numero? (Y/N): ').lower()
    
    while(not obj_Pila.pila_vacia()):
        print(obj_Pila.desapilar())

#EJERCICIO 16

def get_Interseccion_De_Pilas(obj_Pila_1, Obj_Pila_2):
    elemento = None

    obj_aux_Pila = Pila()
    obj_aux_Pila_2 = Pila()
    obj_Interseccion_Pila = Pila()

    while(not obj_Pila_1.pila_vacia()):
    
        while(not Obj_Pila_2.pila_vacia()):

            elemento = Obj_Pila_2.desapilar()
            obj_aux_Pila_2.apilar(elemento)

            if(elemento == obj_Pila_1.elemento_cima()):
                obj_Interseccion_Pila.apilar(elemento)

        obj_aux_Pila.apilar(obj_Pila_1.desapilar())
        
        #Devuelvo elementos a la pila 2 para devolverla a como estaba
        while(not obj_aux_Pila_2.pila_vacia()):
            Obj_Pila_2.apilar(obj_aux_Pila_2.desapilar())
    
    #Devuelvo elementos a la pila 1 para devolverla a como estaba
    while(not obj_aux_Pila.pila_vacia()):
        obj_Pila_1.apilar(obj_aux_Pila.desapilar())

    return obj_Interseccion_Pila

def ejercicio_16():
    obj_Pila = Pila()
    obj_Pila2 = Pila()
    obj_Interseccion_Pila = Pila()

    personajes_Star_Wars_EP_V = ['Luke Skywalker', 'Han Solo', 'Darth Vader', 'Leia Organa',
                                'Yoda', 'Capitán Needan', 'Almirante Ozzel', 'Lando Calrissian']

    personajes_Star_Wars_EP_VII = ['Kylo Ren', 'Rey', 'Han Solo', 'Luke Skywalker', 'C3PO',
                                  'Leia Organa', 'Chewbacca', '	Poe Dameron']


    for i in range(0, len(personajes_Star_Wars_EP_V)):
        obj_Pila.apilar(personajes_Star_Wars_EP_V[i])

    for i in range(0, len(personajes_Star_Wars_EP_VII)):
        obj_Pila2.apilar(personajes_Star_Wars_EP_VII[i])
    
    obj_Interseccion_Pila = get_Interseccion_De_Pilas(obj_Pila, obj_Pila2)

    while(not obj_Interseccion_Pila.pila_vacia()):
        print('El personaje ', obj_Interseccion_Pila.desapilar(), ' esta en ambas peliculas')
    

#EJERCICIO 22
#A FUNCION
def mostrar_PLanetas_En_Orden_De_Mision(obj_Pila):
    obj_Aux_Pila = Pila()
    obj_Aux_Pila = invertir_Pila_Sin_Perder_Elementos(obj_Pila)

    while(not obj_Aux_Pila.pila_vacia()):
        print('Planeta: ', obj_Aux_Pila.desapilar()[0])

#B FUNCIONES
def get_Dinero_Total(obj_Pila):
    obj_Aux_Pila = Pila()
    Vector = None
    total = 0.0

    while(not obj_Pila.pila_vacia()):
        Vector = obj_Pila.desapilar()
        obj_Aux_Pila.apilar(Vector)
        total += Vector[1]
    
    while(not obj_Aux_Pila.pila_vacia()):
        obj_Pila.apilar(obj_Aux_Pila.desapilar())

    return total

def get_Nombre_Con_Mayor_Fortuna(obj_Boba_Pila, obj_Din_Pila):
    total_1 = get_Dinero_Total(obj_Boba_Pila)
    total_2 = get_Dinero_Total(obj_Din_Pila)

    if(total_1 > total_2):
        return ('Boba Fett ' +  'con: ' + str(total_1))
    elif(total_1 < total_2):
        return ('Din Djarin ' + 'con: ' +  str(total_2))
    else:
        return 'Anbos poseen la misma fortuna ' + 'Boba Fett ' +  'con: ' + str(total_1) + ' Din Djarin ' + 'con: ' +  str(total_2)

#C FUNCION

def get_Numero_Mision_Boba_Capturo_A_Han(obj_Pila):
    obj_Aux_Pila = Pila()
    Vector = None
    Mision = 1

    while((not obj_Pila.pila_vacia()) and (obj_Pila.elemento_cima()[2] != 'Han Solo')):
        Mision += 1
        Vector = obj_Pila.desapilar()
        obj_Aux_Pila.apilar(Vector)

    while(not obj_Aux_Pila.pila_vacia()):
        obj_Pila.apilar(obj_Aux_Pila.desapilar())
    
    return Mision

#D FUNCION
def get_Total_Personas_Capturadas(obj_Pila):
    obj_Aux_Pila = Pila()
    contador = 0

    while(not obj_Pila.pila_vacia()):
        obj_Aux_Pila.apilar(obj_Pila.desapilar())

        if (obj_Aux_Pila.elemento_cima()[2] != 'Fallo'):
            contador += 1
    
    while(not obj_Aux_Pila.pila_vacia()):
        obj_Pila.apilar(obj_Aux_Pila.desapilar())
    
    return contador

def ejercicio_22():
    obj_Bitacora_Nave_Boba_Pila = Pila()
    obj_Bitacora_Nave_Din_Pila = Pila() 

    bitacora_Nave_Boba = [['Alderaan', 3479.42, 'Almirante Ozzel'], 
                          ['Anoat', 2389.23, 'Kylo Ren'],
                          ['Corellia', 20045.68,'Han Solo'],
                          ['Base Starkiller', 21354.00, 'Chewbacca'], 
                          ['Christophsis', 3221.30, 'C3PO']
                          ]
                          
    bitacora_Nave_Din = [['Cantonica', 347.42, 'Yoda'], 
                          ['Dagobah', 23809.23, 'Rey'],
                          ['Felucia', 49.00, 'R2-D2'],
                          ['Corellia', 20045.68,'Han Solo'],
                          ['Dantooine', 2134.00, 'Leia Organa'], 
                          ['Eadu', 920981.30, 'Obi-Wan Kenobi'],
                          ['Hoth',0.00,'Fallo']
                          ]

    for i in range(0, len(bitacora_Nave_Boba)):
        obj_Bitacora_Nave_Boba_Pila.apilar(bitacora_Nave_Boba[i])

    for i in range(0, len(bitacora_Nave_Din)):
        obj_Bitacora_Nave_Din_Pila.apilar(bitacora_Nave_Din[i])

    print('Planetas visitados por Boba Fett')
    mostrar_PLanetas_En_Orden_De_Mision(obj_Bitacora_Nave_Boba_Pila)
    
    print('\nPlanetas visitados por Din Djarin')
    mostrar_PLanetas_En_Orden_De_Mision(obj_Bitacora_Nave_Din_Pila)

    print('\nEl que objuvo mayor fortuna fue: ', get_Nombre_Con_Mayor_Fortuna(obj_Bitacora_Nave_Boba_Pila, obj_Bitacora_Nave_Din_Pila))

    print('\nBoba Fett capturo a Han Solo en la mision: ', get_Numero_Mision_Boba_Capturo_A_Han(obj_Bitacora_Nave_Boba_Pila))

    print('\nTotal personas capturadas por Boba Fett: ', get_Total_Personas_Capturadas(obj_Bitacora_Nave_Boba_Pila))
    print('Total personas capturadas por Din Djarin: ', get_Total_Personas_Capturadas(obj_Bitacora_Nave_Din_Pila))

#EJERCICIO 24

#A FUNCIONES
def get_Pos_Groot_And_Roket(obj_Pila):
    obj_Aux_Pila = Pila()
    indice = obj_Pila.tamanio() - 1
    posicion_Groot = None
    posicion_Roket = None

    while((not obj_Pila.pila_vacia()) and ((posicion_Groot == None) or (posicion_Roket == None))):
        obj_Aux_Pila.apilar(obj_Pila.desapilar())

        if(obj_Aux_Pila.elemento_cima()[0] == 'Groot'):
            posicion_Groot = indice
        elif(obj_Aux_Pila.elemento_cima()[0] == 'Rocket Raccoon'):
            posicion_Roket = indice
        
        indice -= 1
    while(not obj_Aux_Pila.pila_vacia()):
        obj_Pila.apilar(obj_Aux_Pila.desapilar())
    
    return posicion_Groot, posicion_Roket

def get_mensaje_Posicion_De_Groot_And_Rocket(Vec_Posiciones):
    mensaje_1 = None
    mensaje_2 = None

    if(Vec_Posiciones[0] != None):
        mensaje_1 = 'Groot se encuentra en la posicion: ' + str(Vec_Posiciones[0])
    else:
         mensaje_1 = 'Groot no esta en la pila'
    
    if(Vec_Posiciones[1] != None):
        mensaje_2 = 'Rocket Raccoon se encuentra en la posicion: ' + str(Vec_Posiciones[1])
    else:
        mensaje_2 = 'Rocket Raccoon no esta en la pila'

    return (mensaje_1 + '\n' + mensaje_2)
#B FUNCION
def get_Personajes_Que_Aparecen_En_Mas_De_5_Peliculas_And_La_Cantidad(obj_Pila):
    obj_Aux_Pila = Pila()
    cant_peliculas = None
    indice = 0
    Vector = None
    Mat = [[]]

    while(not obj_Pila.pila_vacia()):
        obj_Aux_Pila.apilar(obj_Pila.desapilar())
        cant_peliculas = len(obj_Aux_Pila.elemento_cima())-1

        if (cant_peliculas > 5):
            Mat.insert(indice, (obj_Aux_Pila.elemento_cima()[0], cant_peliculas))
            indice += 1
    
    while(not obj_Aux_Pila.pila_vacia()):
        obj_Pila.apilar(obj_Aux_Pila.desapilar())
    
    return Mat

#C FUNCIONES
def get_Cantidad_Peliculas_En_La_Que_Aparece_Black_Widow(obj_Pila):
    obj_Aux_Pila = Pila()
    cant_peliculas = 0

    while((not obj_Pila.pila_vacia()) and (obj_Pila.elemento_cima()[0] != 'Black Widow')):
        obj_Aux_Pila.apilar(obj_Pila.desapilar())

    if(obj_Pila.elemento_cima()[0] == 'Black Widow'):
        cant_peliculas = len(obj_Pila.elemento_cima())-1

    while(not obj_Aux_Pila.pila_vacia()):
        obj_Pila.apilar(obj_Aux_Pila.desapilar())

    return cant_peliculas

def get_Mensaje_Black_Widow(cant_peliculas):
    if (cant_peliculas > 0):
        return 'Black Widow ha participado en: ' + str(cant_peliculas) + ' peliculas'
    else:
        return  'Black Widow no ha participado en ninguna pelicula'

#D FUNCION
def get_Nombres_Que_Empiezan_Con_C_D_And_G(obj_Pila):
    obj_Aux_Pila = Pila()
    indice = 0
    Vector = []

    while(not obj_Pila.pila_vacia()):
        obj_Aux_Pila.apilar(obj_Pila.desapilar())

        if (obj_Aux_Pila.elemento_cima()[0][0] in ['C','D','G']):
            Vector.insert(indice, obj_Aux_Pila.elemento_cima()[0])
            indice += 1

    while(not obj_Aux_Pila.pila_vacia()):
        obj_Pila.apilar(obj_Aux_Pila.desapilar())

    return Vector

def ejercicio_24():
    Mat = None
    Vector = None

    obj_Personajes_Marvel_Pila = Pila()
    # MCU = [['Black Widow', 'Avengers Confidential', 'Iron Man: Rise of Technovore', 'Avengers: Infinity War'],
    #        ['Iron Man', 'Iron Man I', 'Iron Man II','Avengers Confidential', 'Iron Man: Rise of Technovore', 'The Invincible Iron Man', 'Avengers: Infinity War'],
    #        ['Hulk', 'Avengers Confidential', 'Hulk vs Thor', 'Avengers: Infinity War'],
    #        ['Hawkeye', 'Avengers Confidential'],
    #        ['Thor', 'Hulk vs Thor', 'Avengers: Infinity War'],
    #        ['Groot', 'Infinity War']
    #        ['Rocket Raccoon', 'Infinity War']]

    MCU = [['Black Widow', 1 , 3, 4 , 5, 2, 4],
           ['Rocket Raccoon', 3, 7],
           ['Iron Man', 1 , 3, 4 , 5, 2, 4, 7, 9],
           ['Hulk', 9 ,3 , 4 ,6],
           ['Hawkeye', 3],
           ['Groot', 2],
           ['Thor', 3, 4 , 2, 1]]
    
    for i in range(0, len(MCU)):
        obj_Personajes_Marvel_Pila.apilar(MCU[i])
    
    #A
    print('\nPosicion de Groot y Rocket en la pila\n')
    print(get_mensaje_Posicion_De_Groot_And_Rocket(get_Pos_Groot_And_Roket(obj_Personajes_Marvel_Pila)))

    #B
    print('\nPersonajes que aparecen en mas de 5 peliculas')
    Mat = get_Personajes_Que_Aparecen_En_Mas_De_5_Peliculas_And_La_Cantidad(obj_Personajes_Marvel_Pila)
    
    if ((len(Mat)-1) > 0):
        for i in range(0, (len(Mat)-1)):
            print('\nNombre: ', Mat[i][0], '\nTotal Peliculas: ', Mat[i][1])
    else:
        print('\nNingun personaje de MCU en la pila que aparezca en mas de 5 peliculas')

    #C
    print('\nCantidad de peliculas en las que aparece Black Widow')
    print('\n', get_Mensaje_Black_Widow(get_Cantidad_Peliculas_En_La_Que_Aparece_Black_Widow(obj_Personajes_Marvel_Pila)))

    #D
    print('\nPersonajes que empiecen con C, D o G')
    Vector = get_Nombres_Que_Empiezan_Con_C_D_And_G(obj_Personajes_Marvel_Pila)

    if ((len(Vector)-1) > 0):
        for i in range(0, (len(Vector)-1)):
            print('\nNombre: ', Vector[i])
    else:
        print('\nNo hay personajes de MCU en la pila que empiecen con C, D o G')


#-------------------------FIN#-------------------------