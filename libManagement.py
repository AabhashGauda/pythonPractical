class Library:
    OrganizationName="BookOWorm";
    def __init__(this,collegeName,collegeCode):
        this.collegeName=collegeName;
        this.collegeCode=collegeCode;

# class Library1:
#     OrganizationName="BookOWorm";
#     def __init__(this,collegeName,collegeCode):
#         this.collegeName=collegeName;
#         this.collegeCode=collegeCode;
   
class Books(Library):
    bookList=["book1","book2","book3"];
    def printBooks(this):
        for i in this.bookList:
            print(i);
