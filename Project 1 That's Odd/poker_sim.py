# I affirm that I have carried out my academic endeavors with full academic honesty.
import deck as d
import hand as h
import stat_table as t

MAX_HANDS = 100000


def play_rounds():
    count_flush = 0
    count_two_pair = 0
    count_pair = 0
    count_high_card = 0
    print_summary_count = 10000
    discard_deck = []

    card_deck = d.create_deck()
    d.shuffle_deck(card_deck)

    t.print_summary_header()

    for num_hands in range(MAX_HANDS + 1):
        card_hand = h.create_hand()
        count_flushes, count_two_pairs, count_pairs, count_high_cards = h.check_hand(card_hand)

        discard_deck += card_hand

        count_flush += count_flushes
        count_two_pair += count_two_pairs
        count_pair += count_pairs
        count_high_card += count_high_cards

        if d.get_num_cards_in_deck(card_deck) < 5:
            discard_deck += card_deck
            d.shuffle_deck(discard_deck)
            card_deck = discard_deck.copy()
            discard_deck.clear()

        if print_summary_count - 1 == num_hands:
            t.print_summary_row(num_hands, count_pair, count_two_pair, count_flush, count_high_card)
            print_summary_count += 10000


if __name__ == '__main__':
    play_rounds()
