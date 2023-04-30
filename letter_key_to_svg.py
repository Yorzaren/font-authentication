import json
import os
import shutil

with open('dict.txt', 'r', encoding="utf-8") as f:
    data = json.load(f)

# print(data)

parent_dir = "svg_letters"
letter_dir_src = "letters-1"

if not os.path.exists(parent_dir):
    os.makedirs(parent_dir)
else:
    shutil.rmtree(parent_dir)

# A-Z make folders and then add the glyphs
for keys in data:
    # Make the folder
    this_folder = parent_dir + "/" + keys
    os.makedirs(this_folder)

    # String everything together and then output it as char.txt
    full_string = ""
    for char in data[keys]:
        full_string = full_string + char

    with open(this_folder+"/"+keys+".txt", 'w', encoding="utf-8") as text_file:
        text_file.write(full_string)

    # Now copy the symbols into it
    this_letter = keys.split("_")[1]
    print(this_letter)

    for char in data[keys]:
        shutil.copy(letter_dir_src+"/"+this_letter+".svg", this_folder+"/"+char+".svg")