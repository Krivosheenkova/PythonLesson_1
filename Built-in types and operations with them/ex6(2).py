# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
products = int(input("How much products have arrived? "))
n = 1
features = []
prod_list = []
analysis = {}
while n <= products:
    features = dict({'Name': input('What in the package today? '), 'Cost': input('What is the cost? '),
                    'Quantity': input('How much? '), 'Unit': input('Khm. Of what? ')})
    prod_list.append((n, features))
    n += 1
    analysis = dict(
        {'Name': features.get('Name'), 'Cost': features.get('Cost'), 'Quantity': features.get('Quantity'),
         'Unit': features.get('Unit')})
print(analysis)
