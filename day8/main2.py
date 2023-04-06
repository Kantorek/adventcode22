forrest = []
tree_point = 0
col_for = []
for line in open('day8/test'):
  line = line.replace('\n', '')
  forrest.append(list(map(int,line)))

print("Trees on the edge: {}".format(tree_point))
for i, u2d in enumerate(forrest):
  for j, l2r in enumerate(u2d):
    for col in range(len(forrest[0])):
      col_for.append(forrest[col][j])
    north = col_for[:i]
    south = col_for[i+1:]
    west = u2d[:j]
    east = u2d[j+1:]
    print(north, south, west, east)
    col_for = []
print("Visible trees: {}".format(tree_point))