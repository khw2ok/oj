n = int(input())

l = []

for _ in range(n):
  s = input()
  add = 0

  for i, j in enumerate(s):
    if j in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']: add += int(j)

  l.append((s, len(s), add))

# print(l) # serial, len, add, dic

def bubbleSort(a: [], n: int) -> []:
  for i in range(n):
    for j in range(n-1):
      # print(f"- {j}: {a[j]}, {j+1}: {a[j+1]}")
      if a[j][1] < a[j+1][1]:
        continue
      elif a[j][1] > a[j+1][1]:
        # print("swap for len")
        a[j], a[j+1] = a[j+1], a[j]
        continue

      if a[j][2] < a[j+1][2]:
        continue
      elif a[j][2] > a[j+1][2]:
        # print("swap for len")
        a[j], a[j+1] = a[j+1], a[j]
        continue

      if a[j][0] < a[j+1][0]:
        continue
      elif a[j][0] > a[j+1][0]:
        # print("swap for dic")
        a[j], a[j+1] = a[j+1], a[j]

      # print("except")

    # print()
  return a

print("\n".join(map(lambda x: x[0], bubbleSort(l, n))))

