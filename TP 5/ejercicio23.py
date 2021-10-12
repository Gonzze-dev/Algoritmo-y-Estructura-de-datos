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
                                 'cantidad_Derrotados': ocurrencias}, 
                                 'cantidad_Derrotados')
    
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
    
#PUNTO H
def modificar_campo_capturada_de_una_criatura(arbol, criaturas, capturado_por):
    for criatura in criaturas:
        pos = arbol.busqueda(criatura)
        if(pos is not None):
            pos.datos['Capturada'] = capturado_por
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

#PUNTO K
def modificar_datos_de_una_criatura(arbol, campo, criatura, dato):
    pos = arbol.busqueda(criatura)
    if(pos is not None):
        pos.datos[campo] = dato
    else:
        print('La criatura "' + criatura + '" no esta en el arbol')
    return pos

#PUNTO L
def modificar_el_nombre_de_una_criatura(arbol, criatura, modificarlo_por):
    info, datos = arbol.eliminar_nodo(criatura)
    if datos is not None:
        datos['Criatura'] = modificarlo_por
        arbol.insertar_nodo(datos['Criatura'], datos)
    else:
        print('La criatura "' + criatura + '" no esta en el arbol')

#PUNTO N
def listado_de_criaturas_capturadas_por_un_heroe(arbol, nombre_heroe):
    if(arbol.info is not None):
        if(arbol.izq is not None):
            listado_de_criaturas_capturadas_por_un_heroe(arbol.izq, nombre_heroe)
        if(arbol.datos['Capturada'] == nombre_heroe):
            print(arbol.info, arbol.datos)
        if(arbol.der is not None):
            listado_de_criaturas_capturadas_por_un_heroe(arbol.der, nombre_heroe)

def ejercicio_24():
    lista_dic_heroes = Lista()
    arbol_criaturas = Arbol()
    dic_criaturas = [{'Criatura': 'Ceto', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
                     {'Criatura': 'Tifon', 'Derrotado': 'Zeus', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
                     {'Criatura': 'Equidna', 'Derrotado': 'Argos panoptnes', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
                     {'Criatura': 'Dino', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
                     {'Criatura': 'Pefredo', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
                     {'Criatura': 'Enio', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
                     {'Criatura': 'Escila', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
                     {'Criatura': 'Caribdis', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
                     {'Criatura': 'Euriale', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
                     {'Criatura': 'Esteno', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
                     {'Criatura': 'Medusa', 'Derrotado': 'Perseo', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
                     {'Criatura': 'Ladon', 'Derrotado': 'Heracles', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
                     {'Criatura': 'Aguila del Caucaso', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
                     {'Criatura': 'Quimera', 'Derrotado': 'Belerofonte', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
                     {'Criatura': 'Hidra de Lerna', 'Derrotado': 'Heracles', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
                     {'Criatura': 'Leon de Nemea', 'Derrotado': 'Heracles', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
                     {'Criatura': 'Esfinge', 'Derrotado': 'Edipo', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
                     {'Criatura': 'Dragon de la Colquida', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
                     {'Criatura': 'Cerbero', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
                     {'Criatura': 'Cerda de Cromion', 'Derrotado': 'Teseo', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
                     {'Criatura': 'Ortro', 'Derrotado': 'Heracles', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : 'Heracles'},
                     {'Criatura': 'Toro de Creta', 'Derrotado': 'Teseo', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
                     {'Criatura': 'Jabali De Calidon', 'Derrotado': 'Atalanta', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
                     {'Criatura': 'Carcinos', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
                     {'Criatura': 'Gerion', 'Derrotado': 'Heracles', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
                     {'Criatura': 'Cloto', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
                     {'Criatura': 'Laquesis', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : 'Heracles'},
                     {'Criatura': 'Atropos', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
                     {'Criatura': 'Minotauro de Creta', 'Derrotado': 'Teseo', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
                     {'Criatura': 'Harpias', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
                     {'Criatura': 'Argos Panoptnes', 'Derrotado': 'Hermes', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
                     {'Criatura': 'Aves del Estinfalo', 'Derrotado': 'Heracles', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 5, 'Capturada' : '-'},
                     {'Criatura': 'Talos', 'Derrotado': 'Medea', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
                     {'Criatura': 'Sirenas', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
                     {'Criatura': 'Piton', 'Derrotado': 'Apolo', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
                     {'Criatura': 'Cierva de Cerinea', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
                     {'Criatura': 'Basilisco', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
                     {'Criatura': 'Jabali de Erimanto', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
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
    vec_criaturas = ['Cerbero', 'Toro de Creta', 'Cierva de Cerinea', 
                     'Jabali de Erimanto']
    modificar_campo_capturada_de_una_criatura(arbol_criaturas, 
                                                vec_criaturas,'Heracles')

    #PUNTO I
    print('\nBUSQUEDA POR PROXIMIDAD')
    # buscar = input('Ingrese el nombre de la criatura a buscar: ')
    # arbol_criaturas.busqueda_proximidad(buscar)

    #PUNTO J
    print('\nELIMINAR AL BASILISCO Y A LAS SIRENAS')
    vec_criaturas_a_eliminar = ['Basilisco', 'Las Sirenas']
    eliminar_criatura_del_arbol(arbol_criaturas, vec_criaturas_a_eliminar)

    #PUNTO K
    print('\nMODIFICAR EL NODO QUE CONTIENE A LAS AVES DE ESTIFALO, ' 
          + 'AGREGANDO QUE HERACLES DERROTO VARIAS')
    modificar_datos_de_una_criatura(arbol_criaturas, 'Cant_Derrotado','Aves del Estinfalo', 10)
    modificar_datos_de_una_criatura(arbol_criaturas, 'Derrotado','Aves del Estinfalo', 'Heracles')

    #PUNTO L
    print('\nCAMBIAR EL NOMBRE DE LADON POR DRAGON LADON')
    modificar_el_nombre_de_una_criatura(arbol_criaturas, 'Ladon', 'Dragon Ladon')
    
    #PUNTO M
    print('\nLISTADO POR NIVEL DEL ARBOL')
    arbol_criaturas.barrido_por_nivel()

    #PUNTO N
    print('\nLISTADO DE CRIATURAS CAPTURADAS POR HERACLES')
    # listado_de_criaturas_capturadas_por_un_heroe(arbol_criaturas, 'Heracles')


ejercicio_24()