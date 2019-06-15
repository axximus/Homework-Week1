a = "Привет"; b = 'мир'; c = 2
d = '{} {} {}!'.format(a, b, c)
user = 'Максим'
e = 'Привет, {name}!'.format(name = user)
r = f'Приветики, {user}!'
t = f'{a}, {b} и {user}!'
m = 'я'.upper(); n = 'ВЕЛИКИЙ'.lower(); x = 'ЧеЛоВеК'.capitalize()
q = '    Приветищщщще    '
o = 'Прив3т т3б3'.replace('3', 'е')
p = o.replace('3', 'е')
u = 'Привет Приветы'.replace('ы', '')
l = 'Привет ПриветЫ'.lower().replace('ы', '').capitalize()
z = 'Привет мир'.replace('мир', 'python')
k = 'learn.python.ru'
j = 'Предложение из очень очень очень очень многих слов'
h = None; g = 0
name = input('Введите ваше имя: ')
age = int(input('Сколько вам лет? '))
age = 2019 - age
print(f'Привет, {name}, я вас так долго ждала, {name}!')
print(h is None, g is None)
print(q.strip())
print(d)
print(e)
print(r)
print(t)
print(len(e))
print(f'{m} {n} {x}!')
print(o)
print(p)
print(u)
print(l)
print(z)
print(k.split('.'))
print(j.split())
print(len(j.split()))
print(f'Вы родились в {age} году.')