
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