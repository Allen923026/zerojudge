t = int(input())
while t != 0: 
    a,b,c,d = map(int, input().split())
    if (b-a) == (c-b):
        e = d +(b-a)
    else:
        e = int(d*(b/a))
    
    print(a,b,c,d,e)
    t-=1