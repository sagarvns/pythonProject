a = float(input("Enter the value A="))
b = float(input("Enter the value B="))
c = float(input("Enter the value C="))
print(a, b, c)
s = (a + b + c) / 2.0
print(s)
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

print("Area of triangle", area )

