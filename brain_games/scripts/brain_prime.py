#!/usr/bin/env python3
from brain_games.greet import greet_user
from brain_games.engine import play_game
from brain_games.games.prime import generate_prime


def main():
    GAME_NAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    user_name = greet_user(GAME_NAME)
    questions_and_answers = generate_prime()
    play_game(user_name, questions_and_answers)


if __name__ == '__main__':
    main()
