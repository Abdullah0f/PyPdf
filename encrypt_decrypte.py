from PyPDF2 import PdfReader, PdfWriter
reader = PdfReader("file1.pdf")
writer = PdfWriter()

# add all pages to writer
for page in reader.pages:
    writer.addPage(page)

# add password
writer.encrypt("password")

with open("encrypted.pdf", 'wb') as f:
    writer.write(f)

# decrepyt
reader = PdfReader("encrypted.pdf")
writer = PdfWriter()

if reader.is_encrypted:
    reader.decrypt("password")

for page in reader.pages:
    writer.addPage(page)
with open("decrypted.pdf", 'wb') as f:
    writer.write(f)
