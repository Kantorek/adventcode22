dir_list = {}
def is_dir(x: str):
  if x[0:3] == 'dir' and x[4] not in dir_list.keys():
    dir_list.update({x[4]: 0})
term_data = []
for data in open('day7/test'):
  data = data.replace('\n', '')
  term_data.append(data)
  is_dir(data)
print(term_data)
print(dir_list)