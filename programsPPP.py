# '''

#                             Online Python Compiler.
#                 Code, Compile, Run and Debug python program online.
# Write your code in this editor and press "Run" button to execute it.

# '''
import math;
class programs:
    def fibonacci(self,n):
        n1=0;
        n2=1;
        count=0;
        while count<n:
            print(n1);
            nth=n1+n2;
            n1=n2;
            n2=nth;
            count=count+1;
            
    def primeNumbers(self,n):
        if n==0 or n==1:
            return False;
        for i in range(2,n):
            if n%i==0:
                return False;
        return True;
    
    def bubbleSort(self):
        arr=[2,5,1,4,3];
        for i in range(0,len(arr)):
            for j in range(0,len(arr)-1):
                if(arr[j]>arr[j+1]):
                    c=arr[j];
                    arr[j]=arr[j+1];
                    arr[j+1]=c;
        print(arr);    
    
    def selectionSort(self):
        arr=[2,5,1,4,3];
        for i in range(0,len(arr)-1):
            for j in range(i+1,len(arr)):
                if arr[i]>arr[j]:
                    c=arr[i];
                    arr[i]=arr[j];
                    arr[j]=c;
        print(arr)
    
    
    def insertionSort(self):
        arr=[2,5,1,4,3];
        for i in range(1,len(arr)):
            c=i;
            while c>0 and arr[c]<arr[c-1]:
                a=arr[c];
                arr[c]=arr[c-1];
                arr[c-1]=a
                c=c-1
        print(arr);
    
    def linearSearch(self):
        arr=[2,5,1,4,3];
        key=1
        for i in range(len(arr)):
            if key==arr[i]:
                print("found")
                break;
                
    def binarySearch(self):
        arr=[1,2,3,4,5];
        key=4;
        low=0;
        high=len(arr)-1;
        while low<=high:
            mid=low+(high-low)//2;
            if arr[mid]==key:
                print("found");
                break;
            elif arr[mid]<key:
                low=mid+1;
            else:
                high=mid+1;
                
    def palindrome(self):
        string="bbabb";
        if string==string[::-1]:
            print("yes");
        else:
            print("no");
    
    def symmetric(self):
        string="amaama";
        half=int(len(string)/2);
        if len(string)%2==0:
            first=string[:half];
            last=string[half:];
        else:
            first=string[:half];
            last=string[half:];
        if first==last:
            print("yes");
        else:
            print("no");
            
    
        
    
binary=programs();
binary.binarySearch()
    
    
    
    
    
    
    
    
    
    
    
    
    
# fibo=programs();
# fibo.fibonacci(10);

# print("primenubers are")
# prime=programs();
# for i in range(10):
#     if prime.primeNumbers(i):
#         print(i);

# bubble=programs();
# bubble.bubbleSort();

# selection=programs();
# selection.selectionSort()

# insert=programs();
# insert.insertionSort();

# linear=programs();
# linear.linearSearch();

# binary=programs();
# binary.binarySearch();

# palindrome=programs();
# palindrome.palindrome()

# sym=programs();
# sym.symmetric();

# def mergeSort(arr):
#         if len(arr)>1:
#             mid=len(arr)//2;
#             l=arr[:mid];
#             r=arr[mid:];
#             mergeSort(l);
#             mergeSort(r);
#             i=j=k=0;
#             while i<len(l) and j<len(r):
#                 if l[i]<r[j]:
#                     arr[k]=l[i];
#                     i=i+1;
#                 else:
#                     arr[k]=r[j];
#                     j=j+1;
#                 k=k+1;
#             while i<len(l):
#                 arr[k]=l[i];
#                 i=i+1;
#                 k=k+1;
#             while j<len(r):
#                 arr[k]=r[j];
#                 j=j+1;
#                 k=k+1;
# arr=[2,5,1,4,3];
# mergeSort(arr);
# print(arr);

# def fibo(n):
#     if n<=1:
#         return n;
#     else:
#         return (fibo(n-1)+fibo(n-2));

# n=10;
# for i in range(n):
#     print(fibo(i));
    
    
    
# def sieve(n):
#     prime=[True for i in range(n+1)];
#     p=2;
#     while p*p<=n:
#         if(prime[p]==True):
#             for i in range(p*p,n+1,p):
#                 prime[i]=False
#         p=p+1;
#     for p in range(2,n):
#         if prime[p]:
#             print(p);

# n=50;
# sieve(n)

# def towerOfHanoi(n,a,c,b):
#     if n==1:
#         print(a,"->",c);
#         return;
#     towerOfHanoi(n-1,a,b,c)
#     print()