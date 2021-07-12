# LUM12PY678
# LUM13BD609
# LUM12DS678
# LUM13DS609
# LUM12PY676
# LUM19BD601
# LUM11PY679
# LUM10BD601

import re
x='[L][U][M]\d{2}[P][Y]\d{3}'
a=open('stud','r')
b=open('python','w')
for i in a:
    z=i.rstrip('\n')
    # print(z)
    v=re.fullmatch(x,z)
    if v !=None:
        # b.write(i)
        #   or
        b.write(z)
        b.write('\n')
    # else:
        # print(z)
