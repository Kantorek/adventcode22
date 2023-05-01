cycle = 0
# check = [39, 79, 119, 159, 199]
check = [40, 80, 120, 160, 200]
line = ['.']
x = 2

for l in open('day10/input'):
  if l[0] == 'n':
    cycle += 1
    if cycle in check:
      print(''.join(line[1:]))
      line = []
      cycle = 0
    if abs(cycle-x) <= 1:
      line += '#'
    else:
      line += '.'
    
  else: 
    com, val  = l.split()
    val = int(val)
    cycle += 1
    if cycle in check:
      print(''.join(line[1:]))
      line = []
      cycle = 0
    if abs(cycle-x) <= 1:
      line += '#'
    else:
      line += '.'
    cycle += 1
    if cycle in check:
      print(''.join(line[1:]))
      line = []
      cycle = 0
    if abs(cycle-x) <= 1:
      line += '#'
    else:
      line += '.'
    x += val