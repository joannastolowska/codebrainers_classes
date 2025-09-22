list1 = [1, 2, 3]
print(list1)

#ale tez mozna tak:
convert_to_list = list((1,2,3))
print(convert_to_list)

contert_str_to_list = list("to jestlista")
print(contert_str_to_list) #['t', 'o', ' ', 'j', 'e', 's', 't', 'l', 'i', 's', 't', 'a']

print(contert_str_to_list[0:5]) #'t', 'o', ' ', 'j', 'e']

unsorted_list = ['a', 'g', 'c', 'p', 'x', 'b']
print(f'przed sortowaniem {unsorted_list}') #przed sortowaniem ['a', 'g', 'c', 'p', 'x', 'b']
unsorted_list.sort()
print(f'po sortowaniu {unsorted_list}') #po sortowaniu ['a', 'b', 'c', 'g', 'p', 'x']
unsorted_list.count('a')
print(f'Litera a występuje tylko {unsorted_list.count('a')}') #Litera a występuje tylko 1

lst1 = ['a']
lst2 = ['b']
lst3 = ['c']
lst3 = lst1 + lst2
print(f'lista polaczona {lst3}') #na listach dodawanie tylko dziala


list_comprehension = [ #zagniezdzanie list
    ['a', 'b', 'c'],
     [1,    2,   3]
]

print(list_comprehension[0][0]) # odp. a 


new_element = 'dodane'
codebrainers_lista = ['a', 123, [1,3], True, False, None, (1, 3), 'testt', '1231312']
codebrainers_lista.append(new_element)
print(codebrainers_lista[-1] == new_element)
codebrainers_lista.insert(2, new_element)
print(codebrainers_lista)
# ['a', 123, 'dodane', [1, 3], True, False, None, (1, 3), 'testt', '1231312', 'dodane']
print(codebrainers_lista.index('a'))    # sprawdzam gdzie jest a
print(f'Zrzucone {codebrainers_lista.pop()}')
print(f'Po zrzuceniu {codebrainers_lista}')









