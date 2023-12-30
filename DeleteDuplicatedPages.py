import PyPDF2
import re, sys


def extract_text(pageObj):
    return re.sub('[\n\r\s]+', '', pageObj.extract_text())

length_of_input_args = len(sys.argv)

if length_of_input_args <=1:
    print('Also give a PDF filepath on which script will work\n')
    exit(1)
else:
    path_of_input_file= sys.argv[1]
    if length_of_input_args==3: # To give output file path
	    out_fpath = sys.argv[2]
    elif length_of_input_args==2:   # Replace the same file
	    out_fpath = path_of_input_file


in_file = PyPDF2.PdfReader(path_of_input_file, 'rb') 
out_file = PyPDF2.PdfWriter()


pages_to_delete = []
previuspage = in_file.pages[0]
previuos_page_text = extract_text(previuspage)


for page in in_file.pages[1:]:
    page_text = extract_text(page)
    if page_text.startswith(previuos_page_text):
        pages_to_delete.append(previuspage)

    previuos_page_text = page_text
    previuspage = page



pages_to_keep = [page for page in in_file.pages if page not in pages_to_delete]

print(len(pages_to_delete), 'pages to be deleted')
print(len(pages_to_keep), 'pages to be kept')

for page in pages_to_keep:
    out_file.add_page(page)  


with open(out_fpath, 'wb') as f:
    out_file.write(f)