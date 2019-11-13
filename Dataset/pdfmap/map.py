# from tika import parser
import PyPDF2 as p2
import os
path = "C:/Users/karin/OneDrive/Desktop/rb/pdfmap/pdf"
teststring = "hi there (everyone will get better"
pdfmap = []
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.pdf' in file:
            files.append(os.path.join(r, file))

for f in files:
    # print(f)

#PDFpy2
    PDFfile = open(f,"rb")
    pdfr =  p2.PdfFileReader(PDFfile)
    x = pdfr.getPage(0)
    #print(x.extractText())
    y = x.extractText()[102:138]
    if y in pdfmap:
        # pdfmap.append(y)
        print(teststring)
    else:
        # print(teststring)
        print(y)
        pdfmap.append(y)
# print(len(pdfmap))
# test = "(F,K,E,I)(R,M,T,O)(P,R,N,T)(O,I,Q,K)"
# print(test in pdfmap)
# print(test)