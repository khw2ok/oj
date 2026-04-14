from sys import stdin

t = int(stdin.readline().rstrip())

for _ in range(t):
  x1, y1, r1, x2, y2, r2 = map(int, stdin.readline().rstrip().split())
  d = (x2-x1)**2+(y2-y1)**2
  s = (r1+r2)**2

  if x1 == x2 and y1 == y2: # 같은 좌표
    print(-1 if r1 == r2 else 0)
    continue

  if d < r1**2:
    # print("1번 원 안에 2번 원이 있")
    if d > (r1-r2)**2: print(2)
    elif d < (r1-r2)**2: print(0)
    else: print(1)

    continue

  if d < r2**2:
    # print("2번 원 안에 1번 원이 있")
    if d > (r2-r1)**2: print(2)
    elif d < (r2-r1)**2: print(0)
    else: print(1)

    continue

  if d > s: print(0)
  elif d < s: print(2)
  else: print(1)
