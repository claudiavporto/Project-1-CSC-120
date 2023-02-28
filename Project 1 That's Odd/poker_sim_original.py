# I affirm that I have carried out my academic endeavors with full academic honesty.
import random


def create_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    suits = ['S', 'C', 'H', 'D']
    deck = []
    for suit in suits:
        for rank in ranks:
            card = rank + suit
            deck.append(card)
    return deck


def shuffle(card_deck):
    random.shuffle(card_deck)
    return


def deal_cards(card_deck):
    hand = []
    while len(hand) < 5:
        hand.append(card_deck.pop())
    return hand


def get_num_cards_in_deck(card_deck):
    return len(card_deck)


def get_suits_in_hand(card_hand):
    return [card[1] for card in card_hand]


def check_flush(card_hand):
    is_flush = True
    suits_in_hand = get_suits_in_hand(card_hand)
    first_suit_in_hand = suits_in_hand[0]
    for _suit in range(1, len(suits_in_hand)):
        if suits_in_hand[_suit] != first_suit_in_hand:
            is_flush = False
    return is_flush


def get_ranks_in_hand(card_hand):
    return [card[0] for card in card_hand]


def check_pair(card_hand):
    is_pair = False
    ranks_in_hand = get_ranks_in_hand(card_hand)
    pairs = []
    for rank in ranks_in_hand:
        if rank not in pairs:
            if ranks_in_hand.count(rank) > 1:
                pairs.append(rank)
    if len(pairs) == 1:
        is_pair = True

    return is_pair


def check_two_pair(card_hand):
    is_two_pair = False
    pairs = []
    ranks_in_hand = get_ranks_in_hand(card_hand)
    for rank in ranks_in_hand:
        if rank not in pairs:
            if ranks_in_hand.count(rank) > 1:
                pairs.append(rank)
    if len(pairs) == 2:
        is_two_pair = True

    return is_two_pair


def check_hand(card_hand):
    count_flush = 0
    count_two_pair = 0
    count_pair = 0
    count_high_card = 0

    if check_flush(card_hand):
        count_flush = 1
    elif check_two_pair(card_hand):
        count_two_pair = 1
    elif check_pair(card_hand):
        count_pair = 1
    else:
        count_high_card = 1

    return count_flush, count_two_pair, count_pair, count_high_card


def print_summary_header():
    print('# of hands      pairs     %      2 pairs     %     flushes      %     high card     %  ')


def format_num_hands(num_hands):
    return f'{num_hands:>10,}'


def format_count_pair(num_hands, count_pair):
    return f'{count_pair:>8}  {(count_pair / num_hands) * 100: 06.2f}'


def format_count_two_pair(num_hands, count_two_pair):
    return f'{count_two_pair:>8}  {(count_two_pair / num_hands) * 100: 06.2f}'


def format_count_flush(num_hands, count_flush):
    return f'{count_flush:>8}   {(count_flush / num_hands) * 100: 06.2f}'


def format_count_high_card(num_hands, count_high_card):
    return f'{count_high_card:>8}  {(count_high_card / num_hands) * 100: 06.2f}'


def print_summary_row(num_hands, count_pair, count_two_pair, count_flush, count_high_card):
    num_hands += 1
    output_string = f'{format_num_hands(num_hands)}' + '   '
    output_string += f'{format_count_pair(num_hands, count_pair)}' + '   '
    output_string += f'{format_count_two_pair(num_hands, count_two_pair)}' + '  '
    output_string += f'{format_count_flush(num_hands, count_flush)}' + '    '
    output_string += f'{format_count_high_card(num_hands, count_high_card)}'

    print(output_string)


def play_rounds():
    max_hands = 100000
    count_flush = 0
    count_two_pair = 0
    count_pair = 0
    count_high_card = 0
    print_summary_count = 10000
    discard_deck = []

    card_deck = create_deck()
    shuffle(card_deck)

    print_summary_header()

    for num_hands in range(max_hands + 1):
        card_hand = deal_cards(card_deck)
        count_flushes, count_two_pairs, count_pairs, count_high_cards = check_hand(card_hand)

        discard_deck += card_hand

        count_flush += count_flushes
        count_two_pair += count_two_pairs
        count_pair += count_pairs
        count_high_card += count_high_cards

        # add hands to discard pile function: discard_deck += card_hand

        if get_num_cards_in_deck(card_deck) < 5:
            discard_deck += card_deck
            shuffle(discard_deck)
            card_deck = discard_deck.copy()
            discard_deck.clear()

        if print_summary_count - 1 == num_hands:
            print_summary_row(num_hands, count_pair, count_two_pair, count_flush, count_high_card)
            print_summary_count += 10000


if __name__ == '__main__':
    play_rounds()
