from utils import read_input

data = read_input("./day3/input", strip_newline=True)
size_number = len(data[0])


def convert_array_bits_to_int(array_bits):
    number = 0
    for bit in array_bits:
        number = (number << 1) | bit
    return number


def get_bits_reccurence(values=data):
    bits_recurrence = {}
    for i in range(size_number):
        bits_recurrence[i] = {"0": 0, "1": 0}

    for number in values:
        for i, bit in enumerate(number):
            bits_recurrence[i][bit] += 1

    return bits_recurrence


def get_gamma_bits(bits_recurrence):
    gamma_bits = []
    for key in bits_recurrence:
        gamma_bits.append(
            1 if bits_recurrence[key]["0"] <= bits_recurrence[key]["1"] else 0
        )
    return gamma_bits


def get_epsilon_bits(bits_recurrence):
    epsilon_bits = []
    for key in bits_recurrence:
        epsilon_bits.append(
            1 if bits_recurrence[key]["0"] > bits_recurrence[key]["1"] else 0
        )
    return epsilon_bits


def compute_power_consumption():
    bits_recurrence = get_bits_reccurence()
    gamma_bits = get_gamma_bits(bits_recurrence)
    epsilon_bits = get_epsilon_bits(bits_recurrence)

    gamma = convert_array_bits_to_int(gamma_bits)
    epsilon = convert_array_bits_to_int(epsilon_bits)
    return gamma * epsilon, gamma, epsilon


def get_matching_bit_numbers(numbers, bit, position):
    matching_numbers = []
    for number in numbers:
        if int(number[position]) == bit:
            matching_numbers.append(number)
    return matching_numbers


def get_matching_number(get_discriminants_bits):
    numbers = data.copy()
    for i in range(size_number):
        bits_reccurence = get_bits_reccurence(values=numbers)
        discriminants_bits = get_discriminants_bits(bits_reccurence)
        numbers = get_matching_bit_numbers(numbers, discriminants_bits[i], i)
        if len(numbers) == 1:
            matching_number = [int(digit) for digit in numbers[0]]
            return matching_number


def get_life_support_rating():
    oxygen_generator_rating_bits = get_matching_number(get_gamma_bits)
    co2_scrubber_rating_bits = get_matching_number(get_epsilon_bits)

    oxygen_generator_rating = convert_array_bits_to_int(oxygen_generator_rating_bits)
    co2_scrubber_rating = convert_array_bits_to_int(co2_scrubber_rating_bits)

    life_support_rating = oxygen_generator_rating * co2_scrubber_rating

    return life_support_rating, oxygen_generator_rating, co2_scrubber_rating


print("---- Part 1 ----")
power_consumption, gamma, epsilon = compute_power_consumption()
print(f"Gamma: {gamma}")
print(f"Epsilon: {epsilon}")
print(f"Power Consumption: {power_consumption}")

print("---- Part 2 ----")
(
    life_support_rating,
    oxygen_generator_rating,
    co2_scrubber_rating,
) = get_life_support_rating()
print(f"Oxygen Generator Rating: {oxygen_generator_rating}")
print(f"Co2 Scrubber Rating: {co2_scrubber_rating}")
print(f"Life Support Rating: {life_support_rating}")
