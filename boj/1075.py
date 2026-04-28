n = int(input())
f = int(input())
m = n//100*100
while 1:
  if m%f == 0: break
  m += 1
print(f"0{m%100}" if len(str(m%100)) == 1 else m%100)
