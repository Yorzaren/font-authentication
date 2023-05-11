# font-val

This is a proof-of-concept for using fonts as part of a validation process.
Fonts can associate a character/letter with a glyph (an image representation) which could be unrelated to the character.
An example of this is the Wingdings dingbat font. When using Wingdings, typed characters render as pictures unrelated to the characters.
It is possible to create private fonts and distribute them to authorized parties.

By generating a key and associating certain characters with specific letters, it is possible to create a public validation code.
When used with the correct font, the public validation code will show the private validation code, which will authenticate the user.

## Install
```commandline
pip install -r requirements.txt
```

## How to Use

### Generating a Key
Call python to run the script: `run.py`
```commandline
python run.py
```

You can use `--help` to see more options.

By default, it will generate a key based off of 9,900 chinese characters and generate the SVG files needed to generate the font in an external program that you need to download separately.

The key is called `key.txt` and the SVG folder is called `key`.

### Generating the Font
To generate the font, I used [BirdFont](https://github.com/johanmattssonm/birdfont) because you can easily draw glyphs and export and import them.

If you don't want to use the default glyphs you can draw the letters A-Z and then name them similar to the files in `font_generator/letters`.

**Import the SVG Folder:**

Menu > Import and Export > Import SVG Folder > Click the "Select a Folder" button > Navigate to the SVG folder > Click "Import"

Once that is complete you will see a popup telling you how many glyphs BirdFont has imported.

After successfully importing the glyphs, you can save the font and export it.

I export mine as a `.ttf` file.

## Run the Demo
By default, there's some included example files which can display the proof-of-concept working.

Start the site on the localhost by using the following command:

```commandline
flask --app web run --debug
```

Then you can read and navigate the pages.

## Style / Linting / Unit Testing

### Python
[![Tested with Pytest](https://img.shields.io/badge/Tested%20with-Pytest-red?style=for-the-badge)](https://docs.pytest.org/)

Pytest files are found in the `tests` folder.

Run pytest from the root of the project.

You can test for coverage using:
```text
pytest --cov --cov-report=html
```

[![Code style: black](https://img.shields.io/badge/Code%20Style-Black-000000.svg?style=for-the-badge)](https://github.com/psf/black)


```text
isort --profile black .
black --line-length 120 .
flake8 --append-config=.github/linters/.flake8
```
