import json
import string

import web.validator as validator


# Helper function check mapping
def check_mapping(data, private_code: str, public_code: str) -> bool:
    # The bool returned is_fine
    # True = no error
    for i in range(0, len(private_code)):
        this_private_letter = private_code[i]
        this_public_letter = public_code[i]
        # print(this_private_letter)

        array = data["letter_" + this_private_letter]
        # print(array)

        if this_public_letter not in array:
            return False
    # End for loop
    return True


class TestValidatorCode:
    def test_generate_simple_code(self):
        code_size = 5
        code = validator.generate_simple_code(code_size)
        # Check that the function is creating the right length codes
        assert len(code) == code_size

        # Check that the chars in the code are uppercase only
        for char in code:
            assert char in string.ascii_uppercase

        # Check that the codes are random from each other on each call
        assert code != validator.generate_simple_code(code_size)

        # Check that codes can have different lengths
        assert len(code) != len(validator.generate_simple_code(code_size + 4))

    def test_generate_code_from_file(self):
        code_size = 5
        test_source_file = "example/dict.txt"
        code_arr = validator.generate_code_from_file(code_size, test_source_file)

        # Load the file to help check
        with open(test_source_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        private_code = code_arr[0]

        public_code = code_arr[1]

        # Check that the codes public and private are different
        assert private_code != public_code
        # Check that they output the same length
        assert len(private_code) == len(public_code)
        # Check that it generates the right length code
        assert len(private_code) == code_size

        # Check the mapping is correct
        assert check_mapping(data, private_code, public_code) is True

        # Check if mapping function is correct
        # If this is functional it will return false
        # The diff code should be unrelated to the public code mapping, the likelihood of it generating the same
        # code as the private code is unlikely
        diff_code = validator.generate_simple_code(code_size)

        assert check_mapping(data, diff_code, public_code) is False
