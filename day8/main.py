forrest = []
tree_see = 0
for line in open('day8/test'):
  line = line.replace('\n', '')
  forrest.append(line)
width = len(forrest)
length = len(forrest[0])
print(forrest)
tree_see = 2 * (width + length) - 4
print("Trees on the edge: {}".format(tree_see))
for i, u2d in enumerate(forrest[1:-1]):
  for j, l2r in enumerate(u2d[1:-1]):
    pass
