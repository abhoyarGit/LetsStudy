class basic:
    def a(self):
        print("class basic")


#basic.a(basic)

obj1 = basic()
obj1.a()
basic.a(obj1)
basic.a(self=obj1)
