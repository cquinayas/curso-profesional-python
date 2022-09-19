my_list = [1,1,2,3,4,4,5]
my_set = set(my_list)
print(my_set)

my_tuple = ("Hola","Hola","Hola",1)
my_set2 = set(my_tuple)
print(my_set2)

my_set3 = {1,2,3}
print(my_set3)

#añadir un elemento
my_set3.add(4)
print(my_set3)

#añadir multiples elementos
my_set3.update([1,2,5])
print(my_set3)
 
#añadir multiples elementos
my_set3.update((1,7,2),{6,8})
print(my_set3)

#Borrar un elemento existente
my_set3.discard(1)
print(my_set3)
my_set3.remove(2)
print(my_set3)

#Discard permite borrar elemento existentes e inexistentes
my_set3.discard(10)
print(my_set3)

#Con remove no se puede borrar elementos inexistentes
#y_set3.remove(12)
#print(my_set3)

#Borrar un elemento aleatorio
my_set3.pop()
print(my_set3)

#Limpiar el set
my_set3.clear()
print(my_set3)