#Calorie Counting
"""
Puzzle answer will be the highest number of calories is carried among the elves
"""

file = 'input.txt'

# sorts the input, separating each elf as an index with a list as its value
# and including all its items in the list 
#returns the list
def sort_input(input_file):
    with open (input_file) as file:
        inputs = file.readlines()
    storage = [[]]

    elf_counter = 0
    for line in inputs:
        if line == '\n':
            storage.append([])
            elf_counter += 1
        else:
            storage[elf_counter].append(int(line.strip('\n')))
    return storage

elfs_inventories = sort_input(file)

def get_highest_calories(inventories):
    highest_calories = 0
    for inventory in inventories:
        current_calories = sum(inventory)
        if current_calories > highest_calories:
            highest_calories = current_calories
    return highest_calories

answer = get_highest_calories(elfs_inventories)
print(answer)