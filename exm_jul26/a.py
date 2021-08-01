o=open('employee','r')
dic={}
for i in o:
    id,name,des,exp,sal=i.rstrip('\n').split(',')
    dic[int(id)]={'empid':id,'empname':name,'empdes':des,'empexp':exp,'empsal':sal}
# print(dic)
def valid(id=None,**kwargs):
    if id in dic :
        print(dic[id]['empname'])
        if 'prop' in kwargs:
            if kwargs['prop'] in dic[id]:

              print(dic[id][kwargs['prop']])
            else:
                print('invalid property')
    else:
         print('id is in valid')

# valid(1000)
valid(1000,prop='empdes')