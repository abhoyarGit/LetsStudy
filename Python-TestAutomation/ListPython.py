a = [1,2,3]

# Index
print(a.index(2))
print(a.index(3,0,3))
print(a)

'''
#remove element from any poeition
add elemnt in any position
get the location of elemnet
list slicing
add list in the list at position
get number of elemnets in list
minimun value
maximum value
'''



####### Adding Elemnet
# Add an item to the end: append()
# You can add an item to the end of the list with append(). If you want to add to positions other than the end, such as the beginning, use insert() described later.
# Append
##################
l = list(range(3))
print(l)
# [0, 1, 2]

l.append(100)
print(l)
# [0, 1, 2, 100]

l.append('new')
print(l)
# [0, 1, 2, 100, 'new']

#A list is also added as one item, not combined.

l.append([3, 4, 5])
print(l)
# [0, 1, 2, 100, 'new', [3, 4, 5]]



# Extend
######################################################################
#Combine lists: extend(), + operator
#You can combine another list or tuple at the end of the list with extend(). All items are added to the end of the original list.

l = list(range(3))
print(l)
# [0, 1, 2]

l.extend([100, 101, 102])
print(l)
# [0, 1, 2, 100, 101, 102]

l.extend((-1, -2, -3))
print(l)
# [0, 1, 2, 100, 101, 102, -1, -2, -3]
#source: list_add_item.py
#In the case of a string, each character is added one by one.

l.extend('new')
print(l)
# [0, 1, 2, 100, 101, 102, -1, -2, -3, 'n', 'e', 'w']
#source: list_add_item.py
#It is also possible to combine using the + operator instead of extend().

#In the case of the + operator, a new list is returned. You can also add another list to the existing list with +=.

l2 = l + [5, 6, 7]
print(l2)
# [0, 1, 2, 100, 101, 102, -1, -2, -3, 'n', 'e', 'w', 5, 6, 7]

l += [5, 6, 7]
print(l)
# [0, 1, 2, 100, 101, 102, -1, -2, -3, 'n', 'e', 'w', 5, 6, 7]









##    Insert
# Insert an item at specified index: insert()
# You can insert an item at the specified index (position) by insert().
#
# Set the index for the first parameter and the item to be inserted for the second parameter. The index at the beginning is 0 (zero-based indexing). For negative values, -1 means one before the end.

l = list(range(3))
print(l)
# [0, 1, 2]

l.insert(0, 100)
print(l)
# [100, 0, 1, 2]

l.insert(-1, 200)
print(l)
# [100, 0, 1, 200, 2]
# source: list_add_item.py
# Like append(), the list is added as a single item, not combined.

l.insert(0, [-1, -2, -3])
print(l)
# [[-1, -2, -3], 100, 0, 1, 200, 2]
# source: list_add_item.py
# Note that insert() is an O(n) operation and is not efficient. See the official wiki for the computational complexity of various operations on list.
#
# TimeComplexity - Python Wiki
# The deque type is provided in the standard library collections module as a type to add an item to the head with O(1). For example, if you want to treat data as a queue (FIFO), it is more efficient to use deque.
#
# Queue, stack, and deque (double-ended queue) in Python

########## Remove Element
# Remove an item by index and get its value: pop()
# You can remove the item at the specified position and get its value with pop().
#
# The index at the beginning is 0 (zero-based indexing).

l = list(range(10))
print(l)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(l.pop(0))
# 0

print(l)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(l.pop(3))
# 4

print(l)
# [1, 2, 3, 5, 6, 7, 8, 9]
b = [1,2,3,4]
print("B = ", b)

print(l.pop(-2))
# 8

print(l)
# [1, 2, 3, 5, 6, 7, 9]
c = b.pop()
print(b)
print(c)
c = b.pop(0)
print(b)
print(c)

# List Slicing
# Add another list or tuple at specified index: slice
# If you specify a range using slice and assign another list or tuple, all items will be added.

l = list(range(3))
print(l)
# [0, 1, 2]

l[1:1] = [100, 200, 300]
print(l)
# [0, 100, 200, 300, 1, 2]
# source: list_add_item.py
# You can also replace the original item. All items in the specified range are replaced.

l = list(range(3))
print(l)
# [0, 1, 2]

l[1:2] = [100, 200, 300]
print(l)
# [0, 100, 200, 300, 2]

#Remove()
#==================================================================================
#Remove an item by value: remove()
#You can remove the first item from the list where its value is equal to the specified value with remove().

l = ['Alice', 'Bob', 'Charlie', 'Bob', 'Dave']
print(l)
# ['Alice', 'Bob', 'Charlie', 'Bob', 'Dave']

l.remove('Alice')
print(l)
# ['Bob', 'Charlie', 'Bob', 'Dave']

#If the list contains more than one matching the specified value, only the first one is deleted.

l.remove('Bob')
print(l)
# ['Charlie', 'Bob', 'Dave']

#Remove all items: clear()


# del()
#==========================================================================
# Remove items by index or slice: del
# clear(), pop(), and remove() are methods of list. You can also remove elements from a list with del statements.
#  Specify the item to be deleted by index. The first index is 0, and the last index is -1.

l = list(range(10))
print(l)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

del l[0]
print(l)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

del l[-1]
print(l)
# [1, 2, 3, 4, 5, 6, 7, 8]

del l[6]
print(l)
# [1, 2, 3, 4, 5, 6, 8]

l = list(range(10))
del l[2:8:2]
print(l)
# [0, 1, 3, 5, 7, 8, 9]

l = list(range(10))
del l[::3]
print(l)
# [1, 2, 4, 5, 7, 8]





############ Articles
https://note.nkmk.me/en/python-list-append-extend-insert/


