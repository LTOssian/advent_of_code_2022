"""
Bon courage Louisan du futur, si tu finis ça ce soir c'est goldé.
The goal is to find the sum of the total sizes of those directories
"""
from collections import defaultdict

file = 'input.txt'

def sort_input(file):
    with open(file) as f:
        file = f.read()
    return [x for x in file.split('\n')]

lines = sort_input(file)

class FileSystem:
    files_size = defaultdict(int)
    max_usable_space = 70000000 - 30000000
    def __init__(self, commands, limit): 
        self.commands = commands
        self.limit = limit

    def sort_system(self):
        current_path = []
        for line in self.commands:
            keyword = line.strip().split()
            #print(keyword)
            if keyword[0] == '$' and keyword[1] == 'cd':
                if keyword[2] == '..':
                    current_path.pop()
                else:
                    current_path.append(keyword[2])
            elif (keyword[0] == '$' and keyword[1] == 'ls') or keyword[0] == 'dir':
                continue
            else: #at this point, it can only be (size, fileName)
                size = int(keyword[0])
                for i in range(1, len(current_path) + 1):
                    self.files_size['/'.join(current_path[:i])] += size
        print(self.files_size)
#get the sum of all of the directories with a total size of at most {self.limit}
    def get_answer(self):
        sum = 0
        for dir, t_size in self.files_size.items():
            if t_size <= self.limit:
                sum += t_size
        return sum


#we want to free at least 3000000000 of space so that the system can run
    def get_free_space(self):
        #total space of the system - the total space i can use not to break the system
        current_space_to_free = self.files_size['/'] - self.max_usable_space

        min_space_to_delete = self.files_size['/']
        for dir, t_size in self.files_size.items():
            if t_size >= current_space_to_free and t_size < min_space_to_delete:
                min_space_to_delete = t_size
        return min_space_to_delete

elf_device = FileSystem(lines, 100000)
elf_device.sort_system()
answer1 = elf_device.get_answer()
print(answer1)
answer2 = elf_device.get_free_space()
print(answer2)