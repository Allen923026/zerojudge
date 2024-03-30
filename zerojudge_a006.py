import math
a,b,c = map(int,input().split())

t = (b*b)-(4*a*c)
if t<0:
    print("No real root")
else:
    x1 = int((-1*b + math.sqrt(t))/(2*a))
    x2 = int((-1*b - math.sqrt(t))/(2*a))

    if x1>x2:
        print('Two different roots x1={:d} , x2={:d}'.format(x1,x2))
    elif x2>x1:
        print('Two different roots x1={:d} , x2={:d}'.format(x1,x2))
    elif x1 == x2:
        print(f"Two same roots x={x1}")