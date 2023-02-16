import re

y = []
CW = re.compile(r'([A-Z][a-zâ]*)')

with open('iran.txt') as f:
    text = f.read()

x = CW.findall(text)
for i in range(len(x)):
    if x[i] not in y:
        y.append(x[i])

for i in y:
    print(i)