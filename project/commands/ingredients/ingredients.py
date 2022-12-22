import pprint
#
ingredients1 = "Alaska Pollock Fillet (58%) (Fish), Wheat Flour [Wheat Flour, Calcium Carbonate, Iron, Niacin (B3), " \
              "Thiamin (B1)], Rapeseed Oil, Water, Wheat Starch, Wheat Gluten, Rice Flour, Salt, Yeast, Black Pepper, " \
              "Flavouring, Lemon Powder (2%), Raising Agents, Diphosphate, Sodium Bicarbonate, Sunflower Oil, Sea Salt, " \
              "Citric Acid, White Pepper"

# ingredients = "Alaska Pollock Fillet (Fish), Wheat Flour [Wheat Flour, Calcium Carbonate, Iron, Niacin (B3), " \
#               "Thiamin (B1)], Rapeseed Oil, Water, Wheat Starch, Wheat Gluten, Rice Flour, Salt, Yeast, Black Pepper, " \
#               "Flavouring, Lemon Powder, Raising Agents: Diphosphate, Sodium Bicarbonate, Sunflower Oil, Sea Salt, " \
#               "Citric Acid, White Pepper "

def ingredients_to_list(ingredients):
    list_of_terms = []
    current_term = ''
    seperators = ['[', '(', ')', ']', ',']
    for letter in ingredients:
        if letter not in seperators:
            current_term = f'{current_term}{letter}'
        elif letter in seperators:
            if len(current_term.strip()) > 0:
                list_of_terms.append(current_term.strip())
            current_term = ''
            if letter not in [',']:
                list_of_terms.append(letter)

    return list_of_terms

def ingredients_list_to_dict(ingredients_list, percentage=None, lvl=0,):
    ingredients_dict = {}
    sub_list = []
    previous_item = ''
    close_sub = ''
    in_sub = False
    for item in ingredients_list:
        if item not in ['[', '(', ')', ']'] and not in_sub:
            ingredients_dict[item] = 0
            if percentage is not None and previous_item != '':
                ingredients_dict[previous_item] = percentage
                percentage = None
            elif percentage is not None and previous_item == '':
                ingredients_dict["percentage"] = percentage
                percentage = None
            previous_item = item
        elif in_sub and item != close_sub:
            sub_list.append(item)
        elif item == '[' and close_sub == '':
            in_sub = True
            close_sub = ']'
        elif item == '(' and close_sub == '':
            in_sub = True
            close_sub = ')'
        elif item == close_sub:
            if len(sub_list) == 1 and '%' in sub_list[0]:
                percentage = int(sub_list[0].replace('%', ''))
                in_sub = False
                close_sub = ''
                sub_list = []
            else:
                ingredients_dict[previous_item] = ingredients_list_to_dict(sub_list, percentage, lvl+1)
                in_sub = False
                close_sub = ''
                sub_list = []
                percentage = None
        # print(f"{item}, close_sub: {close_sub}, in_sub: {in_sub}, previous: {previous_item} ---- {lvl}")
    return ingredients_dict

def get_percentage_spread_list(number_of_elements, total_pct=1):
    percentage_spread_list = []
    for i in range(number_of_elements + 1):
        percentage_spread_list.append(i ** 2)
    total = sum(percentage_spread_list)
    percentage_spread_list = [x / total * total_pct for x in percentage_spread_list]
    return percentage_spread_list[1:]

def assign_basic_values(ingredients_dict, pct=1):
    list_len = len(ingredients_dict.items())
    percentage_spread_list = get_percentage_spread_list(list_len, pct)
    current_list_of_pct = []
    for key, value in ingredients_dict.items():
        if value == 0:
            current_list_of_pct.append(None)
        elif isinstance(value, int) and value > 0:
            current_list_of_pct.append(value)
        elif 'percentage' in value:
            current_list_of_pct.append(value['percentage'])

    # update_percentage_spread_list(percentage_spread_list, )


list = ingredients_to_list(ingredients1)
dict = ingredients_list_to_dict(list)

pp = pprint.PrettyPrinter(indent=4, sort_dicts=False)
pp.pprint(dict)

# assign_basic_values(dict)

print(get_percentage_spread_list(3))

my_list = [0.07142857142857142, 0.2857142857142857, 0.6428571428571429]
known_values = [None, 0.4, None]

def update_percentage_spread_list(my_list, known_values):
    """
    update my_list[i] with known_values[i] if known_values[i] is not None
    """
    updated_indexes = []
    for i in range(len(my_list)):
        if known_values[i] is not None:
            updated_indexes.append(i)
            my_list[i] = known_values[i]

    cnt_of_values_to_update = len(my_list) - len(updated_indexes)
    current_sum = sum(my_list)
    difference_amount = 1 - current_sum
    list_of_update_values = get_percentage_spread_list(cnt_of_values_to_update, difference_amount)

    print(list_of_update_values)

    cnt = 0
    for i in range(len(my_list)):
        if i not in updated_indexes:
            print(f"updating {my_list[i]} with {list_of_update_values[cnt]}")
            my_list[i] += list_of_update_values[cnt]
            cnt += 1

    return my_list


spread_list = update_percentage_spread_list(my_list, known_values)
print(spread_list)
print(sum(spread_list))