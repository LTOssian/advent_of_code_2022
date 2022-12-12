"""
Puzzle answer if the total score if a rps game
"""
file = 'input.txt'

#dict to identify the keyword corresponding to the input
rules = {
    'rock':  ['A', 'X'],
    'paper': ['B', 'Y'],
    'scissors': ['C','Z']
}
#dict to identify the wkeaness of the key
win_conditions = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}

#dict to identify the points given for each keyword
keywords_to_points = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}

#sort the input, separate each games and each opponents inputs
def sort_input(file):
    with open (file) as file:
            inputs = file.read()

    return [x.split() for x in inputs.split('\n')]

strategy_guide = sort_input(file)

#checks if the key value corresponds to a win or a loss, else its a draw -> returns the score according to the result
def score_checker(opponent_choice, elf_choice):
    keyword_points = keywords_to_points[elf_choice]
    if win_conditions[opponent_choice] == elf_choice:
        return 0 + keyword_points
    elif win_conditions[elf_choice] == opponent_choice:
        return 6 + keyword_points
    else:
        return 3 + keyword_points

#sum the total score for every game
def total_points(games_history):
    score = 0
    for game in games_history:
        opponent_choice, elf_choice = game
        #this loop swaps the letter for the keyword to access the dicts in score_checker()
        for key, value in rules.items():
            if opponent_choice in value:
                opponent_choice = key
            if elf_choice in value:
                elf_choice = key

        score += score_checker(opponent_choice, elf_choice)
    return score

print(total_points(strategy_guide)) #first_answer

"""
Answer to the second part is the total score, 
this time reading the file's second column as the way to end the game : X as win, Y as draw and Z as lose
"""
new_rules = {
    'rock': 'A',
    'paper': 'B',
    'scissors': 'C'
}
strategy_conditions = {
    'win' : 'Z',
    'lose' : 'X',
    'draw' : 'Y'
}
 # ex for A Y, opponent chooses rock and I need to draw, so I chose rose 
def new_total_points(games_history):
    score = 0
    for game in games_history:
        opponent_choice, elf_strategy = game
        opponent_choice, elf_choice = strategy_handler(opponent_choice, elf_strategy)
        score += score_checker(opponent_choice, elf_choice)
    print(score)
    
def strategy_handler(opponent_choice, strategy):
    for key, value in new_rules.items():
        if opponent_choice == value:
            opponent_choice = key
    for key, value in strategy_conditions.items():
        if strategy == value:
            strategy = key
    #at this point we have the opponent's choice and what the user must do
    #print(opponent_choice, strategy)
    if strategy == 'lose':
        elf_choice = win_conditions[opponent_choice]
    elif strategy == 'win':
        for key, value in win_conditions.items():
            if opponent_choice == value:
                elf_choice = key
    else:
        elf_choice = opponent_choice
    return opponent_choice, elf_choice

new_total_points(strategy_guide)