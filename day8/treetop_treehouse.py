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
        self.visible_trees = 0

    def get_visible_n(self):
        self.visible_trees = 0
        for x in range(self.x_):
            for y in range(self.y_):
                current_height = self.graphic[x, y]
                #print(current_height, x, y)

                #search to the left or the current row
                if y == 0 or np.amax(self.graphic[x, :y]) < current_height:
                    self.visible_trees += 1
                #search to the right of the current row
                elif y == self.y_ - 1 or np.amax(self.graphic[x, y+1:]) < current_height:
                    self.visible_trees += 1
                #search upward of the current col
                elif x == 0 or np.amax(self.graphic[:x, y]) < current_height:
                    self.visible_trees += 1
                #search downward of the current col
                elif x == self.x_ - 1 or np.amax(self.graphic[x+1:, y]) < current_height:
                    self.visible_trees += 1

forest = Map(parsed_forest)
forest.get_visible_n()
print(forest.visible_trees)