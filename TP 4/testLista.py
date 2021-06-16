from tdaLista import Lista

datos = [
    {'name':'juan','edad': 34, 'provincia' : 'chaco', 'dni': 32, 'autos': Lista()},
    {'name':'juan','edad': 80, 'provincia' : 'misiones', 'dni': 20, 'autos': Lista()},
    {'name':'maria','edad': 18, 'provincia' : 'entre rios', 'dni': 28, 'autos': Lista()},
    {'name':'julieta','edad': 18, 'provincia' : 'catamarca', 'dni': 45, 'autos': Lista()},
    {'name':'carlos','edad': 40, 'provincia' : 'entre rios', 'dni': 38, 'autos': Lista()},
]

objLista = Lista()
objLista2 = Lista()
objLista3 = Lista()

for dato in datos:
    objLista.insertar(dato, 'name')
    #al poner 'name' se me guarda y a la vez ordena en la lista por el campo ese campo, si pucieera como campo
    #edad, se me guarda y ordena por edad

objLista.barrido()

for dato in datos:
    objLista2.insertar(dato, 'dni')
print()
objLista2.barrido()
#al poner en el metodo eliminar como criterio name, me va a buscar a uno de los dos juan, el primero que encuentre me lo elimina

for dato in datos:
    objLista2.insertar(dato, 'name')

print(objLista2.eliminar("juan", 'name', 32, 'dni'))

#Si quiero eliminar a un juan, en espeecifico, pongo los campos por los cual el metodo
#va a identificarlos, por lo que tenemos que eliminar y la busqueda seria
#eliminar("elemento a buscar", 'campo', "segundo elemento para identificar el elemento a buscar, 'campo', "tercer elemento para identificar el elemento a buscar", 'campo')

autosJS = [
            {'name': "mercedes benz a200", 'anio' : "2006"},
            {'name': "toyota corolla", 'anio' : "2014"},
          ]

for dato in datos:
    objLista3.insertar(dato, 'name')

#supongamos que quiero buscar al juan con DNI 32 y agregarle un auto
posicion_elemento = 0
posicion_elemento = objLista3.busqueda("juan", 'name', 32, 'dni') #primero lo busco y guardo la posicion donde se encuentra
#ACLARACION PARA MI
#EL LA BUSQUEDA DE EL TDA DEVUELVE -1 SI NO ENCUENTRA EL ELEMENTO, Y EN EL ELIMINAR
#DEVUELVE UN NONE, SI NO ENCUENTRA EL ELEMENTO QUE SE QUIERE ELIMINAR

objLista.obtener_elemento(posicion_elemento)['autos'].insertar(autosJS[0], 'name')
#obtenego el elemento de la lista, pongo el capo que voy a modificar, como es una lista, pongo el insert
# y le añado el auto de la posicion 0 del vector autosJS

informacionDeJuan = objLista.obtener_elemento(posicion_elemento)

print(informacionDeJuan)
print("autos de juan")

for i in range(0, informacionDeJuan['autos'].tamanio()):
    print(informacionDeJuan['autos'].obtener_elemento(i))