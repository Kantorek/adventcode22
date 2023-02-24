low_crt = 96 # sub to get correct val {1, 26}
up_crt = 38 # sub to get correct val {27, 52}
def char_to_ASCII(l: str) -> int:
  print(l)
  if l.isupper():
    return ord(l) - up_crt
  elif l.islower():
    return ord(l) - low_crt
  else:
    print("???")

sum = 0
head_of_three = []
for line in open('day3/input'):
  line = line.replace('\n', '')
  head_of_three.append(line)
  two_first = []
  print(head_of_three)
  if len(head_of_three) == 3:
    for letter in head_of_three[0]:
      if letter in head_of_three[1]:
        two_first.append(letter)
        

    for letter in head_of_three[2]:
      if letter in two_first:
        sum = sum + char_to_ASCII(letter)
        break
    head_of_three.clear()
  
print("Sum of group codes is: {}".format(sum))