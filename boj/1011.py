t = int(input())

def sumRangeX2Y(x, y):
    return (y-x+1)*(x+y)//2

for _ in range(t):
    x, y = map(int, input().split(" "))
    dis = y-x
    a = 0
    b = 0
    while True:
        tmp = sumRangeX2Y(1, a)+sumRangeX2Y(1, b)
        a += 1
        if tmp -b >= dis: break
        b += 1
        if tmp >= dis: break
    print(a + b -2)
