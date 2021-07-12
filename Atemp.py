#avail book
#sort author based on sold
# if same author name with different books (is duplicating possible//same keyname) doubt

class Book:
   books = {
    'alchemist': {'bname': 'alchemist', 'author': 'paulo', 'price': 200, 'avcopies': 10, 'sold': 400},
    'hg': {'bname': 'hg', 'author': 'chetan', 'price': 100, 'avcopies': 11, 'sold': 300},
    'rainrising': {'bname': 'rainrising', 'author': 'KK', 'price': 100, 'avcopies': 0, 'sold': 500}
   }
   sorted={}
   auth=[]
   sold=[]

   def available(self,bookname):
       if bookname in self.books:
           if self.books[bookname]['avcopies']==0:
               print('outof stock')
           else:
               print('avail copies of ',bookname,':',self.books[bookname]['sold'])
       else:
           print('enter valid book')
   def sort(self):
       for i in self.books:
        self.sold.append(self.books[i]['sold'])
       self.sold.sort()
       self.sold.reverse()
       # print(self.sold)
       for i in self.sold:
           for j in self.books:
            if i==self.books[j]['sold']:
                self.auth.append(self.books[j]['author'])
       print('sorted order of authors based on sold books',self.auth)


   # def sort(self):
   #      for i in self.books:
   #         # print(i)
   #         self.sorted.update({self.books[i]['bname']:({self.books[i]['sold']:self.books[i]['author']})})
   #      print(self.sorted)
obj=Book()
obj.available('hg')
obj.sort()

