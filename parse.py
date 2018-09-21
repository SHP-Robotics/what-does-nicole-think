import csv


def main():
    data = []
    with open('data.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    headers = data[0]
    data = data[1:]  # filter out headers

    keyed = [{headers[i]: data[t][i] for i in range(len(headers))} for t in range(len(data))]

    print(keyed)

    matches = []
    with open('teams.txt') as f:
        raw = f.read().split('\n \n')
        for match in raw:
            matchnum = match.split('\n')[0]
            teams = match.split('\n')[1].split('\t')[:6]
            red = teams[:3]
            blue = teams[3:]
            matches.append((matchnum, red, blue))

    calculate_10ness(matches, keyed)


def calculate_10ness(matches, teams):
    for match in matches:
        num, red, blue = match
        red_avg = 0
        blue_avg = 0
        for rt in red:
            score = int(next((t for t in teams if t['Team Number'] == rt), {'Overall Rating of the Team': 7})[
                            'Overall Rating of the Team'])
            print(f"red team {rt} has score {score}")
            red_avg += score

        for bt in blue:
            score = int(next((t for t in teams if t['Team Number'] == bt), {'Overall Rating of the Team': 7})[
                            'Overall Rating of the Team'])
            print(f"blue team {bt} has score {score}")
            blue_avg += score

        red_avg /= 3
        blue_avg /= 3

        we_are_in = 'red' if '2144' in red else 'blue'

        print(f"Match {num}: we are in {we_are_in}, red={red_avg:.2f}, blue={blue_avg:.2f}")


if __name__ == '__main__':
    main()
