def hide_card(card_number):
    card_string = card_number.replace(' ', '')
    return '************' + card_string[12:]


card = '905 678123 45612 56'

print(hide_card(card))
