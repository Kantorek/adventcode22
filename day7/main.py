dir_list = {'home/': 0}
path = 'home'
for com in open('day7/test'):
  com = com.replace('\n', '')
  if com[2:] == 'cd /':
    pass
  elif com[2:] == 'cd ..':
    path = path[:path.rfind('/')]
  elif com[2:4] == 'cd':
    path = path + '/' + com[5:]
    dir_list.update({path: 0})
print(dir_list)