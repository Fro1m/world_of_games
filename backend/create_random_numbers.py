import random

'''Creates random numbers'''

def render(amount):
    randoms_list = []
    for numbers in range(amount):
        randoms_list.append(random.randint(0, 101))
    return randoms_list

