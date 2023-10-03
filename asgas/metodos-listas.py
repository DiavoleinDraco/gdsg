
#Con list creamos una lista
lista = list(['pepito','perez',True])  #Aclarar que recibe como parametro una lista (array)
listWithoutStrings = list([1,5,7,37,941,62])
#Con len obtengo la cantidad de elementos
cantidad = len(lista)

lista.append('jasjasjjassjaj') #Agregar elementos a la lista

lista.insert(1,"Añadiendo al inicio")  #este añade algo en la posicion que se le asigne

lista.extend(['pedro','luis',False]) #Se añaden varios elementos

lista.pop(0,) #Elimina algun elemento por la posicion, -1 elimina el ultimo 

lista.remove("Añadiendo al inicio") #Remueve por el valor

 # lista.clear() Elimina absolutamente todo

listWithoutStrings.sort() #Organiza, añadiendo (reverse= true ) los ordena al reves
listWithoutStrings.reverse() #Esto invierte la lista 


print(listWithoutStrings )
