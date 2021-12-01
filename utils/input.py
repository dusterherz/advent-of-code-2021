def read_input(filename="input"):
    f = open(filename, "r")
    return f.readlines()


def read_input_as_numbers(filename="input"):
    return [int(line) for line in read_input(filename=filename)]
