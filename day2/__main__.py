from utils import parse_data, read_input

data = read_input("./day2/input")
planned_course = parse_data(
    data, [{"key": "direction", "format": str}, {"key": "distance", "format": int}]
)


def go_forward(position, distance):
    if "aim" in position:
        position["depth"] += distance * position["aim"]
    position["horizontal"] += distance
    return position


def go_down(position, distance):
    key = "aim" if "aim" in position else "depth"
    position[key] += distance
    return position


def go_up(position, distance):
    key = "aim" if "aim" in position else "depth"
    position[key] -= distance
    return position


def run_course(position):
    operations = {
        "forward": go_forward,
        "down": go_down,
        "up": go_up,
    }

    for instruction in planned_course:
        operations[instruction["direction"]](position, instruction["distance"])

    result = position["horizontal"] * position["depth"]

    print(f"Final horizontal position {position['horizontal']}")
    print(f"Final Depth {position['depth']}")
    print(f"Final horizontal position * Final Depth { result }")


print("---- Part One ----")
run_course({"horizontal": 0, "depth": 0})
print("---- Part Two ----")
run_course({"horizontal": 0, "depth": 0, "aim": 0})
