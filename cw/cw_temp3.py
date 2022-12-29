import re

input_str = input('> ')
ans1 = re.sub('\s', '_', input_str)
ans = ''
for i in range(len(input_str)):
    if input_str[i] == '_'and input_str[i] == ans1[i]:
        ans += ' '
    else:
        ans += ans1[i]
print(ans)