
class Solution:
    def isValid(self, s: str) -> bool:
        n = []
        for i in s:
            if i in ["(" ,"[" ,"{"]:
                n.append(i)
                # print(n)
            elif i in ")":
                if len(n) == 0 or n.pop() != "(":
                    return False
            elif i in "]":
                if len(n) == 0 or n.pop() != "[":
                    return False
            elif i in "}":
                if len(n) == 0 or n.pop() != "{":
                    return False
        return len(n) == 0

