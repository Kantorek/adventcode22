def tree_view(trees: list, x_tree: int) -> int:
  tree_points = 0
  if trees:
    highest_tree = trees.pop()
    tree_points = 1
  while trees:  
    if trees[-1] >= highest_tree:
      tree_points += 1
      highest_tree = trees[-1]
    if highest_tree >= x_tree:
      return tree_points
    trees.pop()
  return tree_points

forrest = []
tree_score = 0
col_for = []
for line in open('day8/input'):
  line = line.replace('\n', '')
  forrest.append(list(map(int,line)))

for i, u2d in enumerate(forrest):
  for j, l2r in enumerate(u2d):
    for col in range(len(forrest[0])):
      col_for.append(forrest[col][j])
    c_tree = u2d
    north = col_for[:i]
    south = col_for[i+1:]
    south_r = list()
    for item in south:
      south_r = [item] + south_r
    west = u2d[:j]
    east = u2d[j+1:]
    east_r = list()
    for item in east:
      east_r = [item] + east_r
    x = tree_view(north, l2r)*tree_view(south_r, l2r)*tree_view(west, l2r)*tree_view(east_r, l2r)
    tree_score += x
    col_for = []
print("The highest score: {}".format(tree_score))
# 335580