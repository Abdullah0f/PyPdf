import PyPDF2

with open("file1.pdf", 'rb') as file:  # 'rb' = read binary and its necessary
    # reader = PyPDF2.PdfReader("file1.txt")#you can use this to read the file without (open)
    reader = PyPDF2.PdfFileReader(file)  # read file
    print(reader.numPages)
    page = reader.getPage(0)  # page = pageobject of page1
    page.rotate_clockwise(90)  # rotate 90 degrees
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)  # add page1 after rotation at the end
    writer.insertBlankPage(page)  # insert a blank page at the beginning
    with open("file2.pdf", 'wb') as file2:  # wb is neccessary
        writer.write(file2)

    merger = PyPDF2.PdfFileMerger()
    file_tobe_merged = ["file1.pdf", "file2.pdf"]
    for _file in file_tobe_merged:  # itterate over files tobe merged
        merger.append(_file)  # append files in the merger
    merger.write("combined.pdf")  # write whats in merger in combined.pdf
