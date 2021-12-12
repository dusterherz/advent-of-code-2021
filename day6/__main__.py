from utils import read_input

data = read_input("./day6/input")
start_fishs = [int(i) for i in data[0].split(",")]


def simulate_live_fishs(fishs, days):
    fish_by_days = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
    }
    for fish in fishs:
        fish_by_days[fish] += 1
    for day in range(1, days + 1):
        reproducing_fish = fish_by_days[0]
        for i in range(0, 8):
            fish_by_days[i] = fish_by_days[i + 1]
        fish_by_days[6] += reproducing_fish  # fishs that has reproduced
        fish_by_days[8] = reproducing_fish  # new fishs created
    return sum(fish_by_days.values())


print(simulate_live_fishs(start_fishs, 80))
start_fishs = [int(i) for i in data[0].split(",")]
print(simulate_live_fishs(start_fishs, 256))
