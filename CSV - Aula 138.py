# Comma Separated Values (CSV)
import csv

with open(r'arquivos aula 138/clientes.csv', 'r') as file:
    data1 = csv.reader(file)  # retorna um iterador
    data2 = csv.DictReader(file)  # retorna um dicionário com chaves
    data3 = [x for x in csv.DictReader(file)]

    for dt in data1:  # Não é possível utilizar fora do gerenciador de contexto, ao menos que generator seja convertido.
        print(dt)

    for dt in data2:
        print(dt)

print(data3)

with open(r'arquivos aula 138/clientes2.csv', 'w') as file:
    writer = csv.writer(
        file,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )

    chaves = data3[0].keys()
    chaves = list(chaves)
    writer.writerow([
        chaves[0],
        chaves[1],
        chaves[2],
        chaves[3]
    ]
    )

    for data in data3:
        writer.writerow(
            [
                data['Nome'],
                data['Sobrenome'],
                data['E-mail'],
                data['Telefone']
            ]
        )
