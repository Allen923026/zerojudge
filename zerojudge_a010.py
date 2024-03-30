num = int(input())
Count = []
result=""
i =2

if num >1 and num<= 100000000:
    while num>1:
        if(num%i==0):
            num//=i
            Count.append(i)
        else:
            if Count:
                if Count.count(i) == 1:
                    result += str(i) + " * "
                elif Count.count(i) > 1:
                    result += str(i) + "^" + str(Count.count(i)) +" * "
            i+=1
    if Count:
        if Count.count(i) == 1:
            result += str(i)
        elif Count.count(i) >1 :
            result += str(i)+"^"+str(Count.count(i))

    print(result)