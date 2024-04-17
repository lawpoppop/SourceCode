import re

pattern = re.compile(r'(?>\d+)(\w+)')
text = "123abc456def"

match = pattern.search(text)
if match:
    print("Match found:", match.group(1))
else:
    print("No match found")
