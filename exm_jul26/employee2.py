f1=open('employee','r')
# employees={'eid':1000,'name:':'ajay','desig':'developer','exp':}
employees={}
for line in f1:
    # print(line)
   eid,name,desig,exp,salary,=line.rstrip('\n').split(',')
   employees[int(eid)]={'eid':eid,'name':name,'desig':desig,'exp':exp,'salary':salary}
print(employees)
def printEmployee(id=None,**kwargs):
    if id in employees:
        print(employees[id]['name'])
        if 'prope' in kwargs:
            if kwargs['prope'] in employees[id]:
               print(employees[id][kwargs['prope']])
            else:
                print('invalid prop')
    else:
        print('invalid id')


id=int(input('enter id'))
# printEmployee(id)
printEmployee(id,prope='salary')