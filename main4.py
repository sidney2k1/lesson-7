a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
avg=(a+b+c)/3
if avg>a and avg>b and avg>c:
    print("%d is higher than %d,%d,%d" %(avg,a,b,c))
elif avg>a and avg>b:
    print("%d is higher than %d,%d" %(avg,a,b))
elif avg>a and avg>c:
    print("%d is higher than %d,%d" %(avg,a,c))
elif avg>c and avg>b:
    print("%d is higher than %d,%d" %(avg,c,b))
elif avg>a:
    print("%d is higher than %d" %(avg,a))
elif avg>b:
    print("%d is higher than %d" %(avg,b))
elif avg>c:
    print("%d is higher than %d" %(avg,c))
else:
    print("invalid input")