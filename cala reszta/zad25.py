# def show_progress(how_many=0,character='*'):
#     for i in range(how_many):
#         print(character)


def show_progress(how_many, character='*'):
    line = character * how_many
    print(line)


show_progress(10)
show_progress(15)
show_progress(30)

show_progress(10, '-')
show_progress(15, '+')

