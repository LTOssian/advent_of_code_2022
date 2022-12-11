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
    index = 0
    for inventory in inventories:
        current_calories = sum(inventory)
        if current_calories > highest_calories:
            highest_calories = current_calories
            index = inventories.index(inventory)
    return highest_calories, index

top_carrying_elf, index_of_highest = get_highest_calories(elfs_inventories)
print(top_carrying_elf, index_of_highest) #first_answer

"""
Answer to the second part will be the sum of the 3 highest calories carried by elves
"""
# uses list comprehension to create a new lists without the previous highest carrying elf 

second_list = [x for x in elfs_inventories if elfs_inventories.index(x) != index_of_highest]
second_carrrying_elf, index_of_second = get_highest_calories(second_list) 

third_list = [x for x in second_list if second_list.index(x) != index_of_second]
third_carrying_elf, index_of_third = get_highest_calories(third_list) 

print(top_carrying_elf + second_carrrying_elf + third_carrying_elf) #second_answer