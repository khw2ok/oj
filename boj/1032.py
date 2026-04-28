a = int(input(""))

l1 = []
l2 = []
l3 = []
for i in range(1, a+1):
  b = input("")
  l1.append(list(b))
# print("l1 : ", l1)
for i in range(0, len(l1[0])):
  l2 = []
  # print("i : ", i)
  for j in range(0, a):
    if len(l2) != 0:
      # print("a :", l2[-1])
      # print("b :", l1[j][i])
      if l2[-1] != l1[j][i]:
        # print("A")
        l3.append(i)
    l2.append(l1[j][i])
  # print(l2)
  # print()
# print("> ", l3)
l4 = l1[0]
for k in l3:
  l4[k] = "?"
print("".join(l4))
