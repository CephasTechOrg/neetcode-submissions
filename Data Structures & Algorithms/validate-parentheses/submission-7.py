class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        Pair = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }
        for c in s:
            if c in Pair:
                if stack and stack[-1] == Pair[c]:
                    stack.pop()
                else:
                    return False    

            else:
                stack.append(c)
        return True if not stack else False