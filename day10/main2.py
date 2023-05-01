cycle = 0
# check = [39, 79, 119, 159, 199]
check = [40, 80, 120, 160, 200]
line = []
x = 1

def sprite(c: int, pos: int, line: list) -> str:
  if c in check:
    print()
    line = []
    return line
  else:
    if pos + 1 > c and pos - 1 < c:
      return '#'
    else:
      return '.'

for l in open('day10/test'):
  if l == 'noop\n':
    cycle += 1
    line.append(sprite(cycle, x, line))
  else: 
    com, val  = l.split()
    val = int(val)
    cycle += 1
    line.append(sprite(cycle, x, line))
    cycle += 1
    x += val
    line.append(sprite(cycle, x, line))

