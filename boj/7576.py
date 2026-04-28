from sys import stdin
m, n = map(int, stdin.readline().rstrip().split())
box = [list(map(int, stdin.readline().rstrip().split())) for _ in range(n)]
tmt = [(x, y) for y in range(n) for x in range(m) if box[y][x] == 1]
# print(tmt)

from collections import deque
q = deque([i for i in tmt])
c = 0

while q:
  for _ in range(len(q)):
    nx, ny = q[0]
    if (nx+1 < m) and (box[ny][nx+1] == 0): box[ny][nx+1] = 2; q.append((nx+1, ny))
    if (nx-1 >= 0) and (box[ny][nx-1] == 0): box[ny][nx-1] = 2; q.append((nx-1, ny))
    if (ny+1 < n) and (box[ny+1][nx] == 0): box[ny+1][nx] = 2; q.append((nx, ny+1))
    if (ny-1 >= 0) and (box[ny-1][nx] == 0): box[ny-1][nx] = 2; q.append((nx, ny-1))
    q.popleft()
  c += 1

if any([j == 0 for i in box for j in i]): print(-1)
else: print(c-1)
