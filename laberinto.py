Matriz = [[1,1,0,1,0],
          [1,1,1,1,1],
          [1,0,1,1,0],
          [1,1,0,1,0],
          [1,0,1,1,1]]

#algoritmo viejo
"""def Buscar_Salida(Laberinto, x, y):
    
    if(x == 4 and y == 4):
        return 1
    elif(((x >= 0 and x <= 2) and (y >= 0 and y <= 2)) and (Laberinto[x][y] == 1)):
        Buscar_Salida(Laberinto, x, y+1)
        Buscar_Salida(Laberinto, x+1, y)
        Buscar_Salida(Laberinto, x-1, y)
        Buscar_Salida(Laberinto, x, y-1)
"""

def Buscar_Salida(Laberinto, x, y, tamanio_matriz):
    if x == tamanio_matriz and y == tamanio_matriz:
        Laberinto[x][y] = 2
        return True
    else:
        if (((x >= 0 and x <= 4) and (y >= 0 and y <= 4)) and (Laberinto[x][y] == 1)):
            Laberinto[x][y] = 2
            if Buscar_Salida(Laberinto,x,y+1, tamanio_matriz) or Buscar_Salida(Laberinto,x+1,y, tamanio_matriz) or Buscar_Salida(Laberinto,x-1,y, tamanio_matriz) or Buscar_Salida(Laberinto,x,y-1, tamanio_matriz):
                return True
        else:
            return False

print(Buscar_Salida(Matriz, 0, 0, (len(Matriz)-1)))
print(Matriz)
