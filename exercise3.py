#biorąc pod uwagę 2 ciągi 's1 i 's2 zwróc
#nowy ciag złozony z pierwszego, srodkowego i 
#ostatniego znaku kadego ciagu wejsciowego

#dane
# *'s1 = "America"
# * 's2 = "Japan"

#oczekiwany wynik:
#'AJrpan'

str1 = 'America'
str2 = 'Japan'

#pierwszy znak
print(str1[0]) #A 
print(str1[-1]) #a
print(str2[0]) #J
print(str2[-1]) #n

print(str1[len(str1)//2]) # znak srodkowy z str1 
print(str2[len(str2)//2]) # znak srodkowy z str2
new_str = str1[0] + str2[0] + str1[len(str1)//2] + str2[len(str2)//2]  + str1[-1]  + str2[-1]
print(f'Nowy ciag znakow {new_str}') #AJrpan

str3 = 'test'
print(len(str3)//2) #2 znalezienie srodkowego 


