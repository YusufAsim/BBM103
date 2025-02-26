year = int(input("please enter a year:"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("{} year is a leap year".format(year))
        else:
            print("{} year is a common year".format(year))
    else:
        print("{} year is a leap year".format(year))
else:
    print("{} year is a common year".format(year))

