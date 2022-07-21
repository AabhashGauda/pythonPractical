#creating a tuple
myTuple=(1,2,3,4,5,6,1,1,1);

#printing a tuple
print(myTuple)

# we can't update the items in the tuple

print(myTuple.count(1)); #counts the number of one's
print(myTuple.index(1)); # returns the index of the  first one

# we can't update the tuple or make changes so to make changes we first need to convert it into the list then make changes example below
tupleBox=("name","name1","name2","name3");
tupleList=list(tupleBox);
tupleList.append("name5");
tupleBox=tuple(tupleList);
print(tupleBox)