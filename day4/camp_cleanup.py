"""
Puzzle answer 
"""
file = "input.txt"

def sort_input(file):
    with open(file) as file:
        inputs = file.read()
    return [line.split(',') for line in inputs.split('\n')]
pairs_list = sort_input(file)
print(pairs_list)
ex = [['67-83','68-84']]

def check_override(pair1, pair2):
    pair1 = pair1.split('-')
    pair2 = pair2.split('-')
    check_list1 = []
    check_list2 = []
    for i in range(int(pair1[1]) - int(pair1[0]) + 1):
        check_list1.append(int(pair1[0]) + i)
    for i in range(int(pair2[1]) - int(pair2[0]) + 1):
        check_list2.append(int(pair2[0]) + i)
    print(check_list1, check_list2)

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
print(open_pairs(pairs_list))

