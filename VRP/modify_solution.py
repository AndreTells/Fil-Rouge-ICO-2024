import random

# swaps n nodes the place of n nodes in the path
def rand_opt_n(path, num_of_nodes, n=1):
    new_state = path[:] # fastest way to copy a list in python
    for k in range(n):
        i = int((num_of_nodes-1) * random.random()) + 1 # generate a random number between 1 and num_of_nodes
        j = int((num_of_nodes-1) * random.random()) + 1 # generate a random number between 1 and num_of_nodes

        new_state[i], new_state[j] = new_state[j], new_state[i]

    return new_state

# randomly chooses a section of the path and reverses it
def rand_reverse_section(path, num_of_nodes):
    i = int((num_of_nodes-1) * random.random()) + 1 # generate a random number between 1 and num_of_nodes
    j = min(i + int((num_of_nodes-1) * random.random()) + 1, num_of_nodes)# generate a random number between 1 and num_of_nodes

    path_slice = list(reversed(path[i:j]))
    new_path = path[:i]+ path_slice+ path[j:]

    return new_path

# uses the rand_opt_n and rand_reverse_section at random (50% each)
def combined_rand_modification(path, num_of_nodes):
    decider = random.random()
    if(decider >=0.5):
        return rand_opt_n(path,num_of_nodes)

    return rand_reverse_section(path, num_of_nodes)
