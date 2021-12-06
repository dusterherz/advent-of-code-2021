from operator import itemgetter

from utils import parse_data, read_input

data = read_input("./day5/input")

max_size = 1000


def get_coors(line):
    values = [int(value) for value in line.split(",")]
    return {"x": values[0], "y": values[1]}


vents = parse_data(
    data,
    [{"key": "start", "format": get_coors}, {"key": "end", "format": get_coors}],
    separator=" -> ",
)


def get_overlapping_vents(part1=True):
    diagram = [[0 for j in range(max_size)] for i in range(max_size)]
    for vent in vents:
        low_x = min(vent["start"]["x"], vent["end"]["x"])
        max_x = max(vent["start"]["x"], vent["end"]["x"])
        low_y = min(vent["start"]["y"], vent["end"]["y"])
        max_y = max(vent["start"]["y"], vent["end"]["y"])
        if (
            vent["start"]["x"] != vent["end"]["x"]
            and vent["start"]["y"] != vent["end"]["y"]
        ):
            if part1:
                continue
            else:
                step_y = 1 if vent["start"]["y"] < vent["end"]["y"] else -1
                step_x = 1 if vent["start"]["x"] < vent["end"]["x"] else -1
                y = vent["start"]["y"]
                x = vent["start"]["x"]
                while x != vent["end"]["x"] or y != vent["end"]["y"]:
                    diagram[y][x] += 1
                    y += step_y
                    x += step_x
                diagram[y][x] += 1
        elif vent["start"]["x"] != vent["end"]["x"]:
            for i in range(low_x, max_x + 1):
                diagram[vent["start"]["y"]][i] += 1
        else:
            for i in range(low_y, max_y + 1):
                diagram[i][vent["start"]["x"]] += 1
    flatten_diagram = sum(diagram, [])
    filtered_diagram = list(filter(lambda x: x >= 2, flatten_diagram))
    return len(filtered_diagram)


print("---- Part One ----")
print(f"Overlapping vents Points : {get_overlapping_vents()}")
print("---- Part Two ----")
print(f"Overlapping vents Points : {get_overlapping_vents(part1=False)}")
