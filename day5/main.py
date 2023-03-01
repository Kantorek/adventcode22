for line in open('day5/input.txt'):
  
  if line[0] != '[':
    break
  lineEmp = line.replace('    ', ' [0]')
  line = lineEmp.replace('[', '')
  line = line.replace(']\n', '')
  # line = line.replace('\n', '')
  line = line.split('] ')
  print(line)