#compoudintrest
p = int(input("Enter the principal = "))
r = int(input("Enter the rate = "))
t = int(input("Enter the time = "))
print("p,r,t")
si=p*r*t/100
ci = p * (1 + r / 100)**t -p
print("compound intrest ",ci,si)
