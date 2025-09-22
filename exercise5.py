#### Ćwiczenie nr 5 : 
#zmodyfikuj program ponizej, tak aby kwota, ilość rat oraz oprocenotwanie były przechowywane w słowmniku
#a nastepnie te wartosci wykorzystywane w obliczeniach

# Zdefiniowanie słownika z danymi
dane = {
    "kwota": float(input("Podaj kwotę: ")),
    "ilosc_lat": int(input("Podaj ilość rat (lat): ")),
    "oprocentowanie": float(input("Podaj oprocentowanie: "))
}

# Obliczenia
kwota_koncowa = dane["kwota"] * (1 + dane["oprocentowanie"] / 100) ** dane["ilosc_lat"] - dane["kwota"]

# Wynik
print(f'Zysk wynosi {kwota_koncowa:.2f}')


#mozna tez tak:
#dane = {
#"kwota": 10000,
#"okres": 3,
#"oprocentowanie": 8}

#zestaw ze słownika ubrać w zmienne:
kwota = dane["kwota"]