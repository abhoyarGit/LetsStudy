# Reverse only letters.
# Given a string s, reverse the string according to the following rules:
#
# All the characters that are not English letters remain in the same position.
# All the English letters(lowercase or uppercase) should be reversed.
# Return s after reversing it.
#
# Example
# 1:
#
# Input: s = "ab-cd"
# Output: "dc-ba"
# Example
# 2:
#
# Input: s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example
# 3:
#
# Input: s = "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"

# Solution 1
# class Solution:
#    def reverseOnlyLetters(self, s: str) -> str:
#         l = [i for i in s]
#         r = []
#         a = {}
#         for i in range(0,len(l)):
#             #if re.match(r'[A-Za-z]',l[i]):
#             if l[i].isalpha():
#                 r.insert(0,l[i])
#             else:
#                 a[i] = l[i]
#                 #print(a)
#         for key in a:
#             r.insert(key,a[key])

#         return "".join([i for i in r])

# Two Pointer Method
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i, j = 0, len(s) - 1
        a = [*s]
        print(a)
        while i < j:
            if not a[i].isalpha():
                i = i + 1
                continue

            if not a[j].isalpha():
                j = j - 1
                continue

            a[i], a[j] = a[j], a[i]
            i = i + 1
            j = j - 1
        print(a)
        return "".join(a)

