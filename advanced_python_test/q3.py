# 3. Create a Book class with instance Library_name, book_name, author, pages?

class Book:
    def values(self,lname,bname,author,pages):
        self.lname=lname
        self.bname=bname
        self.author=author
        self.pages=pages
    def print(self):
        print(self.lname,self.bname,self.author,self.pages)
obj=Book()
obj.values('acv library','book1','sam',90)
obj.print()