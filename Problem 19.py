def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
year = 1900
curr_day = 2
count = 0
while (year <= 2000):
    for month in range(1,13):
        if month in [1,3,5,7,8,10,12]:
            curr_day += 3
            curr_day %= 7
            if curr_day == 1:
                count += 1
        elif month == 2:
            if leap_year(year):
                curr_day += 1
                curr_day %= 7
                if curr_day == 1:
                    count += 1
            else:
                if curr_day == 1:
                    count += 1
        else:
            curr_day += 2
            curr_day %= 7
            if curr_day == 1:
                count += 1
    year += 1
print(count)
        
            
    
