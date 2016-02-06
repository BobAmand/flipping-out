import math
import statistics
import random

default = 16


def flip_coin():      # Heads = 1; Tails = 0
    return random.randint(0, 1)


def multi_flip(n):    # Heads = 1; Tails = 0; 2 to the power of 'n' flips
    bucket = []
    for i in range(2**n):
        bucket.append(flip_coin())
    return bucket     # returns a list of flips at a given 2 to the n.


def simulation(default):     # Default setting 16
    # default = 16
    sim_dict = {}
    for p in range(default):
        sim_dict[p] = multi_flip(p)
    # return sim_dict
    for s in range(4):
        print(sim_dict[s])

simulation(default)
