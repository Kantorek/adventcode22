for data in open('day6/input'):
  marker = list(reversed(data[0:13]))
  for i, letter in enumerate(data[13:-1]):
    marker.insert(0, letter)
    if len(set(marker)) == len(marker):
      print("Id of last letter of marker: {}".format(i+14))
      break
    marker.pop()
  print(marker)