import csv
import json
from collections import defaultdict


def create_json():
    '''create Json file for top
       run scored RCB batsman'''

    # creating dictionary of RCB batsman and their scores
    rcb_batsman_runs = defaultdict(int)
    with open('deliveries.csv', 'r') as file:
        deliveries = csv.DictReader(file)
        for row in deliveries:
            if row['batting_team'] == 'Royal Challengers Bangalore':
                rcb_batsman_runs[row['batsman']] += int(row['total_runs'])

    # Descending sort of batsman based on their scores
    rcb_batsman_runs = dict(sorted(rcb_batsman_runs.items(),
                            key=lambda kv: (kv[1], kv[0]), reverse=True))

    batsman_name = list(rcb_batsman_runs.keys())
    runs_scored = list(rcb_batsman_runs.values())
    data = {'rcb_batsman_runs': []}
    for item1, item2 in zip(batsman_name[:10], runs_scored[:10]):
        data['rcb_batsman_runs'].append([item1, item2])

    with open('rcb_batsman_runs.json', 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    create_json()
