forrest = []
tree_see = 0
for line in open('day8/test'):
  line = line.replace('\n', '')
  forrest.append(line)
width = len(forrest)
length = len(forrest[0])
print(forrest)
tree_see = 2 * (width + length) - 4
print(tree_see)
