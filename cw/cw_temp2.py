import re

input_str = input('> ')
pattern = input('pattern: ')
answer = []
occ = 0
tmp = re.findall(pattern,input_str)
for i in range(len(tmp)):
    ans = re.search(pattern, input_str).span()
    occ += 1
    input_str = input_str[ans[1]:]
    answer.append(ans)
print(occ)
print(answer)