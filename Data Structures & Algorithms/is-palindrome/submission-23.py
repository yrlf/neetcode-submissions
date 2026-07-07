class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        l, r = 0, n - 1

        # while l < r:  # when l == r, break loop
        #     while l < r and not s[l].isalnum():
        #         l += 1
            
        #     while l < r and not s[r].isalnum():
        #         r -= 1
            
        #     if s[l].lower() != s[r].lower():
        #         return False
            
        #     l += 1
        #     r -= 1

        # # l == r -> 回文, 所以没有必要chekc s[l] == s[r]

        # return True


        while l <= r:  # when l > r, break loop
            while l < n and not s[l].isalnum():
                l += 1
            # l > r
            
            while r >= 0 and not s[r].isalnum():
                r -= 1
            

            if l < n and r >= 0 and s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1

        # l > r

        return True