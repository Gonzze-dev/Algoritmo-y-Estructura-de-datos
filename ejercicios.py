#2
def suma_de_numeros_anteriores(numero):
    if (numero >= 0):
        print('',  numero)
        return suma_de_numeros_anteriores(numero - 1)

#3
def producto(numero1, numero2):
    if(numero2 == 1):
        return numero1
    else:
        return numero1 + producto(numero1, numero2 - 1)

#4
def exponencial(base,exponente):
    if(base == 0 and exponente == 0):
        return 'Error'
    elif(exponente == 0):
        return 1
    else:
        return base * exponencial(base, exponente - 1)

#5 Ejercicio Propuesto
def Buscar_valor_letra_romana(Letra_Romano):
    Valor = 0

    if Letra_Romano == 'M':
        Valor = 1000
    elif Letra_Romano == 'D':
        Valor = 500
    elif Letra_Romano == 'C':
        Valor = 100
    elif Letra_Romano == 'L':
        Valor = 50
    elif Letra_Romano == 'X':
        Valor = 10
    elif Letra_Romano == 'V':
        Valor = 5
    elif Letra_Romano == 'I':
        Valor = 1

    return Valor

def Convertir_de_numero_romano_a_numeros_normales(Cadena_Romano):
    Val_letra_1 = 0
    Val_letra_2 = 0
    indice = 2

    if(len(Cadena_Romano) == 0):
        return Val_letra_1
    else:
        Val_letra_1 = Buscar_valor_letra_romana(Cadena_Romano[-1])

        if(len(Cadena_Romano) > 1):
            Val_letra_2 = Buscar_valor_letra_romana(Cadena_Romano[-2])
        else:
            indice = 1

        if(Val_letra_1 > Val_letra_2):
            Val_letra_1 -= Val_letra_2
        else:
            Val_letra_1 += Val_letra_2
        
        return Val_letra_1 + Convertir_de_numero_romano_a_numeros_normales(Cadena_Romano[:-indice])
        
#6
def invertir_palabras(palabra):
    if (len(palabra) == 1):
        return palabra
    else:
        return palabra[-1] + invertir_palabras(palabra[:-1])

#7
def sumatoria(maximo):
    if maximo >= 1:
        return 1/maximo + sumatoria(maximo-1)
    else:
        return maximo

#8 Ejercicio Propuesto
def Numero_decimal_a_binario(Numero_decimal):
    if((Numero_decimal == 0) or (Numero_decimal == 1)):
        return str(Numero_decimal)
    else:
        return Numero_decimal_a_binario((Numero_decimal//2)) + str(Numero_decimal%2)

#9
def logaritmo(base, argumento):
    if((argumento // base) <= 1):
        return 0
    else:
        return 1 + logaritmo(base, argumento//base)

#11
def invertir_numero(numero):
    if (numero < 10):
        return numero
    else:
        return (numero%10)*10**(len(str(numero//10))) + invertir_numero(numero//10)


#22 Ejercicio Propuesto
def usar_la_fuerza(mochila):

    if ((len(mochila) == 0) or (mochila[-1] == 'Sable')):
        return len(mochila)
    else:
        return usar_la_fuerza(mochila[:-1])

def problema_jedi():
    mochilajedi = ['algo', 'algo', 'algo', 'algo', 'algo', 'algo']
    mochilajedi2 = ['algo', 'algo', 'algo', 'algo', 'algo', 'Sable']
    mochilajedi3 = ['algo', 'Sable', 'algo', 'algo', 'algo', 'algo']
    mochilajedi4 = ['Sable', 'algo', 'algo', 'algo', 'algo', 'algo']

    pos_sable = usar_la_fuerza(mochilajedi)

    if(pos_sable == 0):
        print('El sable no esta en la mochila')
    else:
        print('El sable esta en la mochila', '\nObjetos Sacados: ', len(mochilajedi) - pos_sable)



"""def Buscar_Salida(Laberinto, x, y, movimiento, tamanio):

    if((x + y)/2 == 5):
        return 1
    
    if( ( (movimiento == 1) and ((y >= 0) and (y+1 <= 4)) ) and (Laberinto[x][y+1] == 1) ): #me muevo hacia abajo
        y += 1
    elif( ( (movimiento == 1) and ((y >= 0) and (y+1 <= 4)) ) and (Laberinto[x][y+1] == 0) ): #es un obstaculo
        movimiento = 2

    elif( ( (movimiento == 2) and ((y-1 >= 0) and (y <= 4)) ) and (Laberinto[x][y-1] == 1) ): #me muevo hacia arriba

        if( ( (movimiento == 2) and ((x >= 0) and (x+1 <= 4)) ) and (Laberinto[x+1][y] == 1) ): #intento derecha
            movimiento = 3
        elif( ( (movimiento == 2) and ((x-1 >= 0) and (x <= 4)) ) and (Laberinto[x-1][y] == 1) ): #intento izquierda
            movimiento = 4

    elif( ( (movimiento == 3) and ((x-1 >= 0) and (y+1 <= 4)) ) and (Laberinto[x][y-1] == 1) ):
        

    

    return Buscar_Salida(Laberinto, x, y, movimiento, tamanio)"""


Matriz = [[1,1,0],
          [1,1,1],
          [1,0,5],
          ]

def salir(x,y,laberinto,primero):
    
    if laberinto[x][y] == 5:
        return 1
    elif(x == 0 and y == 0):
        if (primero):
            if(salir(x + 1,y,laberinto,0) or salir(x-1, y,laberinto,0) or salir(x, y+1,laberinto,0) or salir(x, y-1,laberinto,0)):
                return 1
    elif(laberinto[x][y] == 0):
        laberinto[x][y] = 2
        if(salir(x + 1,y,laberinto,0) or salir(x-1, y,laberinto,0) or salir(x, y+1,laberinto,0) or salir(x, y-1,laberinto,0)):
            return 1
        else:
            if(laberinto[x][y] == 2):
                laberinto[x][y] = 0
    
    return 0

print(salir(0,0,Matriz,1))
