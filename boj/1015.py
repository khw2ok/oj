n = int(input())
a = list(map(int, input().split()))

a2 = a.copy()
a2.sort()

#print(a)
#print(a2)

d = {}

for i in range(n):
  if a2[i] not in d: d[ a2[i] ] = [i]
  else: d[ a2[i] ].append(i)

#print(d)

p = []

for i in range(n-1, -1, -1):
  #print(a[i])
  p.append(d[ a[i] ].pop())

for i in range(n-1, -1, -1):
  print(p[i], end=" ")
