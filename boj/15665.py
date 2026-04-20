n, m = map(int, input().split())
a = list(map(int, input().split()))
s = set()

a.sort()

def bt(l: list):
  if len(l) == m:
    if tuple(l) not in s:
      s.add(tuple(l))
      print(*l)
    return
  for i in a:
    bt(l+[i])
  return

bt([])
