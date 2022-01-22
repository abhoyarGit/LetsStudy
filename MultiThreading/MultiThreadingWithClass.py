import threading

class A:
    def n1(self):
        for i in range(7):
            print("Child t1 executing")


obj = A()
t1 = threading.Thread(target=obj.n1)
t1.start()
t1.join()
print("Child returned to main thread")