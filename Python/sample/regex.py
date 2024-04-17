import re

# https://regex101.com/
# By default all match is greedy (match as much as possible)
# By default backtrack matching - retry with start point char[n] --> char[n+1]
# to understand backtrack - use https://regex101.com/debugger
#   try reduce backtrack for failed match scenario
# Performance Up method - https://www.youtube.com/watch?v=L5Vqm-REhAU
#   use re.compile
#   instead of using + *, use {m,n}
#   use *?, +?, ?? Non greedy
#   dont use . use [^ ] instead of .* 
#   use Atomic grouping ?> - no backtrack
#     or possessive quantifier .*+ - no backtrack

# print(re.match('.', 'x'))                                     # . match any except \n
# print(re.findall('^a', '\nabc\na01',flags=re.MULTILINE))      # ^ start
# print(re.findall('foo.$', 'foo1\nfoo2\n',flags=re.MULTILINE)) # $ End
# print(re.findall('ab*', 'abbbb'))                             # * >=0
# print(re.findall('ab+', 'abbbb'))                             # + >=1 
# print(re.findall('ab?', 'abbbb'))                             # ? 0/1
# print(re.findall('(a{2})*', 'aaaa'))                          # matches any multiple of 2 'a' characters.
# print(re.findall('ab*bc', 'abbbbc'))                          # * + ? greedy
# print(re.findall('ab*?', 'abbbbc'))                           # *?, +?, ?? Non greedy
# print(re.findall('ab*+bc', 'abbbbc'))                         # *+, ++, ?+ no back-track
# print(re.findall('a{3,5}', 'aaaaaa'))                         # {m,n}
# print(re.findall('a{3,5}?', 'aaaaaa'))                        # {m,n}??
# print(re.findall('a{3,5}+aa', 'aaaaaa'))                      # {m,n}+?
# print(re.findall('\*.', '*a'))                                # \  escapes special characters
# print(re.findall('[a-z]', 'az'))                              # []  set of pattern
# print(re.findall('[^5-7]', 'a5678z'))                         # ^  not in set of characters
# print(re.findall('[A|B]', 'ABA'))                             # |  or non greedy
# print(re.findall(r'(abc)', 'abcABC'))                         # ()  capturing group
# print(re.findall(r'(?im:^abc)', 'abc\nABC'))                  # (?aiLmsux-imsx:...) i ignore case m multiline

# print(re.findall(r'\d+\w+', "123abc456def"))                  # ()  capturing group
# print(re.findall(r'(\d+)\w+', "123abc456def"))                
# print(re.findall(r'\d+(\w+)', "123abc456def"))                
# print(re.findall(r'(\d+)(\w+)', "123abc456def"))              

# print(re.findall(r'\w+\d+', "123abc456"))                     # (?>...) atomic unit, no backtrack
# print(re.findall(r'(?>\w+)\d+', "123abc456"))                 # (?>...) atomic unit, no backtrack, \w+ consume 456 and not allow \d+ to back track

# print(re.match(r'(?P<quote>["]).*(?P=quote)', "\"1a4\""))     # (?P<name>...) group name

txt = "FirstName FamilyName"
patternStr = "(?P<first>\w+) (?P<last>\w+)"
match=re.match(patternStr, txt)
print(match.group('last'))

pattern=re.compile(patternStr)
mo=pattern.search(txt)
print(mo.group("first"))
print(pattern.sub(r"\2, \1", txt))