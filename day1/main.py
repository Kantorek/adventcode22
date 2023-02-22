cal_sum = 0
max_cal = []
for line in open("day1/input"):
  if line != '\n':
    cal_sum = cal_sum + int(line)
  elif line == '\n':
    max_cal.append(cal_sum)
    cal_sum = 0
  else:
    print("???")

sum_of_3 = 0
for i in range(3):
  print('Maximum of calories for {} is: {}'.format(i+1, max(max_cal)))
  sum_of_3 = sum_of_3 + max(max_cal)
  max_cal.remove(max(max_cal))
print("Sum of 3 max calories is: {}".format(sum_of_3))