"""
Answer is the index of the character at which, given the sequence n,
is unique compared to the {sequence - 1} next characters
"""
file = "input.txt"
def sort_input(file):
    with open(file) as f:
        file = f.read()
    return file

datastream = sort_input(file)

from collections import defaultdict
class System:
    
    first_marker_signal = 0

    def __init__(self, datastream, sequence): #datastream: string and sequence: int
        self.datastream = datastream
        self.sequence = sequence

#checks if the first marker appears in this sequence
    def isMarker(self, sequence):
        for char in sequence:
            if sequence.count(char) > 1:
                return False
        return True

#returns the position of the first marker
    def detect_signal(self):
        sliced_data = defaultdict(str)
        i = 0
        while i < len(self.datastream):
            if len(self.datastream[i:i+self.sequence]) < 4:
                break
            sliced_data[i] += (self.datastream[i:i+self.sequence])
            i += 1
        print(sliced_data)

        for key, value in sliced_data.items():
            if self.isMarker(value):
                self.first_marker_signal = key + self.sequence
                return self.first_marker_signal

answer1 = System(datastream, 4)
answer1.detect_signal()
print(answer1.first_marker_signal)

answer2 = System(datastream, 14)
answer2.detect_signal()
print(answer2.first_marker_signal)