from itertools import zip_longest, count

capitais = ['POA', 'BH', 'SP', 'RJ']

estados = ['RS', 'MG', 'SP']

estados_capitais = zip(capitais, estados)
print(estados_capitais)  # <zip object at 0x000001B13366AB00>

estados_capitais = list(zip(capitais, estados))
print(estados_capitais)  # [('POA', 'RS'), ('BH', 'MG'), ('SP', 'SP')]

estados_capitais = list(zip_longest(capitais, estados))
print(estados_capitais)  # [('POA', 'RS'), ('BH', 'MG'), ('SP', 'SP'), ('RJ', None)]

estados_capitais = list(zip_longest(capitais, estados, fillvalue='UF'))
print(estados_capitais)  # [('POA', 'RS'), ('BH', 'MG'), ('SP', 'SP'), ('RJ', 'UF')]

indice = count()

estados_capitais = zip(indice, capitais, estados)

for indice, capital, estado in estados_capitais:
    print(indice, capital, estado)

lista_a = [1, 2, 3, 4, 5, 6, 7, 8]
lista_b = [1, 2, 3, 4]
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]

print(lista_soma)

