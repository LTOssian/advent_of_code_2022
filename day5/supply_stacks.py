"""
First answer is the letters that end up on top of each stack at the end of the procedure
"""
file = "input.txt" #I altered it to have room at the top, otherwise it doesn't work. Will refactor someday

def sort_stack(stack):
    new_stack = [stack[i] + stack[i+1] + stack[i+2] for i in range(0, len(stack), 4)]
    return new_stack

def sort_input(file):
    with open(file) as file:
        inputs = file.read()
        print(inputs)
    stacks, procedure = inputs.split('\n\n')
    stacks = [stack for stack in stacks.split('\n') if stack != stacks.split('\n')[-1]]

    print(stacks)
    sorted_stack = [sort_stack(stack) for stack in stacks]
    print(sorted_stack)
    sorted_procedure = [[i.split()[1], i.split()[3], i.split()[5]] for i in procedure.split('\n')]
    print(sorted_procedure)
    return sorted_stack, sorted_procedure

def proceed(stacks, procedure):
    count = 0
    for step in procedure:
        print(procedure.index(step))
        moves, move_from, move_to = step 
        for a_line in stacks:
            if count == int(moves):
                break
            if a_line[int(move_from)-1] != '   ':
                
                reversed_stack = [x for x in stacks]
                reversed_stack.reverse()
                for line in reversed_stack:
                    if line[int(move_to)-1] != '   ':
                        continue
                    else:
                        count += 1
                        line[int(move_to)-1] = a_line[int(move_from)-1]
                        a_line[int(move_from)-1] = '   '
                        break
        print(count) 
        count = 0
        for e in stacks:
            print(e)

usable_stack, usable_procedures = sort_input(file)
proceed(usable_stack, usable_procedures)            

"""
Second answer is the letters that end up on top,
but the arrangement has to move every item at once instead of one at a time.
"""