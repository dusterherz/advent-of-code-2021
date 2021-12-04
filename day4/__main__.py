from pathlib import Path

data = Path("./day4/input").read_text()


def parse_bingo_cards():
    elements = data.split("\n\n")
    bingo_numbers = [int(number) for number in elements.pop(0).split(",")]
    bingo_cards = []
    for element in elements:
        card = []
        for line in element.split("\n"):
            card_line = [int(number) for number in line.split()]
            if len(card_line) > 0:
                card.append(card_line)
        bingo_cards.append(card)
    return bingo_numbers, bingo_cards


def check_card(bingo_numbers, bingo_card):
    matrix_validation = []
    marked_numbers = []
    unmarked_numbers = []
    for row in bingo_card:
        matrix_validation.append([number in bingo_numbers for number in row])
        marked_numbers += [number for number in row if number in bingo_numbers]
        unmarked_numbers += [number for number in row if number not in bingo_numbers]
    for column in zip(*matrix_validation):
        if all(column):
            return True, marked_numbers, unmarked_numbers
    for row in matrix_validation:
        if all(row):
            return True, marked_numbers, unmarked_numbers
    return False, marked_numbers, unmarked_numbers


def check_cards(numbers, bingo_cards):
    unmarked_numbers = 0
    for card in bingo_cards:
        bingo, marked_numbers, unmarked_numbers = check_card(numbers, card)
        if bingo:
            return True, marked_numbers, unmarked_numbers
    return False, None, None


def get_first_win_card():
    bingo_numbers, bingo_cards = parse_bingo_cards()

    numbers = []
    for number in bingo_numbers:
        numbers.append(number)
        has_bingoed, _, unmarked_numbers = check_cards(numbers, bingo_cards)
        if has_bingoed:
            return sum(unmarked_numbers), number


def get_last_win_card():
    bingo_numbers, bingo_cards = parse_bingo_cards()

    numbers = []
    for number in bingo_numbers:
        numbers.append(number)
        for card_number, card in enumerate(bingo_cards):
            bingo, _, unmarked_numbers = check_card(numbers, card)
            if bingo:
                bingo_cards.pop(card_number)
            if len(bingo_cards) == 0:
                return sum(unmarked_numbers), number


print("----- Part 1 -----")
sum_unmarked_numbers, last_number = get_first_win_card()
print(f"Sum of unmarked numbers: {sum_unmarked_numbers}")
print(f"Last number: {last_number}")
print(f"Final Score: {sum_unmarked_numbers * last_number}")

print("\n----- Part 2 -----")
sum_unmarked_numbers, last_number = get_last_win_card()
print(f"Sum of unmarked numbers: {sum_unmarked_numbers}")
print(f"Last number: {last_number}")
print(f"Final Score: {sum_unmarked_numbers * last_number}")
