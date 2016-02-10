import math
import statistics
import random


def flip_coin():      # Heads = 1; Tails = 0
    return random.randint(0, 1)

n = 16


def multi_flip(n):    # Heads = 1; Tails = 0; 2 to the power of 'n' flips
    head_count = 0
    tail_count = 0
    flip_count = 0
    bucket = []
    for i in range(2 ** n):
        result = flip_coin()
        flip_count += 1
        if result == 1:   # only 1 or 0 is possible (heads)
            head_count += 1
        else:
            tail_count += 1
        for x in range(n):
            if flip_count == (2 ** x):
                bucket.append((head_count, tail_count))  # adds tuple to list
    return bucket     # returns a list of flips at a given 2 to the n.

print(multi_flip(n))    # tuple of heads, tails


def simulation(default):     # Default setting 16
    # default = 16
    sim_dict = {}
    for p in range(default):
        sim_dict[p] = multi_flip(p)
    # return sim_dict
    for s in range(4):
        print(sim_dict[s])

simulation(default)
