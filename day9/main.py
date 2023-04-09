def tail(x_head: int, y_head: int, x_tail: int, y_tail: 
  int, x_prev: int, y_prev: int) -> list:
  if abs(x_head-x_tail) >= 1 or abs(y_head-y_tail) >= 1:
    matrix[y_tail][x_tail] = '#'
    return [x_prev, y_prev]
  return [x_tail, y_tail]


size = 6
matrix = [['-' for x in range(size)] for _ in range(size)]
step = 0
# y, x = int(len(matrix[0])/2), int(len(matrix[0])/2)
y, x = 5, 0
x_p, y_p = 0, 0
y_t, x_t = 5, 0
new_tail = [0, 1]
matrix[y][x] = 's'

for line in open('day9/test'):
  way = line[0]
  length = int(line[2])
  if way == 'D':
    while length:
      y_p = y 
      y += 1
      new_tail = tail(x, y, x_t, y_t, x_p, y_p)
      x_t = new_tail[0]
      y_t = new_tail[1]
      length -= 1
  elif way == 'U':
    while length:
      y_p = y
      y -= 1
      new_tail = tail(x, y, x_t, y_t, x_p, y_p)
      x_t = new_tail[0]
      y_t = new_tail[1]
      length -= 1
  elif way == 'L':
    while length:
      x_p = x
      x -= 1
      new_tail = tail(x, y, x_t, y_t, x_p, y_p)
      x_t = new_tail[0]
      y_t = new_tail[1]
      length -= 1
  elif way == 'R':
    while length:
      x_p = x
      x += 1
      ew_tail = tail(x, y, x_t, y_t, x_p, y_p)
      x_t = new_tail[0]
      y_t = new_tail[1]
      length -= 1

for row in matrix:
  print(row)