month = int(input("Month = \n"))

if month==1 or month==3 or month ==5 or month ==7 or month ==8 or month==10 or month==12:
    print(31)
elif month == 4 or month ==6 or month ==9 or month ==11 :
    print(30)
elif month > 12 or month <=0:
    print("Please Enter the month between 1 to 12 ")
else:
    year = int(input("Year = \n"))
    if (year % 400 == 0) or (year % 4==0 and year % 100!=0):
        print(29)
    else:
        print(28)



