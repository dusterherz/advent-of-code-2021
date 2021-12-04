from utils import read_input

data = read_input("./day3/input", strip_newline=True)
size_number = len(data[0])


def get_bits_reccurence(values=data):
    bits_recurrence = {}
    for i in range(size_number):
        bits_recurrence[i] = {"0": 0, "1": 0}

    for number in values:
        for i, bit in enumerate(number):
            bits_recurrence[i][bit] += 1

    return bits_recurrence


def convert_array_bits_to_int(array_bits):
    number = 0
    for bit in array_bits:
        number = (number << 1) | bit
    return number


def get_gamma_and_epsilon_bits(bits_recurrence):
    gamma_bits = []
    epsilon_bits = []
    for key in bits_recurrence:
        if bits_recurrence[key]["0"] == bits_recurrence[key]["1"]:
            gamma_bits.append(1)
            epsilon_bits.append(0)
        else:
            gamma_bits.append(
                int(max(bits_recurrence[key], key=bits_recurrence[key].get))
            )
            epsilon_bits.append(
                int(min(bits_recurrence[key], key=bits_recurrence[key].get))
            )

    return gamma_bits, epsilon_bits


def compute_power_consumption():
    bits_recurrence = get_bits_reccurence()
    gamma_bits, epsilon_bits = get_gamma_and_epsilon_bits(bits_recurrence)

    gamma = convert_array_bits_to_int(gamma_bits)
    epsilon = convert_array_bits_to_int(epsilon_bits)
    return gamma * epsilon, gamma, epsilon


def get_matching_bit_numbers(numbers, bit, position):
    matching_numbers = []
    for number in numbers:
        if int(number[position]) == bit:
            matching_numbers.append(number)
    return matching_numbers


def get_oxygen_and_co2_ratings():
    gamma_numbers = data.copy()
    epsilon_numbers = data.copy()
    for i in range(size_number):
        bits_reccurence = get_bits_reccurence(values=gamma_numbers)
        gamma_bits, _ = get_gamma_and_epsilon_bits(bits_recurrence=bits_reccurence)
        gamma_numbers = get_matching_bit_numbers(gamma_numbers, gamma_bits[i], i)
        if len(gamma_numbers) == 1:
            break
    for i in range(size_number):
        bits_reccurence = get_bits_reccurence(values=epsilon_numbers)
        _, epsilon_bits = get_gamma_and_epsilon_bits(bits_recurrence=bits_reccurence)
        epsilon_numbers = get_matching_bit_numbers(epsilon_numbers, epsilon_bits[i], i)
        if len(epsilon_numbers) == 1:
            break
    oxygen_rating = [int(digit) for digit in gamma_numbers[0]]
    co2_rating = [int(digit) for digit in epsilon_numbers[0]]
    return oxygen_rating, co2_rating


def get_life_support_rating():
    bits_recurrence = get_bits_reccurence()

    (
        oxygen_generator_rating_bits,
        co2_scrubber_rating_bits,
    ) = get_oxygen_and_co2_ratings()

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
