import json
import random
import string


def generate_simple_code(length: int):
    code = ""
    for i in range(0, length):  # Do it length times
        code += random.choice(string.ascii_uppercase)
    return code


def generate_hard_code(length: int, source_file):
    # Open the file and simplify it to a dict called letter_map
    with open(source_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    # print(data)

    letter_map = {}

    for key in data:
        this_letter = key.split("_")[1]
        letter_map[this_letter] = data[key]

    # print(letter_map)

    # Generate the private code like the previous example
    private_code = ""
    public_code = ""
    for i in range(0, length):  # Do it length times
        this_letter = random.choice(string.ascii_uppercase)
        private_code += this_letter
        public_code += random.choice(letter_map[this_letter])

    print(private_code)
    print(public_code)

    return [private_code, public_code]


if __name__ == "__main__":  # pragma: no cover
    # print(generate_simple_code(6))
    generate_hard_code(2, "font1.txt")
