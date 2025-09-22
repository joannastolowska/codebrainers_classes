empty_d = dict()
print(type(empty_d)) #class dict

# d = {klucz: wartosc}

d = {
    'k'  : 'v',
    'k1' : 'v1',
    'k2' : 'v2',
    'k3' : 'v3'
    }

#print(d[1]) #keyerror!
print(d['k1'])
print(d.get('k1')) #pobieranie wartosci ze słownika, ta metoda lepsza

print(d)

d['k4'] = 'v4' #dodanie czegos do słownika
print(d)

del d['k4'] #usuniecie czegos ze słownika
print(d.get('k4')) #none

d.pop('k3')
print(d.get('k3')) #none

print(d.keys()) #dict_keys(['k', 'k1', 'k2'])
print(d.values()) #dict_values(['v', 'v1', 'v2'])
print(d.items()) #dict_items([('k', 'v'), ('k1', 'v1'), ('k2', 'v2')])



