dir_list = {'home': 0}
path = 'home'
is_listing = False
for com in open('day7/test'):
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
      size = com[:com.rfind(' ')]
      loc = 'home'
      for location in path.split('/'):
        if location != 'home':
          loc = loc + '/' + location
        dir_list[loc] = dir_list[loc] + int(size)
print(dir_list)

