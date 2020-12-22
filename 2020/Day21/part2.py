with open('data.txt', 'r') as f:
    data = [x for x in f.read().split('\n') if x]

split_data = []
for d in data:
    ingredients, allergens = d.split(' (contains ')
    ingredients = set([i for i in ingredients.split(' ') if i])
    allergens = set([a for a in allergens.replace(')', '').split(', ') if a])
    split_data.append((ingredients, allergens))

all_allergen_possibilities = {}
all_ingredients = []
for d in split_data:
    all_ingredients.append(d[0])
    for allergen in d[1]:
        if allergen not in all_allergen_possibilities:
            all_allergen_possibilities[allergen] = set(d[0])
        else:
            all_allergen_possibilities[allergen] &= set(d[0])
allergen_ingredients = set(allergen for allergens in all_allergen_possibilities.values() for allergen in allergens)


def remove_allergen(allergen_to_remove, all_allergens):
    single_allergens = set()
    for key in all_allergens:
        if len(all_allergens[key]) > 1 and allergen_to_remove in all_allergens[key]:
            all_allergens[key].remove(allergen_to_remove)
            if len(all_allergens[key]) == 1:
                single_allergens |= all_allergens[key]
    return single_allergens


single_allergen = [list(a) for a in all_allergen_possibilities.values() if len(a) == 1][0]
while single_allergen:
    all_to_rem = single_allergen.pop()
    single_allergen += list(remove_allergen(all_to_rem, all_allergen_possibilities))

print(','.join(str(ingredient.pop())
               for allergen, ingredient
               in sorted((key, value)
                         for key, value
                         in all_allergen_possibilities.items())))
