v1=open('count2','r')
dict={}
for i in v1:
    z=i.rstrip('\n').split(' ')
    for j in z:
        if j not in dict:
            dict.update({j:1})
        else:
            v=dict[j]
            v=v+1
            dict.update({j:v})
print(dict)