def nazwa():
    pass

instancja_funkcji = nazwa()

suma = lambda arg1, arg2: arg1 + arg2
print(suma(1,2)) # wynik 3

pitagoras = lambda a,b,c,d: ((a * a)+ (b *b )) ** 0.5 + c * d 
print(pitagoras(1,2,3,4)) #wynik 14.23606797749979

#podejscie klasyczne
empty_list = []
for element in range(1,21):
    empty_list.append(element)
print(empty_list) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

#podejscie funkcyjne,inline (krótszy kod!)
empty_list1 = [e for e in 'python']
print(empty_list1) #['p', 'y', 't', 'h', 'o', 'n']

empty_list2 = [digit for digit in range (1,21)]
print(empty_list2) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

#inline_list = [expression for element in interable_seq]
empty_list3 = [digit for digit in range (1,21) if digit % 2 == 0]
print(empty_list3) #[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#to tyczy się listy LOGS w notebookach

log_file = 'logs.txt'
with open(log_file) as f: 
    wystapienia = sum(line.count('ERROR') for line in f)
    print (f' ERROR: {wystapienia}') # ERROR: 6 -> czyli wystapił error 6x

log_file = 'logs.txt'
with open(log_file) as f: 
    wystapienia = sum(line.count('INFO') for line in f)
    print (f' INFO: {wystapienia}') # INFO: 6 -> czyli wystapił error INFO 6x

log_file = 'logs.txt'
with open(log_file) as f: 
    wystapienia = sum(line.count('DEBUG') for line in f)
    print (f' DEBUG: {wystapienia}') # DEBUG: 2 -> czyli wystapił error INFO 2x
