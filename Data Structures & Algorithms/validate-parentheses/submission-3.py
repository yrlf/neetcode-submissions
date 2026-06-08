class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        mapping = {"{":"}", "[":"]", "(":")"}

        n = len(s)
        i = 0
        while i < n: 
            if s[i] in mapping:
                stk.append(s[i])
            else:
                if stk:
                    if mapping[stk.pop()] !=s[i]:
                        return False
                else:
                    return False
            i+=1
        
        return False if len(stk) != 0 else True