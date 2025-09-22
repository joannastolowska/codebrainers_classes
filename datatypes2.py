#wypełnić te elementy wartosciami 

number = 42
number_float = 3.14
characters = "python"
flag = True
list_elements = [1, 2, 3, 4, 5]
dictionary_elements = {'name': 'Anna', 'age': 30}
set_elements = [1,2,3,25,1,2,3]
tuple_elements = (10, 20, 30)

#czy to jest integer
print(number.is_integer()) #true
print(number_float.is_integer()) #false

# Czy zaczyna/konczy sie na dany znak 
print(characters.startswith('X'))
print(characters.endswith('s'))
print(characters.split('o'))
# Uporzadkowana sekwencja
print(list_elements[0])
# Nieuporzadkowane sekwencje
print(dictionary_elements['name'])
print(set_elements.pop())

#krotka
print(tuple_elements)
print(tuple_elements[2])

new_tuple = list(tuple_elements)
new_tuple.append(10)
new_tuple.append('a')
new_tuple.append(True)
tuple_elements = tuple(new_tuple)
print(type(tuple_elements)) #<class 'tuple'>