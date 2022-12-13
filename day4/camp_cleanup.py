"""
Puzzle answer is how many pairs fully override each other
"""
file = "input.txt"

def sort_input(file):
    with open(file) as file:
        inputs = file.read()
    return [line.split(',') for line in inputs.split('\n')]
pairs_list = sort_input(file)

def check_override(pair1, pair2):
    pair1 = pair1.split('-')
    pair2 = pair2.split('-')
    check_list1 = []
    check_list2 = []
    for i in range(int(pair1[1]) - int(pair1[0]) + 1):
        check_list1.append(int(pair1[0]) + i)
    for i in range(int(pair2[1]) - int(pair2[0]) + 1):
        check_list2.append(int(pair2[0]) + i)

    contained = 0
    for num in check_list1:
        if num in check_list2:
            contained += 1
    if contained == len(check_list2) or contained == len(check_list1):
        return 1
    else:
        return 0

def open_pairs(pairs_list):
    n_fully_contained = 0
    for both_pair in pairs_list:
        pair1, pair2 = both_pair
        n_fully_contained += check_override(pair1, pair2)
    return n_fully_contained

print(open_pairs(pairs_list)) #first answer

"""
Second part answer is how many pairs override (not fully) each other
"""

def count_overlaps(pairs_list):
    count = 0
    for pair in pairs_list:
        first_pair, second_pair = pair
        overlap = False
        for num in range(int(first_pair.split('-')[0]), int(first_pair.split('-')[1]) + 1):
            if num in range(int(second_pair.split('-')[0]), int(second_pair.split('-')[1]) +1):
                overlap = True
            else: 
                continue
        if overlap == True:
            count += 1
        else:
            continue
    return count
print(count_overlaps(pairs_list))