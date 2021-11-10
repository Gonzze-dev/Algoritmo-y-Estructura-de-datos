from heap import HeapMax

def ejercicio_16():
    prio_empleado = 1
    prio_staff_TI = 2
    prio_gerente = 3
    
    heapmax_documentos = HeapMax()
    
    documentos_empleados = [
        ['documento 1 empleado', prio_empleado],
        ['documento 2 empleado', prio_empleado],
        ['documento 3 empleado', prio_empleado],
    ]
    
    documentos_empleados_2 = [
        ['documento 4 empleado', prio_empleado],
        ['documento 5 empleado', prio_empleado],
    ]
    
    documentos_staff_TI = [
        ['documento 6 staff TI', prio_staff_TI],
        ['documento 7 staff TI', prio_staff_TI],
    ]
    
    documentos_gerente = [
        ['documento 8 gerente', prio_gerente],
    ]
    
    documentos_gerente_2 = [
        ['documento 9 gerente', prio_gerente],
    ]
    
    #PUNTO A
    heapmax_documentos.arribo_muchos(documentos_empleados)
    
    #PUNTO B
    print(heapmax_documentos.atencion()[1])
    
    #PUNTO C
    heapmax_documentos.arribo_muchos(documentos_staff_TI)
    
    #PUNTO D
    heapmax_documentos.arribo_muchos(documentos_gerente)
    
    #PUNTO E
    print()
    for i in range(2):
        print(heapmax_documentos.atencion()[1])
    
    #PUTNO F
    heapmax_documentos.arribo_muchos(documentos_empleados_2)
    heapmax_documentos.arribo(documentos_gerente_2[0][0], documentos_gerente_2[0][1])
    
    #PUNTO G
    print()
    for i in range(heapmax_documentos.tamanio):
        print(heapmax_documentos.atencion()[1])

ejercicio_16()