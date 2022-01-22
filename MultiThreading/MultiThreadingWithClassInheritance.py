import threading


class A(threading.Thread):
    def run(self):
        for i in range(7):
            print("child executing:", threading.current_thread().getName())


obj = A()
obj.start()
obj.join()
print("Control return to main thread:", threading.current_thread().getName())
