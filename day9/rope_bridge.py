"""

"""
from collections import defaultdict
file = 'example.txt'

def sort_input(file):
    with open(file) as f:
        file = f.read().strip().split('\n')
    return file

commands = sort_input(file)
commands_parsed = defaultdict(list)
for line in commands:
    commands_parsed[line[0]].append(int(line[-1]))
print(commands)
