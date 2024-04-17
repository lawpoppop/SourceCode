pdf_file_path           = 'C:\\law-doc\\toyata\\translation\\2014\\GB_20891_2014.pdf'
output_text_file_path   = 'C:\\law-doc\\toyata\\translation\\2014\\GB_20891_2014.txt'

txt_file_path           = 'C:\\law-doc\\toyata\\translation\\2014\\GB_20891_2014-withNoAutoFix-TopPartRemovedxxx.txt'

# pdf_file_path           = 'C:\\law-doc\\toyata\\translation\\2020\\GB_20891_amd2020.pdf'
# output_text_file_path   = 'C:\\law-doc\\toyata\\translation\\2020\\GB_20891_amd2020.txt'

from PyPDF2 import PdfReader
import re, sys

def read_txt_to_string(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read()
    return data

def pdf_to_text(pdf_file_path):
    text = ""
    with open(pdf_file_path, 'rb') as file:
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def char_equals_breakLineChar(char):
    return char == '。' or char == '；'

def remove_newline_except_before_space(input_str): #combine 2 lines to 1 paragraph
    output_str = ''
    for i in range(len(input_str)):
        # print(str(i)+" " +input_str[i]+" "+str(char_equals_breakLineChar(input_str[i])))
        if i>len(input_str)-2: #handle error for last character
            output_str += input_str[i]
            break
        if input_str[i] == '\n' and not(char_equals_breakLineChar(input_str[i - 1])) and not(input_str[i-1] == ' ')and not(input_str[i+1] == ' '): #delete not needed \n
            continue
        # if input_str[i] == '。' and input_str[i + 1] == '\n':#skip if correct line break
        #     output_str += input_str[i]
        #     continue
        if char_equals_breakLineChar(input_str[i]) and input_str[i + 1] != '\n' and input_str[i + 2] != '\n' and input_str[i + 3] != '\n'  and input_str[i + 4] != '\n' :#auto line break
            output_str += input_str[i] + '\n'
            i+=1
        else:
            output_str += input_str[i]
    return output_str


def remove_pattern(text): 
    # pattern = r'\n[a-zA-Z]{1,2}(\.\d{1,2})+' #remove AA.00.00.00
    pattern = r'\n(\d{1,2})?\s*[a-zA-Z]{1,2}(\.\d{1,2})+' #remove AA.00.00.00
    text=re.sub(pattern, '\n', text)
    pattern = r'\n(\d{1,2})?\s*\d{1,2}(\.\d{1,2})+' #remove 00.00.00
    # pattern = r'\n*\s\d{1,2}(?:\.\d{1,2})+(?:\.\d{1,2})?' #remove 00.00.00
    text=re.sub(pattern, '\n', text)
    return text 

def replace_multiple_spaces_with_single_newline(text): #replace_multiple_spaces for \n
    pattern = r'\s*\n'
    return re.sub(pattern, '\n', text)

def remove_multiple_spaces(text):
    text = re.sub(r'\s*[，]\s*', '， ', text)
    text = re.sub(r'\s*[,]\s*', ', ', text)
    text = re.sub(r'\s+[。]\s+', '。', text)
    return text

def paragraphs_to_single_line(text):
    text = remove_newline_except_before_space(text)
    text = remove_pattern(text)
    # text = replace_multiple_spaces_with_single_newline(text)
    # text = remove_multiple_spaces(text)
    return text

# #test
# pdf_text=""" 
# AA.1.2 line1。line1.2。
# 2 BB.12.44 line2。line1.2；
# 3 A.1 line3。
# 9.1 line4。
# A.1 line5。
# """

# pdf_text = read_txt_to_string(txt_file_path)
pdf_text = pdf_to_text(pdf_file_path)
pdf_text = paragraphs_to_single_line(pdf_text)

# print(pdf_text) #test
# sys.exit()

# Save the single line text to a text file
with open(output_text_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(pdf_text)

print(f"Text saved to '{output_text_file_path}'")