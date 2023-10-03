diccionario = {
    "nombre": 'Pedro',
    "apellido": 'Paternina',
    "edad": 17
}

claves = diccionario.keys() #Obtienes las claves (clave: valor)
print(claves)

get = diccionario.get('edad') #Obtiene algun valor dependiendo de la clave que le añadas
print(get)

diccionario_iterable = diccionario.items()
print(diccionario_iterable)
diccionario.pop('edad') #Elimina un elemento del diccionario
print(diccionario)





diccionario.clear() #Elimina todo lo del diccionario
print(diccionario)