import os

path = r'C:\Users\dioge\Desktop\teste cnis'

search = 'cnis'


def format_size(size):
    base = 1024
    K = base
    M = base ** 2
    G = base ** 3
    T = base ** 4
    P = base ** 5

    if size < K:
        size = size
        text = 'B'
    elif size < M:
        size /= K
        text = 'K'
    elif size < G:
        size /= M
        text = 'M'
    elif size < T:
        size /= G
        text = 'G'
    elif size < P:
        size /= T
        text = 'T'
    else:
        size /= P
        text = 'P'

    size = round(size, 2)
    return f'{size}{text}'


cont = 0
for root, _dirs, arcs in os.walk(path):
    for arc in arcs:
        if search in arc:
            try:
                cont += 1
                full_path = os.path.join(root, arc)
                name_arc, ext_arc = os.path.splitext(arc)
                size = os.path.getsize(full_path)

                print()
                print(f'Founded archive: {name_arc}.')
                print(f'Path: {full_path}.')
                print(f'Size (Bytes): {size}')
                print(f'Size: {format_size(size)}')
                print(f'Extension: {ext_arc}')
                print()
            except (PermissionError, FileNotFoundError, Exception) as error:
                print(error)

print(f'{cont} archives founded')

# print('###' * 15)
# os.chdir(path)  # Mover diretório
# print(os.getcwd())  # Obter diretório atual.
#
# print(os.listdir())  # lista diretório
# # print(os.environ)  # retorna dict com variáveis de ambiente do sistema


# os.mkdir('INSS') # cria um diretório

# cria vários diretórios em linha.
# directory = "TSE"
# parent_dir = r"C:\Users\dioge\Desktop\teste cnis\INSS\JF"
# path = os.path.join(parent_dir, directory)
# os.makedirs(path)




