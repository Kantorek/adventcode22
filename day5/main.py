crates = [ [] for _ in range(9)]
for line in open('day5/input.txt'):
  
  if line[0] != '[':
    break
  lineEmp = line.replace('    ', ' [0]')
  line = lineEmp.replace('[', '')
  line = line.replace(']\n', '')
  line = line.split('] ')
  for col in range(len(line)):
    if line[col] != '0':
      crates[col].append(line[col])
  print(line)
print(crates)