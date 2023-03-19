dir_list = {'home': 0}
path = 'home'
is_listing = False
small_files_size = 0
disk_size = 70000000
update_size = 30000000
dir_to_delete = disk_size
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
      size = com[:com.rfind(' ')]
      loc = 'home'
      for location in path.split('/'):
        if location != 'home':
          loc = loc + '/' + location
        dir_list[loc] = dir_list[loc] + int(size)
print(dir_list)
free_space = disk_size - dir_list['home']
for size in dir_list.values():
  if size <= 100000:
    small_files_size = small_files_size + size
  if size >= update_size - free_space:
    dir_to_delete = min(size, dir_to_delete)
print("Small file size is: {}".format(small_files_size))
print("Directory to delete take: {}".format(dir_to_delete))
