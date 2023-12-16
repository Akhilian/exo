import re

from app.models import Passenger


def import_csv(csv) -> list[Passenger]:
    lines = csv.splitlines()[1:]

    values = []

    for line in lines:
        search = re.search(
            '(\d+),(\d+),(\d+),\"(.+)\",(\w+),([.0-9]+)?,(\d+),(\d+),([./a-zA-Z0-9 ]+),([.0-9]+),([ a-zA-Z0-9]+)?,(\w+)?',
            line)

        if search is None:
            print(line)
            continue

        groups = search.groups()

        values.append(groups)

    passengers = list(map(lambda values: Passenger(
        passengerId=int(values[0]),
        survived=int(values[1]),
        pclass=int(values[2]),
        name=values[3],
        sex=values[4],
        age=values[5],
        sibSp=int(values[6]),
        parch=int(values[7]),
        ticket=values[8],
        fare=float(values[9]),
        cabin=values[10],
        embarked=values[11],
    ), values))

    return passengers
