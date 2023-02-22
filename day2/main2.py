shape_points = {'A': 1, 'B': 2, 'C': 3}
game_points = {'X': 0, 'Y': 3, 'Z': 6}
win_list = ['A', 'B', 'C']
points = 0
for line in open('day2/input'):
  op = line[0]
  you = line[2]
  op_id = win_list.index(op)
  points = points + game_points.get(you)
  if you == 'X':
    points = points + shape_points.get(win_list[op_id-1])
  elif you == 'Y':
    points = points + shape_points.get(win_list[op_id])
  elif you == 'Z':
    if op_id + 1 == 3:
      points = points + 1
    else:
      points = points + shape_points.get(win_list[op_id+1])
  else:
    print("???")
    break

print(points)