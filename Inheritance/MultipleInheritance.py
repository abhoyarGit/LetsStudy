class mother():
    mName = ""
    def mn(self):
        print("Mother : ", self.mName)

class father():
    fName = ""
    def fn(self):
        print("Father : ", self.fName)

class son(mother, father):
    def sn(self):
        print("Father : ", self.fName)
        print("Mother : ", self.mName)


s = son()
s.fName = "a"
s.mName = "b"
s.sn()