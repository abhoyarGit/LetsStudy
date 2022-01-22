def sumRec(arr):
    sum = 0
    l = list(arr)
    if list:
        sum = sum + l.pop()
        return sumRec(l)
    else:
        return sum

total = sum([1,2,3,4,5,6,7,8,9,10,-1])
print(total)

    