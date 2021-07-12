# import re
# x='[abc]' #either a b c
# matcher= re.finditer(x,'asfdfbdfdfc')
# for match in matcher:
#     print(match.start())
#     print(match.group())
#
#

# import re
# x='[^abc]'
# v=re.finditer(x,'asdfbghkc')
# for i in v:
#     print(i.start())
#     print(i.group())
#


import re

x = '\W'  # either a b c
matcher = re.finditer(x, 'a### #f3dfc')
for match in matcher:
    print(match.start())
    print(match.group())


