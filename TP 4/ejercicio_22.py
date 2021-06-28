from tdaLista import Lista

#PUNTO B
def mostrarLaInfoDeDeterminadosPersonajes(objLista, personajes):
    indice = None

    for i in range(0, len(personajes)):
        indice = objLista.busqueda(personajes[i],'nombre')
        if indice > -1:
            print(objLista.obtener_elemento(indice))
        else:
            print('El personaje ', personajes[i], ' no esta en la lista')

#PUNTO C
def mostrarTodosLosPadawansDeDeterminadosMaestros(objLista, maestros):

    for i in range(0, objLista.tamanio()):
        jedi = objLista.obtener_elemento(i)

        for j in range(0, len(jedi['maestros'])):
            if jedi['maestros'][j] in maestros:
                print(jedi)

#PUNTO D
def mostrarJedisDeDeterminadasEspecies(objLista, especies):

    for i in range(0, objLista.tamanio()):
        jedi = objLista.obtener_elemento(i)

        if jedi['especie'] in especies:
            print(jedi)

#PUNTO E
def mostrarTodosLosJedisConDeterminadasIniciales(objLista, letras):

    for i in range(0, objLista.tamanio()):
        jedi = objLista.obtener_elemento(i)

        if jedi['nombre'][0].upper() in letras:
            print(jedi)

#PUNTO F
def mostrarTodosLosJedisConUnaDeterminadaCantidadDeSablesDeDiferenteColor(objLista, cantSablesDiferentes):

    for i in range(0, objLista.tamanio()):
        jedi = objLista.obtener_elemento(i)

        if len(jedi['coloresDeSablesUsados']) > cantSablesDiferentes:
            print(jedi)

#PUNTO G
def indicarLosJedisQueUsaronDeterminadoColorDeSable(objLista, colorSables):
    cantJediConSablesUsados = 0

    for i in range(0, objLista.tamanio()):
        jedi = objLista.obtener_elemento(i)

        for j in range(0, len(jedi['coloresDeSablesUsados'])):
            if jedi['coloresDeSablesUsados'][j] in colorSables:
                cantJediConSablesUsados += 1

    return cantJediConSablesUsados

def mostrarLaCantidadDeJediQueUsaronDeterminadoColorDeSable(objLista, colorSables):
    cantJediConSablesUsados = indicarLosJedisQueUsaronDeterminadoColorDeSable(objLista, colorSables)

    if cantJediConSablesUsados > 0:
        print('La canntidad de jedi que utilizaron un sable de color "', colorSables, '" es de: ', cantJediConSablesUsados)
    else:
        print('No hay ningun jedi que haya tenido un sable de los siguientes colores "', colorSables, '"')

#PUNTO H
def mostrarTodosLosNombresDePadawansDeDeterminadosMaestros(objLista, maestros):
    for i in range(0, objLista.tamanio()):
        jedi = objLista.obtener_elemento(i)

        for j in range(0, len(jedi['maestros'])):
            if jedi['maestros'][j] in maestros:
                print(jedi['nombre'])

datosJedis = [
             {'nombre' : 'Bo Keevil', 'maestros' : [], 'coloresDeSablesUsados' : [], 'especie' : 'Humano'},
             {'nombre' : 'Ahsoka Tano', 'maestros' : [], 'coloresDeSablesUsados' : [], 'especie' : 'Togruta'},
             {'nombre' : 'kit Fisto', 'maestros' : [], 'coloresDeSablesUsados' : [], 'especie' : 'Nautolano'},
             {'nombre' : 'Boba Fett:', 'maestros' : [], 'coloresDeSablesUsados' : [], 'especie' : 'desconocida'},
             {'nombre' : 'Jinx', 'maestros' : [], 'coloresDeSablesUsados' : [], 'especie' : 'Twi´lek'},
             {'nombre' : 'Bossk', 'maestros' : [], 'coloresDeSablesUsados' : [], 'especie' : 'Humano'},
            ]

maestrosJedis = [['Mace Windu', 'Yoda'],
                 ['Luke Skywalker'],
                 ['Lucien Draay'],
                 ['Yoda', 'Qui-Gon jin'],
                 ['Luke Skywalker'],
                 ['Qui-Gon jin'],
                 ]

sablesUsados = [
                ['rojo', 'azul', 'verde'],
                ['violeta'],
                ['gris', 'blanco', 'violeta'],
                ['rosado'], ['amarillo'],
                ['azul'], ['verde'], ['morado'], ['marron'],
                ['blanco']
                ]

listaJedis = Lista()

for datosJedi in datosJedis:
    listaJedis.insertar(datosJedi, 'nombre')


for i in range(0, listaJedis.tamanio()):
    listaJedis.obtener_elemento(i)['coloresDeSablesUsados'] = sablesUsados[i]
    listaJedis.obtener_elemento(i)['maestros'] = maestrosJedis[i]

print('\nORDENAR LA LISTA POR ESPECIE')
listaJedis.ordenar('especie')
listaJedis.barrido()

print('\nMOSTRAR LA INFORMACION DE AHSOKA TANO Y KIT FISTO')
listaJedis.ordenar('nombre')
mostrarLaInfoDeDeterminadosPersonajes(listaJedis, ['Ahsoka Tano', 'kit Fisto'])

print('\nMOSTRAR TODOS LOS PADAWANS DE YODA Y LUKE SKYWALKER')
mostrarTodosLosPadawansDeDeterminadosMaestros(listaJedis, ['Yoda', 'Luke Skywalker'])

print('\nMOSTRAR LOS JEDI DE LAS ESPECIES HUMANO Y TWI´LEK')
mostrarJedisDeDeterminadasEspecies(listaJedis, ['Humano', 'Twi´lek'])

print('\nMOSTRAR TODOS LOS JEDIS CON INICIAL A')
mostrarTodosLosJedisConDeterminadasIniciales(listaJedis, ['A', 'K'])

print('\nMOSTRAR TODOS LOS JEDIS QUE USARON MAS DE 1 COLOR DE SABLE DE LUZ')
mostrarTodosLosJedisConUnaDeterminadaCantidadDeSablesDeDiferenteColor(listaJedis, 1)

print('\nMOSTRAR LOS JEDI QUE HAN TENIDO SABLES DE COLOR AMARILLO O VIOLETA')
mostrarLaCantidadDeJediQueUsaronDeterminadoColorDeSable(listaJedis, ['amarillo', 'violeta'])

print('\nINDICAR LOS NOMBRES DE LOS PADAWANS DE QUI-GON JI Y MACE WINDU')
mostrarTodosLosNombresDePadawansDeDeterminadosMaestros(listaJedis, ['Qui-Gon jin', 'Mace Windu'])