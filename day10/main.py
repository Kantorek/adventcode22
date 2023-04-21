cycle = 0
for line in open('day10/test'):
  if line[0] == 'n':
    cycle += 1
    continue
  com, val  = line.split()
  val = int(val)
  print(val)
print(cycle)