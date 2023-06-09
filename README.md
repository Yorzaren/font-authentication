# font-authentication

**Font Authentication** is a proof of concept for using fonts as part of the authentication process.
Fonts can associate a character/letter with a glyph (an image representation) which could be unrelated to the character.
An example of this is the Wingdings dingbat font. When using Wingdings, typed characters render as pictures unrelated to the characters.
It is possible to create private fonts and distribute them to authorized parties.

By generating a key and associating certain characters with specific letters, it is possible to create a public authentication code.
When used with the correct font, the public authentication code will show the private authentication code, which will authenticate the user.

Image 1 shows the authentication code without the required font installed.
Image 2 shows what the correct authentication code looks when the correct font is installed and loaded.

**Image 1:**
<div align="center">

![image_1](https://github.com/Yorzaren/font-authentication/raw/main/web/static/image_1.png)

</div>

**Image 2:**

<div align="center">

![image_2](https://github.com/Yorzaren/font-authentication/raw/main/web/static/image_2.png)

</div>

A character in the private authentication code can render as multiple characters.
This makes it difficult to bruteforce and discover the mapping because the likelihood of seeing the character again is unlikely.

## Install
```commandline
pip install -r requirements.txt -r requirements-dev.txt
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

**MAKE SURE YOU CHECK SET WIDTH OF GLYPH TO SVG FILE!!!**

If you fail to tick the checkbox, the glyphs will have display overlap and spacing issues.

Once that is complete you will see a popup telling you how many glyphs BirdFont has imported.

Save the file and then run:
```commandline
python birdfont_modifier.py FILENAME
```

The script will fix the space issues and allow the letters a bit more separation from each other.

After successfully importing the glyphs and modifying the file, you can export it.

I export mine as a `.ttf` file.

## Run the Demo
By default, there's some included example files which can display the proof of concept working.

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
