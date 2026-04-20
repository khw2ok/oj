n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

def bt(l: list):
  if len(l) == m:
    print(*l)
    return
  for i in a:
    if (len(l) == 0) or (l[-1] <= i): bt(l+[i])
  return

bt([])
