class Node:
  def __init__(self, x, l, r) -> None:
    self.x = x
    self.l: Node|None = l
    self.r: Node|None = r

n = int(input())
# t = ['.' for _ in range(2**n-1)]
d: dict[str, Node] = {'A': Node('A', None, None)}

for i in range(n):
  n, l, r = input().split()
  c = d[n]

  if i == 25: break

  d[l] = Node(l, None, None)
  d[r] = Node(r, None, None)
  d[n].l = d[l]
  d[n].r = d[r]

  # print(d[n].x, d[n].l.x, d[n].r.x)

def preorder(n: Node|None) -> None:
  if n == None or n.x == '.': return

  print(n.x, end='')
  preorder(n.l)
  preorder(n.r)

  return

preorder(d['A'])
print()

def inorder(n: Node|None) -> None:
  if n == None or n.x == '.': return

  inorder(n.l)
  print(n.x, end='')
  inorder(n.r)

  return

inorder(d['A'])
print()

def postorder(n: Node|None):
  if n == None or n.x == '.': return

  postorder(n.l)
  postorder(n.r)
  print(n.x, end='')

  return

postorder(d['A'])
print()
