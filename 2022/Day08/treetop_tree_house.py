print('Treetop Tree House')

with open('data.txt', 'r') as file:
    tree_map = [[int(y) for y in x] for x in file.read().split('\n')]

with open('test.txt', 'r') as test_file:
    test_tree_map = [[int(y) for y in x] for x in test_file.read().split('\n')]


def visible_trees(trees):
    v_trees = (len(trees) * 2 + len(trees[0]) * 2) - 4
    for i, r in enumerate(trees):
        if len(trees) - 1 > i > 0:
            for j, c in enumerate(r):
                if len(r) - 1 > j > 0:
                    if c > max(r[:j])\
                        or c > max(r[j+1:])\
                        or c > max(x[j] for x in trees[:i])\
                        or c > max(x[j] for x in trees[i+1:]):
                        v_trees += 1
    return v_trees

print('Part 1')
print(f'Test: {visible_trees(test_tree_map)}')
print(f'Data: {visible_trees(tree_map)}')


def navigate(value: int, trees: list):
    if len(trees) == 0:
        return 0
    next_tree = trees.pop(0)
    if next_tree >= value:
        return 1
    if next_tree < value:
        return 1 + navigate(value, trees)
    return 0

def scenic_score(trees):
    score = 0
    for i, r in enumerate(trees):
        if len(trees) - 1 > i > 0:
            for j, c in enumerate(r):
                if len(r) - 1 > j > 0:
                    left = navigate(c, r[:j][::-1])
                    right = navigate(c, r[j+1:])
                    top = navigate(c, [x[j] for x in trees[:i]][::-1])
                    bottom = navigate(c, [x[j] for x in trees[i+1:]])
                    # print(top, left, right, bottom)
                    # print(f'====== {c} ======')
                    # print(f'TOP:    {[x[j] for x in trees[:i]][::-1]}\t{top}')
                    # print(f'LEFT:   {r[:j][::-1]}\t{left}')
                    # print(f'RIGHT:  {r[j+1:]}\t{right}')
                    # print(f'BOTTOM: {[x[j] for x in trees[i+1:]]}\t{bottom}')
                    v_trees = left * right * top * bottom
                    if v_trees >= score:
                        # print(i, j)
                        score = v_trees
    return score

print('Part 2')
print(f'Test: {scenic_score(test_tree_map)}')
print(f'Data: {scenic_score(tree_map)}')  # 2112000 too high
