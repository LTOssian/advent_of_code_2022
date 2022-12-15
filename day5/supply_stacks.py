"""
First answer is the letters that end up on top of each stack at the end of the procedure
"""
from collections import defaultdict

file = "input.txt"
def sort_input(file):
    with open(file) as file:
        lines = file.read()
    return lines.split('\n\n')

crates, instructions = sort_input(file)
sorted_crates = defaultdict(list)
sorted_crates2 = defaultdict(list)
for stack in crates.split('\n')[:-1][::-1]:
    i = 1
    while i < len(stack):
        if stack[i] != ' ':
            sorted_crates[(i+3)//4].append(stack[i])
            sorted_crates2[(i+3)//4].append(stack[i])
        i += 4
print(crates)

print(sorted_crates)

for moves in instructions.split('\n'):
    _, num, _, source, _, destination = moves.split(" ")
    num, source, destination = int(num), int(source), int(destination)

    for i in range(num):
        sorted_crates[destination].append(sorted_crates[source].pop())

answer1 = ''.join([x[-1] for x in sorted_crates.values()])
print(answer1)

"""
Second answer is the same thing but this time I must move crates all at once
"""

for moves in instructions.split('\n'):
    _, num, _, source, _, destination = moves.split(" ")
    num, source, destination = int(num), int(source), int(destination)

    sorted_crates2[destination].extend(sorted_crates2[source][-num:])
    sorted_crates2[source] = sorted_crates2[source][:-num]


answer2 = ''.join([x[-1] for x in sorted_crates2.values()])
print(answer2)

#discovered defaultdict() and extend() methods