def main():
    part_1()
    part_2()


def part_1():
    inp = get_input('./inputs/04_actual.txt')

    total = 0

    for game in inp:
        game = game.strip()
        game_id, numbers = game.split(': ')
        winning_numbers, my_numbers = numbers.split(' | ')

        winning_numbers_list = []
        for winning_number in winning_numbers.split(' '):
            if winning_number:
                winning_numbers_list.append(int(winning_number.strip()))

        my_numbers_list = []
        for my_number in my_numbers.split(' '):
            if my_number:
                my_numbers_list.append(int(my_number.strip()))

        cnt = 0
        for number in my_numbers_list:
            if number in winning_numbers_list:
                cnt += 1

        if cnt > 0:
            points = 1
            for i in range(cnt-1):
                points = points * 2
            total += points

    print('Part 1:', total)


def part_2():
    inp = get_input('./inputs/04_actual.txt')

    total = 0
    cards = {}
    for game in inp:
        game = game.strip()
        game_id, numbers = game.split(': ')
        winning_numbers, my_numbers = numbers.split(' | ')

        cards[int(game_id.lstrip('Card '))] = {}

        winning_numbers_list = []
        for winning_number in winning_numbers.split(' '):
            if winning_number:
                winning_numbers_list.append(int(winning_number.strip()))
        cards[int(game_id.lstrip('Card '))]['winning'] = winning_numbers_list

        my_numbers_list = []
        for my_number in my_numbers.split(' '):
            if my_number:
                my_numbers_list.append(int(my_number.strip()))
        cards[int(game_id.lstrip('Card '))]['my'] = my_numbers_list

    for key in cards.keys():
        total += check_card(key, cards)

    print('Part 2:', total)


def check_card(card_id: int, cards: {}):
    tot = 1
    cnt = 0
    for i, number in enumerate(cards[card_id]['my']):
        if number in cards[card_id]['winning']:
            cnt += 1
    if cnt > 0:
        for i in range(cnt):
            if card_id+i+1 in cards:
                tot += check_card(card_id+i+1, cards)
    return tot


def get_input(file_path):
    with open(file_path) as f:
        return f.readlines()


if __name__ == '__main__':
    main()
