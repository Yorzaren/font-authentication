"""
https://birdfont.org/doku/doku.php/import_multiple_svg_files

This seems to indicate I can just name the files X.svg and it will import.

I think there's a visual glitch so its not showing the correct chinese character
in the BirdFont gui.
"""


import json
import os
import shutil


def write_letter_file(output_location, file_text):
    with open(output_location, "w", encoding="utf-8") as text_file:
        text_file.write(file_text)


def generate_svg_folder(
    source_file, output_folder="svg_letters", input_glyphs="font_generator/letters", split_folders=False
):
    # Open the text file with the data
    with open(source_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # print(data)

    parent_dir = output_folder
    letter_dir_src = input_glyphs

    # Remove the old folder if it exists
    if os.path.exists(parent_dir):
        shutil.rmtree(parent_dir)
    # Make a new folder
    os.makedirs(parent_dir)

    for keys in data:
        if split_folders:
            # Make the folder
            this_folder = parent_dir + "/" + keys
            os.makedirs(this_folder)
        else:
            this_folder = parent_dir

        # String everything together and then output it as char.txt
        full_string = ""
        for char in data[keys]:
            full_string = full_string + char

        # Write a file to help test that the font will work.
        write_letter_file(this_folder + "/" + keys + ".txt", full_string)

        # Now copy the symbols into the folder
        this_letter = keys.split("_")[1]
        print("Creating svg data related to: " + this_letter)

        for char in data[keys]:
            shutil.copy(letter_dir_src + "/" + this_letter + ".svg", this_folder + "/" + char + ".svg")


if __name__ == "__main__":  # pragma: no cover
    generate_svg_folder("simpleScrambled.txt", split_folders=False)
