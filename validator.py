import random
import string


def generate_simple_code(length: int):
    code = ""
    for i in range(0, length):  # Do it length times
        code += random.choice(string.ascii_letters)
    return code


if __name__ == "__main__":  # pragma: no cover
    print(generate_simple_code(6))
