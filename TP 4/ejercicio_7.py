from tdaLista import Lista


def concatenarListas(objLista1, objLista2):

    for i in range(0, objLista2.tamanio()):
        objLista1.insertar(objLista2.obtener_elemento(i), 'name')

def concatenarListasSinRepetirElementos(objLista1, objLista2):
    esDiferente = False
    tamanioObjLista1 = objLista1.tamanio()

    for i in range(0, objLista2.tamanio()):
        for j in range(0, tamanioObjLista1):

            if objLista2.obtener_elemento(i) != objLista1.obtener_elemento(j):
                esDiferente = True
            else:
                esDiferente = False
                break;
        
        if(esDiferente):
            tamanioObjLista1 += 1
            objLista1.insertar(objLista2.obtener_elemento(i), 'name')

def contarInterseccionEntreDosListas(objLista1, objLista2):
    esDiferente = False
    elementosRepetidos = 0

    for i in range(0, objLista2.tamanio()):
        for j in range(0, objLista1.tamanio()):

            if objLista2.obtener_elemento(i) != objLista1.obtener_elemento(j):
                esDiferente = True
            else:
                esDiferente = False
                break;
        
        if(not esDiferente):
            elementosRepetidos += 1

    return elementosRepetidos

def eliminarYmostrarLosNodosDeUnaLista(objLista):
    while(not objLista.lista_vacia()):
        print(objLista.eliminar(objLista.obtener_elemento(0)['name'], 'name'))

def ejercicio7():
    objLista = Lista()
    objLista2 = Lista()
    objLista3 = Lista()
    objLista4 = Lista()

    datos = [
            {'name': 'Gonzalo', 'anio': 2000, 'id' : '01'},
            {'name': 'Juan', 'anio': 2004, 'id' : '02'},
            {'name': 'Clara', 'anio': 2001, 'id' : '03'},
            {'name': 'Angela', 'anio': 2008, 'id' : '04'},
            {'name': 'Marcelo', 'anio': 1978, 'id' : '05'},
            ]
    
    datos2 = [
            {'name': 'Gonzalo', 'anio': 2000, 'id' : '01'},
            {'name': 'Fabiana', 'anio': 2004, 'id' : '02'},
            {'name': 'Susana', 'anio': 2001, 'id' : '03'},
            {'name': 'Angela', 'anio': 2008, 'id' : '04'},
            {'name': 'Marcelo', 'anio': 1978, 'id' : '05'},
            {'name': 'Mora', 'anio': 2004, 'id' : '06'},
            ]
    
    datos3 = [
            {'name': 'Cuco', 'anio': 2010, 'id' : '01'},
            {'name': 'Fabiana', 'anio': 2004, 'id' : '02'},
            {'name': 'Angela', 'anio': 2008, 'id' : '04'},
            {'name': 'Marcelo', 'anio': 1978, 'id' : '05'},
            {'name': 'Mora', 'anio': 2004, 'id' : '06'},
            ]
    
    datos4 = [
            {'name': 'Cuco', 'anio': 2010, 'id' : '01'},
            {'name': 'Tom', 'anio': 564, 'id' : '02'},
            {'name': 'Mora', 'anio': 2004, 'id' : '06'},
            ]

    for dato in datos:
        objLista.insertar(dato, 'name')
    
    for dato in datos2:
        objLista2.insertar(dato, 'name')
    
    for dato in datos3:
        objLista3.insertar(dato, 'name')
    
    for dato in datos4:
        objLista4.insertar(dato, 'name')

    print('Concatenar listas')
    concatenarListas(objLista, objLista2)
    objLista.barrido()

    print('\nConcatenar listas sin repetir elementos')
    concatenarListasSinRepetirElementos(objLista, objLista3)
    objLista.barrido()

    print('\nContar elementos repetidos entre dos listas')
    print('Cantidad de elementos repetidos: ', contarInterseccionEntreDosListas(objLista, objLista4))

    print('\nEliminar y mostrar nodos de una lista')
    eliminarYmostrarLosNodosDeUnaLista(objLista)

ejercicio7()