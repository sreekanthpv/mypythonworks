# 2types of variables
# static-  related to class...access using class name
# instance...related to method...acces  using 'self'
class book:
    lname='abc library' #static variable
    def set(self,bname,author,pages,):
        self.bname=bname
        self.author=author
        self.pages=pages

    def print(self):
        print('book name :',self.bname)
        print('author :',self.author)
        print('pages :',self.pages)
        print(book.lname)
obj=book()
obj.set('critical','anderson',90)
obj.print()
ob=book()
ob.set('criti','anu',80)
ob.print()