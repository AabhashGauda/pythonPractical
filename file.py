file=open("hello.txt","r");
text=file.read();
list=list(text);
print(text)
file.close();
print(list);