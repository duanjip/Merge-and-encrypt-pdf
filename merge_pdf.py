# -*- coding = utf-8 -*-
# @time : 2021/10/7 17:58
# @Author : Jipeng Duan
# @File : merge_pdf.py
# @Software: PyCharm


import os
from PyPDF2 import  PdfFileReader, PdfFileWriter

path = r"C:\Users\1594649073\Desktop\2021.10.7 Au NPs"
file = [i for i in os.listdir(path) if i.endswith('.pdf')]
file_path = [os.path.join(path, file_name) for file_name in file]

output = PdfFileWriter()
outputPages = 0
for pdf in file_path:
    input = PdfFileReader(open(pdf, 'rb'))
    pageCount = input.getNumPages()
    # print(pageCount)
    # outputPages += pageCount
    for i in range(pageCount):
        output.addPage(input.getPage(i))
output.encrypt('duanjipeng')
with open(r"C:\Users\1594649073\Desktop\merge.pdf", 'wb') as outputfile:
    output.write(outputfile)