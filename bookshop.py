# # class Book:
# #     books={
# #         'alchemist':{'bname':'alchemist','author':'paulo','price':200,'avcopies':10,'sold':400},
# #         'halfgirlfirend':{'bname':'halfgirlfriend','author':'chetan','price':100,'avcopies':11,'sold':10},
# #         'rainrising':{'bname':'rainrising','author':'chetan','price':100,'avcopies':0,'sold':300}
# #     }
# #     dic={}
# #     lst=[]
# #     sorted={}
# #     def available(self,name):
# #         if name in self.books:
# #             if self.books[name]['avcopies']==0:
# #                 print('book is out of stock')
# #             else:
# #                 print('avalable copies are',self.books[name]['avcopies'])
# #         else:
# #             print('search a valid book')
# #
# #
# #     def author(self):
# #         for i in self.books:
# #             self.dic.update({self.books[i]['sold']:self.books[i]['author']})
# #         # print(self.dic)
# #         for i in self.dic:
# #             self.lst.append(i)
# #         # print(self.lst)
# #         self.lst.sort()
# #         self.lst.reverse()
# #         # print(self.lst)
# #         print('sorted order of sold')
# #         for i in self.lst:
# #
# #              self.sorted.update({self.dic[i]:i})
# #         print(self.sorted)
# #              # print(self.dic[i],i,'books sold')
#
# obj=Book()
# obj.available('rainrising')
# obj.author()



class Book:
   books = {
    'alchemist': {'bname': 'alchemist', 'author': 'paulo', 'price': 200, 'avcopies': 10, 'sold': 400},
    'hg': {'bname': 'hg', 'author': 'chetan', 'price': 100, 'avcopies': 11, 'sold': 0},
    'rainrising': {'bname': 'rainrising', 'author': 'KK', 'price': 100, 'avcopies': 0, 'sold': 900}
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


obj=Book()
obj.available('hg')
obj.sort()

