pdf_file_path           = 'C:\\law-doc\\toyata\\translation\\2014\\GB_20891_2014.pdf'
output_text_file_path   = 'C:\\law-doc\\toyata\\translation\\2014\\GB_20891_2014.txt'
txt_file_path           = 'C:\\law-doc\\toyata\\translation\\2014\\GB_20891_2014-withNoAutoFix-TopPartRemoved.txt'

from PyPDF2 import PdfReader
import re, sys

def txtFile_to_str(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    return text
def pdfFile_to_str(filename):
    text=""
    with open(filename, 'rb') as file:
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

# *=0++ +=1++ ?=0/1
def remove_pattern(text): 
    pattern = r'([^\s])\n([^\s(])' #auto remove \n
    # print(re.search(pattern, text))
    text=re.sub(pattern, r'\1\2', text)
    pattern = r'([。；])([\s])*([^\n])' #auto add \n
    # print(re.search(pattern, text))
    text=re.sub(pattern, r'\1\n\3', text)
    pattern = r'\n(\d{1,2})?\s*([a-zA-Z]{1,2}|\d{1,2})(\.\d{1,2})+\s*' #remove 00 AA.00.00.00 #remove 00 00.00.00
    # print(re.search(pattern, text))
    text=re.sub(pattern, '\n', text)
    return text 

text="""
AA.1.2 line1。line2。   
2 BB.12.44 line3。line4；
3 A.1 line5。
9.1 line6。
A.1 line7。
line8-1
line8-2。
（1）line9-1。line9-2。
3.2 line 10
"""
# text = txtFile_to_str(txt_file_path)
# text = pdfFile_to_str(pdf_file_path)

text = remove_pattern(text)

print(text);sys.exit(); #test

# Save the single line text to a text file
with open(output_text_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(text)

print(f"Text saved to '{output_text_file_path}'")
