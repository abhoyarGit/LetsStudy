# def a(**kwargs):
#     for i in kwargs:
#         print(i," - ",kwargs[i])
#
#
#
# a("t1"=1,"t2"=2)

def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
    print(kwargs)


# Driver code
myFun(first='Geeks', mid='for', last='Geeks')



