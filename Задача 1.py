with open('recipes.txt', 'w', encoding='utf-8') as f:
    f.write('''Омлет
3
Яйцо | 2 | шт
Молоко | 100 | мл
Помидор | 2 | шт

Утка по-пекински
4
Утка | 1 | шт
Вода | 2 | л
Мед | 3 | ст.л
Соевый соус | 60 | мл

Запеченный картофель
3
Картофель | 1 | кг
Чеснок | 3 | зубч
Сыр гауда | 100 | г

Фахитос
5
Говядина | 500 | г
Перец сладкий | 1 | шт
Лаваш | 2 | шт
Винный уксус | 1 | ст.л
Помидор | 2 | шт''')


def cook_book():
    cook_book = {}
    with open('recipes.txt', encoding='utf-8') as f:
        while True:
            key = f.readline().strip()
            values_number = f.readline().strip()

            if not key or not values_number:
                break

            ingredients = [f.readline().strip().split(' | ') for i in range(int(values_number))]
            f.readline()

            cook_book[key] = []
            for i in range(int(values_number)):
                cook_book[key].append({'ingredient_name':ingredients[i][0], 'quantity':int(ingredients[i][1]), 'measure':ingredients[i][2]})
    print(cook_book)

cook_book()
