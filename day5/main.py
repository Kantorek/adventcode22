for line in open('day5/input.txt'):
  
  if line == 'move 2 from 5 to 9\n':
    break
  lineEmp = line.replace('    ', ' [0]')
  line = lineEmp.replace('[', '')
  line = line.replace('\n', ' ')
  line = line.split('] ')
  print(line)