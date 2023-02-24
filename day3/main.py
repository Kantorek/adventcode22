low_crt = 96 # sub to get correct val {1, 26}
up_crt = 38 # sub to get correct val {27, 52}
sum = 0
for line in open('day3/input'):
  line_center = int((len(line) - 1) / 2)
  for letter in line[:line_center]:
    if letter in line[line_center:]:
      print(letter)
      if letter.isupper():
        sum = sum + ord(letter) - up_crt
      elif letter.islower():
        sum = sum + ord(letter) - low_crt
      else:
        print("???")
        break
      break

print("Sum of all repeting letters is: {}".format(sum))
