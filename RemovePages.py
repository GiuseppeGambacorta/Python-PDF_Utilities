import PyPDF2
import sys




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


pages_to_delete = [1,2,3,4]


if len(pages_to_delete) > len(in_file.pages):
    print('Pages to delete are more than pages in PDF')
    exit(1)

index_to_delete = [i-1 for i in pages_to_delete]
keep_pages = [page for i, page in enumerate(in_file.pages) if i not in index_to_delete]

for page in keep_pages:
     out_file.add_page(page)  


print(len(in_file.pages) - len(out_file.pages), 'pages to be deleted')




with open(out_fpath, 'wb') as f:
    out_file.write(f)