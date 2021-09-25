from arbolbinarioRojoYNegro import Arbol
from random import randint

def contar_el_numero_de_nodos(arbol):
    contador = 0

    if(arbol.info is not None):
        contador += 1
        if(arbol.izq is not None):
           contador += contar_el_numero_de_nodos(arbol.izq)
        if(arbol.der is not None):
           contador += contar_el_numero_de_nodos(arbol.der)
            
    return contador

arbol_con_numero = Arbol()

for i in range(0,15):
    arbol_con_numero.insertar_nodo(randint(0,100))

print(contar_el_numero_de_nodos(arbol_con_numero))

print()
arbol_con_numero.inorden()