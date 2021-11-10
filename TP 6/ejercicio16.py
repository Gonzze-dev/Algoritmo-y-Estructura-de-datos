from grafos import Grafo
from lista import Lista

#PUNTO A
def inicializar_vertices(grafo):
    grafo.insertar_vertice('Atenas', {'latitud' : 17, 'longitud' : 8})
    grafo.insertar_vertice('Zeus', {'latitud' : 13, 'longitud' : 14})
    grafo.insertar_vertice('Hera', {'latitud' : 7, 'longitud' : 1})
    grafo.insertar_vertice('Apolo', {'latitud' : 3, 'longitud' : 5})
    grafo.insertar_vertice('Poseidon', {'latitud' : 1, 'longitud' : 1})
    grafo.insertar_vertice('Artemisa', {'latitud' : 3, 'longitud' : 20})
    grafo.insertar_vertice('Teatro', {'latitud' : 20, 'longitud' : 3})

#PUNTO B
def crear_grafo_completo(grafo):
    lugar = Lista()
    for i in range(grafo.inicio.tamanio()):
        lugar_origen = grafo.inicio.obtener_elemento(i)
        km_lugar_origen = lugar_origen['data']['latitud'] + lugar_origen['data']['longitud']
        for j in range((i+1), grafo.inicio.tamanio()):
            lugar_destino = grafo.inicio.obtener_elemento(j)
            km_lugar_destino = lugar_destino['data']['latitud'] + lugar_destino['data']['longitud']
            distancia = abs(km_lugar_origen - km_lugar_destino)
            
            grafo.insertar_arista(distancia, lugar_origen['info'], lugar_destino['info'])

#PUNTO C
def hallar_arbol_de_expancion_minima_de_x_lugar(grafo, lugar):
    vertice_origen = grafo.buscar_vertice(lugar)
    
    if vertice_origen != -1:
        grafo.prim(vertice_origen)

#PUNTO D
def hallar_camino_mas_corto_entre_dos_lugares(grafo, origen, destino):
    vertice_origen = grafo.buscar_vertice(origen)
    vertice_destino = grafo.buscar_vertice(destino)
    costo = None
    
    if vertice_origen != -1 and vertice_destino != -1:
        camino = grafo.dijkstra(vertice_origen)
        while(not camino.pila_vacia()):
            dato = camino.desapilar()
            if(dato[1][0] == destino):
                if(costo is None):
                    costo = dato[0]
                print('paso por: ', dato[1][0])
                destino = dato[1][1]
        print('el costo total del camino es: ', costo)



def ejercicio_16():
    grafo = Grafo(dirigido=False)
    
    print('CARGAR GRAFO')
    inicializar_vertices(grafo)
    
    print()
    print('CREAR GRAFO COMPLETO')
    crear_grafo_completo(grafo)
    
    print()
    print('HALLAR EL CAMINO MAS CORTO ENTRE DOS LUGARES')
    hallar_camino_mas_corto_entre_dos_lugares(grafo, 'Zeus', 'Zeus')
    
    print()
    print('GRAFO DE EXPANCION MINIMA')
    hallar_arbol_de_expancion_minima_de_x_lugar(grafo, 'Hera')
    
    #comprobar si el grafo esta completo, si esto es verdad, todos tendrian que tener
    #la misma cantidad de elementos en la lista de aristas
    # for i in range(grafo.inicio.tamanio()):
    #     print(grafo.inicio.obtener_elemento(i)['aristas'].
    #         tamanio())



ejercicio_16()