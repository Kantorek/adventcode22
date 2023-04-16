def tail(x_head: int, y_head: int, x_tail: int, y_tail: int, 
  x_prev: int, y_prev: int) -> list:
  if abs(x_tail-x_head) > 1 or abs(y_tail-y_head) > 1:
    return [x_prev, y_prev]
  return [x_tail, y_tail]


size = 3000
matrix = [['-' for x in range(size)] for _ in range(size)]
step = 0
y, x = int(len(matrix[0])/2), int(len(matrix[0])/2)
#y, x = 5, 0
path = [[y, x]]
y_t, x_t = y, x
new_tail = [0, 0]
matrix[y][x] = 's'
sum = 0


for line in open('day9/input'):
  way = line[0]
  length = int(line[2])
  if way == 'D':
    while length:
      y += 1
      path.append([y, x])
      new_tail = tail(x, y, x_t, y_t, path[-2][1], path[-2][0])
      x_t = new_tail[0]
      y_t = new_tail[1]
      matrix[y_t][x_t] = '#'
      length -= 1
  elif way == 'U':
    while length:
      y -= 1
      path.append([y, x])
      new_tail = tail(x, y, x_t, y_t, path[-2][1], path[-2][0])
      x_t = new_tail[0]
      y_t = new_tail[1]
      matrix[y_t][x_t] = '#'
      length -= 1
  elif way == 'L':
    while length:
      x -= 1
      path.append([y, x])
      new_tail = tail(x, y, x_t, y_t, path[-2][1], path[-2][0])
      x_t = new_tail[0]
      y_t = new_tail[1]
      matrix[y_t][x_t] = '#'
      length -= 1
  elif way == 'R':
    while length:
      x += 1
      path.append([y, x])
      new_tail = tail(x, y, x_t, y_t, path[-2][1], path[-2][0])
      x_t = new_tail[0]
      y_t = new_tail[1]
      matrix[y_t][x_t] = '#'
      length -= 1

for row in matrix:
  #print(row)
  for col in row:
    if col == '#':
      sum += 1

print(sum)