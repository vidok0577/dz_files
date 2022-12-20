def readfile_to_dict():
    cook_book ={}
    with open('recipes.txt', encoding='utf8') as f:
        for line in f:
            name = line.strip()
            qty = int(f.readline())
            list_product = []
            for product in [f.readline().strip().split('|') for _ in range(qty)]:
                list_product.append(dict(zip(['ingredient_name', 'quantity', 'measure'], product)))
            cook_book[name] = list_product
            f.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    list_products = {}
    cook_book = readfile_to_dict()
    for dish in dishes:
        for ingredient in cook_book[dish]:
            name, quantity, measure = ingredient.values()
            if name in list_products:
                list_products[name]['quantity'] += int(quantity) * person_count
            else:
                list_products[name] = {'measure': measure, 'quantity': int(quantity) * person_count}
    return list_products

if __name__ == '__main__':
    print(*get_shop_list_by_dishes(['Омлет', 'Фахитос'], 5).items(), sep='\n')