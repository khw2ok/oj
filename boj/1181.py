import sys

inp1 = int(sys.stdin.readline().rstrip())
l1 = []
d1 = {}

for i in range(0, inp1):
  inp2 = sys.stdin.readline().rstrip()
  l1.append(len(inp2))
  if str(len(inp2)) not in d1:
    d1[str(len(inp2))] = []
  if inp2 not in d1[str(len(inp2))]:
    d1[str(len(inp2))].append(inp2)

for i in d1:
  if len(d1[i]) != 1:
    d1[i].sort()

l1.sort()

for i in l1:
  try:
    print(d1[str(i)][0])
    # d1[str(i)]
    d1[str(i)].pop(0)
  except IndexError:
    pass

# print(l1)
# print(d1)
