# -*- coding = utf-8 -*-
# @time : 2021/7/22 16:42
# @Author : Jipeng Duan
# @File : unlock pdf.py
# @Software: PyCharm


import pikepdf

with pikepdf.open(r"C:\Users\1594649073\Desktop\atomic filament\\s41565-020-00789-w.pdf") as pdf:
    pdf.save(r"C:\Users\1594649073\Desktop\atomic filament\\2.pdf")