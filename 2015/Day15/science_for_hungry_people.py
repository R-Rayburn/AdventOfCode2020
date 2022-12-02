print('Science for Hungry People')

# https://stackoverflow.com/questions/7748442/generate-all-possible-lists-of-length-n-that-sum-to-s-in-python
def sums(length, total_sum):
    if length == 1:
        yield (total_sum,)
    else:
        for value in range(total_sum + 1):
            for permutation in sums(length - 1, total_sum - value):
                yield (value,) + permutation


with open('data.txt', 'r') as file:
    ingredients_data = file.read().split('\n')

with open('test.txt', 'r') as test_file:
    test_ingredients = test_file.read().split('\n')

class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories) -> None:
        self.name = name
        self.capacity = capacity
        self.flavor = flavor
        self.texture = texture
        self.durability = durability
        self.calories = calories

    def __str__(self) -> str:
        return f'{self.name} | cap {self.capacity} | fla {self.flavor}'


def format_ingredients(ingredient):
    name, _, capacity, _, durability, _, flavor, _, texture, _, calories = ingredient.split(' ')
    ing = Ingredient(
        name.replace(':', ''),
        int(capacity.replace(',', '')),
        int(durability.replace(',', '')),
        int(flavor.replace(',', '')),
        int(texture.replace(',', '')),
        int(calories)
    )
    return ing


def calc_recipe(ingredients, get_cal_replacement=False):
    ingredients = [format_ingredients(i) for i in ingredients]
    quantity_permutations = list(x for x in sums(len(ingredients), 100) if 0 not in x)
    calculation = []
    calories = []
    for qp in quantity_permutations:
        cap = 0
        dur = 0
        fla = 0
        tex = 0
        cal = 0
        for i, v in enumerate(qp):
            cap += v * ingredients[i].capacity
            dur += v * ingredients[i].durability
            fla += v * ingredients[i].flavor
            tex += v * ingredients[i].texture
            cal += v * ingredients[i].calories
        cap = cap if cap > 0 else 0
        dur = dur if dur > 0 else 0
        fla = fla if fla > 0 else 0
        tex = tex if tex > 0 else 0
        calc = cap * dur * fla * tex
        calculation.append(calc)
        calories.append(cal)
    if get_cal_replacement:
        index_500s = [i for i, x in enumerate(calories) if x == 500]
        return max(calculation[i] for i in index_500s)
    return max(calculation)

print('Part 1')
print(f'Test: {calc_recipe(test_ingredients)}')
print(f'Data: {calc_recipe(ingredients_data)}')
print('Part 2')
print(f'Test: {calc_recipe(test_ingredients, True)}')
print(f'Data: {calc_recipe(ingredients_data, True)}')

