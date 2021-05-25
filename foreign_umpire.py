import csv
import json
from collections import Counter


def plot():
    '''Creating Json file for
       count of foreign umpires'''

    umpire_country = []
    with open('umpires.csv', 'r') as file:
        umpire = csv.DictReader(file)
        for row in umpire:
            if row[' country'] != ' India':
                umpire_country.append(row[' country'].strip())

    # creating a dictionary of foreign umpire country and their count
    foreign_umpire_country_count = Counter(umpire_country)
    data = {'foreign_umpires_count': []}
    for item in foreign_umpire_country_count.items():
        data['foreign_umpires_count'].append([item[0], item[1]])

    with open('foreign_umpires_count.json', 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    plot()
