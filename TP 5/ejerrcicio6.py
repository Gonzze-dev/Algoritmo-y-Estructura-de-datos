from TDA_Arbol_Binario_RyN_MOD2 import Arbol

#def mostrarVillano(este_arbol):


# pos = arbol.busqueda(padre)
# if pos:
#     if(not pos.izq):
#         pos.izq = Arbol(hijo)
#     else:
#         if not pos.izq.der:
#             pos.izq.der = Arbol(hijo)
#         else:
#             aux = pos.izq.der
#             while not aux.der:
#                 aux = aux.der
#             aux = Arbol(hijo)

#PUNTO B
def mostrarVillano(arbol):
    if(arbol.info is not None):
        if(arbol.izq is not None):
            mostrarVillano(arbol.izq)
        if(arbol.datos['esHeroe'] == False):
            print(arbol.info, arbol.datos)
        if(arbol.der is not None):
            mostrarVillano(arbol.der)

#PUNTO C
def mostrar_personajes_que_empiezan_con_una_letra(arbol, letra):
    if(arbol.info is not None):
        if(arbol.izq is not None):
            mostrar_personajes_que_empiezan_con_una_letra(arbol.izq, letra)
        if(arbol.datos['name'][0] == letra):
            print(arbol.info, arbol.datos)
        if(arbol.der is not None):
            mostrar_personajes_que_empiezan_con_una_letra(arbol.der, letra)

#PUNTO D
def contar_superheroes(arbol):
    contador = 0
    if(arbol.info is not None):
        if(arbol.izq is not None):
             contador += contar_superheroes(arbol.izq)
        if(arbol.datos['esHeroe'] == True):
            contador += 1
        if(arbol.der is not None):
             contador += contar_superheroes(arbol.der)

    return contador

#PUNTO E
def arreglar_nombre_superheroe(arbol, nombre_aprox, nombre_a_reenplazar):
    nombre_aprox = 'Doctor'
    arbol.busqueda_proximidad(nombre_aprox);
    nombreABuscarReal = 'Doctor Strnger'
    pos = arbol.busqueda(nombre_a_reenplazar)
    if(pos):
        print(pos.datos)
        nuevo_nombre = input('Ingrese el nombre a reemplazar: ')
        pos.datos['name'] = nuevo_nombre
    else:
        print('El nombre "' + nombre_a_reenplazar + '" no esta en el arbol')
#PUNTO F
def listado_superheroes_de_manera_desendente(arbol):
    if(arbol.info is not None):
            if(arbol.der is not None):
                listado_superheroes_de_manera_desendente(arbol.der)
            if(arbol.datos['esHeroe'] == True):
                print(arbol.info)
            if(arbol.izq is not None):
                listado_superheroes_de_manera_desendente(arbol.izq)

#PUNTO G
def generar_bosque(arbol, arbol_heroes, arbol_villanos, campo='name'):
    if(arbol.info is not None):
        if(arbol.datos['esHeroe'] == True):
            arbol_heroes = arbol_heroes.insertar_nodo(arbol.info, arbol.datos)
        else:
            arbol_villanos = arbol_villanos.insertar_nodo(arbol.info, arbol.datos)
        if(arbol.izq is not None):
            arbol_heroes, arbol_villanos = generar_bosque(arbol.izq, arbol_heroes, arbol_villanos, campo)
        if(arbol.der is not None):
            arbol_heroes, arbol_villanos = generar_bosque(arbol.der, arbol_heroes, arbol_villanos, campo)

    return arbol_heroes, arbol_villanos

def ejercicio6():
    arbolMCU = Arbol()
    arbol_heroes = Arbol()
    arbol_villanos = Arbol()
    
    personajesMCU = [
                        {'name': 'Doctor Strnger', 'esHeroe': True},
                        {'name': 'Caballero Negro', 'esHeroe': True},
                        {'name': 'Iron man', 'esHeroe': True},
                        {'name': 'Doctor Muerte', 'esHeroe': False},
                        {'name': 'Doctor Octopus', 'esHeroe': False},
                        {'name': 'Calavera', 'esHeroe': True},
                        {'name': 'Thanos', 'esHeroe': False},
                        {'name': 'Spider man', 'esHeroe': True}
                    ]

    arbolMCU = arbolMCU.cargar_arbol(personajesMCU, 'name')
    
    print('MOSTRAR VILLANOS ALFABETICAMENTE')
    mostrarVillano(arbolMCU)

    print('\nPERSONAJES QUE EMPIEZAN CON LA LETRA C')
    mostrar_personajes_que_empiezan_con_una_letra(arbolMCU, 'C')

    print('\nCONTAR SUPERHEROES')
    print('La cantidad de superheroes en el arbol es de: ', contar_superheroes(arbolMCU))
    
    print('\nARREGLAR EL NOMBRE DEL DOCTOR STRANGE')
    #arreglar_nombre_superheroe(arbolMCU, 'Doc', 'Doctor Strnger')
    
    print('\nLISTADO DE SUPERHEROES DE MANERA DESENEDENTE')
    listado_superheroes_de_manera_desendente(arbolMCU)

    print('\nGENEREAR BOSQUE DE SUPER HEROES Y VILLANOS')
    arbol_heroes, arbol_villanos = generar_bosque(arbolMCU, arbol_heroes, arbol_villanos)
    print('ARBOL HEROES')
    arbol_heroes.inorden()
    print('ARBOL VILLANOS')
    arbol_villanos.inorden()

ejercicio6()