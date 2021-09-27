from TDA_Arbol_Binario import Arbol
from sys import getsizeof

tabla = [['Despejado', 0.22], ['Nublado', 0.15], ['Lluvia', 0.03], 
        ['Baja', 0.26], ['Alta', 0.14], ['1', 0.05], ['2', 0.01],
        ['3', 0.035],  ['5', 0.06],  ['7', 0.02],  ['8', 0.025]]

dic = {}

def comparable(arbol):
    return arbol.frecuencia

def generar_arbol_huff(bosque):

    while(len(bosque) > 1):
        arbol1 = bosque.pop(0)
        arbol2 = bosque.pop(0)
        nuevo_arbol = Arbol(frecuencia=arbol1.frecuencia+arbol2.frecuencia)
        nuevo_arbol.izq = arbol1
        nuevo_arbol.der = arbol2
        bosque.append(nuevo_arbol)
        bosque.sort(key=comparable)

    return bosque[0]

def generar_tabla(arbol, cadena='', dic=None):
    if(arbol is not None):
        if(arbol.izq is None):
            dic[arbol.info] = cadena
        else:
            cadena += '0'
            generar_tabla(arbol.izq, cadena, dic)
            cadena = cadena[0:-1]
            cadena += '1'
            generar_tabla(arbol.der, cadena, dic)

def codificar(variables, dic):
    cadena_cod = ''
    for variable in variables:
        cadena_cod += dic[variable]
    return cadena_cod
    
def decodificar(cadena_cod, arbol_huff):
    datos_deco = ''
    arbol_aux = arbol_huff
    pos = 0
    while(pos < len(cadena_cod)):
        if(cadena_cod[pos] == '0'):
            arbol_aux = arbol_aux.izq
        else:
            arbol_aux = arbol_aux.der
        pos += 1
        if(arbol_aux.izq is None):
            datos_deco += arbol_aux.info + '-'
            arbol_aux = arbol_huff

    return datos_deco[:-1]

def ejercicio7():
    bosque = []
    diccionario = {}

    cadena_cod = ''
    estado_deco = ''
    variables = ['Nublado', 'Baja', '1', '2', '3']

    for info, frecuencia in tabla:
        arbol = Arbol(info, frecuencia)
        bosque.append(arbol)
    
    bosque.sort(key=comparable)

    arbol_huff = generar_arbol_huff(bosque)

    arbol_huff.barrido_por_nivel_huff()
   
    generar_tabla(arbol_huff, dic = diccionario)

    cadena_cod = codificar(variables, diccionario)
    estado_deco = decodificar(cadena_cod, arbol_huff)

    print('Estado original: ', variables);
    print('Peso del estado sin codificar: ', getsizeof(variables))

    print('Estado codificado: ', cadena_cod)
    print('Peso de los datos codificado: ', getsizeof(cadena_cod))

    print('\nEstado decodificado: ', estado_deco)

ejercicio7()