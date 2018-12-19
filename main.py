import sys

path_to_invoice = sys.argv[1]
import PyPDF2

pdfFileObj = open(path_to_invoice, "rb")
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages
print(pdfReader.numPages)
pageObj = pdfReader.getPage(0)
extracted_text = pageObj.extractText()


def extract_pvm_sum(data):
    result = data.split("21% PVM, EUR: ")[1].split("VISO ")[0]
    return result


pvm_sum = extract_pvm_sum(data=extracted_text)
print(pvm_sum)


def extract_pvm_moketojo_kodas(data):
    pass
