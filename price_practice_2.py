def format_price(price):
    price = int(float(price))
    print(f'Цена: {price} руб.')
format_price(input('Введите цену: '))