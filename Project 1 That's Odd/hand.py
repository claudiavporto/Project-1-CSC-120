import deck as d
import card as c

HAND_LENGTH = 5


def create_hand():
    '''
    Creates a card hand from a shuffled deck of cards.

    :return: The card hand.
    '''

    hand = []
    card_deck = d.create_deck()
    d.shuffle_deck(card_deck)
    while len(hand) < HAND_LENGTH:
        hand.append(card_deck.pop())
    return hand


def __get_suits_in_hand(card_hand):
    return [c.get_suit(card) for card in card_hand]


def __get_first_suit_in_hand(suits_in_hand):
    return suits_in_hand[0]


def __get_ranks_in_hand(card_hand):
    return [c.get_rank(card) for card in card_hand]


def __check_flush(card_hand):
    is_flush = True
    suits_in_hand = __get_suits_in_hand(card_hand)
    __get_first_suit_in_hand(suits_in_hand)
    for _suit in range(1, len(suits_in_hand)):
        if suits_in_hand[_suit] != __get_first_suit_in_hand(suits_in_hand):
            is_flush = False
    return is_flush


def __check_pair(card_hand):
    is_pair = False
    ranks_in_hand = __get_ranks_in_hand(card_hand)
    pairs = []
    for rank in ranks_in_hand:
        if rank not in pairs:
            if ranks_in_hand.count(rank) > 1:
                pairs.append(rank)
    if len(pairs) == 1:
        is_pair = True

    return is_pair


def __check_two_pair(card_hand):
    is_two_pair = False
    pairs = []
    ranks_in_hand = __get_ranks_in_hand(card_hand)
    for rank in ranks_in_hand:
        if rank not in pairs:
            if ranks_in_hand.count(rank) > 1:
                pairs.append(rank)
    if len(pairs) == 2:
        is_two_pair = True

    return is_two_pair


def check_hand(card_hand):
    '''
    Determines which kind of the four types (Flush, Pair, Two-Pair, or High Card) the card hand is.

    :param card_hand: The card hand to check.
    :return: The counts of each of the four types of hands. The correct type of hand should return 1
     and the rest return 0.
    '''

    count_flush = 0
    count_two_pair = 0
    count_pair = 0
    count_high_card = 0

    if __check_flush(card_hand):
        count_flush = 1
    elif __check_two_pair(card_hand):
        count_two_pair = 1
    elif __check_pair(card_hand):
        count_pair = 1
    else:
        count_high_card = 1

    return count_flush, count_two_pair, count_pair, count_high_card


def __test_create_hand():
    print(f'Hand: {create_hand()}')


def __test_get_suits():
    card_hand = create_hand()
    print(f'Test Get Suits Hand: {card_hand}')
    print(f'Hand suits: {__get_suits_in_hand(card_hand)}')


def __test_get_ranks():
    card_hand = create_hand()
    print(f'Test Get Ranks Hand: {card_hand}')
    print(f'Hand Ranks: {__get_ranks_in_hand(card_hand)}')


def __test_check_flush():
    flush_card_hand = ['3D', 'AD', '7D', 'JD', '2D']
    print(f'Flush Hand: {flush_card_hand}')
    print(f'Flush Check [SHOULD BE True]: {str(__check_flush(flush_card_hand))}')


def __test_two_pair():
    hand_1 = ['3H', '3D', '3D', '8C', '8H']
    hand_2 = ['4S', 'AC', 'AD', '7H', '4D']
    print(f'Two Pair Hand 1: {hand_1}')
    print(f'Check Two Pair Hand 1 [SHOULD BE True]: {__check_two_pair(hand_1)}')
    print(f'Two Pair Hand 2: {hand_2}')
    print(f'Check Two Pair Hand 2 [SHOULD BE True]: {__check_two_pair(hand_2)}')


def __test_pair():
    hand_1 = ['3H', '3D', '3D', '8C', '6H']
    hand_2 = ['4S', 'AC', 'AD', '7H', '5D']
    print(f'Pair Hand 1: {hand_1}')
    print(f'Check Pair Hand 1 [SHOULD BE True]: {__check_pair(hand_1)}')
    print(f'Pair Hand 2: {hand_2}')
    print(f'Check Pair Hand 2 [SHOULD BE True]: {__check_pair(hand_2)}')


def __test_check_hand():
    flush_hand = ['3D', 'AD', '7D', 'JD', '2D']
    two_pair_hand_1 = ['3H', '3D', '3D', '8C', '8H']
    two_pair_hand_2 = ['4S', 'AC', 'AD', '7H', '4D']
    pair_hand_1 = ['3H', '3D', '3D', '8C', '6H']
    pair_hand_2 = ['4S', 'AC', 'AD', '7H', '5D']
    high_card_hand = ['4S', 'AC', 'JD', '7H', '5D']
    print(f'Check for Flush Hand [SHOULD PRINT (1, 0, 0, 0)]: {check_hand(flush_hand)}')
    print(f'Check for Two Pair Hand (case 1) [SHOULD PRINT (0, 1, 0, 0)]: {check_hand(two_pair_hand_1)}')
    print(f'Check for Two Pair Hand (case 2) [SHOULD PRINT (0, 1, 0, 0)]: {check_hand(two_pair_hand_2)}')
    print(f'Check for Pair Hand (case 1) [SHOULD PRINT (0, 0, 1, 0)]: {check_hand(pair_hand_1)}')
    print(f'Check for Pair Hand (case 2) [SHOULD PRINT (0, 0, 1, 0)]: {check_hand(pair_hand_2)}')
    print(f'Check for High Card Hand [SHOULD PRINT (0, 0, 0, 1)]: {check_hand(high_card_hand)}')


if __name__ == "__main__":
    __test_create_hand()
    __test_get_suits()
    __test_get_ranks()
    __test_check_flush()
    __test_two_pair()
    __test_pair()
    __test_check_hand()