def create_card(rank, suit):
    '''
    Creates a single card.

    :param rank: The given rank.
    :param suit: The given suit.
    :return: A string card.
    '''

    card = rank + suit
    return card


def get_rank(card):
    '''
    Finds and returns the rank in a given card.

    :param card: The given card.
    :return: A string of the rank found in the given card.
    '''

    return card[0]


def get_suit(card):
    '''
    Finds and returns the suit in a given card.

    :param card: The given card.
    :return: A string of the suit found in the given card.
    '''

    return card[1]

def __test_create_card():
    return create_card('A', 'S')

def __test_get_rank(card):
    print(f'Test Card Rank: {get_rank(card)}')

def __test_get_suit(card):
    print(f'Test Card Suit: {get_suit(card)}')

if __name__ == "__main__":
    print(f'Test Card: {test_create_card()}')
    test_get_rank(test_create_card())
    test_get_suit(test_create_card())
