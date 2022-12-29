import re

input_str = input('> ')
pattern = input('pattern: ')
answer = re.findall(pattern, input_str)
print(f'{pattern} occurred {len(answer)} times in input')