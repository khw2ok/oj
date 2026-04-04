a, b = map(int, input().split())

ya, xa = (a-1)%4, (a-1)//4
yb, xb = (b-1)%4, (b-1)//4

print(abs(yb-ya)+abs(xb-xa))
