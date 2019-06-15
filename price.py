def discounted(price, discount, max_discount = 25):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - price * discount  / 100
    return (price_with_discount)
product = {
    'name': 'Mi 8',
    'price': 32000,
    'stock': 12,
    'discount': 22
    }
product['with_discount'] = discounted(product['price'], product['discount'])
print(product['with_discount'])
print(discounted(37266, 10))