first_sectors = []
second_sectors = []
sum_of_overlaps = 0
for line in open('day4/input'):
  line = line.replace('\n', '')
  line = line.replace('-', ',')
  line = line.split(',')
  print(line)
  for id in range(int(line[0]), int(line[1])+1):
    first_sectors.append(id)
  for id in range(int(line[0]), int(line[1])+1):
    second_sectors.append(id)
  print(first_sectors, second_sectors)
  if len(first_sectors) > len(second_sectors):
    for sec in first_sectors:
      if sec not in first_sectors:
        continue
      second_sectors.remove(sec)
    if second_sectors == None:
      sum = sum + 1
  elif len(second_sectors) >= len(first_sectors):
    for sec in second_sectors:
      if sec not in second_sectors:
        continue
      first_sectors.remove(sec)

    if first_sectors == None:
      sum = sum + 1
print(sum)