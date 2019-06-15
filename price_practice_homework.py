def get_summ(one, two, delimiter = '&'):
    one = str(one).capitalize()
    two = str(two).capitalize()
    delimiter = str(delimiter)
    summary = f'{one} {two}'
    print(summary)
get_summ(input('Что мы делаем с языком изучения? '), input('Введите язык изучения: '))

