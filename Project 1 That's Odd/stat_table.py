def print_summary_header():
    '''
    Prints out table header line.
    '''

    print('# of hands      pairs     %      2 pairs     %     flushes      %     high card     %  ')


def format_num_hands(num_hands):
    '''
    Formats the number of hands column.

    :param num_hands: Given number of hands.
    :return: Number of hands right-aligned with header.
    '''

    return f'{num_hands:>10,}'


def format_count_pair(num_hands, count_pair):
    '''
    Formats the count pairs column.

    :param num_hands: Given number of hands.
    :param count_pair: Given number of pairs.
    :return: Number of pairs right-aligned and percentage lined up with % symbol in header.
    '''

    return f'{count_pair:>8}  {(count_pair / num_hands) * 100: 06.2f}'


def format_count_two_pair(num_hands, count_two_pair):
    '''
    Formats the count two-pairs column.

    :param num_hands: Given number of hands.
    :param count_two_pair: Given number of two-pairs.
    :return: Number of two-pairs right-aligned and percentage lined up with % symbol in header.
    '''

    return f'{count_two_pair:>8}  {(count_two_pair / num_hands) * 100: 06.2f}'


def format_count_flush(num_hands, count_flush):
    '''
    Formats the count flush column.

    :param num_hands: Given number of hands.
    :param count_flush: Given number of flushes.
    :return: Number of flushes right-aligned and percentage lined up with the % symbol in header.
    '''

    return f'{count_flush:>8}   {(count_flush / num_hands) * 100: 06.2f}'


def format_count_high_card(num_hands, count_high_card):
    '''
    Formats the count high-card column.

    :param num_hands: Given number of hands.
    :param count_high_card: Given number of high-cards.
    :return: Number of high-cards right-aligned and percentage lined up with the % symbol in header.
    '''

    return f'{count_high_card:>8}  {(count_high_card / num_hands) * 100: 06.2f}'


def print_summary_row(num_hands, count_pair, count_two_pair, count_flush, count_high_card):
    '''
    Creates a line string with number of hands and counts of all different possible types of cards with percentages.
    
    :param num_hands: Given number of hands.
    :param count_pair: Given number of pairs.
    :param count_two_pair: Given number of two-pairs.
    :param count_flush: Given number of flushes.
    :param count_high_card: Given number of high-cards.
    :return: Prints formatted string summary line.
    '''

    num_hands += 1
    output_string = f'{format_num_hands(num_hands)}' + '   '
    output_string += f'{format_count_pair(num_hands, count_pair)}' + '   '
    output_string += f'{format_count_two_pair(num_hands, count_two_pair)}' + '  '
    output_string += f'{format_count_flush(num_hands, count_flush)}' + '    '
    output_string += f'{format_count_high_card(num_hands, count_high_card)}'

    print(output_string)