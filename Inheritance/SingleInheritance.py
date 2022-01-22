class foo1():
    def func1(self):
        print("This is class foo1, def func1")

class foo2(foo1):
    def func2(self):
        print("This is class foo2, def func2")


obj = foo2()
obj.func1()
obj.func2()