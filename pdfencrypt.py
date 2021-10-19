# -*- coding = utf-8 -*-
# @time : 2021/7/10 15:55
# @Author : 段吉鹏
# @File : pdfencrypt.py
# @Software: PyCharm


from PyPDF2 import PdfFileReader, PdfFileWriter

path = r"C:\\Users\\1594649073\\Desktop\\2021.10.7 Au NPs\\AccuReD_High_Accuracy_Training_of_CNNs_on_ReRAM_GPU_Heterogeneous_3-D_Architecture.pdf"

pdf_reader = PdfFileReader(path, 'rb')
page_counts = pdf_reader.getNumPages()
pdf_writer = PdfFileWriter()
for i in range(page_counts):
    pdf_writer.addPage(pdf_reader.getPage(i))

pdf_writer.encrypt("123")
with open(r"C:\\Users\\1594649073\\Desktop\\" + "encrypt2.pdf", "wb") as out:
    pdf_writer.write(out)