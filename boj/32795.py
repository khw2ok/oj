from sys import stdin

t = int(stdin.readline().rstrip())

for _ in range(t):
  a = set(stdin.readline().rstrip())
  b = set(stdin.readline().rstrip())

  print("NO" if b-a else "YES")
