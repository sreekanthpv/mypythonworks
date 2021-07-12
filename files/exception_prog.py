# user defined exceptions
a=int(input('enter age'))
if a<18:
    raise Exception('not eligible')
else:
    print('eligible')