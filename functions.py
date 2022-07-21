def greet(name="name"):
    print("good morning "+name)

greet("dance")


def dance(name="name"):
    return name+" is a good dancer"

show=dance("user");
print(show)

def factorial(n):
    i=n
    if i == 0 or i == 1:
        return 1;
    else:
        return n*factorial(n-1);

answer=factorial(2);
print(answer)   