class Calculator:


 def __init__(self, a, b):
    self.a = a
    self.b = b


 def add(self):
    self.c = self.a + self.b
    print('add is :', self.c)


 def sub(self):
    self.d = self.a - self.b
    print('sub is', self.d)


 def mul(self):
    self.e = self.a * self.b
    print('mul is:', self.e)


 def div(self):
    self.f = self.a / self.b
    print('div', self.f)


obj = Calculator(1, 2)
obj.add()
obj.sub()
obj.mul()
obj.div()
