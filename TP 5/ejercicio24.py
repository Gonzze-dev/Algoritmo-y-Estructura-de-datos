from TDA_Arbol_Binario_RyN_MOD2 import Arbol
from TDA_Cola import Cola
from TDA_Lista import Lista

#PUNTO B
def cargar_descripcion(arbol):
    pendientes = Cola()
    pendientes.arribo(arbol)
    
    while(not pendientes.cola_vacia()):
        nodo = pendientes.atencion()
        print(nodo.info, nodo.datos)
        nodo.datos['Descripcion'] = input('Cargar descripcion de la criatura: ')
        if(nodo.izq is not None):
            pendientes.arribo(nodo.izq)
        if(nodo.der is not None):
            pendientes.arribo(nodo.der)

#PUNTO D
def contar_ocurrencias_de_heroe(arbol, nombre_heroe):
    contador = 0

    if(arbol.info is not None):
        if(arbol.datos['Derrotado'] == nombre_heroe):
            contador += 1
        if(arbol.izq is not None):
            contador += contar_ocurrencias_de_heroe(arbol.izq, nombre_heroe)
        if(arbol.der is not None):
            contador += contar_ocurrencias_de_heroe(arbol.der, nombre_heroe)
    
    return contador

def recompilar_datos_de_un_arbol(arbol, campo, vec_datos=[]):
    if(arbol.info is not None):
        if(not((arbol.datos[campo] in vec_datos))
            and (arbol.datos[campo] not in ['', '-', None])):
            vec_datos.append(arbol.datos[campo])
        if(arbol.izq is not None):
            heroes = recompilar_datos_de_un_arbol(arbol.izq, campo, vec_datos)
        if(arbol.der is not None):
            heroes = recompilar_datos_de_un_arbol(arbol.der, campo, vec_datos)

    return vec_datos

def contar_mayor_cantidad_de_criaturas_derrotadas_por_un_heroe(arbol):
    vector_heroes = recompilar_datos_de_un_arbol(arbol, 'Derrotado')
    ocurrencias = 0
    lista_dic_heroes = Lista()

    for nombre_heroe in vector_heroes:
        ocurrencias = contar_ocurrencias_de_heroe(arbol, 
                        nombre_heroe)
        lista_dic_heroes.insertar({'nombre': nombre_heroe,
                                 'cantidad_derrotados': ocurrencias}, 
                                 'cantidad_derrotados')
    
    return lista_dic_heroes

def imprimir_tres_heroes_con_mas_criaturas_derrotadas(lista):
    i = lista.tamanio()-1
    while((not lista.lista_vacia()) and (i >= (lista.tamanio()-3))):
        print(lista.obtener_elemento(i))
        i -= 1

#PUNTO E
def inorden_criaturas_derrotadas_por_un_heroe(arbol, nombre):
    if(arbol.info is not None):
        if(arbol.izq is not None):
            inorden_criaturas_derrotadas_por_un_heroe(arbol.izq, nombre)
        if(arbol.datos['Derrotado'] == nombre):
            print(arbol.datos['Criatura'])
        if(arbol.der is not None):
            inorden_criaturas_derrotadas_por_un_heroe(arbol.der, nombre)
    


def ejercicio_24():
    lista_dic_heroes = Lista()
    dic_criaturas = [{'Criatura': 'Ceto', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Tifon', 'Derrotado': 'Zeus', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Equidna', 'Derrotado': 'Argos panoptnes', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Dino', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Pefredo', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Enio', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Escila', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Caribdis', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Euriale', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Esteno', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Medusa', 'Derrotado': 'Perseo', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Ladon', 'Derrotado': 'Heracles', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Aguila del Caucaso', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Quimera', 'Derrotado': 'Belerofonte', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Hidra de Lerna', 'Derrotado': 'Heracles', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Leon de Nemea', 'Derrotado': 'Heracles', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Esfinge', 'Derrotado': 'Edipo', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Dragon de la Colquida', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Gerbero', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Cerda de Cromion', 'Derrotado': 'Teseo', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Ortro', 'Derrotado': 'Heracles', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Toro de Creta', 'Derrotado': 'Teseo', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Jabali De Calidon', 'Derrotado': 'Atalanta', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Carcinos', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Gerion', 'Derrotado': 'Heracles', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Cloto', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Laquesis', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Atropos', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Minotauro de Creta', 'Derrotado': 'Teseo', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Harpias', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Argos Panoptnes', 'Derrotado': 'Hermes', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Aves del Estinfalo', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Talos', 'Derrotado': 'Medea', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Sirenas', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Piton', 'Derrotado': 'Apolo', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Cierva de Cerinea', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Basilisco', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Jabali del Erimanto', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion'},

                    ]
    arbol_criaturas = Arbol()

    arbol_criaturas = arbol_criaturas.cargar_arbol(dic_criaturas, 'Criatura')

    print('\nLISTADO INORDEN DE LAS CRIATURAS')
    #arbol_criaturas.inorden()

    print('\nCARGAR DESCRIPCION DE CADA CRIATURA')
    #cargar_descripcion(arbol_criaturas)

    print('\nMOSTRAR LA INFORMACION DE TALOS')
    #print(arbol_criaturas.busqueda('Talos').datos)

    print('\nDETERMINAR LOS 3 HEROES O DIOSES'
            + 'QUE DERROTARON MAYOR CANTIDAD DE CRIATURAS')
    # lista_dic_heroes = contar_mayor_cantidad_de_criaturas_derrotadas_por_un_heroe(arbol_criaturas)
    # imprimir_tres_heroes_con_mas_criaturas_derrotadas(lista_dic_heroes)

    print('\nIMPRIMIR LAS CRIATURAS DERROTADAS POR HERACLES')
    inorden_criaturas_derrotadas_por_un_heroe(arbol_criaturas, 'Heracles')


ejercicio_24()