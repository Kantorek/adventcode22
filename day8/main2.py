def tree_score(trees: list) -> int:
  tree_points = 1
  highest_tree = trees.pop()
  while trees:  
    if trees[-1] >= highest_tree:
      tree_points = tree_points + 1
      highest_tree = trees[-1]
    trees.pop()
  return tree_points
forrest = []
tree_score = 0
col_for = []
for line in open('day8/test'):
  line = line.replace('\n', '')
  forrest.append(list(map(int,line)))

for i, u2d in enumerate(forrest):
  for j, l2r in enumerate(u2d):
    for col in range(len(forrest[0])):
      col_for.append(forrest[col][j])
    c_tree = u2d
    north = col_for[:i]
    south = col_for[i+1:].reverse()
    west = u2d[:j]
    east = u2d[j+1:].reverse()
    
      
    col_for = []
print("Visible trees: {}".format(tree_point))