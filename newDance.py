'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

# add natural numbers till n

# n=5;
# i=0;
# sum=0
# while i<=n :
#     sum=sum+i;
#     i+=1;
    
# print(sum);

#while with else
# count=4;
# i=0;
# while i<count:
#     print("hello world");
#     i+=1;
# else:
#     print("no hello world");


#program to print table of given numbers
# number=2;
# for i in range(11):
#     print(i*2);

#program to find sum of n natural numbers
# n=5
# sum=0;
# for i in range(n):
#     sum=sum+i;


#list looping
# list=['apple','banana','watermelon','papaya'];
# list2=['red','yellow','green','yellowish'];

# for index in range(len(list)):
#     for index2 in range(len(list2)):
#         print(list[index],list2[index2]);


# program to print a right triangle
# n=5;
# for i in range(n):
#     for j in range(i+1):
#         print("* ",end="") # end="" is use to print the ouput in single line
#     print();


#python strings

# a="string";
# # for value in a:
# #     print(value,end="");
# for index in range(len(a)):
#     print(a[index]);

#concatination of two strings

# a="string";
# b="second string";
# print(a+b);
# print(a*4)  # this prints the value in a repeatedly
# print(len(a)); # gives the length of the string

#deleting the string
# del a
# slicing the string
# print(a[1:4]); # not including 4


#prime number check
# n=5;
# for i in range(2,int(n/2)+1):
#     if(n%i==0):
#         print("not prime");
#         break;
# else:
#     print ("prime",i);

# prime number till n
# def isPrime(n):
#     if(n==1 or n==0):
#         return False;
#     for i in range(2,n):
#         if(n%i==0):
#             return False;
#     return True;

# n=10;
# for i in range(n):
#     if(isPrime(i)):
#         print(i)

# check palindrome
data="amaama";
# if(value==value[::-1]):
#     print("yes is palindrome");
# else:
#     print("no")

# half=int(len(data)/2);
# if len(data)%2==0:
#     first=data[:half];
#     last=data[half:];
# else:
#     first=data[:half];
#     last=data[half:];

# if first==last:
#     print("symmetric");
# else:
#     print("not symmetric");

# string="amaama";
# half=int(len(string)/2);
# if len(string)%2==0:
#     first=string[:half];
#     last=string[half:];
# else:
#     first=string[:half];
#     last=string[last:];
    
# if(first==last):
#     print("symmetric");
# else:
#     print("not symmetric");

#list
# list1=[1,2,3,4,5,5,6,67];

#looping a list
# for i in list:
#     print(i);

#deleting in the list
# del list1;
# for i in list1:
#     print(i);
# list1.pop(1); # removes or pops the 1 index passed
# list1.pop();# removes element form the last
# print(list1);

#star print
# n=5;
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="");
#     print()

# for i in range(n):
#     for j in range(n-1,i,-1):
#         print("*",end="");
#     print()
    
#tuple
tuple1=(1,2,3,4,5,6);
# for i in tuple1:
#     print(i);

listTuple=list(tuple1);
print(listTuple);

tuple2=("1",)
print(tuple2)

string="string";
list1=[];
print(string)
for i in string:
    list1.append(i);
print(list1)

temp=list1[0];
list1[0]=list1[-1];
list1[-1]=temp;
value="";
for i in list1:
    value=value+i;
    
print(value)
    