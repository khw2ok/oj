t = int(input())

for _ in range(t):
  k = int(input())
  n = int(input())

  apt = [[i for i in range(1, n+1)]]

  for i in range(1, k+1):
    apt.append([1])
    for j in range(1, n):
      apt[i].append(apt[i][j-1]+apt[i-1][j])
  print(apt[k][n-1])
