n = int(input())
node = list(map(int, input().split()))
r = int(input())

g = [[0]*n for _ in range(n)]

def check():
  print("[")
  print("\n".join([", ".join(map(str, i)) for i in g]))
  print("]")

root_id: int

for i in range(n):
  if node[i] == -1:
    root_id = i
    continue
  g[node[i]][i] = 1

def search(_id: int):
  cur = g[_id]
  cnt = 0

  # print("s", _id)

  t = 0
  for i in range(n):
    if i == r: continue
    if cur[i]: t = 1; break

  if not t: return 1
  for i in range(n):
    if i != r and cur[i]:
      cnt += search(i)

  return cnt

print(0 if root_id == r else search(root_id))
