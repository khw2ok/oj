n, k = map(int, input().split())
l = list(input())

c = 0
b = 1
for i in l:
  if i == "1": c = 0
  else: c += 1

  if c >= k:
    b = 0
    break

print(b)
