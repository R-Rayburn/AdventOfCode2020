import re
from functools import reduce
paren_pattern = re.compile('\\([0-9*+\\s]*\\)')
sum_pattern = re.compile('\\d+\\s\\+\\s\\d+')


def solve_equation(equation_to_solve):
    e = equation_to_solve
    while '+' in e:
        instance = re.search(sum_pattern, e).group()
        summation = str(sum([int(x) for x in instance.split(' + ')]))
        e = e.replace(instance, summation, 1)
    if '*' in e:
        return reduce((lambda x, y: x * y), [int(x) for x in e.split(' * ')])
    return int(e)


with open('data.txt', 'r') as f:
    equations = [x for x in f.read().split('\n') if x]
total_sum = 0

for equation in equations:
    while '(' in equation:
        paren_equation = paren_pattern.search(equation).group()
        paren_solution = solve_equation(paren_equation[1:-1])
        equation = equation.replace(paren_equation, str(paren_solution))
    solution = solve_equation(equation)
    total_sum += solution
print(total_sum)
