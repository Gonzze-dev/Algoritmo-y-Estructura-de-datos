from cola import Cola
from pila import Pila
from random import randint


#EJERCICIO 1
def sacar_Vocales(palabra):
    obj_Cola = Cola()
    nueva_Palabra = ''
    Volcales = ['a', 'e', 'i', 'o', 'u']
    
    for i in range(0, len(palabra)):
        obj_Cola.arribo(palabra[i])
    
    for i in range(0, len(palabra)):
        if (obj_Cola.en_frente() in Volcales):
            obj_Cola.atencion()
        else:
            obj_Cola.mover_final()
    
    while(not obj_Cola.cola_vacia()):
        nueva_Palabra += obj_Cola.atencion()
    
    return nueva_Palabra

def ejercicio_1():
    
    palabra = 'Palabra'

    print(sacar_Vocales(palabra))

#EJERCICIO 2
def invertir_Cola(contenedor):
    obj_Cola = Cola()
    obj_Pila = Pila()

    for i in range(0, len(contenedor)):
        obj_Cola.arribo(contenedor[i])

    while(not obj_Cola.cola_vacia()):
        obj_Pila.apilar(obj_Cola.atencion())
    
    while(not obj_Pila.pila_vacia()):
        obj_Cola.arribo(obj_Pila.desapilar())

    for i in range(0, obj_Cola.tamanio()):
        contenedor[i] = obj_Cola.atencion()
    
    return contenedor

def ejercicio_2():
    vector = [1,2,3,4,5,6,7,8,9]

    vector = invertir_Cola(vector)

    for i in range(0, len(vector)):
        print(vector[i])
        
#EJERCICIO 3
def es_Palindromo(palabra):
    obj_Cola = Cola()
    obj_Pila = Pila()
    letra = None

    for i in range(0, len(palabra)):
        letra = palabra[i].lower()
        obj_Cola.arribo(letra)
        obj_Pila.apilar(letra)

    mitad = len(palabra)//2

    for i in range(0, mitad):
        if(obj_Pila.desapilar() != obj_Cola.atencion()):
            return False

    return True

def ejercicio_3():
    palabra = 'Neuquen'
    palabra2 = 'Palabra'

    print('Palabra 1: ', es_Palindromo(palabra))
    print('Palabra 1: ', es_Palindromo(palabra2))

#EJERCICIO 6
def contar_Ocurrencias(obj_Cola, numero_a_contar):
    contador = 0

    for i in range(0, obj_Cola.tamanio()):

        if(obj_Cola.mover_final() == numero_a_contar):
            contador += 1

    return contador

def ejercicio_6():
    obj_Cola = Cola()

    for i in range(0, 15):
        obj_Cola.arribo(randint(1, 10))
    
    numero = int(input('ingrese un numero: '))

    print('Cantidad de ocurrencias: ', contar_Ocurrencias(obj_Cola, numero))

#EJERCICIO 11

def imprimir_Cola(obj_Cola):
    mat = []
    for i in range(0, obj_Cola.tamanio()):
        mat.append(obj_Cola.en_frente())
        print('Nombre: ', mat[i][0], 
              '\nPlaneta: ', mat[i][1])

        obj_Cola.mover_final()
#A
def get_Pj_De_Los_Planetas_Alderaan_Endor_Tatooine(obj_Cola):
    Planetas = ['Alderaan', 'Endor', 'Tatooine']
    indice = 0
    Mat_PJ_de_SW = []

    for i in range(0, obj_Cola.tamanio()):

        if (obj_Cola.en_frente()[1] in Planetas):
            Mat_PJ_de_SW.append(obj_Cola.en_frente())
            indice += 1

        obj_Cola.mover_final()

    return Mat_PJ_de_SW

def mostrar_Pj_De_Star_Wars_Con_Su_Planeta(personajes_y_Planetas):
    
    for personaje_y_Planeta in personajes_y_Planetas:
        print('Nombre: ', personaje_y_Planeta[0], 
              '\nPlaneta: ', personaje_y_Planeta[1])
    
#B
def get_Planeta_Natal_De_Luke_Y_Han_Solo(obj_Cola):
    luke_Y_Han = ['Luke Skywalker', 'Han Solo']
    nombre_Personajes_Y_Planetas = []

    for Planeta in range(0, obj_Cola.tamanio()):

        if (obj_Cola.en_frente()[0] in luke_Y_Han):
            nombre_Personajes_Y_Planetas.append(obj_Cola.en_frente())

        obj_Cola.mover_final()

    return nombre_Personajes_Y_Planetas

def mostrar_Planeta_Natal_De_Luke_Y_Han_Solo(personajes_y_Planetas):
    luke = []
    han = []

    for personaje_y_Planeta in personajes_y_Planetas:
        if (personaje_y_Planeta[0] == 'Luke Skywalker'):
            luke.append(personaje_y_Planeta)
        elif(personaje_y_Planeta[0] == 'Han Solo'):
            han.append(personaje_y_Planeta)
    
    if (len(luke) == 0):
        print('Luke no esta en la cola')
    else:
        print('Nombre: ', luke[0][0], 
              '\nPlaneta: ', luke[0][1])
    
    if (len(han) == 0):
        print('Han no esta en la cola')
    else:
        print('Nombre: ', han[0][0], 
              '\nPlaneta: ', han[0][1])

#C
def insertar_Personaje_Antes_Que_Yoda(obj_Cola):

    nombre = input('ingrese el nombre del personaje: ')
    planeta_Natal = input('Ingrese el planeta natal del personaje: ')

    for i in range(0, obj_Cola.tamanio()):

        if (obj_Cola.en_frente()[0] == 'Yoda'):
            obj_Cola.arribo([nombre, planeta_Natal])
        
        obj_Cola.mover_final()

#D
def eliminar_Personaje_Despues_De_Jar_Jar_Binks(obj_Cola):
    contador = 1

    while(obj_Cola.en_frente()[0] != 'Jar Jar Binks'):
            obj_Cola.mover_final()
            contador +=1

    if(obj_Cola.tamanio() == contador):
        obj_Cola.mover_final()
    elif(obj_Cola.en_frente()[0] == 'Jar Jar Binks'):
        obj_Cola.mover_final()
        obj_Cola.atencion()

    for i in range(contador, obj_Cola.tamanio()):
        obj_Cola.mover_final()


def ejercicio_11():
    obj_Cola = Cola()

    Mat_PJ_de_SW = [
                   ['Chewbacca', 'Anoat'],
                   ['Obi-Wan Kenobi', 'Tatooine'],
                   ['Yoda','Endor'],
                   ['BB8', 'Alderaan'],
                   ['Padme Amidala','Atollon'],
                   ['Luke Skywalker', 'Tatooine'],   
                   ['Han Solo','Corellia'],
                   ['Jar Jar Binks', 'Anoat']
                   ]
    
    for datos_PJ in Mat_PJ_de_SW:
        obj_Cola.arribo(datos_PJ)
    
    print('\nMOSTRAR PERSONAJE CON SU PLANETA DE ORIGEN\n')
    mostrar_Pj_De_Star_Wars_Con_Su_Planeta(get_Pj_De_Los_Planetas_Alderaan_Endor_Tatooine(obj_Cola))

    print('\nPLANETA DE LUKE Y HAN\n')

    mostrar_Planeta_Natal_De_Luke_Y_Han_Solo(get_Planeta_Natal_De_Luke_Y_Han_Solo(obj_Cola))
    
    print('\nINSERTAR PERSONAJE ANTES QUE YODA\n')
    insertar_Personaje_Antes_Que_Yoda(obj_Cola)

    imprimir_Cola(obj_Cola)

    print('\nELIMINAR PERSONAJE DESPUES DE JAR JAR BINKS\n')
    eliminar_Personaje_Despues_De_Jar_Jar_Binks(obj_Cola)

    imprimir_Cola(obj_Cola)



#EJERCICIO 16
def unificar_Colas(obj_Cola_1, obj_Cola_2):
    minimo = None

    obj_Cola_Unificada = Cola()

    if obj_Cola_1.en_frente() < obj_Cola_2.en_frente():
        minimo = obj_Cola_1.en_frente()
    else:
        minimo = obj_Cola_2.en_frente()

    for i in range(0, obj_Cola_1.tamanio()):
        obj_Cola_Unificada.arribo(obj_Cola_1.mover_final())
    
    for i in range(0, obj_Cola_2.tamanio()):
        
        while(obj_Cola_2.en_frente() > obj_Cola_Unificada.en_frente()):
            obj_Cola_Unificada.mover_final()
            
        obj_Cola_Unificada.arribo(obj_Cola_2.mover_final())

        #agrege el if ya que como en la cola tengo el minimo, el numero a insertar 
        # me quedaria al final de la cola, por lo que no quedaria la cola ordenada
        if(obj_Cola_Unificada.en_frente() != minimo):         
            while((obj_Cola_Unificada.en_frente() > minimo)):
                obj_Cola_Unificada.mover_final()
        else:
            
            for i in range(0, obj_Cola_Unificada.tamanio()-1):
                obj_Cola_Unificada.mover_final()
        
    return obj_Cola_Unificada
        
def ejercicio_16():
    obj_Cola_1 = Cola()
    obj_Cola_2 = Cola()
    obj_Cola_Unificada = Cola()

    vec_Num_1 = [1,3,5,6,8,9,11,12,13,16]
    vec_Num_2 = [0,0,0,0,1,1,2,3,6,7,10,13,14,15]

    for i in range(0, len(vec_Num_1)):
        obj_Cola_1.arribo(vec_Num_1[i])
    
    for i in range(0,len(vec_Num_2)):
        obj_Cola_2.arribo(vec_Num_2[i])
    
    obj_Cola_Unificada = unificar_Colas(obj_Cola_1, obj_Cola_2)

    print(obj_Cola_Unificada.tamanio(), ' ', len(vec_Num_1), ' ', len(vec_Num_2))

ejercicio_16()