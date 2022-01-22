def sum_digits(num):
    # fill in
    digit = []
    sumNum = 0
    while (num / 10 != 0):
        digit.insert(0, num % 10)
        num = num // 10
    print(digit)
    return sum(digit)
#Recursion
def sum_digitsRec(num):
    # fill in
    sumNum = 0
    while (num / 10 != 0):
        sumNum = sumNum + num%10
        num = num // 10
        return
    else:
        return sumNum
    return sum(digit)


print(sum_digits(0))