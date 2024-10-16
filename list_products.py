# Создание словаря из списков рецептов

with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ingredients_count = file.readline()
        ingredients = []
        for el in range(int(ingredients_count)):
            recipe = file.readline().strip().split(' | ')
            ingredient_name, quantity, measure = recipe
            ingredients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        file.readline()
        cook_book[dish_name] = ingredients

# Список продуктов на несколько персон

def get_shop_list_by_dishes(person_count: int, dishes: list):
    """ Функция, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить.
    На выходе получается словарь с названием ингредиентов и его количестом для блюда.
    Если блюда нет в cook_book выводит сообщение о том что такого блюда нет в кулинарной книге.
    
    """

    result = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredients in cook_book[dish]:
                if ingredients['ingredient_name'] not in result:
                    result[ingredients['ingredient_name']] = {'measure': ingredients['measure'], 'quantity': (int(ingredients['quantity']) * person_count)}
        else:
             print(f'{dish} - такого блюда нет в кулинарной книге')
    print(result)
get_shop_list_by_dishes(2, ['Запеченный картофель', 'Омлет'])