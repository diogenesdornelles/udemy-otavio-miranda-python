from PyPDF2 import PdfFileReader, PdfFileMerger, PdfFileWriter
import os

#  https://pypdf2.readthedocs.io/en/latest/

# reader = PdfFileReader(r"xxx.pdf")
# page = reader.pages[0]
# print(page.extract_text())


current_path = os.getcwd()
folder_old_pdf = 'path_file'
path_old_pdf = os.path.join(current_path, folder_old_pdf)

# ================ JOIN PDFs ====================

# new_folder = 'new'
# path_new_folder = os.path.join(path_old_pdf, new_folder)
# if not os.path.exists(path_new_folder):
#     os.makedirs(path_new_folder)
#
# new_pdf = PdfFileMerger()
# for root, dirs, files in os.walk(path_old_pdf):
#     for file in files:
#         full_path_file = os.path.join(root, file)
#         pdf_file = open(full_path_file, 'rb')
#         new_pdf.append(pdf_file)
#
# with open(f'{path_new_folder}/new_arc.pdf', 'wb') as new_file:
#     new_pdf.write(new_file)

# ================ SPLIT PDFs ====================

divisions = 2  # Any  to split file.

with open(r'arquivos_aula_150/new/new_arc.pdf', 'rb') as old_file:
    reader = PdfFileReader(old_file)
    num_pages_file = reader.getNumPages()
    pages_to_split = [0]
    for division in range(divisions, 0, -1):
        number_page = num_pages_file // division
        pages_to_split.append(number_page + pages_to_split[-1])
        num_pages_file -= number_page
    print(pages_to_split)
    for num_page in range(0, len(pages_to_split) - 1):
        writer = PdfFileWriter()
        for page in range(pages_to_split[num_page], pages_to_split[num_page + 1]):
            current_page = reader.getPage(page)
            writer.add_page(current_page)
        with open(f'arquivos_aula_150/new_file{num_page + 1}.pdf', 'wb') as new_pdf:
            writer.write(new_pdf)
        del writer
