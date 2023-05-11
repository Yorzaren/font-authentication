import argparse
import os
import pathlib
import string

from colorama import Back, Fore, Style
from colorama import init as colorama_init

from font_generator.cjk import CJK, CJK_A, CJK_ALL, CJK_B
from font_generator.create_letter_key import generate_dict
from font_generator.letter_key_to_svg import generate_svg_folder
from font_generator.zh import HSK, ZH_ALL

# Initialize for to use colorful print messages later
colorama_init()

"""
Default it generates the key and the svg folders

If you only want to generate the svg files for the font, you pass input_key.
If input_key is passed, input_string and generate_from are not used.

Otherwise, input can be from:
- input_string which will take whatever characters you want
- generate_from will generate the key from a set of provided strings (default)

output changes the name of the output files default is key.txt and key folder for svg files

key_only will only output a key.txt without the svg files.
If you want to make the svg files from a key, use input_key.

split_folders will split the svg files into associated letter folders which will be easier on BirdFont
input_glyphs allows for you to define a different set of glyphs A-Z to associate with in a folder.
If that folder can't be found, it will default to the provided glyphs.

"""

parser = argparse.ArgumentParser(description="-------------------- Generate the key or svg files --------------------")
# If not defined, generate the key and the svg files
parser.add_argument("--key_only", action="store_true", help="Generate the key.txt only")
parser.add_argument("--input_string", help="Generate key from an input string (Overrides: generate_from)")
parser.add_argument(
    "--generate_from",
    choices=["AZ", "ZH_ALL", "ZH_HSK", "CJK", "CJK_A", "CJK_B", "CJK_ALL"],
    default="ZH_ALL",
    help="Generate key from default strings (default: ZH_ALL)",
)
parser.add_argument(
    "--input_key", help="If have a key and want to generate svg files (Overrides: input_string and generate_from)"
)

# Additional commands
parser.add_argument("-o", "--output", default="key.txt", help="Output filename (default: key.txt)")
parser.add_argument("--input_glyphs", default="font_generator/letters", help="Define the glyphs you want to use")
parser.add_argument("--split_folders", action="store_true", help="Split the svg files into folders")

args = parser.parse_args()

# print(args)


def __generate_svg_files(input_key: str, input_glyphs: str, split_folders: bool):
    if input_key is not None:
        print(f"{Fore.BLUE}Generating svg files from {input_key}...{Style.RESET_ALL}")
        if os.path.isfile(input_key):
            folder = pathlib.Path(input_key).stem  # Get name without extension

            if os.path.exists(input_glyphs) is False:
                print(
                    f"{Fore.RED}Error: The folder {input_glyphs} could not be found at: "
                    f"{Back.BLACK}{os.path.abspath(input_glyphs)}{Style.RESET_ALL}"
                )
                print(f"{Fore.YELLOW}Warning: Defaulting to preset glyphs{Style.RESET_ALL}")
                glyph_folder = "font_generator/letters"
            else:
                glyph_folder = input_glyphs

            generate_svg_folder(input_key, output_folder=folder, input_glyphs=glyph_folder, split_folders=split_folders)

            print(
                f"{Fore.GREEN}Complete: Files located "
                f"{Fore.BLUE}{Back.BLACK}{Style.BRIGHT}{os.path.abspath(folder)}{Style.RESET_ALL}"
            )

        else:
            print(
                f"{Fore.RED}Error: The file {input_key} could not be found.{Style.RESET_ALL}\n"
                f"File not found at: {os.path.abspath(input_key)}"
            )


# If the input_key is not blank, override and only generate svg files.
if args.input_key is not None:
    __generate_svg_files(args.input_key, args.input_glyphs, args.split_folders)
else:
    # Key generation
    if args.input_string is not None:
        generate_dict(args.input_string, args.output)
        print(
            f"{Fore.GREEN}Complete: {args.output} is located at "
            f"{Fore.BLUE}{Back.BLACK}{Style.BRIGHT}{os.path.abspath(args.output)}{Style.RESET_ALL}"
        )
    # There's no user supplied input so default to generation with a preset
    else:
        input_set = args.generate_from
        string_in = "ZH_ALL"  # Set to default

        if input_set == "AZ":
            string_in = string.ascii_uppercase
        elif input_set == "ZH_ALL":
            string_in = ZH_ALL
        elif input_set == "ZH_HSK":
            string_in == HSK
        elif input_set == "CJK":
            string_in = CJK
        elif input_set == "CJK_A":
            string_in == CJK_A
        elif input_set == "CJK_B":
            string_in == CJK_B
        elif input_set == "CJK_ALL":
            string_in == CJK_ALL

        generate_dict(string_in, args.output)
        print(
            f"{Fore.GREEN}Complete: {args.output} is located at "
            f"{Fore.BLUE}{Back.BLACK}{Style.BRIGHT}{os.path.abspath(args.output)}{Style.RESET_ALL}"
        )
    if args.key_only is False:
        __generate_svg_files(args.output, args.input_glyphs, args.split_folders)
