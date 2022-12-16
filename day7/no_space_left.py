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
                print(current_path, size)
                for i in range(1, len(current_path)+1):
                    self.files_size['/'.join(current_path[:i])] += size

#get the sum of all of the directories with a total size of at most {self.limit}
    def get_answer(self):
        sum = 0
        for dir, t_size in self.files_size.items():
            if t_size <= self.limit:
                sum += t_size
        return sum
answer1 = FileSystem(lines, 100000)
answer1.sort_system()
print(answer1.get_answer())