cycle = 0
check = [19, 59, 99, 139, 179, 219]
sum_check = []
x = 1

for line in open('day10/input'):
  if line[0] == 'n':
    cycle += 1
    if cycle in check:
      print(x, (cycle+1) * x)
      sum_check.append((cycle+1) * x)
  else: 
    com, val  = line.split()
    val = int(val)
    cycle += 1
    if cycle in check:
      print(x, (cycle+1) * x)
      sum_check.append((cycle+1) * x)
    cycle += 1
    x += val
    if cycle in check:
      print(x, (cycle+1) * x)
      sum_check.append((cycle+1) * x)
    
print(sum(sum_check))