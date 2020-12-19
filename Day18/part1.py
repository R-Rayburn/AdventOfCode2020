import re


def solve_equation(equation):
    try:
        value = int(equation)
        return value
    except ValueError:
        equation = equation.split(' ')
        rmv = int(equation[-1])
        rmo = equation[-2]
        equation = ' '.join(equation[:-2])
        if rmo == '*':
            return solve_equation(equation) * rmv
        else:
            return solve_equation(equation) + rmv


def solve_paren(equations):
    solutions = []
    for equation in equations:
        solutions.append(solve_equation(equation[1:-1]))
    return solutions


with open('data.txt', 'r') as f:
    equations = [x for x in f.read().split('\n') if x]
total_sum = 0
paren_pattern = re.compile('\\([0-9*+\\s]*\\)')
for equation in equations:
    while '(' in equation:
        paren_equations = paren_pattern.findall(equation)
        paren_solutions = []
        if len(paren_equations) > 0:
            paren_solutions = solve_paren(paren_equations)
        for i in range(len(paren_solutions)):
            equation = equation.replace(paren_equations[i], str(paren_solutions[i]))
    solution = solve_equation(equation)
    total_sum += solution
print(total_sum)
