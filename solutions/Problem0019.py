daysPerMonth = [31,28,31,30,31,30,31,31,30,31,30,31]

dayOfWeek = 1

count = 0
#iterate through each month of each year and check if its a sunday
for year in range(1900,2001):
    for month in range(12):
        # if we find a sunday but don't count 1900
        if dayOfWeek == 0 and year >= 1901:
            count += 1
        # check for leap years
        if month == 1 and (year % 4 ==0 and year % 100 != 0 or year % 400 == 0):
            dayOfWeek = (dayOfWeek + daysPerMonth[month] + 1) % 7
        else:
            dayOfWeek = (dayOfWeek + daysPerMonth[month]) % 7

print(count)
        
