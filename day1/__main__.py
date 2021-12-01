from utils import read_input_as_numbers

data = read_input_as_numbers("./day1/input")


def compute_increase(window_size=1):
    prev_depth = sum(data[:window_size])
    increase = 0
    for i in range(1, len(data)):
        depth = sum(data[i : i + window_size])
        if depth > prev_depth:
            increase += 1
        prev_depth = depth
    return increase


print("---- Part 1 ----")
print(f"Increase: {compute_increase()}")

print("---- Part 2 ----")
print(f"Increase: {compute_increase(3)}")
