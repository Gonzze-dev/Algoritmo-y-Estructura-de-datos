Matriz = [[1,1,0,1,0],
          [1,1,1,1,1],
          [1,0,1,1,0],
          [1,1,0,1,0],
          [1,0,1,1,1]]

def Buscar_Salida(Laberinto, x, y):
    
    if(x == 4 and y == 4):
        return 1
    elif(((x >= 0 and x <= 2) and (y >= 0 and y <= 2)) and (Laberinto[x][y] == 1)):
        Buscar_Salida(Laberinto, x, y+1)
        Buscar_Salida(Laberinto, x+1, y)
        Buscar_Salida(Laberinto, x-1, y)
        Buscar_Salida(Laberinto, x, y-1)
    

print(Buscar_Salida(Matriz, 0, 0))

"""def Buscar_Salida(Laberinto,x,y):
    if x == 4 and y == 5:
        return Laberinto
    else:
        if (((x >= 0 and x <= 4) and (y >= 0 and y <= 4)) and (Laberinto[x][y] == 1)):
            Laberinto[x][y]=2
            if Buscar_Salida(Laberinto,x,y+1):
                return Laberinto
            elif Buscar_Salida(Laberinto,x+1,y):
                return Laberinto
            elif Buscar_Salida(Laberinto,x-1,y):
                return Laberinto
            elif Buscar_Salida(Laberinto,x,y-1):
                return Laberinto
        else:
            return False

print(Buscar_Salida(Matriz,0,0))"""