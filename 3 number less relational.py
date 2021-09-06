a = 3
b = 2
c = 1
if a <= b and a <= c:
    less = a
else:
    if b <= c:
        less = b
    else:
        less = c
print(less)
if a <= b and a <= c:
    less=a
elif b<=c:
    less = b
else:
   less = c

print(less)