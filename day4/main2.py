first_sectors = []
second_sectors = []
sec_overlap = []
set_of_id = set()
for line in open('day4/test'):
  line = line.replace('\n', '')
  line = line.replace('-', ',')
  line = line.split(',')
  print(line)
  for id in range(int(line[0]), int(line[1])+1):
    first_sectors.append(id)
  for id in range(int(line[2]), int(line[3])+1):
    second_sectors.append(id)
  print(first_sectors, second_sectors)

  for sec in first_sectors:
    if sec in second_sectors:
      sec_overlap.append(sec)
  
  if sec_overlap:
    start_id = sec_overlap[0]
    end_id = sec_overlap[-1]
    if start_id == end_id:
      set_of_id.add(start_id)
    else:
      set_of_id.add((start_id, end_id))
  first_sectors.clear()
  second_sectors.clear()
  sec_overlap.clear()
print(len(set_of_id))