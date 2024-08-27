print("Enter a number(Numerator):")
a=int(input())
print("Enter a number(denominator):")
b=int(input())
if a%b==0:
    print("\n" +str(a)+ " is divisible by " +str(b))
else:
    print("\n" +str(a)+ " is not divisible by " +str(b))