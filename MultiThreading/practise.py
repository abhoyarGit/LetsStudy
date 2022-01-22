
import threading
from time import sleep
def a(text):
    for i in range(5):
        print(text)
        sleep(1)

def b(text):
    for i in range(5):
        print(text)
        sleep(1)
obj1 = threading.Thread(target=a, args=("This is a",))
obj2 = threading.Thread(target=b, args=("This is b",))

obj1.start()
obj2.start()

obj1.join()
obj2.join()