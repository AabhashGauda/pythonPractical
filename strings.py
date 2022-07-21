# strings are array of symbols

#single line string
x="name"

#multiline string
a=''' lorem dfad
adfadfassd
asdf
adsf'''

#looping in the strings
a="hello world"
print(a[5]); # spaces are also stored in the index

for y in a:
    print(y)

#length of string
print(len(a)); # prints the length of the string

#check string
txt = "The best things in life are free!"
print("free" not in txt); # this returns true or false weather the string is present of not present in teh string


#slicing of strings

b="helloworld"
print(b[2:5]); #prints the strings form index 2 (including) to index 5(not including)

# modifying strings
a="hello world"
print(a.upper()); # converts to the upper case
print(a.lower()); # converts to lower case

b="    hello there     "
print(a.strip()); # this strips the whitespaces form the start and the end of the string (not in between)

# replacement
print(a.replace("h","H")); #replaces h with H 


