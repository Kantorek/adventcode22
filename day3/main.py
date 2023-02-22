low_crt = 96 # sub to get correct val {1, 26}
up_crt = 38 # sub to get correct val {27, 52}
for line in open('day3/input'):
  line_center = int((len(line) - 1) / 2)
  print(line_center)
  print(line[:11])
  print(line[11:])