import random


def guess(difficulty, guess):
    random_number = random.randint(0, difficulty)
    if guess == random_number:
        return 'ok', random_number
    else:
        return 'failed', random_number
