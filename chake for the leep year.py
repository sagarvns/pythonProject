#leep year
year = 2000#int(input("Enter in your leep year = "))
if year % 400 == 0:
    print(year, "this is leap Year")
elif year % 4 == 0 and year % 100 != 0:
    print(year,"thise is leap Year")
else:
    print(year,"not leap year")
