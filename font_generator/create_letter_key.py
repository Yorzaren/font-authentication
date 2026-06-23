"""
This will generate a sorted dictionary of chinese characters into a relation between A-Z
and output it to a txt file.


Most of the code is just repetitive - so actually you could be lazy and loop print to add to the code

for x in string.ascii_uppercase:
    print(f'letter_key["{x}"] = {x}')

"""

import json

from Cryptodome.Random.random import (
    shuffle as shuffle,  # Can also use random.shuffle if this doesn't work
)


def generate_dict(input_string: str, output_file: str, scramble=True, debug=False):
    character_array = []

    # Take the imported characters and the add them to an array
    for x in input_string:
        character_array.append(x)

    # Debugging messages
    print(f"Array size: {len(character_array)}")
    if debug:  # pragma: no cover
        print("Original array:")
        print(character_array)

    # Shuffle array
    if scramble is True:
        shuffle(character_array)
        if debug:  # pragma: no cover
            # Check that it is scrambled
            print("Scrambled array:")
            print(character_array)

    # Create the dictionary
    letter_key = {}

    # Create the empty lists
    letter_A = []
    letter_B = []
    letter_C = []
    letter_D = []
    letter_E = []
    letter_F = []
    letter_G = []
    letter_H = []
    letter_I = []
    letter_J = []
    letter_K = []
    letter_L = []
    letter_M = []
    letter_N = []
    letter_O = []
    letter_P = []
    letter_Q = []
    letter_R = []
    letter_S = []
    letter_T = []
    letter_U = []
    letter_V = []
    letter_W = []
    letter_X = []
    letter_Y = []
    letter_Z = []

    letters = {
        0: letter_A,
        1: letter_B,
        2: letter_C,
        3: letter_D,
        4: letter_E,
        5: letter_F,
        6: letter_G,
        7: letter_H,
        8: letter_I,
        9: letter_J,
        10: letter_K,
        11: letter_L,
        12: letter_M,
        13: letter_N,
        14: letter_O,
        15: letter_P,
        16: letter_Q,
        17: letter_R,
        18: letter_S,
        19: letter_T,
        20: letter_U,
        21: letter_V,
        22: letter_W,
        23: letter_X,
        24: letter_Y,
        25: letter_Z,
    }

    for index, x in enumerate(character_array):
        remainder = index % 26
        letters[remainder].append(x)

    # Assign it to the dictionary
    letter_key["letter_A"] = letter_A
    letter_key["letter_B"] = letter_B
    letter_key["letter_C"] = letter_C
    letter_key["letter_D"] = letter_D
    letter_key["letter_E"] = letter_E
    letter_key["letter_F"] = letter_F
    letter_key["letter_G"] = letter_G
    letter_key["letter_H"] = letter_H
    letter_key["letter_I"] = letter_I
    letter_key["letter_J"] = letter_J
    letter_key["letter_K"] = letter_K
    letter_key["letter_L"] = letter_L
    letter_key["letter_M"] = letter_M
    letter_key["letter_N"] = letter_N
    letter_key["letter_O"] = letter_O
    letter_key["letter_P"] = letter_P
    letter_key["letter_Q"] = letter_Q
    letter_key["letter_R"] = letter_R
    letter_key["letter_S"] = letter_S
    letter_key["letter_T"] = letter_T
    letter_key["letter_U"] = letter_U
    letter_key["letter_V"] = letter_V
    letter_key["letter_W"] = letter_W
    letter_key["letter_X"] = letter_X
    letter_key["letter_Y"] = letter_Y
    letter_key["letter_Z"] = letter_Z

    # Write it to a file
    with open(output_file, "w", encoding="utf-8") as text_file:
        text_file.write(json.dumps(letter_key))
