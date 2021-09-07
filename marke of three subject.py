h = int(input("Enter the Hindi mark = "))
e = int(input("Enter the English mark = "))
m = int(input("Enter the Math mark = "))
if m<40 or h<40 or e<40:
    print("Failed")
else:
    per = (m + h + e) * 100 / 300
    print("Student get =",per," percentage. \n")
    if per >= 60:
        print("first Division")
    elif (per >= 50):
        print("Second division")
    else:
        print("Third")