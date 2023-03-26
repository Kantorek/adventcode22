forrest = []
tree_see = 0
for line in open('day8/test'):
  line = line.replace('\n', '')
  forrest.append(list(map(int,line)))
width = len(forrest)
length = len(forrest[0])
print(forrest)
tree_see = 2 * (width + length) - 4
print("Trees on the edge: {}".format(tree_see))
for i, u2d in enumerate(forrest[1:-1]):
  for j, l2r in enumerate(u2d[1:-1]):
    if max(forrest[i+1][:j+1]) < l2r:
      print('TREE!')
      print(l2r)
      tree_see = tree_see + 1
    elif max(forrest[i+1][j+2:]) < l2r:
      print('TREE!')
      print(l2r)
      tree_see = tree_see + 1
print("Trees on the edge: {}".format(tree_see))
