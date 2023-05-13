"""

This code isn't used except for getting characters from tables.

Leaving this here if needed again.


"""

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/CJK_Unified_Ideographs_Extension_D"
response = requests.get(url)
# print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table", class_="wikitable")
# print(table)

full_string = ""

for glyph_data in table.find_all("tbody"):
    rows = glyph_data.find_all("tr")[2:]  # Drop the first 2 rows bc its title and header
    # print(rows)
    for row in rows:
        char_string = ""
        col = row.find_all("td")
        this_row_text = col[1:]  # Drop the first one because that's the U+XXXX
        for x in this_row_text:
            # print(f"This char: {x.text}")
            char_string += x.text
        # print(char_string)
        full_string += char_string

print(full_string.replace(" ", "").replace("\n", ""))
