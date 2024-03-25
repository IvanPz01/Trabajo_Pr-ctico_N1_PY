def number_spiral (fila, colum): # recibe dos parametros fila y columna
    if fila > colum: # si la fila es mayor que la columna
        if fila % 2 == 0: # si la fila es par
            resul_fila = (fila**2 - colum + 1) # multiplica la fila por si misma, le resta la columna y le suma 1 y lo guarda en una variable
            return resul_fila # retorna el resultado
        else: # si la fila es impar
            resul_fila = ((fila-1)**2 + colum) # resta la fila menos 1, la multiplica por si misma y le suma la columna y lo guarda en una variable
            return resul_fila # retorna el resultado
    else: # si la columna es mayor que la fila
        if colum % 2 == 0: # si la columna es par
            resul_column = ((colum-1)**2 + fila) # resta la columna menos 1, la multiplica por si misma, le suma la fila y lo guarda en una variable
            return resul_column # retorna el resultado
        else:# si la columna es impar
            resul_column = (colum**2 - fila + 1) # multiplica la columna por si misma, le resta la fila, le suma 1 y lo guarda en una variable
            return resul_column # retorna el resultado
        
 

print(number_spiral(2, 3)) # 8

print("todos los casos han pasado exitosamente")