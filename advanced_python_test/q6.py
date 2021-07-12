# 6. Create objects of the following file and print the details of student
# with maximum mark? anu,1,bca,200 rahul,2,bba,177 vinod,3,bba,187 ajay,4,bca,198 maya,5, bba,195


class Student:
    def values(self,name,roll,dep,mark):
        self.name=name
        self.roll=roll
        self.dep=dep
        self.mark=mark
    def print(self):
        print(self.name)
        print(self.roll)
        print(self.dep)
        print(self.mark)
f=open('file7a','r')
lst=[]
for i in f:
    z=i.rstrip('\n').split(',')
    # print(z)
    n=z[0]
    r=z[1]
    d=z[2]
    m=z[3]
    obj=Student()
    obj.values(n,r,d,m)
    lst.append(obj)
# print(lst)
m=[]
for i in lst:
    m.append(i.mark)
for i in lst:
    if i.mark==max(m):
        print(i.name,i.dep,i.roll,i.mark)



