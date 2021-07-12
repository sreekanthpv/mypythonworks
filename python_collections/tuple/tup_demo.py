#immutable

tup=1,2,3,4,5
print(tup)
tup1=()
print(tup1)
print(type(tup1))



# keywords
print('max value',max(tup))
print('min value',min(tup))
print('len value',len(tup))




# heterogenenous
t= 8.9, 'h'
print(t)



# indexing is possible
print(tup[-1])

#

# nesting is possible
t1=(3,4,(5,6),[4,5])
print(t1)
# provides security(immutable)