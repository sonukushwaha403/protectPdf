from PyPDF2 import pdfFileWriter, PdfFileReader
pdf_file_path="path of file"
pdf_file_path_encrypted="Path of encrypted file"
pdfwriter=PdfFileWriter()
pdf=PdfFileReader(pdf_file_path)

for page_num in range(pdf.numPages):
    pdfwriter.addPage(pdf.getPage(page_num))

password="FOLLOW"
pdfwriter.encrypt(password)

with open(pdf_file_path_encrypted,'wb') as f:
    pdfwriter.write(f)
    f.close()
