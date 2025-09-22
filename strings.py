kurs = 'Codebrainers '  #dodanie spacji na okncu, ale to obarczone błędem
typ_kursu = 'Tester'

grupa = kurs + typ_kursu
print(grupa)

print(f"{kurs} {typ_kursu}")
print('-' * 120) #------------------------------

# wyswietlanie apostrofow i cudzyslowiow
print("Test'Test'") # Test'Test'
print('Test"Test"') # Test"Test"

print('Test\'Test') #Test'Test
print('Test"Test') #Test"Test

#znak specjalny \n
print('pierwszalinia\n\nDrugalinia\n') #jak wstawimy \n to beda dwie linie

print('pierwszalinia\n' \
      'drugalinia\n' \
      'trzecialinia\n' \
      'czwarta\n' \
      'piata\n')

#znak specjalny \t
print("Columna1\t\tColumna2\t\tColumna3\t\t")  #Columna1                Columna2                Columna3

#\a

#wyswietlanie sciezki do katalogu
print('Informacje znajduja sie w katalogu C:\nowy katalog\testy') #Informacje znajduja sie w katalogu C:#owy katalog     esty
print(r'Informacje znajduja sie w katalogu C:\nowy katalog\testy') #to jest surowy tekst wyswietlony

print('\u00A9')  #znak coppywright
print(r"Znaczek copywright ukryty jest pod tym kodem \u00A9") #bez "r" sie nie da



