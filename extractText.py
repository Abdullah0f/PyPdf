import PyPDF2 as p
# extract text from pdf file
reader = p.PdfReader("file1.pdf")
for i, page in enumerate(reader.pages):
    print('Page: '+str(i), end="\n\n")
    print(page.extract_text())
    print('---------------------------\n\n\n')
