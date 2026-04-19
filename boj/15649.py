n, m = map(int, input().split())

def bt(l: list):
  if len(l) == m:
    print(*l)
    return
  for i in range(1, n+1):
    if i not in l: bt(l+[i])
  return

bt([])
