def tail(head_p: tuple(int, int), tail_p: tuple(int, int)):
  pass

size = 6
matrix = [['-' for x in range(size)] for _ in range(size)]
step = 0
x, y = int(len(matrix[0])/2), int(len(matrix[0])/2)
x, y = 0, 5
matrix[x][y] = 's'

for line in open('day9/test'):
  way = line[0]
  length = int(line[2])
  if way == 'D':
    while length:
      y += 1
      matrix[x][y] = '#'
      length -= 1
  elif way == 'U':
    while length:
      y -= 1
      matrix[x][y] = '#'
      length -= 1
  elif way == 'L':
    while length:
      x -= 1
      matrix[x][y] = '#'
      length -= 1
  elif way == 'R':
    while length:
      x += 1
      matrix[x][y] = '#'
      length -= 1

for row in matrix:
  print(row)