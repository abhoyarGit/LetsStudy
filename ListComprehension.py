squares = []
for i in range(5):
    squares.append(i**2)

print(squares)
# [0, 1, 4, 9, 16]


squares = [i ** 2 for i in range(5)]
print(squares)

def thrice(num):
    return num * 3

thriceList = [thrice(i) for i in range(5)]
print(thriceList)