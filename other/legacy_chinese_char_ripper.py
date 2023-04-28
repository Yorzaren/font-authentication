# hanziDB.csv is from https://github.com/ruddfawcett/hanziDB.csv
# This code will just rip it.
# This code isn't used except for getting the list of simp chinese characters
# to be used in a different script as a hard coded value.
# Keep this just in case you need to regenerate it.

import csv
output = ""

with open('hanziDB.csv', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            output = output + (row[1])

print(output)