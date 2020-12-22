with open('data.txt', 'r') as f:
    data = [x for x in f.read().split('\n') if x]

split_data = []
for d in data:
    ingredients, allergens = d.split(' (contains ')
    ingredients = set([i for i in ingredients.split(' ') if i])
    allergens = set([a for a in allergens.replace(')', '').split(', ') if a])
    split_data.append((ingredients, allergens))
print(split_data)

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
print(sum([ingredient not in allergen_ingredients for ingredients in all_ingredients for ingredient in ingredients]))
