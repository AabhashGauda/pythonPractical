myList=["apple","mango","cherry","apple"];
print(myList);

print(myList[1]);

#checking the value is in the list
if "apple" in myList:
    print("yes ");

#change item value
myList[2]="banana";
print(myList)

#to insert the value or item in the list
myList.insert(2,"watermelon");
print(myList);

myList.append("orange"); #this will add the value in the end of the list

#extend() this is use to concat two list or any other collection datatype

myList.remove("banana");
print(myList);
myList.pop(1); # remove element from the index 1
print(myList);
myList.pop(); # removes element form the last
print(myList);

myList.clear();
print(myList);
