size = 20
matrix = [['-' for x in range(size)] for _ in range(size)]
x, y = int(len(matrix[0])/2), int(len(matrix[0])/2)
for line in open('day9/test'):
  way = line[0]
  length = int(line[2])
matrix[x][y] = 's'
for row in matrix:
  print(row)