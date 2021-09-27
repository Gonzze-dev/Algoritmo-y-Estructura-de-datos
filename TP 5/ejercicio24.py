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
        if(arbol.datos['Capturado'] == nombre_heroe):
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
    vector_heroes = recompilar_datos_de_un_arbol(arbol, 'Capturado')
    ocurrencias = 0
    lista_dic_heroes = Lista()

    for nombre_heroe in vector_heroes:
        ocurrencias = contar_ocurrencias_de_heroe(arbol, 
                        nombre_heroe)
        lista_dic_heroes.insertar({'nombre': nombre_heroe,
                                 'cantidad_Capturados': ocurrencias}, 
                                 'cantidad_Capturados')
    
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
        if(arbol.datos['Capturado'] == nombre):
            print(arbol.datos['Criatura'])
        if(arbol.der is not None):
            inorden_criaturas_derrotadas_por_un_heroe(arbol.der, nombre)
    
#PUNTO H
def modificar_campo_capturado_de_una_criatura(arbol, criaturas, capturado_por):

    for criatura in criaturas:
        pos = arbol.busqueda(criatura)
        if(pos is not None):
            pos.datos['Capturado'] = capturado_por
        else:
            print('La criatura "' + criatura + '" no esta en el arbol')


#PUNTO J
def eliminar_criatura_del_arbol(arbol, criaturas):

    for criatura in criaturas:
        info, datos = arbol.eliminar_nodo(criatura)

        if(info is None or datos is None):
            print('La criatura "' + criatura + '" no se encontro en el arbol')
        else:
            print('Eliminado: ', info, '\n', datos)

#PUNTO L
def modificar_el_nombre_de_una_criatura(arbol, criatura, modificarlo_por):
    pos = arbol.busqueda(criatura)
    if(pos is not None):
        pos.datos['Criatura'] = modificarlo_por
        print('\nNombre de la criatura modificada con exito', '\n', pos.datos)
    else:
        print('La criatura "' + criatura + '" no se encontro en el arbol')

def ejercicio_24():
    lista_dic_heroes = Lista()
    arbol_criaturas = Arbol()
    dic_criaturas = [{'Criatura': 'Ceto', 'Capturado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Tifon', 'Capturado': 'Zeus', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Equidna', 'Capturado': 'Argos panoptnes', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Dino', 'Capturado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Pefredo', 'Capturado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Enio', 'Capturado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Escila', 'Capturado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Caribdis', 'Capturado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Euriale', 'Capturado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Esteno', 'Capturado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Medusa', 'Capturado': 'Perseo', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Ladon', 'Capturado': 'Heracles', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Aguila del Caucaso', 'Capturado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Quimera', 'Capturado': 'Belerofonte', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Hidra de Lerna', 'Capturado': 'Heracles', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Leon de Nemea', 'Capturado': 'Heracles', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Esfinge', 'Capturado': 'Edipo', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Dragon de la Colquida', 'Capturado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Cerbero', 'Capturado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Cerda de Cromion', 'Capturado': 'Teseo', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Ortro', 'Capturado': 'Heracles', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Toro de Creta', 'Capturado': 'Teseo', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Jabali De Calidon', 'Capturado': 'Atalanta', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Carcinos', 'Capturado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Gerion', 'Capturado': 'Heracles', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Cloto', 'Capturado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Laquesis', 'Capturado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Atropos', 'Capturado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Minotauro de Creta', 'Capturado': 'Teseo', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Harpias', 'Capturado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Argos Panoptnes', 'Capturado': 'Hermes', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Aves del Estinfalo', 'Capturado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Talos', 'Capturado': 'Medea', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Sirenas', 'Capturado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Piton', 'Capturado': 'Apolo', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Cierva de Cerinea', 'Capturado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Basilisco', 'Capturado': '-', 'Descripcion' : 'No hay descripcion'},
                     {'Criatura': 'Jabali de Erimanto', 'Capturado': '-', 'Descripcion' : 'No hay descripcion'},
                    ]
    
    arbol_criaturas = arbol_criaturas.cargar_arbol(dic_criaturas, 'Criatura')

    #PUNTO A
    print('\nLISTADO INORDEN DE LAS CRIATURAS')
    # arbol_criaturas.inorden()

    #PUNTO B
    print('\nCARGAR DESCRIPCION DE CADA CRIATURA')
    # cargar_descripcion(arbol_criaturas)

    #PUNTO C
    print('\nMOSTRAR LA INFORMACION DE TALOS')
    # print(arbol_criaturas.busqueda('Talos').datos)

    #PUNTO D
    print('\nDETERMINAR LOS 3 HEROES O DIOSES'
            + 'QUE DERROTARON MAYOR CANTIDAD DE CRIATURAS')
    # lista_dic_heroes = contar_mayor_cantidad_de_criaturas_derrotadas_por_un_heroe(arbol_criaturas)
    # imprimir_tres_heroes_con_mas_criaturas_derrotadas(lista_dic_heroes)

    #PUNTO E
    print('\nIMPRIMIR LAS CRIATURAS DERROTADAS POR HERACLES')
    # inorden_criaturas_derrotadas_por_un_heroe(arbol_criaturas, 'Heracles')

    #PUNTO F
    print('\nIMPRIMIR LAS CRIATURAS DERROTADAS QUE NO HAN SIDO DERROTADAS')
    # inorden_criaturas_derrotadas_por_un_heroe(arbol_criaturas, '-')

    #PUNTO H
    print('\nMODIFICAR LOS NODOS CERBERO, TORO DE CRETA, CIERVA CERINEA,'
          + ' Y JABALI DE ERIMANTO, E INDICAR QUE HERACLES LAS ATRAPO')
    # vec_criaturas = ['Cerbero', 'Toro de Creta', 'Cierva de Cerinea', 
    #                 'Jabali de Erimanto']
    # modificar_campo_capturado_de_una_criatura(arbol_criaturas, 
    #                                             vec_criaturas,'Heracles')

    #PUNTO I
    print('\nBUSQUEDA POR PROXIMIDAD')
    # buscar = input('Ingrese el nombre de la criatura a buscar: ')
    # arbol_criaturas.busqueda_proximidad(buscar)

    #PUNTO J
    print('\nELIMINAR AL BASILISCO Y A LAS SIRENAS')
    # vec_criaturas_a_eliminar = ['Basilisco', 'Las Sirenas']
    # eliminar_criatura_del_arbol(arbol_criaturas, vec_criaturas_a_eliminar)

    #PUNTO K


    #PUNTO L
    print('\nCAMBIAR EL NOMBRE DE LADON POR DRAGON LADON')
    modificar_el_nombre_de_una_criatura(arbol_criaturas, 'Ladon', 'Dragon Ladon')

    # #PUNTO M
    print('\nLISTADO POR NIVEL DEL ARBOL')
    arbol_criaturas.barrido_por_nivel()

    #PUNTO N


ejercicio_24()