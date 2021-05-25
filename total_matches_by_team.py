import csv
import json
from collections import defaultdict


def abbreviate_team_name(name):
    '''making abbreviation names'''
    split_name = name.split(' ')
    short_name = [each[0] for each in split_name]
    return ''.join(short_name)


def plot():
    '''Creating Json file for
    total matches played by team by season'''

    team_seasonal_matches = defaultdict(lambda: defaultdict(int))
    season = set()

    '''creating a dictionay of teams to a dictionay of
       seasons with numbers of matches played'''
    with open('matches.csv', 'r') as file:
        matches = csv.DictReader(file)
        for row in matches:
            team_seasonal_matches[abbreviate_team_name(
                                  row['team1'])][row['season']] += 1
            team_seasonal_matches[abbreviate_team_name(
                                  row['team2'])][row['season']] += 1
            season.add(int(row['season']))
        season = sorted(list(season))

    ''' initializing total matches as zero
        in non played season to all teams'''
    for row in team_seasonal_matches.keys():
        for col in list(season):
            team_seasonal_matches[row][str(col)] = (team_seasonal_matches
                                                    [row][str(col)])
        team_seasonal_matches[row] = dict(sorted(team_seasonal_matches
                                          [row].items(),
                                          key=lambda x: (x[0], x[1])))

    data = {'season': []}
    data['season'] = season
    for row in team_seasonal_matches.items():
        temporary_list = []
        for col in row[1].items():
            temporary_list.append(col[1])
        data[row[0]] = []
        data[row[0]] += temporary_list

    with open('matches_by_season.json', 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    plot()
