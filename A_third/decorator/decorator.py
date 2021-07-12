# DECORATOR
#adding extra features without changing function definition
#vaccination program

def check(func):
    def wrapper(name,age):
        if age<18:
            print('not eligible')
        else:
            return func(name,age)
    return wrapper

@check
def vaccine(name,age):
    print(name,'eligible for vaccination')
vaccine('anu',19)

@check
def eligible(name,age):
    print(name,age)
eligible('aaml',24)