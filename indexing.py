word = 'python'

print(word[0]) #p
print(word[1])  # y
print(word[2])  # t
print(word[3])  # h
print(word[4])  # o
print(word[5])  # n

print(word[-4]) #t


word ='python'
#012345
#-654321

#słowo PYT, czyli liczba która nas interesuje + 1, np. word[0:3]
print(word[0:2]) #py
print(word[0:3]) #pyt
print(word[-3:]) #hon czyli od srodka do konca 

kurs = 'codebrainers'
nowy_kurs = kurs #kopia

#co ile
print(kurs[0:-1:2]) 
#kurs[start:koniec:krok] wez co 2 znak

print(f'ilosc znakow {len(kurs)}')  #dlugosc elementu
print(kurs[0:len(kurs)]) #tu coś nie wyszło!
print({len(kurs)}) 

t= [1, 2, 3]
print(t[2]) #wydrukuj mi 2 wyraz
c= (1,2,3)
print(c[1]) #wydrukuj mi 1 wyraz
