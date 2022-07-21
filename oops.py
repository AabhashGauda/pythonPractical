# class is a blue print for creating objects (no memory to create the class)
# object is a instace of a class and it takes memory

class Employee:
    #class has variables and objects
    companyName="Google";
    def setPersonalDetails(self,name,houseNumber):
        self.name=name;
        self.houseNumber=houseNumber;
    
    def printPersonalDetails(self):
        print("company name is "+self.companyName)
        print("name is "+self.name);
        print("house number is "+self.houseNumber);
    

class Laptop:
    def __init__(this,name,ram,speed):
          this.name=name;
          this.ram=ram;
          this.speed=speed;
    def printDetailsOfLaptop(this):
        print("the name of laptop is "+this.name+" ram of laptop is "+this.ram+" and speed of laptop is "+this.speed)
        
employee1=Employee();
employee1.setPersonalDetails("name","1234567890");
employee1.companyName="microsoft";
employee1.printPersonalDetails();

laptop1=Laptop("nameOfLaptop","8gb","fast");
laptop1.printDetailsOfLaptop();
