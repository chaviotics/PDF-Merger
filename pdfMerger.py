import PyPDF2
import sys

# sample input:
# python pdfMerger.py dummy.pdf tilt.pdf twopage.pdf wtr.pdf {sample inputs}

inputs = sys.argv[1:] # grabs all the arguments

def pdf_merger(pdf_list):
    for pdf in pdf_list:
        print(pdf)

pdf_merger(inputs)

