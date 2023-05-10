"""
import font_generator.zh as zh
import font_generator.cjk as cjk
from font_generator.create_letter_key import generate_dict
from font_generator.letter_key_to_svg import generate_svg_folder

if __name__ == "__main__":
    folder = "CJK_D"
    name = folder + ".txt"

    generate_dict(cjk.CJK_D, name, scramble=True)
    generate_svg_folder(name, output_folder=folder, input_glyphs="font_generator/letters", split_folders=False)
"""
