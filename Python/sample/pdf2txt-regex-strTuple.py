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

def remove_pattern(text): 
    pattern = r'([^。；：])(\n)([^\s])' #auto remove \n
    # print(re.search(pattern, text))
    text=re.sub(pattern, r'\1\3', text)
    pattern = r'([。；：])([\s])*([^\n（])' #auto add \n
    # print(re.search(pattern, text))
    text=re.sub(pattern, r'\1\n\3', text)
    pattern = r'\n(\d{1,2})?\s*([a-zA-Z]{1,2}|\d{1,2})(\.\d{1,2})+\s*' #remove 00 AA.00.00.00 #remove 00 00.00.00
    # print(re.search(pattern, text))
    text=re.sub(pattern, '\n', text)
    return text 

def remove_pattern_new(text): 
    # print("----------")
    # print("Before:"+text)
    # pattern = r'^(\(1\))' #auto add \n
    # print(re.search(pattern, text))

    patternStart1 = r'^(（\d+）)' # detect non paragraph line start with (\d)
    patternStart2 = r'^(\d{1,2}\s)' # detect non paragraph line start with (\d)
    patternStart2 = r'^(\d{1,2}\s)' # detect non paragraph line start with (\d)
    patternStart3 = r'^(\d{1,2})?\s*([a-zA-Z]{1,2}|\d{1,2})(\.\d{1,2})+\s*' #line start with 00 AA.00.00.00 #remove 00 00.00.00
    # print(re.search(pattern, text))
    if not(re.search(patternStart1, text) or re.search(patternStart2, text) or re.search(patternStart3, text)): #skip add remove \n for non paragraph line
        # pattern = r'([^。；：])(\n)([^\s\n])' #auto remove \n
        # # print(re.search(pattern, text))
        # text=re.sub(pattern, r'\1\3', text)
        
        pattern = r'([。；：])([\s])*(.+)' #auto add \n
        # print(re.search(pattern, text))
        text=re.sub(pattern, r'\1\n\3', text)
    else:
        text+="\n"

    # pattern = r'^(\d{1,2})?\s*([a-zA-Z]{1,2}|\d{1,2})(\.\d{1,2})+\s*' #remove 00 AA.00.00.00 #remove 00 00.00.00
    # # print(re.search(pattern, text))
    # text=re.sub(pattern, '', text)

    # print("After:"+text)
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
text = pdfFile_to_str(pdf_file_path)

outText=text.split('\n')
combineLine=""
for line in outText:
    combineLine += remove_pattern_new(line)
    # print("Combined:"+combineLine)

# print(combineLine);sys.exit(); #test

# Save the single line text to a text file
with open(output_text_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(combineLine)

print(f"Text saved to '{output_text_file_path}'")
