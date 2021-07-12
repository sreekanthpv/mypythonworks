# # ........................'a+'
# import re
# x= 'a+' #a including group
# v='aaa ab ac aaaa'
# matcher=re.finditer(x,v)
# for i in matcher:
#     print(i.start())
#     print(i.group())
#




#........................ 'a*'
# import re
#
# x = 'a*'  # count including zero number of a
# v = 'aac ab ac aaaa'
# matcher = re.finditer(x,v)
# for i in matcher:
#     print(i.start())
#     print(i.group())





# .................'a?'
# import re
#
# x = 'a?'  # count a as eeach including zero no of a  (other letters also zero)
# v = 'aca ab ac aaaa'
# matcher = re.finditer(x, v)
# for i in matcher:
#     print(i.start())
#     print(i.group())
#





# ...................'a{2}'
# import re
#
# x = 'a{2}'  # no of position
# v = 'aaa ab ac aaaa'
# matcher = re.finditer(x, v)
# for i in matcher:
#     print(i.start())
#     print(i.group())





# ........................a{min,max}
# import re
#
# x = 'a{1,3}'  # min 2 ,max 3
# v = 'aaa ab ac aaaa'
# matcher = re.finditer(x, v)
# for i in matcher:
#     print(i.start())
#     print(i.group())



# .......................'^a'
# import re
#
# x = '^c'  # a to check the string is starting with a or any letter
# v = 'caaa ab ac aaaa'
# matcher = re.finditer(x, v)
# for i in matcher:
#     print(i.start())
#     print(i.group())







# ........................'a$'
# import re
#
# x = 'a$'  # to check ending is a
# v = 'aaa ab ac aaaa'
# matcher = re.finditer(x, v)
# for i in matcher:
#     print(i.start())
#     print(i.group())
#
#













