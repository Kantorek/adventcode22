draw_dic = {'A': 'X', 'B': 'Y', 'C': 'Z'}
win_dic = {'A': 'Y', 'B': 'Z', 'C': 'X'}
bonus_points_dic = {'X': 1, 'Y': 2, 'Z': 3}
points = 0
for line in open('day2/input'):
  op = line[0]
  you = line[2]
  if draw_dic.get(op) == you:
    # draw
    points = points + 3 + bonus_points_dic.get(you)
  elif win_dic.get(op) == you:
    # win
    points = points + 6 + bonus_points_dic.get(you)
  else:
    # lose
    points = points + bonus_points_dic.get(you)
print(points)