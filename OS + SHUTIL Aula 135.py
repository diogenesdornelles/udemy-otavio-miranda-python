import os
import shutil
import re

path = r'C:\Users\dioge\Desktop\teste cnis'
os.chdir(path)
print(os.getcwd())
new_folder = 'new'
full_path = os.path.join(path, new_folder)

pdf = '\.pdf'
txt = '\.txt'

if not os.path.exists(full_path):
    os.mkdir(full_path)
else:
    print('Dir already exist')

for root, dirs, files in os.walk(path):
    for n, file in enumerate(files):
        try:
            old_path = os.path.join(root, file)
            srch_pdf = re.findall(f".*{pdf}$", file)
            if srch_pdf:
                file = f'cnis{n}{pdf}'
            new_file_path = os.path.join(full_path, file)
            srch_txt = re.findall(f".*{txt}$", file)
            if srch_txt:
                os.remove(old_path)
            if old_path != new_file_path:
                shutil.copy(old_path, new_file_path)
                print(f'File {file} copied do {full_path}')
        except Exception as error:
            print('Ocorreu um erro.')
            break
