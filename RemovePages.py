import PyPDF2
import sys


length_of_input_args = len(sys.argv)

if length_of_input_args == 1:
    print('Also give the original pdf file name and the ouput file name\n')
    exit(1)
elif length_of_input_args == 2:
    print('Also give  the output file name\n')
    exit(1)


input_file_name = sys.argv[1]
output_file_name = sys.argv[2]


in_file = PyPDF2.PdfReader(input_file_name, 'rb')
out_file = PyPDF2.PdfWriter()


pages_to_delete = [1, 2, 3, 4]

if len(pages_to_delete) > len(in_file.pages):
    print('Pages to delete are more than pages in PDF')
    exit(1)

index_to_delete = [i-1 for i in pages_to_delete]
pages_to_keep = [page for i, page in enumerate(in_file.pages) if i not in index_to_delete]

for page in pages_to_keep:
    out_file.add_page(page)


print(len(in_file.pages) - len(out_file.pages), 'pages deleted')


with open(output_file_name, 'wb') as f:
    out_file.write(f)
