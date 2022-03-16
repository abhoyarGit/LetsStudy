# Function to print all n–digit binary numbers without any consecutive 1's
def countStrings(n, out='', last_digit=0):
    # if the number becomes n–digit, print it
    if n == 0:
        print(out)
        return

    # append 0 to the result and recur with one less digit
    countStrings(n - 1, out + '0', 0)

    # append 1 to the result and recur with one less digit
    # only if the last digit is 0
    if last_digit == 0:
        countStrings(n - 1, out + '1', 1)


if __name__ == '__main__':
    # total number of digits
    n = 2

    countStrings(n)