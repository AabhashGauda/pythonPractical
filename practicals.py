# 1. matrix multiplication
# a=[[1,2,3],[3,2,1],[1,3,2]];
# b=[[4,5,6],[7,8,9],[1,2,3]];
# c=[[0,0,0],[0,0,0],[0,0,0]];

# for i in range(len(a)):
#     for j in range(len(b[0])):
#         for k in range(len(b)):
#             c[i][j]+=a[i][k]*b[k][j];

# print(c);

#2. gcd of two numbers
# a=int(input("enter the first number "));
# b=int (input("enter the first number "));
# i=1
# while i<=a and i<=b:
#     if a%i==0 and b%i==0:
#         gcd=i;
#     i=i+1;

# print(gcd);

#gcd with math

# from math import gcd;
# a=5;
# b=5;
# result=gcd(a,b);
# print(result);


# maximum form list of numbers

# list=[1,2,3,4,5,6,10,9,7,5];

# max=list[0];
# for i in range(len(list)):
#     if max<list[i]:
#         max=list[i];

# print(max)


# exponent of a number

# a=2;
# b=3;

# print(a**b);

# linear search

# list=[1,4,2,5,3,7];
# number=5
# for i in list:
#     if i==number:
#         print("found")
#         break;
    
# binary search

arr=[1,2,3,4,5,6,7];
low=0;
high=len(arr)-1;
key=7;
ans=0;
while low<=high:
    mid=low+(high-low)//2;
    
    if arr[mid]==key:
        print("found ",mid);
        break;
    elif arr[mid]<key:
        low=mid+1;
    else:
        high=mid-1;

if low>high:
    print("not found")
    


