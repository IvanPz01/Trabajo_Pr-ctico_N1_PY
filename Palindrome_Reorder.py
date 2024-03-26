def palindrome_reorder(palindromo):
    list_pali = {}
    list_resul = []

    if len(palindromo) > 1 and len(palindromo) < 10**6: # validacion de la longitud del palindromo
        for i in palindromo: # recorre el palindromo
            list_pali[i] = list_pali.get(i, 0) + 1 # guarda en un diccionario la letra y la cantidad de veces que se repite
        
        print(list_pali)

        odds = 0
        for k, v in list_pali.items(): # recorre el diccionario
            
            if v % 2 != 0: # si la cantidad de veces que se repite la letra es impar
                odds += 1 
                if odds > 1: # si la variable odds es mayor a 1
                    return "NO SOLUTION"
            
            if v > 2: # si la cantidad de veces que se repite la letra es mayor a 2
                list_resul.append(k*(v//2)) # agrega la letra a la lista de resultado
                
            if v == 2: # si la cantidad de veces que se repite la letra es igual a 2
                list_resul.append(k) # agrega la letra a la lista de resultado

        for k,v in list_pali.items(): # recorre el diccionario
            if v % 2 != 0:
                list_resul.append(k)

        for k,v in list_pali.items().__reversed__(): # recorre el diccionario en reversa
            if v % 2 == 0: # si la cantidad de veces que se repite la letra es par
                if v > 2:
                    list_resul.append(k*(v//2)) # agrega la letra a la lista de resultado
                
                if v == 2: # si la cantidad de veces que se repite la letra es igual a 2
                    list_resul.append(k)
            if v % 2 != 0:
                if v > 2:
                    list_resul.append(k*(v//2)) # agrega la letra a la lista de resultado
        return "".join(list_resul) # retorna la lista de resultado como un string
    else:
        return print("El palindromo debe tener una longitud mayor a 1 y menor a 10^6")



# Casos de prueba
assert palindrome_reorder("aabbc") == "abcba", "Error en el caso de prueba"
print("todos los casos han pasado exitosamente")