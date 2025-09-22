

#if conditions: 
  #   print('Test')

if 5 > 0:
    print('Test') #test
#ostep linijki miedzy warunkami (to osobny fragment kodu)
if 5 < 0:
    print('Test2') # nic nie wydrukował 

if 5 < 0:
    print('Test2')
else: 
    print('jestem w else') #jestem w else #czyli jesli to jest nie prawda, to mi o tym napisz
################
a=7 #jesli zmienimy na 9, to pojdzie dalej i sprawdzi elif
if a>9:
    print('a wieksze od 9')
elif a>8:
    print("a jest wieksze od 8") #wydrukował a jest wieksze od 9 i zakonczyl prace
else:
    print("a jest wieksze od 7") #wydrukował: a jest wieksze od 7

    condition = 1 == 1
    print(condition)

    if condition:
        print("to jest prawda") #to jest prawda

    #and, or, not
    if 1>0 and 2>1: #sprawdz warunek 1 i warunek 2, oba musza byc prawda,zeby przejść
        print("prawda") #prawda

    if 1<0 or 2>1: #sprawdz warunek 1, jesli nieprawda, to sprawdź kolejny. ale jak 1 bedzie prawda, to nie idz dalej
        print('or')

    if not False:
        print('not') #not

    if not True:
        print('not1') #not

print(1 >0 and 2 >1) #true <-sprawdzenie
print(1<0 or 2<1) #false <-sprawdzenie

