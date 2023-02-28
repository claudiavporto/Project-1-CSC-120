import card as c
import random


def create_deck():
    '''
    Creates a deck of cards.

    :return: The deck of cards.
    '''

    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    suits = ['H', 'S', 'D', 'C']
    deck = []
    for suit in suits:
        for rank in ranks:
            card = c.create_card(rank, suit)
            deck.append(card)
    return deck


def shuffle_deck(card_deck):
    '''
    Shuffles the order of the given deck of cards.

    :param card_deck: The given deck of cards.
    :return: no return
    '''

    random.shuffle(card_deck)


def get_num_cards_in_deck(card_deck):
    '''
    Finds and returns the length of the given card deck.

    :param card_deck: The given card deck.
    :return: The length of the given card deck.
    '''

    return len(card_deck)


def __test_create_deck():
    print(create_deck())


def __test_shuffle_deck(card_deck):
    shuffle_deck(card_deck)
    print(card_deck)


def __test_get_num_cards_in_deck(card_deck):
    print(get_num_cards_in_deck(card_deck))


if __name__ == "__main__":
    __test_create_deck()
    __test_shuffle_deck(create_deck())
    __test_get_num_cards_in_deck(create_deck())