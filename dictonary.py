# dictionary is a collection of key value pairs

myDict={
    "name":"name",
    "email":"email@email.com",
    "marks":[1,2,3,4],
    "parents":{
        "parentName":"parentName",
        "mobileNumber":12345
    }
}

print(myDict);
print(myDict["marks"][1]); # accessing on particular index of the marks list in the dictonary
print(myDict["parents"]);
print(myDict["parents"]["parentName"]);# accessing the particular key of a dictonary inside a dictonary

print(myDict.values());
print(myDict.keys());
updateDict={
    "nameThing":"some thing",
    "nameAnimal":"some animal",
    "email":"newEmail@email.com" #this will update the previous value also
}

myDict.update(updateDict);
print(myDict);