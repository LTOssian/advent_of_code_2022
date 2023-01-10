"""
Comme d'hab, bon courage mon sang. A demain soir // sike, ca fait 3 semaines haha 
"""
import numpy as np

file = "input.txt"

def sort_input(file):
    with open(file) as f:
        file = f.read().split()
    return [list(map(int, list(line))) for line in file] 

parsed_forest = sort_input(file) # we get a xy graphic with a tree at each coordinate

class Map:
    def __init__(self, parsed_forest):
        self.x_ = len(parsed_forest)
        self.y_ = len(parsed_forest[0])

        self.graphic = np.array(parsed_forest) #numpy array is the best way I found to visualize and access coordinates
        self.visible_trees = self.get_visible_trees()
        self.highest_scenic = self.get_highest_scenic()

    def get_visible_trees(self):
        visible_trees = 0
        for x in range(self.x_):
            for y in range(self.y_):
                current_height = self.graphic[x, y]
                #print(current_height, x, y)

                #search to the left or the current row
                if y == 0 or np.amax(self.graphic[x, :y]) < current_height:
                    visible_trees += 1
                #search to the right of the current row
                elif y == self.y_ - 1 or np.amax(self.graphic[x, y+1:]) < current_height:
                    visible_trees += 1
                #sear
                # ch upward of the current col
                elif x == 0 or np.amax(self.graphic[:x, y]) < current_height:
                    visible_trees += 1
                #search downward of the current col
                elif x == self.x_ - 1 or np.amax(self.graphic[x+1:, y]) < current_height:
                    visible_trees += 1
        return visible_trees

    def get_highest_scenic(self):
        highest_scenic = 1

        for x in range(1, self.x_ - 1):
            for y in range(1, self.y_ - 1):
                #print(f"coordonnées : {x},{y}")
                current_scenic = 1
                current_height = self.graphic[x, y]
                #print(f"current height is {current_height}")
                cardinal = [self.graphic[:x, y][::-1], self.graphic[x, y+1:], self.graphic[x+1:, y], self.graphic[x, :y][::-1]]
                for dir in cardinal:
                    count = 0
                    for tree_height in dir:
                        count += 1
                        #print(count, dir, current_scenic)
                        if tree_height >= current_height or len(dir) == count:
                            current_scenic *= count
                            break
                #print(current_scenic)
                if current_scenic > highest_scenic:
                    highest_scenic = current_scenic
        return highest_scenic                 

forest = Map(parsed_forest)
print(forest.visible_trees)
print(forest.highest_scenic)