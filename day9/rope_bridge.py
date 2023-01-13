"""
1 week later, t'abuses
"""
file = 'input.txt'

def sort_input(file):
    with open(file) as f:
        file = f.read().strip().split('\n')
    return [i[0] for i in file], [int(j[2:]) for j in file]
moves, values = sort_input(file)
coords = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1)
}

class Rope:
    def __init__(self, rope_size, moves, values):
        self.rope_size = rope_size
        self.moves = moves
        self.values = values
        self.motions = self.get_motions()
        self.visited_by_tail = self.visited_by_tail()

    def get_motions(self):
        motions = list()        
        for index in range(len(self.values)):
            for iterate in range(self.values[index]):
                motions.append([coords[self.moves[index]][0], coords[self.moves[index]][1]])
        return motions

    def visited_by_tail(self):
        x_init = [0] * self.rope_size
        y_init = [0] * self.rope_size
        visited = {(x_init[-1], y_init[-1])}
        for position in self.motions:
            _x, _y = position[0], position[1]
            x_init[0] += _x
            y_init[0] += _y
            for i in range(self.rope_size - 1):
                distance_x = x_init[i + 1] - x_init[i]
                distance_y = y_init[i + 1] - y_init[i]
                if abs(distance_x) == 2 or abs(distance_y) == 2:
                    x_init[i + 1] = x_init[i] + int(distance_x/2)
                    y_init[i + 1] = y_init[i] + int(distance_y / 2)
            visited.add((x_init[-1], y_init[-1]))
        return len(visited)

rope_bridge = Rope(2, moves, values)
print(rope_bridge.visited_by_tail)
longer_rope = Rope(10, moves, values)
print(longer_rope.visited_by_tail)