# cake_01_taste = 'vanilia'
# cake_01_glaze = 'chocolade'
# cake_01_text = 'Happy Brithday'
# cake_01_weight = 0.7

cake01 = {
    'taste': 'vanilia',
    'glaze': 'chocolade',
    'text': 'Happy Brithday',
    'weight': 0.7
}


# cake_02_taste = 'tee'
# cake_02_glaze = 'lemon'
# cake_02_text = 'Happy Python Coding'
# cake_02_weight = 1.3

cake02 = {
    'taste': 'tee',
    'glaze': 'lemon',
    'text': 'Happy Python Coding',
    'weight': 1.3
}
 
def show_cake_info(a_cake):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(
        a_cake['taste'], a_cake['glaze'], a_cake['text'], a_cake['weight']))

cake = [cake01, cake02]

for c in cake:
    show_cake_info(c)