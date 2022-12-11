#Calorie Counting
"""
Puzzle input will be the number of calories each Elf carries
"""

# Read the input file, separate each line for an item and each paragraph for an Elf's inventory 
file = 'input.txt'

def get_input(input_file):
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

elfs_inventories = get_input(file)

def get_highest_calories(inventories):
    highest_calories = 0
    for inventory in inventories:
        current_calories = 0
        for calories in inventory:
            current_calories += calories
        if current_calories > highest_calories:
            highest_calories = current_calories
    return highest_calories

answer = get_highest_calories(elfs_inventories)
print(answer)