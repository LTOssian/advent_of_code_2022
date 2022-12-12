"""
Puzzle answer is the sum of the  priorities of items that appears twice in a line
"""
import string

file = 'input.txt'
#sort the input, separate each line as an element of a list
def sort_input(file):
    with open(file) as file:
        inputs = file.read()
    return [rucksack for rucksack in inputs.split('\n')]

rucksack_inventory = sort_input(file)

priorities = dict()
for char in string.ascii_letters:
    priorities[char] = string.ascii_letters.index(char) + 1

def check_items(bag1, bag2):
    for key, value in priorities.items():
        if key in bag1 and key in bag2:
            return value            
def get_priority_score(inventory):
    priority_score = 0
    for bags in inventory:
        first_bag = bags[:int(len(bags)/2)]
        second_bag = bags[int(len(bags)/2):]
        priority_score += check_items(first_bag, second_bag)
    return priority_score

print(get_priority_score(rucksack_inventory))