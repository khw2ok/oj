from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().rstrip().split())

cam = []

q = deque()

for i in range(n):
  c = list(stdin.readline().rstrip())
  if "I" in c: q.append((i, c.index("I")))
  cam.append(c)

# print(cam)

s = set([q[0]])
cnt = 0

while q:
  cx, cy = q.popleft()
  if cam[cx][cy] == "P": cnt += 1
  # print(cx, cy, cam[cx][cy], s)
  if cx+1 < n and (cx+1, cy) not in s and cam[cx+1][cy] != "X":
    s.add((cx+1, cy))
    q.append((cx+1, cy))
  if cx-1 >= 0 and (cx-1, cy) not in s and cam[cx-1][cy] != "X":
    s.add((cx-1, cy))
    q.append((cx-1, cy))
  if cy+1 < m and (cx, cy+1) not in s and cam[cx][cy+1] != "X":
    s.add((cx, cy+1))
    q.append((cx, cy+1))
  if cy-1 >= 0 and (cx, cy-1) not in s and cam[cx][cy-1] != "X":
    s.add((cx, cy-1))
    q.append((cx, cy-1))

print(cnt if cnt else "TT")
