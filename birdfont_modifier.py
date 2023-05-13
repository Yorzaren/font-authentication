import argparse
import os
import xml.etree.ElementTree as ET

from colorama import Back, Fore, Style
from colorama import init as colorama_init

# Initialize for to use colorful print messages later
colorama_init()


def update_bf_file(
    filename: str, designer="Yorzaren", designer_url="https://github.com/Yorzaren/", space_l=0, space_r=0, backup=False
):
    if os.path.exists(filename) is False:
        print(
            f"{Fore.RED}Error: The file {filename} could not be found at: "
            f"{Back.BLACK}{os.path.abspath(filename)}{Style.RESET_ALL}"
        )
    else:
        tree = ET.parse(filename)
        root = tree.getroot()

        # Update the designer info
        for designer_name in root.iter("designer"):
            designer_name.text = designer
        for designer_link in root.iter("designer_url"):
            designer_link.text = designer_url

        # Shift the glyph spacing
        for elem in root.iter("collection"):
            # A collection item stores the data about the glyph
            # print(elem.attrib)
            uni = elem.get("unicode")

            if uni is not None and uni != "U+20":
                # Not having a uni means it's probably the .notdef glyph
                # U+20 is SPACE
                for child in elem:
                    # print(child.tag, child.attrib)
                    if child.tag == "glyph":
                        # Update the offsets
                        child.attrib["left"] = str(float(child.attrib["left"]) + space_l)
                        child.attrib["right"] = str(float(child.attrib["right"]) + space_r)

        # Output updated file
        if backup:
            new_file = "Fixed_" + os.path.basename(filename)
        else:
            new_file = filename
        with open(new_file, "w") as file_handle:
            file_handle.write(ET.tostring(root, encoding="utf8").decode("utf8"))

        print(
            f"{Fore.GREEN}Finished: {new_file} located at: "
            f"{Back.BLACK}{Fore.BLUE}{os.path.abspath(new_file)}{Style.RESET_ALL}"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="-------------------- Fix BirdFont file --------------------")
    # If not defined, generate the key and the svg files
    parser.add_argument("filename", help="Name of the BirdFont file")
    parser.add_argument("--designer", help="Change designer name")
    parser.add_argument("--designer_url", help="Change designer url")
    parser.add_argument("--space_l", type=int, default=0, help="Set the space offset for the glyphs (default: 0)")
    parser.add_argument("--space_r", type=int, default=5, help="Set the space offset for the glyphs (default: 5)")
    parser.add_argument(
        "--backup", action="store_true", default=5, help="Set the space offset for the glyphs (default: 5)"
    )
    args = parser.parse_args()

    # print(args)

    # Don't allow for people to set designer url without designer name
    if args.designer_url is not None and args.designer is None:
        print(f"{Fore.RED}Error: You must declare designer name using --designer before you can use --designer_url")
    # Allow people to set the designer without the designer url
    elif args.designer is not None and args.designer_url is None:
        update_bf_file(
            filename=args.filename,
            designer=args.designer,
            designer_url="",
            space_l=args.space_l,
            space_r=args.space_r,
            backup=args.backup,
        )
    # Both designer values are defined
    elif args.designer is not None and args.designer_url is not None:
        update_bf_file(
            filename=args.filename,
            designer=args.designer,
            designer_url=args.designer_url,
            space_l=args.space_l,
            space_r=args.space_r,
            backup=args.backup,
        )
    # Default to myself as the designer
    else:
        update_bf_file(filename=args.filename, space_l=args.space_l, space_r=args.space_r, backup=args.backup)
