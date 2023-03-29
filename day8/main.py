forrest = []
tree_see = 0
col_for = []
for line in open('day8/input'):
  line = line.replace('\n', '')
  forrest.append(list(map(int,line)))
width = len(forrest)
length = len(forrest[0])
tree_see = 2 * (width + length) - 4
print("Trees on the edge: {}".format(tree_see))
for i, u2d in enumerate(forrest[1:-1]):
  for j, l2r in enumerate(u2d[1:-1]):
    for col in range(width):
      col_for.append(forrest[col][j+1])
    if max(forrest[i+1][:j+1]) < l2r:
      print(forrest[i+1][:j+1])
      tree_see = tree_see + 1
    elif max(forrest[i+1][j+2:]) < l2r:
      print(forrest[i+1][j+2:])
      tree_see = tree_see + 1
    elif max(col_for[:i+1]) < l2r:
      print(col_for[:i+1])
      tree_see = tree_see + 1
    elif max(col_for[i+2:]) < l2r:
      print(col_for[i+2:])
      tree_see = tree_see + 1
    col_for = []
print("Visible trees: {}".format(tree_see))
# 1827