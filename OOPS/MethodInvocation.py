class Sample:
    def __init__(self,data):
        self.data = data
        self.left = None

    def add(self,val):
        self.left.add(val)
        print(self.left)
        return val + val


a = Sample(2)
a.add(6)