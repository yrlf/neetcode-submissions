class Solution:
    def isValid(self, s: str) -> bool:
        
        n = len(s)

        stack = []

        mapping = {
            ")":"(",
            "]":"[",
            "}":"{"
        }


        for i in range(n):
            if s[i] in mapping:
                if not stack or stack[-1] != mapping[s[i]]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(s[i])
        
        
        return True if not stack else False