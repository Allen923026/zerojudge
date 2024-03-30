while True:
    try:
        year = input()
        if (int(year)%4 == 0 and int(year)%100!=0 or  int(year)%400==0):
            print("閏年")
        else:
            print("平年")
    except:
        break