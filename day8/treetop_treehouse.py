"""
Comme d'hab, bon courage mon sang. A demain soir
"""

file = "example.txt"

def sort_input(file):
    with open(file) as f:
        file = f.read().split('\n')
    return file
