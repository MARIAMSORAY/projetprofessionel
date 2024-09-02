import random

def random_blocked_cells(num_blocked=3):
    all_cells = [(i, j) for i in range(5) for j in range(5)]
    return random.sample(all_cells, num_blocked)
