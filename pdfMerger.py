import PyPDF2
import sys

# sample input:
# python pdfMerger.py dummy.pdf tilt.pdf twopage.pdf wtr.pdf {sample inputs}

inputs = sys.argv[1:] # grabs all the arguments

def pdf_merger(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(f'Merged {pdf}')
        merger.append(pdf)

    merger.write('Merged PDFs.pdf')

pdf_merger(inputs)



