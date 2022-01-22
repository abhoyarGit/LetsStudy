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


t1 = threading.Thread(target=a, args=("This def a",))
t2 = threading.Thread(target=b, args=("This def b",))

t1.start()
t2.start()


t1.join()
t2.join()
