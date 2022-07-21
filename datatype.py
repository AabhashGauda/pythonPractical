#datatypes
"""  Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""


#setting the datatype
x="hello world" #str
x=20 #int
x=20.5 # float
x=1j #complex
x=["apple","banana","cherry"] #list
x=("apple","banana","cherry") #tuple
x=range(6) #range
x={"name":"jhon","age":36} #dict :- it is key value pair data 
x={"apple","banana","cherry"} #set

x=True #boolean


# to set the specific datatype we use constructor function

x=str("hello world");
print(x);
x=int(20);
print(x);
x=float(20.5);
print(x);
x=complex(1j); # in this j act as i in complex number (imaginary number)
print(x);
x=list(['apple','banana']);
print(x);
x=tuple(('apple','mango'));
print(x);
x=range(5);
print(x);
x=dict(name="jhon",age=14);
print(x);
x=set(("apple","orange"));

print(x);

import random; # it is inbuilt module
print(random.randrange(1,5)); # random number is printed not including the 5