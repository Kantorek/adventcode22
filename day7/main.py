dir_list = {'home': 0}
path = 'home'
is_listing = False
for com in open('day7/input'):
  com = com.replace('\n', '')
  if com[2:] == 'cd /':
    pass
  elif com[2:] == 'cd ..':
    path = path[:path.rfind('/')]
  elif com[2:4] == 'cd':
    path = path + '/' + com[5:]
    dir_list.update({path: 0})
  elif com[2:4] == 'ls':
    is_listing = True
  elif is_listing:
    if com[0] == '$':
      is_listing = False
      continue
    if com[0] != 'd':
      com = com[:com.rfind(' ')]
      dir_list[path] = dir_list[path] + int(com)
print(dir_list)
