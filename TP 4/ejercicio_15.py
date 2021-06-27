from tdaLista import Lista

#PUNTO A
def getCantidadDePokemonsDeUnEntrenador(nombreEntrenador, objLista):
    posEntrenador = objLista.busqueda(nombreEntrenador, 'nombre')

    if(posEntrenador != -1):
        return objLista.obtener_elemento(posEntrenador)['pokemons'].tamanio()
    else:
        return None

def mostrarCantidadDePokemonsDeUnEntrenador(nombreEntrenador, objLista):
    cantidadPokemons = getCantidadDePokemonsDeUnEntrenador(nombreEntrenador, objLista)

    if cantidadPokemons is not None:
        print('La cantidad de pokemons de ', nombreEntrenador, ' es', cantidadPokemons)
    else:
        print('El entrenador ', nombreEntrenador, ' no esta en la lsita')

#PUNTO B
def mostrarEntrenadoresConMasDeTresTorneosGanados(objLista):

    for i in range(0, objLista.tamanio()):
        if objLista.obtener_elemento(i)['cantTorneosGanados'] > 3:
            print(objLista.obtener_elemento(i)['nombre'])

#PUNTO C
def getIndiceEntrenadorConMasTorenosGanados(objLista):
    indice = None
    cantTorneosGanados = 0

    for i in range(0, objLista.tamanio()):
        if objLista.obtener_elemento(i)['cantTorneosGanados'] > cantTorneosGanados:
            cantTorneosGanados = objLista.obtener_elemento(i)['cantTorneosGanados']
            indice = i
    
    return indice

def getPokemonConMayorNivelDeUnEntrenador(entrenador):
    pokemon = None
    lvlPokemon = 0
    
    for i in range(0, entrenador['pokemons'].tamanio()):
        if entrenador['pokemons'].obtener_elemento(i)['nivel'] > lvlPokemon:
            lvlPokemon = entrenador['pokemons'].obtener_elemento(i)['nivel']
            pokemon = entrenador['pokemons'].obtener_elemento(i)
    
    return pokemon

#PUNTO D
def mostrarDatosDeUnEntrenadorYDeSusPokemones(entrenador):
    print('Nombre: ', entrenador['nombre'], ' Torneos Ganados: ', entrenador['cantTorneosGanados'], ' Batallas Perdidas: ', entrenador['cantBatallasPerdidas'], ' Batallas Ganadas: ', entrenador['cantBatallasGanadas'])

    print('\nPOKEMONES')
    for i in range(0, entrenador['pokemons'].tamanio()):
        print(entrenador['pokemons'].obtener_elemento(i))

#PUNTO E
def mostrarEntrenadoresConUnPorcentajeDeBatallasGanadas(objLista, porcentajeEnNumero):
    entrenador = None
    total = None


    for i in range(0, objLista.tamanio()):
        entrenador = objLista.obtener_elemento(i)
        total = entrenador['cantBatallasPerdidas'] + entrenador['cantBatallasGanadas']

        if (entrenador['cantBatallasGanadas']*100)/total > porcentajeEnNumero:
            print(objLista.obtener_elemento(i))

#PUNTO F
def mostrarLosEntrenadoresQueTenganPokemonesConCiertoTipoYSubTipoOOtroTipoYSubTipo(objLista, tipo1, subtipo1, tipo2, subtipo2):
    entrenador = None
    pokemon = None

    for i in range(0, objLista.tamanio()):
        entrenador = objLista.obtener_elemento(i)

        for i in range(0, entrenador['pokemons'].tamanio()):
            pokemon = entrenador['pokemons'].obtener_elemento(i)
            if ((pokemon['tipo'].lower() == tipo1.lower()) and (pokemon['subtipo'].lower() == subtipo1.lower())) or ((pokemon['tipo'].lower() == tipo2.lower()) and (pokemon['subtipo'].lower() == subtipo2.lower())):
                print(entrenador)
                break

#PUNTO G
def mostrarElPromedioDelNivelDeLosPokemonesDeUnEntrenador(objLista):
    sumaLvls = 0

    for i in range(0, objLista.tamanio()):
        entrenador = objLista.obtener_elemento(i)
        
        for i in range(0, entrenador['pokemons'].tamanio()):
            sumaLvls += entrenador['pokemons'].obtener_elemento(i)['nivel']

        print('El promedio de los pokemones del entrenador ', entrenador['nombre'], ' es de: ', sumaLvls/entrenador['pokemons'].tamanio())

#PUNTO H
def getCuantosEntrenadoresTienenDeterminadoPokemon(objLista, nombrePokemon):
    ocurrencias = 0

    for i in range(0, objLista.tamanio()):
        entrenador = objLista.obtener_elemento(i)
        
        for i in range(0, entrenador['pokemons'].tamanio()):
                if entrenador['pokemons'].obtener_elemento(i)['nombre'].lower() == nombrePokemon.lower():
                    ocurrencias += 1
                    break

    return ocurrencias

def msotrarCantidadDeEntrenadoresQueTienenDeterminadoPokemon(objLista, nombrePokemon):
    ocurrencias = getCuantosEntrenadoresTienenDeterminadoPokemon(objLista, nombrePokemon)

    print('este pokemon "', nombrePokemon, '" lo tienen: ', ocurrencias, ' entrenadores')

#PUNTO I
def mostrarEntrenadoresConPokemonesRepetidos(objLista):
    ocurrencias = None

    for i in range(0, objLista.tamanio()):
        entrenador = objLista.obtener_elemento(i)
        
        for i in range(0, entrenador['pokemons'].tamanio()):
            ocurrencias = 0

            for j in range(0, entrenador['pokemons'].tamanio()):
                if entrenador['pokemons'].obtener_elemento(i)['nombre'].lower() == entrenador['pokemons'].obtener_elemento(j)['nombre'].lower():
                    ocurrencias += 1

                    if ocurrencias > 1:
                        break
            
            if ocurrencias > 1:
                print(entrenador)
                break
        
#PUNTO J
def getCantidadDeEntrenadoresQueTenganUnPokemonDeUnDeterminadoConjunto(objLista, conjunto):
    cantDeEntrenadoresQueTenganXPokemon = 0

    for i in range(0, objLista.tamanio()):
        entrenador = objLista.obtener_elemento(i)
        
        for i in range(0, entrenador['pokemons'].tamanio()):

            if entrenador['pokemons'].obtener_elemento(i)['nombre'] in conjunto:
                cantDeEntrenadoresQueTenganXPokemon += 1
                break

    return cantDeEntrenadoresQueTenganXPokemon

def mostrarCantidadDeEntrenadoresQueTenganUnPokemonDeUnDeterminadoConjunto(objLista, conjunto):
    cantDeEntrenadoresQueTenganXPokemon = getCantidadDeEntrenadoresQueTenganUnPokemonDeUnDeterminadoConjunto(objLista, conjunto)

    print('La cantidad de entrenadores que tienen algun pokemon del conjunto "', conjunto, '" es de: ', cantDeEntrenadoresQueTenganXPokemon)

#PUNTO K
def mostrarSiUnDeterminadoEntrenadorTieneUnDeterminadoPokemon(objLista, nombreEntrenador, nombrePokemon):
    indiceEntrenador = None
    indicePokemon = None
    entrenador = None

    indiceEntrenador =  objLista.busqueda(nombreEntrenador, 'nombre')
    if indiceEntrenador > -1:
        indicePokemon = objLista.obtener_elemento(indiceEntrenador)['pokemons'].busqueda(nombrePokemon, 'nombre')
        if indicePokemon > -1:
            entrenador = objLista.obtener_elemento(indiceEntrenador)
            pokemon = entrenador['pokemons'].obtener_elemento(indicePokemon)
            print('El entrenador ', entrenador['nombre'], ' tiene al pokemon ', pokemon['nombre'])
            print('INFO ENTRENADOR')
            print('Nombre: ', entrenador['nombre'], ' Torneos Ganados: ', entrenador['cantTorneosGanados'], ' Batallas Perdidas: ', entrenador['cantBatallasPerdidas'], ' Batallas Ganadas: ', entrenador['cantBatallasGanadas'])
            print('Pokemon: ', pokemon['nombre'], ' Nivel: ', pokemon['nivel'], ' Tipo: ', pokemon['tipo'], ' Sub Tipo: ', pokemon['subtipo'])
        else:
            print('El Entrenador ', nombreEntrenador, ' no tiene a ', nombrePokemon)
    else:
        print('El Entrenador ', nombreEntrenador, ' no esta en la lista')

datosEntrenador = [
                    {'nombre': 'Ash', 'cantTorneosGanados' : 3, 'cantBatallasPerdidas': 30, 'cantBatallasGanadas': 180, 'pokemons': Lista()}, 
                    {'nombre': 'Serena', 'cantTorneosGanados' : 1, 'cantBatallasPerdidas': 64, 'cantBatallasGanadas': 300, 'pokemons': Lista()},
                    {'nombre': 'Misty', 'cantTorneosGanados' : 4, 'cantBatallasPerdidas': 33, 'cantBatallasGanadas': 50, 'pokemons': Lista()},
                    {'nombre': 'Brock', 'cantTorneosGanados' : 9, 'cantBatallasPerdidas': 150, 'cantBatallasGanadas': 20, 'pokemons': Lista()},
                    {'nombre': 'Clemo', 'cantTorneosGanados' : 0, 'cantBatallasPerdidas': 98, 'cantBatallasGanadas': 1, 'pokemons': Lista()},
                    ]

datosPokemnos1 = [{'nombre': 'Pikachu', 'nivel': 100, 'tipo' : 'Electrico', 'subtipo': 'ninguno'},
                 {'nombre': 'Raichu', 'nivel': 30, 'tipo' : 'Electrico', 'subtipo': 'Rayo'},
                 {'nombre': 'Pikachu', 'nivel': 100, 'tipo' : 'Electrico', 'subtipo': 'ninguno'},
                 {'nombre': 'Bulbasaur', 'nivel': 23, 'tipo' : 'Agua', 'subtipo': 'ninguno'},
                 {'nombre': 'Ivysaur', 'nivel': 12, 'tipo' : 'Fuego', 'subtipo': 'ninguno'},
                 ]

datosPokemnos2 = [{'nombre': 'Venusaur', 'nivel': 30, 'tipo' : 'Viento', 'subtipo': 'ninguno'},
                 {'nombre': 'Raichu', 'nivel': 50, 'tipo' : 'Electrico', 'subtipo': 'Rayo'},
                 {'nombre': 'Squirtle', 'nivel': 90, 'tipo' : 'Agua', 'subtipo': 'ninguno'},
                 ]

datosPokemnos3 = [{'nombre': 'Weedle', 'nivel': 90, 'tipo' : 'Yerba', 'subtipo': 'ninguno'},
                  {'nombre': 'Wigglytuff', 'nivel': 20, 'tipo' : 'Fuego', 'subtipo': 'Planta'},
                  {'nombre': 'Terrakion', 'nivel': 3, 'tipo' : 'Tierra', 'subtipo': 'Ninguno'},
                 ]

datosPokemnos4 = [{'nombre': 'Spearow', 'nivel': 12, 'tipo' : 'Magnetismo', 'subtipo': 'ninguno'},
                 {'nombre': 'Ekans', 'nivel': 30, 'tipo' : 'Hielo', 'subtipo': 'ninguno'},
                 {'nombre': 'Arbok', 'nivel': 2, 'tipo' : 'Hielo', 'subtipo': 'ninguno'},
                 {'nombre': 'Ivysaur', 'nivel': 1, 'tipo' : 'Fuego', 'subtipo': 'ninguno'},
                 ]

datosPokemnos5 = [{'nombre': 'Arbok', 'nivel': 100, 'tipo' : 'Hielo', 'subtipo': ''},
                 {'nombre': 'Nidoking', 'nivel': 100, 'tipo' : 'Ninguno', 'subtipo': 'ninguno'},
                 {'nombre': 'Arbok', 'nivel': 1, 'tipo' : 'Hielo', 'subtipo': ''},
                 ]

vectPokemons = [datosPokemnos1, datosPokemnos2, datosPokemnos3, datosPokemnos4, datosPokemnos5]

listaEntrenadores = Lista()

for datoEntrenador in datosEntrenador:
    listaEntrenadores.insertar(datoEntrenador, 'nombre')

for i in range(0, len(vectPokemons)):
    for pokemon in vectPokemons[i]:
        listaEntrenadores.obtener_elemento(i)['pokemons'].insertar(pokemon, 'nombre')


print('CANTIDAD DE POKEMONES DE UN ENTRENADOR')
mostrarCantidadDePokemonsDeUnEntrenador('Ash', listaEntrenadores)

print('\nLISTAR ENTRENADORES CON MAS DE TRES TORNEOS GANADOS')
mostrarEntrenadoresConMasDeTresTorneosGanados(listaEntrenadores)

print('\nOBTENER EL POKEMON DE MAYOR NIVEL DEL ENTRENADOR CON MAS TORNEOS GANADOS')
indiceEntrenador = getIndiceEntrenadorConMasTorenosGanados(listaEntrenadores)
pokemon = None

pokemon = getPokemonConMayorNivelDeUnEntrenador(listaEntrenadores.obtener_elemento(indiceEntrenador))

print(pokemon)

print('\nMOSTRAR LA INFO DE UN ENTRENADOR Y EL DE SUS POKEMONES')
mostrarDatosDeUnEntrenadorYDeSusPokemones(listaEntrenadores.obtener_elemento(3))

print('\nMOSTRAR ENTRENADORES CON MAS DE UN 79% DE BATALLAS GANADAS')
mostrarEntrenadoresConUnPorcentajeDeBatallasGanadas(listaEntrenadores, 79)

print('\nMOSTRAR ENTRENADORES QUE TENGAN POKEMONES FUEGO Y PLANTA O AGUA Y VOLADOR')
mostrarLosEntrenadoresQueTenganPokemonesConCiertoTipoYSubTipoOOtroTipoYSubTipo(listaEntrenadores, 'fuego', 'planta', 'agua', 'volador')

print('\nPROMEDIO DE NIVELES DE LOS POKEMONES DE LOS ENTRENADORES')
mostrarElPromedioDelNivelDeLosPokemonesDeUnEntrenador(listaEntrenadores)

print('\nDETERMINAR CUANTOS ENTRENADORES TIENEN EL MISMO POKEMON')
msotrarCantidadDeEntrenadoresQueTienenDeterminadoPokemon(listaEntrenadores, 'Raichu')

print('\nMOSTRAR ENTRENADORES QUE TIENEN POKEMONES REPETIDOS')
mostrarEntrenadoresConPokemonesRepetidos(listaEntrenadores)

print('\nDETERMINAR CUANTOS ENTRENADORES TIENEN A Tyrantrum, Terrakion o Wingull')
mostrarCantidadDeEntrenadoresQueTenganUnPokemonDeUnDeterminadoConjunto(listaEntrenadores, ('Tyrantrum', 'Terrakion', 'Wingull'))

print('\nDETERMINAR SI UN DETERMINADO ENTRENADOR X TIENE UN DETERMINADO POKEMON')
nombreEntrenador = input('Ingrese el nombre del entrenador: ')
nombrePokemon = input('Ingrese el nombre del pokemon: ')

mostrarSiUnDeterminadoEntrenadorTieneUnDeterminadoPokemon(listaEntrenadores, nombreEntrenador, nombrePokemon)