x=lambda a,b:a*b;
print(x(2,3))

def doubler(number):
    return lambda a:a*number;

doubleIt=doubler(2);
print(doubleIt(4));