from random import randint
from brain_games import NUM_OF_GAME_ROUNDS

MIN_NUMBER = 1
MAX_NUMBER = 99


def generate_even():
    '''Generates list of tuples with questions and correct answers
    for Brain Even game.'''

    q_a_list = list()
    rounds_left = NUM_OF_GAME_ROUNDS
    while rounds_left > 0:
        number = randint(MIN_NUMBER, MAX_NUMBER)
        question = str(number)

        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        q_a_list.append((question, correct_answer))
        rounds_left -= 1

    return q_a_list
