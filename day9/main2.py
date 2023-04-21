path = set([(0, 0)])

rope = [[0, 0] for _ in range(10)]

for line in open('day9/input'):
  way, length  = line.split()
  length = int(length)

  for _ in range(length):
    dx = 1 if way == 'R' else -1 if way == 'L' else 0
    dy = 1 if way == 'U' else -1 if way == 'D' else 0

    rope[0][0] += dx
    rope[0][1] += dy

    for i in range(9):
      H = rope[i]
      T = rope[i+1]

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
        
      path.add(tuple(rope[-1]))

print(len(path))