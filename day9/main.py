def tail(x_head: int, y_head: int, x_tail: int, y_tail: int) -> (int, int):
  if abs(x_head-x_tail) > 1 or abs(y_head-y_tail) > 1:
    matrix[y_tail][x_tail] = '#'
    x_tail = x_head_p
    y_tail = y_head_p

size = 6
matrix = [['-' for x in range(size)] for _ in range(size)]
step = 0
x, y = int(len(matrix[0])/2), int(len(matrix[0])/2)
x, y = 0, 5
x_t, y_t = 0, 5
matrix[x][y] = 's'

for line in open('day9/test'):
  way = line[0]
  length = int(line[2])
  if way == 'D':
    while length:
      y_p = y 
      y += 1
      tail(x, y, x_t, y_t)
      length -= 1
  elif way == 'U':
    while length:
      y_p = y
      y -= 1
      tail(x, y, x_t, y_t)
      length -= 1
  elif way == 'L':
    while length:
      x_p = x
      x -= 1
      tail(x, y, x_t, y_t)
      length -= 1
  elif way == 'R':
    while length:
      x_p = x
      x += 1
      tail(x, y, x_t, y_t)
      length -= 1

for row in matrix:
  print(row)