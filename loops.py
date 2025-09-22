#sa tylko 2 rodzaje w py 
students = ['Adam', "Jan", 'Tomek', 'anna']

for student in students:
    print(f'na kursie jest {student}')

#na kursie jest Adam
#na kursie jest Jan
#na kursie jest Tomek
#na kursie jest anna
    if student == "Tomek":
        break
#na kursie jest Adam
#na kursie jest Jan
#na kursie jest Tomek

word = 'python'
for letter in word:
    print(f'litera w slowie to {letter}')
#litera w slowie to p
#litera w slowie to y
#litera w slowie to t
#litera w slowie to h
#litera w slowie to o
#litera w slowie to n

students_dictionary = {'student1': 'Adam',
                       'student2': 'Tomek',
                       'student3': 'anna' }
for student in students_dictionary.values():
    print(f"w slowniku jest {student}")
#w slowniku jest Adam
#w slowniku jest Tomek
#w slowniku jest anna

for key, value in students_dictionary.items():
    print(f'W slowniku jest {key}, {value}')
#W slowniku jest student1, Adam
#W slowniku jest student2, Tomek
#W slowniku jest student3, anna

for i in range(4):
    print(i) #0 1 2 3
    if i == 2:
        break  #0 1 2 

    