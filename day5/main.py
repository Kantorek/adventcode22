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
      crates[col].insert(0, line[col])
  
print(crates)

for line in open('day5/input.txt'):
  if line[0] == 'm':
    line = line.replace('\n', '')
    line = line.replace('move ', '')
    line = line.replace('from ', '')
    line = line.replace('to ', '')
    line = line.split(' ')
    num_of_crates, take_pile, dest_pile = int(line[0]), int(line[1])-1, int(line[2])-1
    for num in range(num_of_crates):
      crates[dest_pile].append(crates[take_pile].pop())
print(crates)

for last in range(len(crates)):
  print(crates[last][-1])
