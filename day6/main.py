for data in open('day6/input'):
  marker = list(reversed(data[0:3]))
  for i, letter in enumerate(data[3:-1]):
    marker.insert(0, letter)
    if len(set(marker)) == len(marker):
      print("Id of last letter of marker: {}".format(i+4))
      break
    marker.pop()
  print(marker)