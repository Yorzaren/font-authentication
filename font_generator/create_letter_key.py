"""
This will generate a sorted dictionary of chinese characters into a relation between A-Z
and output it to a txt file.


Most of the code is just repetitive - so actually you could be lazy and loop print to add to the code

for x in string.ascii_uppercase:
    print(f'letter_key["{x}"] = {x}')

"""

import json
import random  # Consider the benefits of swapping to cryptorandom


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
        random.shuffle(character_array)
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

    # Sort them into the sub-arrays
    for x in character_array:
        index = character_array.index(x)
        if index % 26 == 0:
            letter_A.append(x)
        elif index % 26 == 1:
            letter_B.append(x)
        elif index % 26 == 2:
            letter_C.append(x)
        elif index % 26 == 3:
            letter_D.append(x)
        elif index % 26 == 4:
            letter_E.append(x)
        elif index % 26 == 5:
            letter_F.append(x)
        elif index % 26 == 6:
            letter_G.append(x)
        elif index % 26 == 7:
            letter_H.append(x)
        elif index % 26 == 8:
            letter_I.append(x)
        elif index % 26 == 9:
            letter_J.append(x)
        elif index % 26 == 10:
            letter_K.append(x)
        elif index % 26 == 11:
            letter_L.append(x)
        elif index % 26 == 12:
            letter_M.append(x)
        elif index % 26 == 13:
            letter_N.append(x)
        elif index % 26 == 14:
            letter_O.append(x)
        elif index % 26 == 15:
            letter_P.append(x)
        elif index % 26 == 16:
            letter_Q.append(x)
        elif index % 26 == 17:
            letter_R.append(x)
        elif index % 26 == 18:
            letter_S.append(x)
        elif index % 26 == 19:
            letter_T.append(x)
        elif index % 26 == 20:
            letter_U.append(x)
        elif index % 26 == 21:
            letter_V.append(x)
        elif index % 26 == 22:
            letter_W.append(x)
        elif index % 26 == 23:
            letter_X.append(x)
        elif index % 26 == 24:
            letter_Y.append(x)
        elif index % 26 == 25:
            letter_Z.append(x)

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
