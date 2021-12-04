def read_input(filename="input", strip_newline=False):
    f = open(filename, "r")
    lines = f.readlines()
    if strip_newline:
        lines = [line.strip() for line in lines]
    return lines


def read_input_as_numbers(filename="input"):
    return [int(line) for line in read_input(filename=filename)]
