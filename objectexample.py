def nazwa():
    return 2
print(type(nazwa()))

lista = [1,2]
print(type(lista))

class ExampleClass:
    def class_method():
        return 2
    
print(type(ExampleClass))
print(type(ExampleClass.class_method()))

x=10
y = 'Python'
z = None

print(id(x))  #4327385816
print(id(y))  #4308899744

x = 1
print(id(x)) #4388923832 coś innego, po nowym zadeklarowaniu x

