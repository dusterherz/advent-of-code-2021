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


def get_step(start, end):
    if start < end:
        return 1
    if start > end:
        return -1
    return 0


def get_overlapping_vents(part1=True):
    diagram = [[0 for j in range(max_size)] for i in range(max_size)]
    for vent in vents:
        # Skip diagonals vent in part 1
        if (
            vent["start"]["x"] != vent["end"]["x"]
            and vent["start"]["y"] != vent["end"]["y"]
            and part1
        ):
            continue
        step_x = get_step(vent["start"]["x"], vent["end"]["x"])
        step_y = get_step(vent["start"]["y"], vent["end"]["y"])
        y = vent["start"]["y"]
        x = vent["start"]["x"]
        while x != vent["end"]["x"] or y != vent["end"]["y"]:
            diagram[y][x] += 1
            x += step_x
            y += step_y
        diagram[y][x] += 1
    flatten_diagram = sum(diagram, [])
    filtered_diagram = list(filter(lambda x: x >= 2, flatten_diagram))
    return len(filtered_diagram)


print("---- Part One ----")
print(f"Overlapping vents Points : {get_overlapping_vents()}")
print("---- Part Two ----")
print(f"Overlapping vents Points : {get_overlapping_vents(part1=False)}")
