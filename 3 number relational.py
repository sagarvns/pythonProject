a=1
b=3
c=2
if a>=b and a>=c:
    max=a
else:
    if b>=c:
        max=b
    else:
        max=c
print(max)

if a>=b and a>=c:
    max=a
elif b>=c:
    max=b
else:
    max=c
print(max)