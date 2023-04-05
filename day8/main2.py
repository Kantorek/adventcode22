forrest = []
tree_point = 0
col_for = []
for line in open('day8/input'):
  line = line.replace('\n', '')
  forrest.append(list(map(int,line)))
width = len(forrest)
length = len(forrest[0])
print("Trees on the edge: {}".format(tree_point))
for i, u2d in enumerate(forrest[1:-1]):
  for j, l2r in enumerate(u2d[1:-1]):
    
    col_for = []
print("Visible trees: {}".format(tree_point))