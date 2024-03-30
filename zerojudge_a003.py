M,D = input().split()
S=(int(M)*2+int(D))%3

if S == 0:
    print("普通")
elif S == 1:
    print("吉")
elif S==2:
    print("大吉")