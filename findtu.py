def isleap(year):
    return (year % 4) == 0 and (year % 100 != 0 or year % 400 == 0)


def find_leap_year():
    yearlist=[]
    for year in range(1800, 2200):  # 限定搜索范围
        
        J = year // 100
        K = year % 100
        q = 29
        m = 14  # 对应到上一年的2月
        h = (q + (13*(m+1))//5 + K + (K//4) + 5 - J) % 7
        if m==14 and ( q==29 or q ==28) and  isleap(year+1)==False :
            continue
        if h == 4:  
            if m>12:
              yearlist.append(year+1)
            else:
              yearlist.append(year)
    return yearlist

year = find_leap_year()
print(f"The year when February 29th is a Thursday is: {year}")

