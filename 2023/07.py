from collections import Counter


def main():
    part_1()
    part_2()


def part_1():
    inp = get_input('./inputs/07_actual.txt')

    hands = get_hands(inp, with_joker=False)
    total = get_points(hands, with_joker=False)

    print('Part 1:', total)


def part_2():
    inp = get_input('./inputs/07_actual.txt')

    hands = get_hands(inp, with_joker=True)
    total = get_points(hands, with_joker=True)

    print('Part 2:', total)


def get_hand_type(cards: list, with_joker=False):
    """ Gets the type of the given hand

    :param cards: All cards of a hand
    :param with_joker: If J counts as a joker or a jack
    :return: The type
    """
    if not cards:
        return 0

    if not with_joker or 'J' not in cards:
        counter = Counter(cards)
        most_common_cnt = counter.most_common(1)[0][1]

        second_common_cnt = None
        if len(counter) > 1:
            second_common_cnt = counter.most_common(2)[1][1]

        # Check full house pairs
        if len(counter) > 1 and most_common_cnt == 3 and second_common_cnt == 2:
            return 'full_house'

        # Check two pairs
        if len(counter) > 1 and most_common_cnt == 2 and most_common_cnt == second_common_cnt:
            return 'two_pairs'

        return most_common_cnt
    else:
        joker_count = cards.count('J')
        cards_no_jokers = cards
        if joker_count > 0:
            cards_no_jokers = list(filter('J'.__ne__, cards))

        rank_no_jokers = get_hand_type(cards_no_jokers)

        if rank_no_jokers == 'two_pairs':
            return 'full_house'

        if rank_no_jokers + joker_count == 5:
            return 5

        return rank_no_jokers + joker_count


def get_hands(inp: list, with_joker=False):
    """Parses the input and returns a dict with hands for each category:
    5=Five of a kind
    4=Four of a kind
    full_house=FUll house
    3=Three of a kind
    two_pairs=Two pairs
    2=One pair
    1=Highest value

    :param inp: The input file as a list
    :param with_joker: If J counts as a joker or a jack
    :return:A  dict with the hand type as key and the hands as values
    """
    hand_types = {
        5: [],
        4: [],
        'full_house': [],
        3: [],
        'two_pairs': [],
        2: [],
        1: [],
    }

    for pair in inp:
        pair = pair.strip()
        hand, value = pair.split()
        hand_type = get_hand_type(list(hand), with_joker=with_joker)
        hand_types[hand_type].append({
            'hand': hand,
            'value': int(value)
        })
    return hand_types


def get_points(hands: dict, with_joker=False):
    """Calculates the points for all hands.

    :param hands: A dict of all hands
    :param with_joker: If J counts as a joker or a jack
    :return: The total of all calculated points
    """
    total = 0

    if with_joker:
        joker_value = 0
    else:
        joker_value = 11

    ranks = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'J': joker_value,
        'T': 10
    }

    rank = 1
    for key, hand_type in reversed(hands.items()):
        if not hand_type:
            continue

        if len(hand_type) == 1:
            total += rank * hand_type[0]['value']
            rank += 1
            continue

        all_hands = []
        for pair in hand_type:
            hand = list(pair['hand'])
            for index, card in enumerate(hand):
                if card in ranks:
                    hand[index] = ranks[card]
                else:
                    hand[index] = int(card)
            all_hands.append((hand, pair['value']))

        for hand in sorted(all_hands, reverse=False):
            total += rank * hand[1]
            rank += 1
            continue
    return total


def get_input(file_path):
    with open(file_path) as f:
        return f.readlines()


if __name__ == '__main__':
    main()
