class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        l, r = 0, n - 1

        while l <= r:
            while l <= r and not s[l].isalnum():
                l += 1

            while l <= r and not s[r].isalnum():
                r -= 1

            # 跳过非字母数字后，可能已经交叉了
            if l > r:
                break

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True