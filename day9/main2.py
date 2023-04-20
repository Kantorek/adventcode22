path = set([(0, 0)])

H = [0, 0]
T = [0, 0]

for line in open('day9/input'):
  way, length  = line.split()
  length = int(length)

  for _ in range(length):
    dx = 1 if way == 'R' else -1 if way == 'L' else 0
    dy = 1 if way == 'U' else -1 if way == 'D' else 0

    H[0] += dx
    H[1] += dy

    Hx = H[0] - T[0]
    Hy = H[1] - T[1]

    if abs(Hx) > 1 or abs(Hy) > 1:
      if Hx == 0:
        T[1] += Hy // 2
      elif Hy == 0:
        T[0] += Hx // 2
      else:
        T[0] += 1 if Hx > 0 else -1
        T[1] += 1 if Hy > 0 else -1
      
    path.add(tuple((T)))

print(len(path))