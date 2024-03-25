def missing_number(num,array): # recibe dos parametros num y array
    list = []
    for i in range(1, num+1): # recorre el rango de 1 hasta num+1
        list.append(i)

    sum_missing = sum(array) # suma los elementos del array
    sum_list = sum(list) # suma los elementos de la lista
    resul = sum_list - sum_missing # resta la suma de la lista menos la suma del array
    print(resul)
    return resul
    

assert missing_number(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"

print("todos los casos han pasado exitosamente")

