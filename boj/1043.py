n, m = map(int, input().split())
truth, *tp = map(int, input().split())

p = []
g = [[0]*n for _ in range(n)]

for _ in range(m):
  party, *pp = map(int, input().split())

  p.append(set(pp))

  for i in pp:
    for j in range(n):
      if j+1 in pp and (i-1 != j): g[i-1][j] = 1

#print("\n".join(", ".join(map(str, i)) for i in g))

from collections import deque

q = deque(tp)
s = set(tp)

while q:
  cur = q.popleft()
  for i in range(n):
    if g[cur-1][i] and i+1 not in s:
      q.append(i+1)
      s.add(i+1)

#print(s)

ans = 0
for i in p:
  #print(i, i-s, i == i-s)
  if i == i-s: ans += 1

print(ans)
