

class practical:
    def matrixMultiplication(this):
        a=[[1,3,2],[1,4,5],[1,1,1]];
        b=[[1,3,2],[1,4,5],[1,1,1]];
        c=[[0,0,0],[0,0,0],[0,0,0]];

        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    c[i][j]+=a[i][k]*b[k][j];

        print(c);
    def gcdOfNumber(this):
        a=5;
        b=10;
        i=1;
        while i<=a and i<=b:
            if a%i==0 and b%i==0:
                gcd=i
                
            i=i+1;
        
        print(gcd);
    
    def exponentOfNumber(this,exponent,number):
        this.exponent=exponent;
        print(number**this.exponent);
    
    def maxNumberOfList(this):
        list=[1,5,3,2,6,8,4];
        max=list[0];
        for i in range(len(list)):
            if max<list[i]:
                max=list[i];
        
        print(max);
    
    def linearSearch(this,key):
        list=[1,5,3,2,6,8,4];
        this.key=key;
        for i in list:
            if i==this.key:
                print("found");
                break;
        else:
            print("not found");
    
    def binarySearch(this,key):
        this.key=key;
        list=[1,2,3,4,5,6,7];
        low=0;
        high=len(list)-1;
        while low<=high:
            mid=low+(high-low)//2;
            if list[mid]==key:
                print("found");
                print(mid);
                break;
            elif list[mid]<key:
                low=mid+1;
            else:
                high=mid-1;
        else:
            print("not found");

    def primeNumbersTillN(this,number):
        this.number=number;
        if this.number==0 or this.number==1:
            print("not prime");
        else:
            for num in range(2,number+1):
                i=2;
                for i in range(2,num):
                    if num%i==0:
                        i=num;
                        break;
                if i!=num:
                    print(num)
    
    def insertionSort(this):
        list=[1,3,2,6,4,5];
        n=len(list);
        for i in range(1,n,1):
            key=list[i];
            j=i-1;
            while list[j]>key:
                list[j+1]=list[j];
                j=j-1;
            list[j+1]=key;
        
        print(list);

    def selectionSort(this,list):
        size=len(list);
        for i in range(size):
            minIndex=i;
            for j in range(i+1,size):
                if list[j]<list[minIndex]:
                    minIndex=j
                    
        (list[i],list[minIndex])=(list[minIndex],list[i]);

        


            





    
practical=practical();
practical.matrixMultiplication();
practical.gcdOfNumber();
practical.exponentOfNumber(2,2);
practical.maxNumberOfList()
practical.linearSearch(1
)
practical.binarySearch(77)
practical.primeNumbersTillN(100);
practical.insertionSort();
list=[1,3,2,6,4,5];

practical.selectionSort(list);
print(list)




