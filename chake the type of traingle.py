# chake the type of triangle
a =5
b = 6
c = 7
if a == b and b == c:
    print(" Equilatrle ")
elif a == b or b == c or a == c:
    print("Isoscales")
else:
    print("Scalace")
count=0
if a==b:
    count+=1
if a==c:
    count+=1
if b==c:
    count+=1
print(count)