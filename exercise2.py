#### Ćwiczenie nr 2: 
#zmodyfikuj program ponizej, tak aby kwota, ilość rat oraz oprocenotwanie było wprowadzone przez uzytkownika

# Zdefiniowanie zmiennych

kwota = float(input("Podaj kwotę: "))
ilosc_lat = int(input("Podaj ilość rat: "))
oprocentowanie = float(input("Podaj oprocentowanie: "))

# Obliczenia 
kwota_koncowa = kwota * (1 + oprocentowanie / 100) ** ilosc_lat - kwota

# Wynik
print(f'Zysk wynosi {kwota_koncowa:.2f}')
