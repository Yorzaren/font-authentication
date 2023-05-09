import hashlib
import json
import os
import shutil
import string

import pytest

from font_generator.create_letter_key import generate_dict
from font_generator.letter_key_to_svg import generate_svg_folder

# Main
T_F1 = "test_letters"
T_F2 = "test_letters_split"


def hash_file(filename):  # Simple Hash function
    h = hashlib.sha1()  # Doesn't matter

    # open file for reading in binary mode
    with open(filename, "rb") as file:
        # loop till the end of the file
        chunk = 0
        while chunk != b"":
            # read only 1024 bytes at a time
            chunk = file.read(65536)
            h.update(chunk)

    # return the hex representation of digest
    return h.hexdigest()


def delete_file(filename: str):
    if os.path.exists(filename):
        os.remove(filename)


class TestLetterKey:
    @pytest.mark.order(1)
    def test_create_simple_letter_key(self):
        SIMPLE_LETTERS = string.ascii_letters
        # Create a key where they are assigned in order
        # A and a are assigned to letter_A and so on and so forth.
        generate_dict(SIMPLE_LETTERS, "simpleKey.txt", scramble=False)
        generate_dict(SIMPLE_LETTERS, "simpleScrambled.txt")

    @pytest.mark.order(2)
    def test_scramble_key(self):
        assert hash_file("simpleKey.txt") == hash_file("simpleKey.txt")

        # Check that the scrambled and the unscrambled keys are not the same.
        assert hash_file("simpleKey.txt") != hash_file("simpleScrambled.txt")

    @pytest.mark.order(3)
    def test_letter_key_to_svg(self):
        output_folder = T_F1
        letter_dir = "font_generator/letters"

        # Define the hashes associated with the files
        hash_dic = {
            "letter_A": hash_file(letter_dir + "/A.svg"),
            "letter_B": hash_file(letter_dir + "/B.svg"),
            "letter_C": hash_file(letter_dir + "/C.svg"),
            "letter_D": hash_file(letter_dir + "/D.svg"),
            "letter_E": hash_file(letter_dir + "/E.svg"),
            "letter_F": hash_file(letter_dir + "/F.svg"),
            "letter_G": hash_file(letter_dir + "/G.svg"),
            "letter_H": hash_file(letter_dir + "/H.svg"),
            "letter_I": hash_file(letter_dir + "/I.svg"),
            "letter_J": hash_file(letter_dir + "/J.svg"),
            "letter_K": hash_file(letter_dir + "/K.svg"),
            "letter_L": hash_file(letter_dir + "/L.svg"),
            "letter_M": hash_file(letter_dir + "/M.svg"),
            "letter_N": hash_file(letter_dir + "/N.svg"),
            "letter_O": hash_file(letter_dir + "/O.svg"),
            "letter_P": hash_file(letter_dir + "/P.svg"),
            "letter_Q": hash_file(letter_dir + "/Q.svg"),
            "letter_R": hash_file(letter_dir + "/R.svg"),
            "letter_S": hash_file(letter_dir + "/S.svg"),
            "letter_T": hash_file(letter_dir + "/T.svg"),
            "letter_U": hash_file(letter_dir + "/U.svg"),
            "letter_V": hash_file(letter_dir + "/V.svg"),
            "letter_W": hash_file(letter_dir + "/W.svg"),
            "letter_X": hash_file(letter_dir + "/X.svg"),
            "letter_Y": hash_file(letter_dir + "/Y.svg"),
            "letter_Z": hash_file(letter_dir + "/Z.svg"),
        }

        # Generate the SVGs related to the dict_key.txt file
        # If everything is done correctly it the hashes of the files will match.
        generate_svg_folder("simpleKey.txt", output_folder=output_folder, input_glyphs=letter_dir, split_folders=False)

        # Open the original file to get the letter_key
        with open("simpleKey.txt", "r", encoding="utf-8") as f:
            data = json.load(f)

        # Check each entry
        for letter_key in data:
            # print(letter_key)
            for entry in data.get(letter_key):
                entry_svg = "svg_letters/" + entry + ".svg"
                assert os.path.isfile(entry_svg) is True
                this_file_hash = hash_file(entry_svg)
                assert this_file_hash == hash_dic.get(letter_key)
                # print(entry)

    @pytest.mark.order(4)
    def test_split_folder(self):
        output_folder = T_F2
        generate_svg_folder("example/dict.txt", output_folder=output_folder, split_folders=True)

        # If things are split correctly it will output 26 folders, 1 for each letter A-Z
        assert len(next(os.walk(output_folder))[1]) == 26

    @pytest.mark.order(5)
    def test_teardown(self):
        delete_file("simpleKey.txt")
        delete_file("simpleScrambled.txt")

        if os.path.exists(T_F1):
            shutil.rmtree(T_F1)
        if os.path.exists(T_F2):
            shutil.rmtree(T_F2)
