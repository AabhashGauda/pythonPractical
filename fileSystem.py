# file=open('hello.txt','a');

# # data =file.read();
# # print(data);
# # file.close();

# file.write("this is file append");
# file.close();

# file=open("hello.txt");
# text=file.read();
# if 'file' in text:
#     print("yes present");
# else:
#     print("not present")

file=open("hello.txt");
fileData=file.read();
list=[];

for i in fileData:
    string = i.lower().replace(',','').replace('.','').split(" ");
    print(string) 
    for s in string:
        list.append(s)

print(list)

if 'this' in list:
    print("yes")
else:
    print("no")