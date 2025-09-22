#definicja

def sum_two_numbers(a,b):
   return a + b

#wywołanie
result = sum_two_numbers(2,3)
print(f'wynik dzialania funkcji: {result}') #wynik: 3

result1 = sum_two_numbers("test","test")
print(f'wynik dzialania funkcji: {result1}') 

x= float(input("podaj liczbe "))
y=float(input ("podaj liczbe"))
         
result2 = sum_two_numbers(x,y)
print(f'wynik dzialania funkcji {result2}')

#podaj liczbe 5
#podaj liczbe5
#wynik dzialania funkcji 10.0

# Definicja
def sum_two_numbers(a, b):
    '''
    Docstring - dokumentacja
    Funkcja przyjmuje dwie liczby i zwraca ich sume
    :param a: liczba
    :param b: liczba
    '''
    return a + b
help(sum_two_numbers)
input("Press any key")
# Wywolanie
result = sum_two_numbers(2, 3)
print(f"Wynik dzialania funkcji {result}")
result1 = sum_two_numbers('Test', 'Test')
print(f"Wynik dzialania funkcji {result1}")
x = float(input("Podaj liczbe "))
y = float(input("Podaj liczbe "))
result2 = sum_two_numbers(x, y)
print(f"Wynik dzialania funkcji {result2}")
result3 = sum_two_numbers(float(10), 3)
print(f"Wynik dzialania funkcji {result3}")


def sum_two_numbers(a, b):
    '''
    Docstring - dokumentacja
    Funkcja przyjmuje dwie liczby i zwraca ich sume
    :param a: liczba
    :param b: liczba
    '''
    return a + b

def main():
    help(sum_two_numbers)
    input("Press any key")

    # Wywolanie
    result = sum_two_numbers(2, 3)
    print(f"Wynik dzialania funkcji {result}")

    result1 = sum_two_numbers('Test', 'Test')
    print(f"Wynik dzialania funkcji {result1}")

    x = float(input("Podaj liczbe "))
    y = float(input("Podaj liczbe "))

    result2 = sum_two_numbers(x, y)
    print(f"Wynik dzialania funkcji {result2}")

    result3 = sum_two_numbers(float(10), 3)
    print(f"Wynik dzialania funkcji {result3}")

    if __name__ == "__main__":
        main()






