from sys import stdin

n = int(stdin.readline().rstrip())
a, b = map(int, stdin.readline().rstrip().split())
m = int(stdin.readline().rstrip())

g = [[0]*n for _ in range(n)]

for _ in range(m):
  x, y = map(lambda x: int(x)-1, stdin.readline().rstrip().split())

  g[x][y] = 1
  g[y][x] = 1

# print("\n".join([", ".join(map(str, i)) for i in g]))

vis = set([a-1])

def search(x, c):
  t = 0

  if x == b-1:
    print(c)
    return 1

  for i in range(n):
    if g[x][i] and i not in vis:
      vis.add(i)
      t += search(i, c+1)

  return t

if search(a-1, 0) == 0: print(-1)
