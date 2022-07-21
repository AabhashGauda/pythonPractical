# import sys
# n=len(sys.argv);
# print("total arguments passed: ",n);


# matrix multiplication
# a=[[1,2,3],[1,1,1],[1,0,1]];
# b=[[1,2,4],[1,1,0],[1,0,0]];
# c=[[0,0,0],[0,0,0],[0,0,0]];
# for i in range(len(a)):
#     for j in range(len(b[0])):
#         for k in range(len(b)):
#             c[i][j]+=a[i][k]*b[k][j];

# print(c);

# matrix multiplication using numpy
# import numpy as np

# a=[[1,2,3],[1,1,1],[1,0,1]];
# b=[[1,2,4],[1,1,0],[1,0,0]];

# result=np.dot(a,b);
# print(result)

# gcd of two numbers

a=int(input("enter the number 1 "));
b=int (input("enter the number 2"));
i=1;
while(i<=a and i<=b):
    if(a%i==0 and b%i==0):
        gcd=i;
    i=i+1    

print(gcd)
