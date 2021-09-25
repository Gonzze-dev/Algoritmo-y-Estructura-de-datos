from TDA_Cola import Cola

class Arbol(object):
    
    def __init__(self, info=None, datos=None):
        self.info = info
        self.datos = datos
        self.der = None
        self.izq = None
        self._altura = 0
    
    def cargar_arbol(self, datosJS, campo):
        for dato in datosJS:
            self = self.insertar_nodo(dato[campo], dato);
    
        return self

        

    def arbol_vacio(self):
        return self.info is None
    
    def altura(self, arbol):
        if(arbol is None):
            return -1
        else:
            return arbol._altura

    def actualizar_altura(self):
        if(self is not None):
            altura_izq = self.altura(self.izq)
            altura_der = self.altura(self.der)
            self._altura = (altura_izq if altura_izq > altura_der else altura_der) + 1
    
    def rotacion_simple(self, control):
        if(control):
            aux = self.izq
            self.izq = aux.der
            aux.der = self
        else:
            aux = self.der
            self.der = aux.izq
            aux.izq = self
        self.actualizar_altura()
        aux.actualizar_altura()
        return aux

    def rotacion_doble(self, control):
        if(control):
            self.izq = self.izq.rotacion_simple(False)
            self = self.rotacion_simple(True)
        else:
            self. der = self.der.rotacion_simple(True)
            self = self.rotacion_simple(False)
        return self

    def balancear(self):
        if(self is not None):
            if(self.altura(self.izq)-self.altura(self.der) == 2):
                if(self.altura(self.izq.izq) >= self.altura(self.izq.der)):
                    self = self.rotacion_simple(True)
                else:
                    self = self.rotacion_doble(True)
            elif(self.altura(self.der)-self.altura(self.izq) == 2):
                if(self.altura(self.der.der) >= self.altura(self.der.izq)):
                    self = self.rotacion_simple(False)
                else:
                    self = self.rotacion_doble(False)
        return self

    def insertar_nodo(self, dato, datos=None):
        if(self.info is None):
            self.info = dato
            self.datos = datos
        elif(dato < self.info):
            if(self.izq is None):
                self.izq = Arbol(dato, datos)
            else:
                self.izq = self.izq.insertar_nodo(dato, datos)
        else:
            if(self.der is None):
                self.der = Arbol(dato, datos)
            else:
                self.der = self.der.insertar_nodo(dato, datos)
        self = self.balancear()
        self.actualizar_altura()
        return self

    def inorden(self):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.inorden()
            print(self.info, self.datos)
            if(self.der is not None):
                self.der.inorden()

    def postorden(self):
        if(self.info is not None):
            if(self.der is not None):
                self.der.postorden()
            print(self.info)
            if(self.izq is not None):
                self.izq.postorden()

    def preorden(self):
        if(self.info is not None):
            print(self.info, self._altura)
            if(self.izq is not None):
                self.izq.preorden()
            if(self.der is not None):
                self.der.preorden()

    def busqueda(self, clave):
        pos = None
        if(self.info is not None):
            if(self.info == clave):
                pos = self
            elif(clave < self.info and self.izq is not None):
                pos = self.izq.busqueda(clave)
            elif(self.der is not None):
                pos = self.der.busqueda(clave)
        return pos
    
    def busqueda_proximidad(self, clave):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.busqueda_proximidad(clave)
            if(self.info[0:len(clave)] == clave):
                print(self.info)
            if(self.der is not None):
                self.der.busqueda_proximidad(clave)

    def remplazar(self):
        """Determina el nodo que remplazará al que se elimina."""
        info, datos = None, None
        if(self.der is None):
            info = self.info
            datos = self.datos
            if(self.izq is not None):
                self.info = self.izq.info
                self.der = self.izq.der
                self.izq = self.izq.izq
                self.datos = self.izq.datos
            else:
                self.info = None
                self.datos = None
        else:
            info, datos = self.der.remplazar()
        return info, datos

    def eliminar_nodo(self, clave):
        """Elimina un elemento del árbol y lo devuelve si lo encuentra."""
        info, datos = None, None
        if(self.info is not None):
            if(clave < self.info):
                if(self.izq is not None):
                    info, datos = self.izq.eliminar_nodo(clave)
            elif(clave > self.info):
                if(self.der is not None):
                    info, datos = self.der.eliminar_nodo(clave)
            else:
                info = self.info
                datos = self.datos
                if(self.der is None and self.izq is None):
                    self.info = None
                    self.datos = None
                elif(self.izq is None):
                    self.info = self.der.info
                    self.izq = self.der.izq
                    self.der = self.der.der
                    self.datos = self.datos
                elif(self.der is None):
                    self.info = self.izq.info
                    self.der = self.izq.der
                    self.izq = self.izq.izq
                    self.datos = self.datos
                else:
                    info_aux, datos_aux = self.izq.remplazar()
                    self.info = info_aux
                    self.datos = datos_aux
                    # raiz.info, raiz.nrr = aux.info, aux.nrr
        # self = self.balancear()
        self.actualizar_altura()
        return info, datos
    
    def contar_ocurrencias(self, buscado):
        cantidad = 0
        if(self.info is not None):
            if(self.info == buscado):
                cantidad += 1
            if(self.izq is not None):
                cantidad += self.izq.contar_ocurrencias(buscado)
            if(self.der is not None):
                cantidad += self.der.contar_ocurrencias(buscado)
        return cantidad
    
    def contar_pares_impares(self):
        pares, impares = 0, 0
        if(self.info is not None):
            if(self.info % 2 == 0):
                pares += 1
            else:
                impares += 1
            if(self.izq is not None):
                par, impar = self.izq.contar_pares_impares()
                pares += par
                impares += impar
            if(self.der is not None):
                par, impar = self.der.contar_pares_impares()
                pares += par
                impares += impar
        return pares, impares

    def barrido_por_nivel(self):
        pendientes = Cola()
        pendientes.arribo(self)
        while(not pendientes.cola_vacia()):
            nodo = pendientes.atencion()
            print(nodo.info)
            if(nodo.izq is not None):
                pendientes.arribo(nodo.izq)
            if(nodo.der is not None):
                pendientes.arribo(nodo.der)    

    def barrido_por_nivel_huff(self):
        pendientes = Cola()
        pendientes.arribo(self)
        while(not pendientes.cola_vacia()):
            nodo = pendientes.atencion()
            print(nodo.info, nodo.frecuencia)
            if(nodo.izq is not None):
                pendientes.arribo(nodo.izq)
            if(nodo.der is not None):
                pendientes.arribo(nodo.der)
