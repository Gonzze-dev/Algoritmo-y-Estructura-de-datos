
tablaHashPokemon = []

def crear_tabla(tamanio):
    tabla = [None] * tamanio
    return tabla

def funcionHashTipoPokemon(pokemons, tablaHash):
    pos = (ord(pokemons['Tipo'])*33 + ord(pokemons['Tipo'])) % len(tablaHash)

def agregar_ta(tabla, hash, dato, criterio=None):
    posicion = hash(dato, tabla)
    if(tabla[posicion] is None):
        tabla[posicion] = Lista()
    insertar(tabla[posicion], dato, criterio)
    