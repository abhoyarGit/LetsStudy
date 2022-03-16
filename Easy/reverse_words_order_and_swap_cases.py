'''
STDIN                 Function
-----                 --------
aWESOME is cODING  →  sentence = "aWESOME is cODING"

op = Coding IS Awesome
'''

def reverse_words_order_and_swap_cases(sentence):
    words = sentence.split(' ')
    r_words = words[::-1]
    rev_sen = " ".join(r_words)
    op = ""
    for i in rev_sen:
        if i.islower():
            op  = op + i.upper()
        elif i.isupper():
            op = op + i.lower()
        else:
            op = op + i

    return op

a = 'aWESOME is cODING'
print(reverse_words_order_and_swap_cases(a))
