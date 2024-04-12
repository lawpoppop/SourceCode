pdf_file_path           = 'C:\\law-doc\\toyata\\translation\\2014\\GB_20891_2014.pdf'
output_text_file_path   = 'C:\\law-doc\\toyata\\translation\\2014\\GB_20891_2014.txt'

from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

output_string = StringIO()
with open(pdf_file_path, 'rb') as in_file:
    parser = PDFParser(in_file)
    doc = PDFDocument(parser)
    rsrcmgr = PDFResourceManager()
    device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)

# Save the single line text to a text file
with open(output_text_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(output_string.getvalue())

print(f"Text saved to '{output_text_file_path}'")