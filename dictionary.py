import random
from vars import ALPHABET

"""
Создание словаря алфавита с набором случайных значений
Имеет вид: "буква": "код"
"""


def create_letters(number):
    new_letters = {}
    while len(new_letters) < 33:
        for letter in ALPHABET:
            done = True
            random_value = random.randint(100 * number, 999)
            for i in range(0, number + 1):
                if random_value in new_letters.values():
                    done = False
            if done:
                new_letters.update({letter: random_value})
    new_letters_list = list(new_letters.items())
    new_letters_list.sort()
    for i, v in new_letters_list:
        new_letters[i] = v
