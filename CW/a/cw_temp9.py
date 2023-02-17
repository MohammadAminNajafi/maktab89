import re

num = input()
result = re.finditer(r'\d+', num)
for i in result:
    print(i.span(), i.group())