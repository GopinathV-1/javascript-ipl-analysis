import csv
import json
from collections import defaultdict


def abbreviate_team_name(name):
    '''making abbreviation names'''
    split_name = name.split(' ')
    short_name = [each[0] for each in split_name]
    return ''.join(short_name)


def plot():
    '''Creating Json file for total
       runs scored by each team'''

    # creating a dictionary of team and their score
    total_run = defaultdict(int)
    with open('deliveries.csv', 'r') as file:
        deliveries = csv.DictReader(file)
        for row in deliveries:
            total_run[abbreviate_team_name
                      (row['batting_team'])] += int(row['total_runs'])

    data = {'total_run': []}
    for item in total_run.items():
        data['total_run'].append([item[0], item[1]])

    with open('total_runs.json', 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    plot()
