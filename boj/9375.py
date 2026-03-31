from sys import stdin

t = int(stdin.readline().rstrip())

for _ in range(t):
  n = int(stdin.readline().rstrip())
  c = {}

  for _ in range(n):
    name, category = stdin.readline().rstrip().split()

    if category not in c: c[category] = 0
    c[category] += 1

  s = 1
  for i in map(lambda x: x+1, c.values()): s *= i

  print(s-1)
