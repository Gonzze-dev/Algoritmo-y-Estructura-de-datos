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



#EJERCICIO 12
def unificar_Colas(obj_Cola_1, obj_Cola_2):
    cant_Veces_Que_Se_Movieron_Los_Elementos_De_La_Cola = None

    obj_Cola_Unificada = Cola()

    for i in range(0, obj_Cola_1.tamanio()):
        obj_Cola_Unificada.arribo(obj_Cola_1.mover_final())
    
    for i in range(0, obj_Cola_2.tamanio()):
        cant_Veces_Que_Se_Movieron_Los_Elementos_De_La_Cola = 1

        while(obj_Cola_2.en_frente() > obj_Cola_Unificada.en_frente()):
            obj_Cola_Unificada.mover_final()
            cant_Veces_Que_Se_Movieron_Los_Elementos_De_La_Cola += 1

        obj_Cola_Unificada.arribo(obj_Cola_2.mover_final())
        
        for i in range(0, obj_Cola_Unificada.tamanio()-cant_Veces_Que_Se_Movieron_Los_Elementos_De_La_Cola):
            obj_Cola_Unificada.mover_final()
        
    return obj_Cola_Unificada
        
def ejercicio_12():
    obj_Cola_1 = Cola()
    obj_Cola_2 = Cola()
    obj_Cola_Unificada = Cola()

    Cola_Concatenada = '[ '

    vec_Num_1 = [1,3,5,6,8,9,11,12,13,16]
    vec_Num_2 = [0,0,0,0,1,1,2,3,6,7,10,13,14,15]

    for i in range(0, len(vec_Num_1)):
        obj_Cola_1.arribo(vec_Num_1[i])
    
    for i in range(0,len(vec_Num_2)):
        obj_Cola_2.arribo(vec_Num_2[i])
    
    obj_Cola_Unificada = unificar_Colas(obj_Cola_1, obj_Cola_2)

    for i in range(0, obj_Cola_Unificada.tamanio()):
       Cola_Concatenada += str(obj_Cola_Unificada.mover_final()) + ' ,'
    
    print(Cola_Concatenada, ']')

#FUNCION GENERAL
def get_Personajes_Concatenados_De_Un_Vector(vec_Personajes):
    
    personajes = '';

    if (len(vec_Personajes) > 0):
        for i in range (0, len(vec_Personajes)):
            personajes += vec_Personajes[i] + '\n'
    else:
        personajes = 'No hay personajes cargados'
    
    return personajes

def get_Personajes_Concatenados_De_Una_Matriz(mat_Personajes):
    
    personajes = '';

    if (len(mat_Personajes) > 0):
        for i in range (0, len(mat_Personajes)):
            personajes += mat_Personajes[i][0] + ' ' + mat_Personajes[i][1] + '\n'
    else:
        personajes = 'No hay personajes cargados'
    
    return personajes

def get_Mensaje_Si_Existe_Personaje_O_Super_Heroe(nombre_1, nombre_2):
    
    if(nombre_1 != None):
        return 'El nombre de ' + nombre_2 + ' es: ' + nombre_1
    else:
        return nombre_2 + ' no esta en la cola' + nombre_1

#A
def get_Nombre_Personaje(obj_Cola, nombre_Super_Heroe):
    nombre = None

    for i in range(0, obj_Cola.tamanio()): #recorro todo para dejar la cola como esta originamente
        
        if (obj_Cola.en_frente()[1] == nombre_Super_Heroe):
            nombre = obj_Cola.en_frente()[0]

        obj_Cola.mover_final()

    return nombre

#B
def  get_Super_Heroinas(obj_Cola):
    
    vec_Personajes_Femeninos = []

    for i in range(0, obj_Cola.tamanio()):

        if (obj_Cola.en_frente()[2] == 'F'):
            vec_Personajes_Femeninos.append(obj_Cola.en_frente()[1])

        obj_Cola.mover_final()

    return vec_Personajes_Femeninos

#C
def  get_Personajes_Masculinos(obj_Cola):
    
    vec_Personajes_Masculinos = []

    for i in range(0, obj_Cola.tamanio()):

        if (obj_Cola.en_frente()[2] == 'M'):
            vec_Personajes_Masculinos.append(obj_Cola.en_frente()[0])

        obj_Cola.mover_final()

    return vec_Personajes_Masculinos

#D
def get_Nombre_Del_Super_Heroe(obj_Cola, nombre_Personaje):
    nombre = None

    for i in range(0, obj_Cola.tamanio()): #recorro todo para dejar la cola como esta originamente
        
        if (obj_Cola.en_frente()[0] == nombre_Personaje):
            nombre = obj_Cola.en_frente()[1]

        obj_Cola.mover_final()
    
    return nombre

#E
def get_Nombres_Con_S(obj_Cola):
    vec_Super_Heroes_O_Personajes_Con_S = []

    for i in range(0, obj_Cola.tamanio()):

        if(obj_Cola.en_frente()[0][0] == 'S' or obj_Cola.en_frente()[1][0] == 'S'):
            vec_Super_Heroes_O_Personajes_Con_S.append([obj_Cola.en_frente()[0], obj_Cola.en_frente()[1]])

        obj_Cola.mover_final();    

    return vec_Super_Heroes_O_Personajes_Con_S


#EJERCICIO 22
def ejercicio_22():
    obj_Cola = Cola()

    array_Personajes_MCU = [
                            ['Tony Stark', 'Iron Man', 'M'],
                            ['Thor Odinson', 'Thor', 'M'],
                            ['Carol Danvers','Capitana Marvel','F'],
                            ['Steve Rogers', 'Capitan America', 'M'],
                            ['Scott Lang', 'Hombre Hormiga', 'F'],
                            ['Stephen Strange', 'Doctor Strange', 'M'],
                           ]
    
    for i in range(0, len(array_Personajes_MCU)):
        obj_Cola.arribo(array_Personajes_MCU[i])

    print('NOMBRE DE CAPITANA MARVEL')
    print(get_Mensaje_Si_Existe_Personaje_O_Super_Heroe(get_Nombre_Personaje(obj_Cola, 'Capitana Marvel'), 'Capitana Marvel'))

    print('\nSUPER HEROINAS')
    print(get_Personajes_Concatenados_De_Un_Vector(get_Super_Heroinas(obj_Cola)))

    print('PERSONAJES MASCULINOS')
    print(get_Personajes_Concatenados_De_Un_Vector(get_Personajes_Masculinos(obj_Cola)))

    print('NOMBRE DE SUPER HEROE DE SCOTT LANG')
    print(get_Mensaje_Si_Existe_Personaje_O_Super_Heroe(get_Nombre_Del_Super_Heroe(obj_Cola, 'Scott Lang'), 'Scott Lang'))

    print('\nPERSONAJES Y SUPER HEROES CON INICIAL S')
    print(get_Personajes_Concatenados_De_Una_Matriz(get_Nombres_Con_S(obj_Cola)))

    print('NOMBRE DE SUPER HEROE DE CAROL DANVERS')
    print(get_Mensaje_Si_Existe_Personaje_O_Super_Heroe(get_Nombre_Del_Super_Heroe(obj_Cola, 'Carol Danvers'), 'Carol Danvers'))

ejercicio_22() 