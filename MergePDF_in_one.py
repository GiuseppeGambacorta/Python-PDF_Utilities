import PyPDF2
import sys
import os

length_of_input_args = len(sys.argv)
if length_of_input_args <=1:
    print('Also give a folder path on which script will work\n')
    exit(1)


folder_path = sys.argv[1]
files = os.listdir(folder_path)
pdf_files = [file for file in files if file.endswith('.pdf')]
pdf_files = [os.path.join(folder_path, file) for file in pdf_files]

pdf_files.sort(key=os.path.getmtime)

out_file = PyPDF2.PdfWriter()
for file in pdf_files:
    in_file = PyPDF2.PdfReader(file, 'rb')
    for page in in_file.pages:
        out_file.add_page(page)


output_path = os.path.join(folder_path, 'Merged.pdf')
with open(output_path, 'wb') as f:
    out_file.write(f)